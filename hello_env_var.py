import os
from dotenv import load_dotenv

load_dotenv() # also takes path if not pwd


api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL')

print(f"API_KEY={api_key} DB {database}")