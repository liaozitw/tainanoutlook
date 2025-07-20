import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# The SCOPES variable defines the permissions the application requests.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    """Runs the interactive authorization flow and saves the token."""
    # Create the flow using your client secrets file.
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)

    # The prompt='consent' ensures that you are prompted for consent every time,
    # which is necessary to receive a refresh token.
    creds = flow.run_local_server(port=8080, prompt='consent')

    # Save the credentials for the server to use.
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

    print("Successfully created token.json.")
    print("You can now upload this file to your server in the correct directory.")

if __name__ == '__main__':
    main()
