from ariadne import (
    ObjectType,
    QueryType,
    graphql_sync,
    make_executable_schema,
    load_schema_from_path,
)
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request
from rmp_requests import get_professor

# /---------------------------------------------------------\
explorer_html = ExplorerGraphiQL().html(None)
type_defs = load_schema_from_path("schema/demo.graphql")
query = QueryType()

new_search = ObjectType("NewSearch")


@query.field("newSearch")
def resolve_new_search(_, info):
    return {}


@new_search.field("teacher")
def resolve_teacher(parent, info, fullName):
    return get_professor(fullName)


schema = make_executable_schema(type_defs, query, new_search)
# \---------------------------------------------------------/


app = Flask(__name__)


@app.route("/")
def home():
    return "Connected"


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
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
