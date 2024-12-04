# app_name/utils.py

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_html_welcome(user_email, user_name):
    subject = "Welcome to Our Platform"
    message = render_to_string('welcome_email.html', {'user_name': user_name})
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
