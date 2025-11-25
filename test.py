# ❌ Example: How XSS happens (INSECURE — for understanding only)
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    user_input = request.args.get("name", "")
    # ❗ Directly rendering user input causes XSS
    return f"<h1>Hello {user_input}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
