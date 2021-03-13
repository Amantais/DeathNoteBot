import os 
from dotenv import load_dotenv

load_dotenv() 

BOT_TOKEN = os.getenv('BOT_TOKEN')
admins = [
    os.getenv('admins')
]
IP = os.getenv('ip')