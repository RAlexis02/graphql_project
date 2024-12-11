from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema

app = Flask(__name__)

# GraphQL Schema
class Query(ObjectType):
    hello = String(name=String(default_value="World"))
    
    def resolve_hello(root, info, name):
        return f"Hello, {name}!"

schema = Schema(query=Query)

# Root Route (Home Page)
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>GraphQL API</title>
        </head>
        <body>
            <h1>Welcome to the GraphQL API!</h1>
            <p>This API allows you to query data using GraphQL.</p>
            <p>Visit the <a href="/graphql">GraphQL Playground</a> to explore the API.</p>
        </body>
    </html>
    """

# GraphQL Route
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
