from api import app
from api.resolvers import getPeople_resolver, authenticate_resolver
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from dotenv import load_dotenv


# load environment variables
load_dotenv()


# graphql queries
query = ObjectType('Query')
query.set_field('getPeople', getPeople_resolver)


# graphql mutations
mutation = ObjectType('Mutation')
mutation.set_field('authenticate', authenticate_resolver)


# graphql schema
type_defs = load_schema_from_path('schema.graphql')
schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)


# graphql playground
@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200


# graphql api
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
