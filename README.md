# CodeAlpha_LanguageTranslationTool

A Language Translation Tool built as part of the **CodeAlpha AI/ML Internship Program**.

## Features

- Translate text between 65+ languages
- Auto language detection
- Swap source and target languages
- Copy translated text to clipboard
- Text-to-speech — listen to the translation
- Clean and simple user interface
- **No server required** — runs entirely in the browser

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Translation API:** MyMemory (free, no API key required)
- **Hosting:** GitHub Pages (static site)

## Live Demo

[View the live site](https://weiwei-gitch.github.io/CodeAlpha_LanguageTranslationTool/)

## How to Run Locally

Simply open `index.html` in any browser — no installation needed.

```bash
git clone https://github.com/weiwei-gitch/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
open index.html   # or double-click the file
```

## Deployment

This project is deployed via **GitHub Pages** as a fully static site.

To deploy your own copy:

1. Fork or clone this repository
2. Go to **Settings → Pages**
3. Set the source branch to `main` and folder to `/ (root)`
4. GitHub Pages will serve `index.html` automatically

## Project Structure

```
CodeAlpha_LanguageTranslationTool/
├── index.html        # Main app (HTML + CSS + JS in one file)
└── README.md
```

## How It Works

The app calls the [MyMemory Translation API](https://mymemory.translated.net/) directly from JavaScript in the browser. No backend or API key is needed — translation requests are made client-side on every button click.

