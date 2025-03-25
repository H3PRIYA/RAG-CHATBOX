import os
import re
import numpy as np
import pandas as pd
import torch
from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModel, pipeline
import faiss
import PyPDF2
from fuzzywuzzy import fuzz

app = Flask(__name__)

class AdvancedRAGChatbot:
    def __init__(self, document_paths):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        
        # Load embedding model
        self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        self.model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2").to(self.device)
        print("Loaded embedding model: sentence-transformers/all-MiniLM-L6-v2")
        
        # Load generative model
        self.generator = pipeline("text2text-generation", model="google/flan-t5-base", device=0 if self.device == "cuda" else -1)
        print("Initialized google/flan-t5-base model for generation")
        
        # Initialize storage for documents, embeddings, and indices
        self.documents = {}
        self.embeddings = {}
        self.indices = {}
        self.csv_data = {}
        
        # Process each document
        for doc_path in document_paths:
            if doc_path.endswith('.pdf'):
                self.process_pdf(doc_path)
            elif doc_path.endswith('.csv'):
                self.process_csv(doc_path)
            else:
                print(f"Unsupported file type: {doc_path}")
        print("Document processing complete.")

    def process_pdf(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            texts = [page.extract_text() for page in reader.pages]
            self.documents[pdf_path] = texts
            print(f"Processing PDF: {pdf_path}")
            embeddings = self.generate_embeddings(texts)
            print(f"Generated embeddings with shape: {embeddings.shape}")
            index = faiss.IndexFlatL2(embeddings.shape[1])
            index.add(embeddings)
            self.indices[pdf_path] = index
            self.embeddings[pdf_path] = embeddings
            print(f"Processed PDF with {len(texts)} pages.")

    def process_csv(self, csv_path):
        df = pd.read_csv(csv_path)
        print(f"Processing CSV: {csv_path}")
        print(f"Detected columns in CSV: {list(df.columns)}")
        print("First few rows of CSV:\n", df.head())
        texts = df.apply(lambda row: ' '.join(row.astype(str)), axis=1).tolist()
        self.documents[csv_path] = texts
        self.csv_data[csv_path] = df
        embeddings = self.generate_embeddings(texts)
        print(f"Generated embeddings with shape: {embeddings.shape}")
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        self.indices[csv_path] = index
        self.embeddings[csv_path] = embeddings
        print(f"Processed CSV with {len(texts)} rows.")

    def generate_embeddings(self, texts):
        print(f"Generating embeddings for {len(texts)} texts...")
        inputs = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512).to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
        return embeddings

    def extract_identifier(self, query):
        # Look for patterns like S1000 (S followed by 4 digits)
        match = re.search(r'S\d{4}', query, re.IGNORECASE)
        return match.group(0) if match else None

    def find_identifier_column(self, df):
        # Look for a column that likely contains identifiers (e.g., 'Student_ID', 'ID')
        for col in df.columns:
            if 'id' in col.lower():
                return col
        return None

    def extract_field(self, query):
        # Extract the field being asked about (e.g., 'age', 'gender')
        query = query.lower()
        if 'age' in query:
            return 'age'
        if 'gender' in query:
            return 'gender'
        if 'department' in query:
            return 'department'
        # Add more fields as needed
        return None

    def find_field_column(self, df, field):
        # Map the field to the appropriate column using fuzzy matching
        field = field.lower()
        for col in df.columns:
            if fuzz.partial_ratio(field, col.lower()) > 80:
                return col
        return None

    def process_query(self, query):
        print(f"Processing query: {query}")
        try:
            # Check for CSV-specific queries
            identifier = self.extract_identifier(query)
            if identifier:
                print(f"Detected potential identifier: {identifier}. Checking if it's a CSV query...")
                for doc_path in self.csv_data:
                    df = self.csv_data[doc_path]
                    print(f"Available columns in {doc_path}: {list(df.columns)}")
                    id_column = self.find_identifier_column(df)
                    if id_column and identifier in df[id_column].values:
                        print(f"Found identifier {identifier} in column {id_column}")
                        field = self.extract_field(query)
                        print(f"Looking for field related to keyword: {field}")
                        field_column = self.find_field_column(df, field)
                        if field_column:
                            print(f"Matched keyword '{field}' to column '{field_column}'")
                            value = df[df[id_column] == identifier][field_column].iloc[0]
                            print(f"Found value: {value}")
                            return str(value)

            # Fallback to semantic search
            print("No CSV-specific query detected or identifier not found. Falling back to semantic search...")
            print("Performing semantic search...")
            query_embedding = self.generate_embeddings([query])[0]
            contexts = []
            for doc_path in self.indices:
                distances, indices = self.indices[doc_path].search(query_embedding.reshape(1, -1), k=3)
                for idx in indices[0]:
                    contexts.append(self.documents[doc_path][idx])
            combined_context = " ".join(contexts)
            print(f"Combined context: {combined_context}")

            prompt = f"Question: {query}\nContext: {combined_context}\nAnswer the question concisely based on the context:"
            print(f"Prompt: {prompt}")
            response = self.generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
            print(f"Generated response: {response}")
            return response
        except Exception as e:
            print(f"Error in process_query: {e}")
            raise

# Initialize the chatbot
try:
    project_root = os.path.dirname(os.path.abspath(__file__))
    document_paths = [
        os.path.join(project_root, 'datasets', 'Data Science Interview.pdf'),
        os.path.join(project_root, 'datasets', 'Students_Grading_Dataset.csv')
    ]
    chatbot = AdvancedRAGChatbot(document_paths)
    print("Chatbot initialized successfully.")
except Exception as e:
    print(f"Failed to initialize chatbot: {e}")
    chatbot = None

print(f"Chatbot object: {chatbot}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global chatbot
    if chatbot is None:
        return jsonify({'response': 'Error: Chatbot failed to initialize. Check the server logs for details.'})

    data = request.get_json()
    user_input = data.get('message', '').strip()

    if not user_input:
        return jsonify({'response': 'Error: Empty message received.'})

    try:
        print(f"Processing query: {user_input}")
        response = chatbot.process_query(user_input)
        print(f"Response: {response}")
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error processing query: {e}")
        return jsonify({'response': f'Error: Failed to fetch'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)