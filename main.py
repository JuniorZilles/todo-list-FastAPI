import uvicorn
import os
from dotenv import load_dotenv
from src.app import app

load_dotenv('.env')

if __name__ == '__main__':
    port = int(os.getenv('PORT', default=3000))
    uvicorn.run("main:app", port=port, log_level="info")