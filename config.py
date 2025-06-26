# Database configuration settings

import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    # Database configuration
    DB_PATH = os.getenv('DB_PATH', 'yolov11.db')

    # For compatibility with existing code
    DB_CONFIG = {
        'database': DB_PATH
    }

    # Secret key for session management and token generation
    SECRET_KEY = os.getenv('SECRET_KEY', 'root@123')

    # Admin credentials
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

    # Google OAuth configuration
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', '472643417236-cnon98ph74j2dn6oglpprsjp9sfsqu4b.apps.googleusercontent.com')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', '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s')
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid_configuration"

    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    PORT = int(os.getenv('PORT', 4000))

    # Application specific folders and allowed extensions
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')
    RESULT_FOLDER = os.getenv('RESULT_FOLDER', 'static/results')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'mp4'}
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))