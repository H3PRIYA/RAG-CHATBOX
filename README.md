Flask-Based Retrieval-Augmented Generation (RAG) Chatbot
This project implements a Retrieval-Augmented Generation (RAG) chatbot using Flask. The chatbot processes PDF and CSV files to answer user queries through a web interface. It uses a custom RAG pipeline with sentence-transformers/all-MiniLM-L6-v2 for embeddings, FAISS for similarity search, and google/flan-t5-base for text generation. The project avoids using the LangChain framework for bonus points.

Features
Processes PDF and CSV files to answer user queries.
Provides a web-based interface for interaction.
Dynamically handles CSV data using fuzzy matching for flexible column mapping.
Supports queries like "what is the age of S1000?" (CSV-based) and "what is data science" (PDF-based).
Project Structure
main.py: The main Flask application and RAG chatbot implementation.
templates/index.html: The HTML template for the web interface.
datasets/: Directory for dataset files (not included in the repository due to size and sensitivity; see below for details).
requirements.txt: List of Python dependencies required to run the project.
.gitignore: Excludes sensitive or unnecessary files (e.g., venv/, datasets/) from version control.
Prerequisites
Before setting up the project, ensure you have the following installed on your system:

Python 3.8 or higher: Download and install from python.org.
Git: Download and install from git-scm.com to clone the repository.
A code editor like Visual Studio Code (optional but recommended).
Setup Instructions
Follow these steps to set up and run the chatbot on your machine.

1. Clone the Repository
Clone the project repository to your local machine using Git.

bash

Collapse

Wrap

Copy
git clone https://github.com/your-username/flask-rag-chatbot.git
cd flask-rag-chatbot
Note: Replace https://github.com/your-username/flask-rag-chatbot.git with the actual URL of your GitHub repository (e.g., https://github.com/harip/flask-rag-chatbot.git if your GitHub username is harip).

2. Create a Virtual Environment
Set up a virtual environment to manage the project’s dependencies.

bash

Collapse

Wrap

Copy
python -m venv venv
Activate the virtual environment:

On Windows:
bash

Collapse

Wrap

Copy
.\venv\Scripts\activate
On macOS/Linux:
bash

Collapse

Wrap

Copy
source venv/bin/activate
After activation, your terminal prompt should change to indicate the virtual environment is active (e.g., (venv)).

3. Install Dependencies
Install the required Python packages listed in requirements.txt.

bash

Collapse

Wrap

Copy
pip install -r requirements.txt
If you encounter issues with requirements.txt, you can install the dependencies manually:

bash

Collapse

Wrap

Copy
pip install numpy==1.24.3 torch==2.0.1 transformers==4.30.2 sentence-transformers==2.2.2 flask pandas pypdf2 python-docx faiss-cpu fuzzywuzzy python-Levenshtein
4. Prepare the Dataset Files
The chatbot requires two dataset files to function: a PDF file and a CSV file. These files are not included in the repository due to their size and potential sensitivity. You’ll need to provide your own dataset files and place them in the datasets/ folder.

Create the datasets/ Folder
If the datasets/ folder doesn’t exist, create it:

bash

Collapse

Wrap

Copy
mkdir datasets
Dataset File Requirements
Data Science Interview.pdf: A PDF file containing information about data science (e.g., definitions, concepts, interview questions). You can create a simple PDF with a few pages of text. For example:

Page 1: "Data science is a field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data."
Save this as datasets/Data Science Interview.pdf.
Students_Grading_Dataset.csv: A CSV file with student data, including columns like Student_ID, First_Name, Last_Name, Email, Gender, Age, Department, etc. You can create a small CSV file with the following content:

csv

Collapse

Wrap

Copy
Student_ID,First_Name,Last_Name,Email,Gender,Age,Department,Attendance (%),Midterm_Score,Final_Score,Assignments_Avg,Quizzes_Avg,Participation_Score,Projects_Score,Total_Score,Grade,Study_Hours_per_Week,Extracurricular_Activities,Internet_Access_at_Home,Parent_Education_Level,Family_Income_Level,Stress_Level (1-10),Sleep_Hours_per_Night
S1000,Omar,Williams,omar.williams@example.com,Male,21,Computer Science,85,78,82,75,80,90,85,83,B,15,Yes,Yes,College,Medium,5,4.7
S1001,Maria,Brown,maria.brown@example.com,Female,22,Mathematics,90,85,88,82,85,95,90,88,A,20,Yes,Yes,Graduate,Medium,4,9.0
S1002,Ahmed,Jones,ahmed.jones@example.com,Male,20,Physics,80,70,75,68,70,85,80,75,C,12,No,Yes,High School,Low,6,6.2
Save this as datasets/Students_Grading_Dataset.csv.
Verify Dataset Files
Ensure the following files are in the datasets/ folder:

