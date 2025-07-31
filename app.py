from flask import Flask
import os
from dotenv import load_dotenv

# 블루프린트 import
from routes.hospital import hospital_bp
from routes.drugstore import drugstore_bp
from routes.emergency import emergency_bp
from routes.board import board_bp
from routes.main import main_bp

load_dotenv("config.env")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# 블루프린트 등록
app.register_blueprint(hospital_bp)
app.register_blueprint(drugstore_bp)
app.register_blueprint(emergency_bp)
app.register_blueprint(board_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST", "0.0.0.0"),
        port=int(os.getenv("FLASK_PORT", 8080)),
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "false",
    )
