from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker! Simple Flask app is working."

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/info", methods=['GET'])
def info():
    return {
            "app": "flask_project",
            "version": "1.0"
            }

@app.route("/version")
def version():
    return { "version": "1.0" }
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
