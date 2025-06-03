# Darwix AI Assessment Solution

This repository implements two features for the Darwix AI assessment:

- **Audio Transcription with Diarization**: Transcribes audio files and identifies speakers, returning results in JSON format.  
- **AI Blog Post Title Suggestions**: Suggests blog post titles using NLP within a Django application.

---

## Prerequisites

- **Python 3.10 or later**: [Download](https://www.python.org/downloads/)
- **Git for Windows**: [Download](https://git-scm.com/)
- **FFmpeg**: [Download](https://www.gyan.dev/ffmpeg/builds/)
- **API Keys**: [AssemblyAI](https://www.assemblyai.com/) and [Hugging Face](https://huggingface.co/)
- **Text Editor**: Notepad or Visual Studio Code
- **Command Prompt**: Built-in on Windows 10/11

---

## Setup Instructions (Windows)

### 1. Install Required Software

**Python 3.10+:**

```bash
python --version
```

Expected:

```
Python 3.10.x
```

---

**Git:**

```bash
git --version
```

Expected:

```
git version 2.x.x
```

---

**FFmpeg:**

- Download `ffmpeg-release-full.7z` from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
- Extract to `C:\ffmpeg` using 7-Zip
- Add `C:\ffmpeg\bin` to your **System PATH**

Verify:

```bash
ffmpeg -version
```

Expected:

```
ffmpeg version ...
```

---

### 2. Clone or Create the Repository

**Clone Existing:**

```bash
git clone https://github.com/also-aditya/Darwix_assignment.git
cd Darwix_assignment
```

**OR Create from Scratch:**

```bash
mkdir Darwix_assignment
cd Darwix_assignment
git init
```

---

### 3. Set Up Project Structure

Ensure the following structure:

```
Darwix_assignment/
├── blog/
│   ├── migrations/
│   │   └── __init__.py
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
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root:

```
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

Use Notepad or VS Code. Make sure the file is named `.env`, not `.env.txt`.

---

### 5. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

If torch fails:

```bash
pip install torch==2.3.0 --no-cache-dir
```

---

### 6. Run the Django Application

```bash
cd blog_project
python manage.py migrate
python manage.py runserver
```

Open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Endpoints

### Feature 1: Audio Transcription with Diarization

- **URL:** `/api/transcribe/`
- **Method:** POST
- **Content-Type:** `multipart/form-data`

#### Input:

```
audio_file: .wav or .mp3 file
```

#### Output:

```json
{
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
```

#### Example cURL:

```bash
curl -X POST -F "audio_file=@C:\Users\YourUsername\Documents\test_audio.wav" http://127.0.0.1:8000/api/transcribe/
```

If path has spaces:

```bash
curl -X POST -F "audio_file=@\"C:\Program Files\test audio.wav\"" http://127.0.0.1:8000/api/transcribe/
```

---

### Feature 2: Blog Post Title Suggestions

- **URL:** `/api/suggest-titles/`
- **Method:** POST
- **Content-Type:** `application/json`

#### Input:

```json
{
  "content": "This is a blog post about the benefits of AI in healthcare, including diagnostics and treatment."
}
```

#### Output:

```json
{
  "titles": [
    "AI in Healthcare: Transforming Diagnostics",
    "The Future of Medicine with AI",
    "How AI Enhances Healthcare Outcomes"
  ]
}
```

#### Example cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"content\":\"This is a blog post about the benefits of AI in healthcare, including diagnostics and treatment.\"}" http://127.0.0.1:8000/api/suggest-titles/
```

---

## Testing with Postman

### Transcription:

- Method: POST  
- URL: `http://127.0.0.1:8000/api/transcribe/`  
- Body: `form-data`  
  - Key: `audio_file`  
  - Type: File  
  - Choose File: Your .wav/.mp3 file  

### Title Suggestions:

- Method: POST  
- URL: `http://127.0.0.1:8000/api/suggest-titles/`  
- Headers: `Content-Type: application/json`  
- Body (raw, JSON):

```json
{
  "content": "This is a blog post about AI in healthcare."
}
```

---

## Project Structure Recap

```
darwix-ai-assessment/
├── blog/
│   ├── migrations/
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
```

---

## Implementation Notes

- **Transcription**: Uses AssemblyAI (default language: English; update `language_code` for others).
- **Title Suggestions**: Uses Hugging Face `facebook/bart-large-cnn`.
- **Error Handling**: Graceful handling for invalid inputs.
- **File Cleanup**: Audio files deleted post-processing.

---

## Dependencies (`requirements.txt`)

```txt
django==5.1
assemblyai==0.26.0
transformers==4.40.0
torch==2.3.0
python-dotenv==1.0.1
requests==2.31.0
```

---

## Pushing to GitHub

Ensure `.gitignore` includes:

```
venv/
*.pyc
__pycache__/
.env
db.sqlite3
```

Add, commit, and push:

```bash
git add .
git commit -m "Darwix AI assessment solution"
git remote add origin https://github.com/your-username/darwix-ai-assessment.git
git push -u origin main
```

---

## Troubleshooting (Windows)

### cURL Not Found

```bash
curl --version
```

If not found, [download cURL](https://curl.se/windows), extract to `C:\curl`, and add to PATH.

---

### FFmpeg Not Found

```bash
ffmpeg -version
```

Ensure `C:\ffmpeg\bin` is in PATH.

---

### Virtual Environment Issues

```bash
venv\Scripts\activate.bat
```

To recreate:

```bash
rmdir /s venv
python -m venv venv
```

---

### API Key Errors

Ensure `.env` is correct with no extra spaces.

---

### Dependency Errors

Update pip:

```bash
python -m pip install --upgrade pip
```

If torch fails:

```bash
pip install torch==2.3.0 --no-cache-dir
```

---

### cURL Syntax Errors

Use backslashes `\` in paths and escape quotes in JSON:

```bash
{\"content\":\"text\"}
```

For PowerShell:

```bash
curl.exe -X POST -H "Content-Type: application/json" -d '{"content":"This is a blog post about AI."}' http://127.0.0.1:8000/api/suggest-titles/
```

---

### Slow Responses

Use smaller audio files (<5MB). First title suggestion might take longer due to model loading.

---

For support, check server logs in Command Prompt or contact [your contact info].
