import datetime
import time
from typing import List, Dict

# Placeholder functions for API integrations
def get_text_messages() -> List[Dict]:
    # TODO: Implement actual API call to retrieve text messages
    return [{"sender": "Alice", "content": "Hey, how's it going?", "timestamp": datetime.datetime.now() - datetime.timedelta(days=7)}]

def get_whatsapp_messages() -> List[Dict]:
    # TODO: Implement actual API call to retrieve WhatsApp messages
    return [{"sender": "Bob", "content": "Let's catch up soon!", "timestamp": datetime.datetime.now() - datetime.timedelta(days=10)}]

def prompt_user(contact: str):
    print(f"It's been a while since you talked to {contact}. Would you like to follow up?")
    response = input("Enter 'y' for yes, 'n' for no: ")
    if response.lower() == 'y':
        print(f"Great! Don't forget to reach out to {contact}.")
    else:
        print("Okay, maybe next time.")

def check_last_interaction(messages: List[Dict], threshold_days: int) -> List[str]:
    current_time = datetime.datetime.now()
    contacts_to_follow_up = []
    
    for message in messages:
        days_since_last_interaction = (current_time - message['timestamp']).days
        if days_since_last_interaction >= threshold_days:
            contacts_to_follow_up.append(message['sender'])
    
    return contacts_to_follow_up

def main():
    threshold_days = 7  # Adjust this value as needed
    
    while True:
        text_messages = get_text_messages()
        whatsapp_messages = get_whatsapp_messages()
        all_messages = text_messages + whatsapp_messages
        
        contacts_to_follow_up = check_last_interaction(all_messages, threshold_days)
        
        for contact in contacts_to_follow_up:
            prompt_user(contact)
        
        # Wait for 24 hours before checking again
        time.sleep(24 * 60 * 60)

if __name__ == "__main__":
    main()