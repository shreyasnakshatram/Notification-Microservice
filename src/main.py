from fastapi import FastAPI, Depends
from configs.env import *
from services.notifications.notification_router import notification_router
from services.notification_templates.notification_template_router import notification_template_router
from database.db_support import get_db
from database.create_tables import create_tables
from services.notification_templates.models.notification_template import NotificationTemplate

app = FastAPI()

app.include_router(prefix = "/notification", router=notification_router, tags=['Notification'], dependencies=[Depends(get_db)])
app.include_router(prefix = "/notification_template", router = notification_template_router, tags=['Notification Template'], dependencies=[Depends(get_db)])

@app.get("/")
def read_root():
    return "Welcome To Notification Microservice"

# if __name__ == "__main__":
#     create_tables([NotificationTemplate])