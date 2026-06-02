import os

class Config:
    ENV = os.getenv('ENV', 'production')
    DEBUG = os.getenv('DEBUG', 'False').lower() == "true"