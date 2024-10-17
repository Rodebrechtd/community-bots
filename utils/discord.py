import requests
import sys

def send_discord_message(webhook_url, message):
    if not webhook_url:
        raise ValueError("Discord webhook URL is missing or invalid.")
    
    try:
        payload = {
            'content': message
        }
        response = requests.post(webhook_url, data=payload)

        # If the status code is anything other than success (204 for Discord), fail the job
        if response.status_code != 204:
            print(f"Failed to send message: {response.status_code} - {response.text}")
            sys.exit(1) 
        else:
            print("Message sent successfully!")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1) 

def send_discord_message_with_local_image(webhook_url, message, image_path=None):
    if not webhook_url:
        raise ValueError("Discord webhook URL is missing or invalid.")

    if not image_path:
        raise ValueError("Image path is missing or invalid.")

    try:
        with open(image_path, 'rb') as f:
            files = {'file': f}
            payload = {
                'content': message
            }
            response = requests.post(webhook_url, files=files, data=payload)

        # If the status code is anything other than success (200 for file upload), fail the job
        if response.status_code != 200:
            print(f"Failed to send message: {response.status_code} - {response.text}")
            sys.exit(1) 
        else:
            print("Message with image sent successfully!")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1) 
    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")
        sys.exit(1)  