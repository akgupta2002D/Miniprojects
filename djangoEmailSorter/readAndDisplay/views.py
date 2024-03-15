import win32com.client
from django.shortcuts import render
from .models import Email
import pythoncom
# Create your views here.


def read(request):
    context = {
        'name': 'Ankit',
    }
    return render(request, 'readAndDisplay/home.html', context)


# Retreive the Email and Show it on the screen.
"""
Changes Associated.
1. New Model name Emails to retrieve the data and store it.
2. New Display to show the image. (ShowEmail.html, css, js)
3. New View for it do display the page and let us click refresh.
"""


def extract_latest_email():
    pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch(
        "Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 corresponds to the inbox
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # True for descending order

    latest_email = messages.GetFirst()
    if latest_email:
        print(f"Subject: {latest_email.Subject}")
        print(f"Received: {latest_email.ReceivedTime}")
        print("Body:")
        print(latest_email.Body)
        # Save to database
        pythoncom.CoUninitialize()  # Uninitialize the COM library
        return {
            'subject': latest_email.Subject,
            'received': latest_email.ReceivedTime,
            'body': latest_email.Body
        }

    else:
        return None


def check_email(request):
    email_details = extract_latest_email()
    if email_details:
        # Optionally save to database
        Email.objects.create(
            subject=email_details['subject'],
            received=email_details['received'],
            body=email_details['body']
        )
        context = {'email': email_details}
    else:
        context = {'message': 'No new emails.'}
    return render(request, 'email_display.html', context)


if __name__ == "__main__":
    extract_latest_email()
