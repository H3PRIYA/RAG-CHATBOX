# Advanced RAG Chatbot

## Overview
The **Advanced RAG Chatbot** is an intelligent chatbot that utilizes Retrieval-Augmented Generation (RAG) to provide accurate and contextually relevant responses. It processes PDFs and CSVs, retrieves information efficiently, and generates responses using a transformer-based model.

## Features
- **Retrieval-Augmented Generation (RAG):** Combines information retrieval with text generation for better answers.
- **PDF and CSV Processing:** Extracts and indexes data from PDFs and CSV files.
- **Semantic Search:** Uses FAISS for fast similarity search.
- **Natural Language Processing (NLP):** Leverages pre-trained transformers for embedding and text generation.
- **Flask Web Server:** Provides an API for chatbot interaction.

## Technologies Used
- Python
- Flask
- PyTorch
- Transformers (Hugging Face)
- FAISS (Facebook AI Similarity Search)
- PyPDF2
- FuzzyWuzzy
- Pandas & NumPy

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Usage
- Start the Flask server and send POST requests to `/chat` with a JSON payload:
  ```json
  {
    "message": "What is the student ID S1001's age?"
  }
  ```
- The chatbot will respond with relevant information from processed documents.

## Project Structure
```
├── datasets/
│   ├── Data Science Interview.pdf
│   ├── Students_Grading_Dataset.csv
├── templates/
│   ├── index.html
├── main.py
├── requirements.txt
├── README.md
```

## API Endpoints
- **`/`** : Renders the frontend UI.
- **`/chat`** (POST) : Accepts user queries and returns chatbot responses.

## License
This project is open-source under the [MIT License](LICENSE).

## Contributors
- Your Name ([GitHub Profile](https://github.com/your-username))


