# CodeAlpha_LanguageTranslationTool

A Language Translation Tool built as part of the **CodeAlpha AI/ML Internship Program**.

## Features
- Translate text between 30+ languages
- Auto language detection
- Swap source and target languages
- Copy translated text to clipboard
- Text-to-speech — listen to the translation
- Clean and simple user interface

## Tech Stack
- **Backend:** Python + Flask
- **Translation API:** MyMemory (free, no API key required)
- **Frontend:** HTML, CSS, JavaScript

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5001
```

## Project Structure
```
CodeAlpha_LanguageTranslationTool/
├── app.py               # Flask backend + API logic
├── requirements.txt     # Python dependencies
├── README.md
└── templates/
    └── index.html       # Frontend UI
```

## How It Works
1. User enters text and selects source & target language
2. Flask backend sends the text to MyMemory Translation API
3. API returns the translated text
4. Result is displayed on screen
5. User can copy or listen to the translation

---
*Built for CodeAlpha Internship - Task 1*
