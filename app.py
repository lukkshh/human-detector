from flask import Flask , render_template , request
from utils import Base64Image , SaveImage , Detect , CleanUp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload():

    path = SaveImage(request.files['image'])

    human = Detect(path)

    b64img = Base64Image(path)

    CleanUp(path)

    return render_template("index.html", base64=b64img , human=human)

if __name__ == "__main__":
    app.run(debug=True)