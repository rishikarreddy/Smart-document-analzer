from flask import Flask, render_template, request
import os
from utils.extract_text import extract_text
from utils.ocr import extract_text_from_image
from utils.summarize import summarize_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        if filename.lower().endswith(('.pdf', '.txt')):
            text = extract_text(filepath)
        elif filename.lower().endswith(('.jpg', '.png', '.jpeg')):
            text = extract_text_from_image(filepath)
        else:
            text = "Unsupported file format."

        summary = summarize_text(text)
        result = {'text': text, 'summary': summary}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
