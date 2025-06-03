Darwix AI Assessment Solution
This repository implements two features for the Darwix AI assessment:

Audio Transcription with Diarization: Transcribes audio files and identifies speakers, returning results in JSON format.
AI Blog Post Title Suggestions: Suggests blog post titles using NLP within a Django application.

Prerequisites

Python 3.10 or later: Download from python.org.
Git for Windows: Download from git-scm.com.
FFmpeg: Download from gyan.dev.
API Keys: Obtain from assemblyai.com and huggingface.co.
Text Editor: Notepad or Visual Studio Code for creating files like .env.
Command Prompt: Built into Windows 10/11 for running commands.

Setup Instructions (Windows)
1. Install Required Software

Python 3.10+:
Download and install, checking "Add Python to PATH" during setup.
Verify:python --version

Expected: Python 3.10.x or higher.


Git:
Install with default settings.
Verify:git --version

Expected: git version 2.x.x.


FFmpeg:
Download ffmpeg-release-full.7z from gyan.dev.
Extract to C:\ffmpeg using 7-Zip.
Add to PATH:
Right-click 'This PC' > Properties > Advanced system settings > Environment Variables.
Under "System variables," edit Path, add C:\ffmpeg\bin.


Verify:ffmpeg -version

Expected: FFmpeg version information.



2. Clone or Create the Repository

