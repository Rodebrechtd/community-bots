import requests

def send_discord_message(webhook_url, message):
    if not webhook_url:
        raise ValueError("Discord webhook URL is missing or invalid.")
    
    try:
        payload = {
            'content': message
        }
        response = requests.post(webhook_url, data=payload)

        # Check for various response statuses
        if response.status_code == 204:
            print("Message sent successfully!")
        elif response.status_code == 404 and response.json().get('code') == 10015:
            print("Failed to send message: Unknown Webhook. The webhook may have been deleted or is incorrect.")
        else:
            print(f"Failed to send message: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

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

            # Check for successful or failed responses
            if response.status_code == 200:
                print("Message sent successfully!")
            elif response.status_code == 404 and response.json().get('code') == 10015:
                print("Failed to send message: Unknown Webhook. The webhook may have been deleted or is incorrect.")
            else:
                print(f"Failed to send message: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")