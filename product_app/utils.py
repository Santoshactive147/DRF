# # app_name/utils.py

# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.conf import settings

# def send_html_welcome(user_email, user_name):
#     subject = "Welcome to Our Platform"
#     message = render_to_string('welcome_email.html', {'user_name': user_name})
#     send_mail(
#         subject,
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         [user_email],
#         fail_silently=False,
#     )


# utils.py

# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.conf import settings

# # def send_welcome_email(user_email, user_name):
# #     subject = "Welcome to Our Platform"
# #     message = render_to_string('welcome_email.html', {'user_name': user_name})
# #     send_mail(
# #         subject,
# #         message,
# #         settings.DEFAULT_FROM_EMAIL,  # Default email address
# #         [user_email],
# #         html_message=message,
# #         fail_silently=False,
# #     )


# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.conf import settings

# def send_welcome_email():
#     # Render the plain-text content
#     text_content = render_to_string(
#         "welcome_email.html",  # Path to your plain-text email template
#         context={"my_variable": 42},  # Context data to pass to the template
#     )

#     # Render the HTML content
#     html_content = render_to_string(
#         "welcome_email.html",  # Path to your HTML email template
#         context={"my_variable": 42},  # Context data to pass to the template
#     )

#     # Create the email instance
#     msg = EmailMultiAlternatives(
#         "Subject here",  # Email subject
#         text_content,  # Plain-text content
#         settings.DEFAULT_FROM_EMAIL,  # From email address (get it from settings)
#         ["to@example.com"],  # Recipient email(s)
#         headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
#     )

#     # Attach the HTML content to the email instance
#     msg.attach_alternative(html_content, "text/html")

#     # Send the email
#     msg.send()

# # Call the function to send the email
# send_welcome_email()


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(user_email, user_name):
    """
    Sends a welcome email to the newly registered user.
    """
    # Render the plain-text content
    text_content = render_to_string(
        "welcome_email.html",  # Path to your plain-text email template
        context={"my_variable": user_name},  # Pass the user's name or any other data
    )

    # Render the HTML content
    html_content = render_to_string(
        "welcome_email.html",  # Path to your HTML email template
        context={"my_variable": user_name},  # Pass the user's name or any other data
    )

    # Create the email instance
    msg = EmailMultiAlternatives(
        "Welcome to Our Platform!",  # Subject
        text_content,  # Plain-text content
        settings.DEFAULT_FROM_EMAIL,  # Sender email from settings
        [user_email],  # Registered user's email
        headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},  # Optional headers
    )

    # Attach the HTML content to the email instance
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()
