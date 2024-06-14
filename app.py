from flask import Flask #type: ignore
from API.api import route_manager


app = Flask(__name__)
route_manager(app)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
