from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

USER = os.getenv("USER_LOGIN")
ADMIN = os.getenv("ADMIN_LOGIN")
SECURITY = os.getenv("SECURITY_LOGIN")
USER_ADMIN = os.getenv('USER_ADMIN_LOGIN')
USER_ADMIN_SECURITY = os.getenv('USER_ADMIN_SECURITY_LOGIN')
PASSWORD = os.getenv('PASSWORD')