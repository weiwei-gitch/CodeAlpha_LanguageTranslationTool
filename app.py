"""
CodeAlpha Internship - Task 1: Language Translation Tool
Uses MyMemory Free Translation API (no API key required)
"""

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Supported languages
LANGUAGES = {
    "auto": "Auto Detect",
    "en": "English",
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese (Simplified)",
    "ar": "Arabic",
    "bn": "Bengali",
    "nl": "Dutch",
    "pl": "Polish",
    "tr": "Turkish",
    "sv": "Swedish",
    "da": "Danish",
    "fi": "Finnish",
    "el": "Greek",
    "he": "Hebrew",
    "id": "Indonesian",
    "ms": "Malay",
    "th": "Thai",
    "vi": "Vietnamese",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "ta": "Tamil",
    "te": "Telugu",
}


@app.route("/")
def index():
    return render_template("index.html", languages=LANGUAGES)


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "").strip()
    source_lang = data.get("source_lang", "en")
    target_lang = data.get("target_lang", "hi")

    if not text:
        return jsonify({"error": "Please enter some text to translate."}), 400

    if source_lang == target_lang and source_lang != "auto":
        return jsonify({"translated_text": text})

    # Build language pair
    if source_lang == "auto":
        lang_pair = f"en|{target_lang}"
    else:
        lang_pair = f"{source_lang}|{target_lang}"

    # Call MyMemory API
    url = "https://api.mymemory.translated.net/get"
    params = {"q": text, "langpair": lang_pair}

    try:
        response = requests.get(url, params=params, timeout=10)
        result = response.json()

        if result.get("responseStatus") == 200:
            translated = result["responseData"]["translatedText"]
            return jsonify({"translated_text": translated})
        else:
            return jsonify({"error": "Translation failed. Please try again."}), 500

    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out. Please try again."}), 500
    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
