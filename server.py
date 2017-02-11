from flask import Flask
app = Flask(__name__)

@app.route("/")
def run():
    return "Running"

@app.route("/generate/<username>")
def generate(username):
    return "Generating lyrics for @" + username

if __name__ == "__main__":
    app.run()
