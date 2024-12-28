Import requests
Import json
Import time
From datetime import datetime

# Clear screen function
Def cls():
    Print("\033[2J\033[H", end="")

# Logo display function
Def logo():
    Print("""
\033[1;36m
$$$$$$$\   $$$$$$\     $$$$$\ 
$$  __$$\ $$  __$$\    \__$$ |
$$ |  $$ |$$ /  $$ |      $$ |
$$$$$$$  |$$$$$$$$ |      $$ |
$$  __$$< $$  __$$ |$$\   $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |\$$$$$$  |
\__|  \__|\__|  \__| \______/

\033[1;34mSend Messages to Non-End-to-End Encrypted Chats
\033[1;33mDeveloped by: Your Name Raj Thakur 
""")

# Messenger function to send messages
Def message_on_messenger(token, thread_id, messages, delay):
    Headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Updated API URL
    Url = f"https://www.facebook.com/profile.php?id=61571112957467{thread_id}/messages"

    For message in messages:
        Data = {
            "Message": message.strip()
        }
        Response = requests.post(url, headers=headers, json=data)
        Timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        If response.status_code == 200:
            Print(f"\033[1;32m[✓] {timestamp} - Message sent: {message.strip()}")
        Else:
            Print(f"\033[1;31m[×] {timestamp} - Failed to send message: {response.text}")
        
        Time.sleep(delay)

# Main script
If __name__ == "__main__":
    Cls()
    Logo()

    # User inputs
    Print("\033[1;34m[+] Enter your Facebook Graph API token:")
    Token = input("Token: ").strip()

    Print("\033[1;34m[+] Enter the thread ID where you want to send messages:")
    Thread_id = input("Thread ID: ").strip()

    Print("\033[1;34m[+] Enter the name of the text file containing messages:")
    File_name = input("File Name: ").strip()

    Print("\033[1;34m[+] Enter the delay time (in seconds) between each message:")
    Delay = int(input("Delay (seconds): "))

    # Reading messages from the file
    Try:
        With open(file_name, 'r', encoding='utf-8') as file:
            Messages = file.readlines()
    Except FileNotFoundError:
        Print("\033[1;31m[×] Error: File not found!")
        Exit(1)

    Print("\033[1;32m[✓] Starting to send messages...\n")

    # Sending messages
    Message_on_messenger(token, thread_id, messages, delay)

    Print("\033[1;32m[✓] All messages sent successfully!")
