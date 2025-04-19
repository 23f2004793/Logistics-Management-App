class Config():
    DEBUG = False 
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dummy.sqlite3"
    DEBUG = True
    SECRET_KEY = "hydrabadi-biryani-is-love" # hash user creds in session.
    SECURITY_PASSWORD_HASH = "bcrypt" # mechanism for hashing password.
    SECURITY_PASSWORD_SALT = "kolkata-biryani-is-good" # helps hashing the password.
    WTF_CSRF_ENABLED = False 
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"