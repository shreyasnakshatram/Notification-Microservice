import os
from dotenv import load_dotenv
load_dotenv()

APP_ENV = os.getenv('APP_ENV')

#smptlib credentials
EMAIL_ADDRESS_SMPT = os.getenv('EMAIL_ADDRESS_SMPT')
PASSWORD_SMPT = os.getenv('PASSWORD_SMPT')

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

COMMON_SERVICE_PORT=os.getenv("COMMON_SERVICE_PORT")
INTERNAL_NLB = os.getenv("INTERNAL_NLB")
DEFAULT_USER_ID = os.getenv("DEFAULT_USER_ID")