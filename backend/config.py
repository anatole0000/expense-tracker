# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'  # Path to your SQLite database file
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance reasons
    SECRET_KEY = 'your_secret_key'  # For session management and CSRF protection
