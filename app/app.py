from flask import Flask 
app = Flask(__name__)

@app.route("/")
def home():
#    return "CI/CD Pipeline Working Successfully 🚀 .   Check Now. AUTO BUILD WORKING 🚀 . we break pods"
     return 1/0
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
