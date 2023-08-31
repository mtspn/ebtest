import requests

# Eventbrite API endpoint for event information
EVENTBRITE_EVENT_URL = "https://www.eventbriteapi.com/v3/events/{}"

# Eventbrite API endpoint for attendee information
EVENTBRITE_ATTENDEE_URL = "https://www.eventbriteapi.com/v3/events/{}/attendees/"

# Your Eventbrite API token (replace with your actual token)
API_TOKEN = "YOUR_EVENTBRITE_API_TOKEN"

# List of Event IDs for the events you want to retrieve attendee lists for
event_ids = ["EVENT_ID_1", "EVENT_ID_2"]  # Add your event IDs here

# Function to retrieve event information
def get_event_info(event_id):
    event_url = EVENTBRITE_EVENT_URL.format(event_id)
    params = {"token": API_TOKEN}

    response = requests.get(event_url, params=params)

    if response.status_code == 200:
        event_data = response.json()
        event_date = event_data['start']['local']

        return event_date
    else:
        print(f"Failed to retrieve event information for Event ID {event_id}. Status Code: {response.status_code}")
        return None

# Function to retrieve attendee emails for a given event ID
def get_attendee_emails(event_id):
    attendee_url = EVENTBRITE_ATTENDEE_URL.format(event_id)
    params = {"token": API_TOKEN}

    response = requests.get(attendee_url, params=params)

    if response.status_code == 200:
        attendee_data = response.json()

        print(f"Event ID: {event_id}")
        event_date = get_event_info(event_id)
        if event_date:
            print(f"Event Date: {event_date}")

        print("Attendee Emails:")
        for attendee in attendee_data['attendees']:
            print(f"Attendee Email: {attendee['profile']['email']}")
        print()
    else:
        print(f"Failed to retrieve attendee list for Event ID {event_id}. Status Code: {response.status_code}")

# Iterate through the list of event IDs and retrieve attendee emails and event dates
for event_id in event_ids:
    get_attendee_emails(event_id)
