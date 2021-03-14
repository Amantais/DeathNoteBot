import os 
from dotenv import load_dotenv

load_dotenv() 

BOT_TOKEN = os.getenv('BOT_TOKEN')
admins = [
    os.getenv('admins')
]
IP = os.getenv('ip')
DB_HOST = IP
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DB_HOST}/{'postgres'}"

