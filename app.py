from flask import Flask, render_template, request
import os

from ocr.ocr_engine import extract_text
from entity.entity_extraction import extract_entities
from postprocess.clean_validate import clean_data

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    raw_text = None

    if request.method == "POST":
        file = request.files["file"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        raw_text = extract_text(path)
        entities = extract_entities(raw_text)
        result = clean_data(entities)

    return render_template(
        "index.html",
        result=result,
        raw_text=raw_text
    )


if __name__ == "__main__":
    app.run(debug=True)
