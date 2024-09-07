from flask import Flask, jsonify, request
from rmp_requests import get_rmp_professor
from temple_requests import get_academic_programs, get_curriculum

app = Flask(__name__)


@app.route("/")
def home():
    return "<div>Connected</div>"


@app.route("/academic-programs")
def get_academic_programs_wrapper():
    data = get_academic_programs()
    return jsonify(data)


@app.route("/curriculum/<path:url>")
def get_curriculum_wrapper(url):
    data = get_curriculum(url)
    return jsonify(data)


# @app.route("/classSearch/<path:endpoint>")
# def get_request_wrapper(endpoint):
#     data = get_request(endpoint)
#     return jsonify(data)


@app.route("/rmp/getProfessor")
def get_rmp_professor_wrapper():
    professor_name = request.args.get("searchProfessor")
    data = get_rmp_professor(professor_name)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
