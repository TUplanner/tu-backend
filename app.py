from flask import Flask, jsonify
from temple_requests import get_academic_programs

app = Flask(__name__)


@app.route("/")
def home():
    return "<div>Connected</div>"


@app.route("/academic-programs")
def get_academic_programs_wrapper():
    data = get_academic_programs()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
