Flask-Based Retrieval-Augmented Generation (RAG) Chatbot
This project implements a Retrieval-Augmented Generation (RAG) chatbot using Flask. The chatbot processes PDF and CSV files to answer user queries through a web interface. It uses a custom RAG pipeline with sentence-transformers, FAISS, and google/flan-t5-base for retrieval and generation.

Project Structure
main.py: The main Flask application and RAG chatbot implementation.
templates/index.html: The HTML template for the web interface.
datasets/: Contains the dataset files (not included in the repository due to size and sensitivity).
Setup Instructions
Clone the Repository:
bash

Collapse

Wrap

Copy
git clone https://github.com/your-username/flask-rag-chatbot.git
cd flask-rag-chatbot
Create a Virtual Environment:
bash

Collapse

Wrap

Copy
python -m venv venv
source venv/Scripts/activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
Install Dependencies:
bash

Collapse

Wrap

Copy
pip install -r requirements.txt
Alternatively, install the dependencies manually:
bash

Collapse

Wrap

Copy
pip install numpy==1.24.3 torch==2.0.1 transformers==4.30.2 sentence-transformers==2.2.2 flask pandas pypdf2 python-docx faiss-cpu fuzzywuzzy python-Levenshtein
Add Dataset Files:
Place your dataset files (Data Science Interview.pdf and Students_Grading_Dataset.csv) in the datasets/ folder.
Note: These files are not included in the repository due to size and sensitivity. You’ll need to provide your own dataset files with the following requirements:
Data Science Interview.pdf: A PDF file containing information about data science (e.g., definitions, concepts).
Students_Grading_Dataset.csv: A CSV file with student data, including columns like Student_ID, First_Name, Last_Name, Email, Gender, Age, Department, etc. Example:
text

Collapse

Wrap

Copy
Student_ID,First_Name,Last_Name,Email,Gender,Age,Department
S1000,Omar,Williams,omar.williams@example.com,Male,21,Computer Science
S1001,Maria,Brown,maria.brown@example.com,Female,22,Mathematics
S1002,Ahmed,Jones,ahmed.jones@example.com,Male,20,Physics
Run the Application:
bash

Collapse

Wrap

Copy
python main.py
Open http://192.168.0.105:5000 in your browser to access the chatbot. If running on a different machine, replace 192.168.0.105 with your machine’s IP address.
Usage
The chatbot interface allows you to ask questions about the documents or CSV data.
Example queries:
"what is the age of S1000?" (Expected response: "21")
"what is data science" (Expected response: A definition of data science based on the PDF content)
Requirements
Python 3.8+
Dependencies listed in requirements.txt
Notes
The project avoids using the LangChain framework for bonus points.
Future enhancements could include support for DOCX, images, and videos.
If you encounter an OpenMP conflict error (OMP: Error #15), set the environment variable KMP_DUPLICATE_LIB_OK=TRUE as a workaround:
bash

Collapse

Wrap

Copy
export KMP_DUPLICATE_LIB_OK=TRUE  # On macOS/Linux
set KMP_DUPLICATE_LIB_OK=TRUE     # On Windows (PowerShell)
Alternatively, reinstall dependencies with compatible versions as specified in the setup instructions.
