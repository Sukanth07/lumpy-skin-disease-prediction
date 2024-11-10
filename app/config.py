import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), '.'))
print(BASE_DIR)

MODELS_DIR = os.path.join(BASE_DIR, 'final_models')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

GEMINI_MODEL_NAME = 'gemini-1.5-flash-latest'