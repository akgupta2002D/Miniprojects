import win32com.client


def extract_latest_email():
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
    else:
        print("No emails in the inbox.")


if __name__ == "__main__":
    extract_latest_email()
