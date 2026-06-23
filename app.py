from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# A short dictionary of supported languages for the user interface dropdown
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'zh-CN': 'Chinese (Simplified)',
    'ar': 'Arabic',
    'ur': 'Urdu',
    'hi': 'Hindi',
    'ja': 'Japanese'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    original_text = ""
    src_lang = "auto"
    tgt_lang = "en"

    if request.method == 'POST':
        original_text = request.form.get('text', '')
        src_lang = request.form.get('source_lang', 'auto')
        tgt_lang = request.form.get('target_lang', 'en')

        if original_text.strip():
            try:
                # Use deep-translator to process translation via Google Translate API
                translated_text = GoogleTranslator(source=src_lang, target=tgt_lang).translate(original_text)
            except Exception as e:
                translated_text = f"Translation Error: {str(e)}"

    return render_template('index.html', 
                           languages=SUPPORTED_LANGUAGES, 
                           translated_text=translated_text,
                           original_text=original_text,
                           src_lang=src_lang,
                           tgt_lang=tgt_lang)

if __name__ == '__main__':
    app.run(debug=True)