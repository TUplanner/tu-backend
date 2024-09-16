from flask import Flask, jsonify, request
from ariadne import graphql_sync, make_executable_schema, load_schema_from_path
from ariadne.explorer import ExplorerGraphiQL
from resolvers.query_resolvers import query
from resolvers.new_search_resolvers import new_search

# Load schema and resolvers once
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, new_search)

# Explorer instantiation
explorer_html = ExplorerGraphiQL().html(None)


# Flask app setup
app = Flask(__name__)


@app.route("/")
def home():
    return "Connected"


@app.route("/graphql", methods=["GET", "POST"])
def graphql_handler():
    if request.method == "GET":
        return explorer_html, 200
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value={"request": request}, debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)
