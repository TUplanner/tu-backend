from flask import Flask, jsonify, request
from ariadne import (
    QueryType,
    graphql_sync,
    make_executable_schema,
    load_schema_from_path,
)
from ariadne.explorer import ExplorerGraphiQL
from course_requests import get_request
from rmp_requests import get_rmp_professor
from temple_requests import get_academic_programs, get_curriculum

query = QueryType()


@query.field("hello")
def resolve_hello(_, info):
    user_agent = info.context["request"].headers.get("User-Agent", "Guest")
    return f"Hello, {user_agent}!"


@query.field("academicPrograms")
def resolve_academic_programs(*_):
    return get_academic_programs()


@query.field("curriculum")
def resolve_curriculum(_, info, url):
    return get_curriculum(url)


@query.field("classSearch")
def resolve_class_search(_, info, endpoint):
    return get_request(endpoint)


@query.field("getRMPProfessor")
def resolve_get_rmp_professor(_, info, professorName):
    return get_rmp_professor(professorName)


# Load schema from file
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query)

app = Flask(__name__)


@app.route("/")
def home():
    return "Connected"


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    explorer_html = ExplorerGraphiQL().html(None)
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value={"request": request}, debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)
