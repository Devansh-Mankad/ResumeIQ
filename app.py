from flask import Flask
from database.database import initialize_database

# Initialize Flask App
app = Flask(__name__)
app.config["SECRET_KEY"] = "ResumeIQ"

# Initialize Database
initialize_database()

from routes.auth import auth
app.register_blueprint(auth)

# Home page
@app.route("/")
def home():
    return "ResumeIQ is Running 🚀"

if __name__ == "__main__":
    app.run(debug=True)