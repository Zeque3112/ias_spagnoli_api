import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    # ENV = os.getenv('ENV', 'production')
    ENV = os.getenv('ENV', 'development')
    DEBUG = os.getenv('DEBUG', 'False').lower() == "true"