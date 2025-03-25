# Flask-Based Retrieval-Augmented Generation (RAG) Chatbot  

This project implements a Retrieval-Augmented Generation (RAG) chatbot using Flask. The chatbot processes PDF and CSV files to answer user queries through a web interface.  

## Features  
- **Processes PDF and CSV files** to answer user queries.  
- **Provides a web-based interface** for easy interaction.  
- **Dynamically handles CSV data** using fuzzy matching for flexible column mapping.  
- **Supports intelligent query handling**, such as:  
  - "What is the age of S1000?" (CSV-based query)  
  - "What is data science?" (PDF-based query)  

## Tech Stack  
- **Flask** (for the web framework)  
- **sentence-transformers/all-MiniLM-L6-v2** (for embeddings)  
- **FAISS** (for similarity search)  
- **google/flan-t5-base** (for text generation)  
- **Fuzzy matching** (for flexible CSV column mapping)  

## Project Structure  
- `main.py` - The main Flask application and RAG chatbot implementation.  
- `index.html` - Frontend interface for interacting with the chatbot.  
- `Students_Grading_Dataset.csv` - Sample CSV dataset used for query processing.  
- `Data Science Interview.pdf` - Sample PDF file used for answering questions.  
- `README.md` - This documentation file.  

## Installation and Setup  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/H3PRIYA/RAG-CHATBOX
   cd RAG-CHATBOX
   ```
2. **Create a Virtual Environment (Optional but Recommended)**  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask App**  
   ```bash
   python main.py
   ```
5. **Access the Web Interface**  
   Open `http://127.0.0.1:5000` in your browser.  

## Usage  
- Upload CSV or PDF files via the web interface.  
- Enter queries related to the uploaded files.  
- The chatbot will process and return relevant answers.  

## Innovations and Enhancements
- Dynamic CSV Handling: Used fuzzy matching to map query keywords to CSV columns, making the chatbot adaptable to any CSV file.
- Performance Boost: Installed python-Levenshtein to speed up fuzzy matching, improving performance.
- Web Interface: Built a Flask app with a responsive HTML interface and real-time query handling using AJAX.
- Error Handling: Added checks to display user-friendly error messages if the chatbot fails to process queries.

