from flask import Flask
import os
from database.database import initialize_database

# Flask App
app = Flask(__name__)
app.config["SECRET_KEY"] = "ResumeIQ"
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Initialize Database
initialize_database()

from routes.auth import auth
from routes.dashboard import dashboard
from routes.analysis import analysis

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(analysis)

# Home Page
@app.route("/")
def home():
    return app.view_functions["dashboard.dashboard_page"]()

if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)