from fastapi import Request, APIRouter
from services.notifications.interaction.send_notification import EmailProvider

notification_router = APIRouter()

@notification_router.post("/notifications/order-placed")
async def handle_order_placed(request: Request):
    # template = templates.get_template("order_confirmation.html")
    # email_body = template.render(order='event')

    email_provider = EmailProvider()
    email_provider.send_email(
        'event.customer_email,'
        "Order Confirmation",
        'hey'
    )
    # Potentially send SMS using SMSProvider too
    return {"status": "Notification sent"}