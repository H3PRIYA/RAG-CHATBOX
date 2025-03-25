# Flask-Based Retrieval-Augmented Generation (RAG) Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot using Flask. The chatbot processes PDF and CSV files to answer user queries through a web interface. It uses a custom RAG pipeline with `sentence-transformers`, FAISS, and `google/flan-t5-base` for retrieval and generation.

## Project Structure

- `main.py`: The main Flask application and RAG chatbot implementation.
- `templates/index.html`: The HTML template for the web interface.
- `datasets/`: Contains the dataset files (not included in the repository due to size and sensitivity).

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
  
