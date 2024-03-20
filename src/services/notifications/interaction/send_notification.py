from configs.env import *
from fastapi.templating import Jinja2Templates
import smtplib

templates = Jinja2Templates(directory="templates")

class EmailProvider:
    def send_email(recipient, subject, body):
        email = EMAIL_ADDRESS_SMPT
        password = PASSWORD_SMPT
        
        # with smtplib.SMTP(host = "smtp.gmail.com", port = "587") as connection:
        #     connection.starttls()
        #     connection.login(user = email, password = password)
        #     connection.sendmail(
        #         from_addr = email, 
        #         to_addrs = "philiplewis989@gmail.com", 
        #         msg = body
        #     )