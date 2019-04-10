from celery import shared_task
from . import emails
from .models import Subscriber


@shared_task
def senf_confirmation_email_to_subscriber(subscriber_id):
    subscriber = Subscriber.objects.get(id=subscriber_id)
    emails.send_confirmation_email(subscriber)