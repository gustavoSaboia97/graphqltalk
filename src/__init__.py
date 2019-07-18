from flask import Flask
from .routes.graphql import graphql_blueprint

app = Flask(__name__)

app.register_blueprint(graphql_blueprint)

if __name__ == "__main__":
    app.run()
