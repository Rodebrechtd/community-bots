import requests

def send_discord_message(webhook_url, message):
    if not webhook_url:
        raise ValueError("Discord webhook URL is missing or invalid.")
    try:
        payload = {
            'content': message
        }
        response = requests.post(webhook_url, data=payload)
        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

def send_discord_message_with_local_image(webhook_url, message, image_path=None):
    try:
        with open(image_path, 'rb') as f:
            files = {'file': f}
            payload = {
                'content': message
            }
            response = requests.post(webhook_url, files=files, data=payload)
            if response.status_code == 200:
                print("Message sent successfully!")
            else:
                print(f"Failed to send message: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")