Create a GitHub Repository:
Go to github.com, create a new repository (e.g., darwix-ai-assessment), and note the URL (e.g., https://github.com/your-username/darwix-ai-assessment.git).


Clone Locally:
Open Command Prompt:git clone https://github.com/your-username/darwix-ai-assessment.git
cd darwix-ai-assessment


Alternatively, create a new directory and initialize Git:mkdir darwix-ai-assessment
cd darwix-ai-assessment
git init





3. Set Up Project Structure
Ensure the following structure exists (create manually if not cloning):
darwix-ai-assessment/
├── blog/
│   ├── migrations/
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── utils/
│       ├── __init__.py
│       ├── transcription.py
│       └── title_suggestion.py
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md


Copy the provided files (from the assessment codebase) into this structure.
Use Notepad or VS Code to create/edit files.

4. Configure Environment Variables

Obtain API Keys:
Sign up at assemblyai.com for an AssemblyAI API key.
Sign up at huggingface.co for a Hugging Face API key (optional for local BART model).


Create .env File:
Open Notepad, add:ASSEMBLYAI_API_KEY=your_assemblyai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key


Save as .env in darwix-ai-assessment (ensure it’s .env, not .env.txt).
In File Explorer, enable "File name extensions" (View > File name extensions) to verify.



5. Set Up Virtual Environment

Create a virtual environment:python -m venv venv


Activate it:venv\Scripts\activate.bat

Your prompt should show (venv).
Install dependencies:pip install -r requirements.txt

If torch fails, try:pip install torch==2.3.0 --no-cache-dir



6. Run the Django Application

Navigate to the project directory:cd blog_project


Apply migrations:python manage.py migrate


Start the server:python manage.py runserver


Verify by opening http://127.0.0.1:8000 in a browser (shows Django’s default page).

Endpoints
Feature 1: Audio Transcription with Diarization

URL: /api/transcribe/
Method: POST
Content-Type: multipart/form-data
Input:
audio_file: Audio file (.wav or .mp3, e.g., a short conversation with multiple speakers).


Output:{
  "transcription": [
    {
      "speaker": "Speaker A",
      "text": "Hello, how are you?",
      "start_time": 0.0,
      "end_time": 2.5
    },
    {
      "speaker": "Speaker B",
      "text": "I'm doing great, thanks!",
      "start_time": 2.6,
      "end_time": 4.0
    }
  ]
}


Example cURL Command:
Prepare an audio file (e.g., C:\Users\YourUsername\Documents\test_audio.wav).
Run in Command Prompt:curl -X POST -F "audio_file=@C:\Users\YourUsername\Documents\test_audio.wav" http://127.0.0.1:8000/api/transcribe/


For paths with spaces:curl -X POST -F "audio_file=@\"C:\Program Files\test audio.wav\"" http://127.0.0.1:8000/api/transcribe/





Feature 2: Blog Post Title Suggestions

URL: /api/suggest-titles/
Method: POST
Content-Type: application/json
Input:{
  "content": "This is a blog post about the benefits of AI in healthcare, including diagnostics and treatment."
}


Output:{
  "titles": [
    "AI in Healthcare: Transforming Diagnostics",
    "The Future of Medicine with AI",
    "How AI Enhances Healthcare Outcomes"
  ]
}


Example cURL Command:
Run in Command Prompt:curl -X POST -H "Content-Type: application/json" -d "{\"content\":\"This is a blog post about the benefits of AI in healthcare, including diagnostics and treatment.\"}" http://127.0.0.1:8000/api/suggest-titles/





Testing with cURL

Windows Notes:
cURL is built into Windows 10/11. Verify: curl --version.
Use backslashes (\) in file paths (e.g., C:\Users\YourUsername\Documents\test_audio.wav).
Escape quotes in JSON payloads (e.g., {\"content\":\"text\"}).
For PowerShell, use curl.exe and single quotes for JSON:curl.exe -X POST -H "Content-Type: application/json" -d '{"content":"This is a blog post about AI."}' http://127.0.0.1:8000/api/suggest-titles/





Alternative Testing with Postman

Install Postman from postman.com.
Transcription:
Create a POST request to http://127.0.0.1:8000/api/transcribe/.
In "Body" > form-data, add key audio_file, set type to File, and select your audio file.
Click "Send".


Title Suggestions:
Create a POST request to http://127.0.0.1:8000/api/suggest-titles/.
In "Headers," add Content-Type: application/json.
In "Body" > raw > JSON, enter:{
  "content": "This is a blog post about AI in healthcare."
}


Click "Send".



Project Structure
darwix-ai-assessment/
├── blog/
│   ├── migrations/
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── utils/
│       ├── __init__.py
│       ├── transcription.py
│       └── title_suggestion.py
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

Implementation Notes

Transcription: Uses AssemblyAI for transcription and diarization, supporting multilingual audio (default: English; modify language_code in blog/utils/transcription.py for other languages, e.g., es for Spanish).
Title Suggestions: Uses Hugging Face's facebook/bart-large-cnn model to generate three titles.
Error Handling: Handles invalid inputs (e.g., missing files, invalid JSON) and API errors.
File Management: Temporary audio files are deleted after processing.

Dependencies
Listed in requirements.txt:

django==5.1
assemblyai==0.26.0
transformers==4.40.0
torch==2.3.0
python-dotenv==1.0.1
requests==2.31.0

Pushing to GitHub

Ensure .gitignore excludes:venv/
*.pyc
__pycache__/
.env
db.sqlite3


Add and commit files:git add .
git commit -m "Darwix AI assessment solution"


Push:git remote add origin https://github.com/your-username/darwix-ai-assessment.git
git push -u origin main



Troubleshooting (Windows)

cURL Not Found:
Verify: curl --version.
If missing, download from curl.se/windows, extract to C:\curl, and add to PATH.


FFmpeg Not Found:
Verify: ffmpeg -version.
Ensure C:\ffmpeg\bin is in PATH.


Virtual Environment Issues:
Use venv\Scripts\activate.bat in Command Prompt.
Recreate if needed: rmdir /s venv && python -m venv venv.


API Key Errors:
Check .env for valid ASSEMBLYAI_API_KEY and no extra spaces.


Dependency Errors:
Update pip: python -m pip install --upgrade pip.
Install torch separately: pip install torch==2.3.0 --no-cache-dir.


cURL Syntax Errors:
Use backslashes in file paths.
Escape JSON quotes: {\"content\":\"text\"}.


Slow Responses:
Use small audio files (<5MB) for transcription.
First title suggestion request may be slow due to BART model loading.



For issues, check server logs in Command Prompt or contact [your contact details].
