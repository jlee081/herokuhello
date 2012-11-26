from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def homepage():
	return "welcome home"	

@app.route("/jason")
def jason():
    return "wassssuuuppp Jason!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "80"))
    app.run(port=port)