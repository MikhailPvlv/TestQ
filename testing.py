import os
from auth_project.settings import EMAIL_HOST_PASSWORD

from dotenv import load_dotenv

load_dotenv()
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
print(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)


