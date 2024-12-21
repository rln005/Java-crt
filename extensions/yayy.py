import pyautogui
import pyperclip
import time

def send_love_messages(message, count):
    print("Make sure WhatsApp Web is open and the chat is selected.")
    time.sleep(5)  # Time to switch to the WhatsApp Web tab

    for i in range(count):
        # Copy the message with emojis to the clipboard
        pyperclip.copy(message)
        # Paste the message into the chat box
        pyautogui.hotkey("ctrl", "v")  # For Mac, use "command" instead of "ctrl"
        pyautogui.press("enter")  # Press Enter to send the message
        print(f"Message {i + 1} sent: {message}")
        time.sleep(0.5)  # Small delay between messages

# Usage
message = "I love you 😘❤️"  # Message with emojis
count = 25  # Number of messages to send

send_love_messages(message, count)