datasets/Data Science Interview.pdf
datasets/Students_Grading_Dataset.csv
5. Run the Application
Start the Flask application to launch the chatbot.

bash

Collapse

Wrap

Copy
python main.py
The terminal should display output similar to:

text

Collapse

Wrap

Copy
Initializing AdvancedRAGChatbot...
Using device: cpu
Loaded embedding model: sentence-transformers/all-MiniLM-L6-v2
Device set to use cpu
Initialized google/flan-t5-base model for generation
...
* Running on http://127.0.0.1:5000
* Running on http://192.168.0.105:5000
Open your web browser and go to http://192.168.0.105:5000 (or http://127.0.0.1:5000 if running locally).
You should see the chatbot interface with a welcome message: "Hello! I'm a RAG Chatbot. Ask me anything about the documents or CSV data."
Usage
The chatbot interface provides a text input field and a "Send" button.
Enter queries related to the dataset files and click "Send".
Example queries and expected responses:
Query: "what is the age of S1000?"
Expected Response: "21"
Query: "what is data science"
Expected Response: "Data science is a field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data." (Based on the content of Data Science Interview.pdf)
Requirements
Python: 3.8 or higher
Dependencies: Listed in requirements.txt:
numpy==1.24.3
torch==2.0.1
transformers==4.30.2
sentence-transformers==2.2.2
flask
pandas
pypdf2
python-docx
faiss-cpu
fuzzywuzzy
python-Levenshtein
Troubleshooting
OpenMP Conflict Error
If you encounter an error like:

text

Collapse

Wrap

Copy
OMP: Error #15: Initializing libomp140.x86_64.dll, but found libiomp5md.dll already initialized.
This is due to a conflict between multiple OpenMP runtime libraries used by numpy and torch.

Quick Fix: Set the environment variable KMP_DUPLICATE_LIB_OK=TRUE as a workaround (note that this may cause performance issues or crashes):
On Windows (PowerShell):
bash

Collapse

Wrap

Copy
$env:KMP_DUPLICATE_LIB_OK = "TRUE"
python main.py
On macOS/Linux:
bash

Collapse

Wrap

Copy
export KMP_DUPLICATE_LIB_OK=TRUE
python main.py
Recommended Fix: Reinstall dependencies in a clean virtual environment to avoid the conflict:
bash

Collapse

Wrap

Copy
deactivate
rm -rf venv
python -m venv venv
.\venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
pip install numpy==1.24.3 torch==2.0.1 transformers==4.30.2 sentence-transformers==2.2.2 flask pandas pypdf2 python-docx faiss-cpu fuzzywuzzy python-Levenshtein
Insufficient Memory (Paging File Error)
If you see an error like:

text

Collapse

Wrap

Copy
Error loading generative model: The paging file is too small for this operation to complete. (os error 1455)
Fix: Increase your system’s paging file size:
On Windows:
Right-click "This PC" > "Properties" > "Advanced system settings" > "Performance" > "Settings."
Go to the "Advanced" tab, click "Change" under Virtual Memory.
Uncheck "Automatically manage paging file size for all drives."
Select the C: drive, choose "Custom size," and set:
Initial size: 4096 MB (4 GB)
Maximum size: 8192 MB (8 GB)
Click "Set," then "OK," and restart your computer.
Free up RAM by closing unnecessary applications (use Task Manager: Ctrl + Shift + Esc).
Chatbot Fails to Initialize
If the chatbot fails to initialize with an error like "Error: Chatbot failed to initialize. Check the server logs for details":

Check the terminal logs for the specific error.
Common causes:
Missing Dataset Files: Ensure Data Science Interview.pdf and Students_Grading_Dataset.csv are in the datasets/ folder.
Dependency Issues: Reinstall dependencies as shown in the setup instructions.
Memory Issues: See the "Insufficient Memory" section above.
Flask App Not Accessible
If you cannot access http://192.168.0.105:5000:

Ensure the Flask server is running (check the terminal for Running on http://0.0.0.0:5000).
Try accessing http://127.0.0.1:5000 on the same machine.
Check if port 5000 is blocked by your firewall. Allow access to port 5000 in your firewall settings.
Notes
The project avoids using the LangChain framework for bonus points.
Future enhancements could include support for DOCX, images, and videos.
The chatbot is designed to run on a CPU by default. If you have a compatible GPU, it will automatically use CUDA (modify main.py if you need to force CPU usage).
Contributing
Contributions are welcome! If you’d like to contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -m "Add your feature").
Push to your branch (git push origin feature/your-feature).
Open a pull request on GitHub.
License
This project is licensed under the MIT License. See the  file for details (if a license file is added to the repository).
