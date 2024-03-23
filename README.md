Simple Keylogger

The Simple Keylogger is a Python program designed to capture and log keystrokes entered by users. It operates silently in the background, recording keystrokes into a text file.

Features:
Keystroke Logging: The program captures and logs keystrokes entered by users.
Silent Operation: It operates discreetly in the background without any visible indication to the user.
Customization: Users can customize the log file name and location according to their preferences.
Termination: The keylogger can be stopped at any time by pressing a predefined key combination.
Components:
pynput: The library used to monitor keyboard events.
Key: Represents keys on the keyboard.
Listener: Listens for and handles keyboard events.
on_press(key): Function to handle key press events and log keystrokes.
on_release(key): Function to handle key release events and stop the keylogger.
main(): The main function orchestrating the keylogger's operation and user interaction.
How to Use:
Run the program.
The keylogger starts capturing keystrokes silently in the background.
Press the predefined key combination (e.g., 'Esc') to stop the keylogger.
Access the keylog.txt file in the same directory as main.py to view the recorded keystrokes.
Example:
Suppose you run the keylogger program and type:

Hello, world!
The keylog.txt file will contain:

2024-03-11 12:00:01: 'H'
2024-03-11 12:00:02: 'e'
2024-03-11 12:00:03: 'l'
2024-03-11 12:00:04: 'l'
2024-03-11 12:00:05: 'o'
2024-03-11 12:00:06: ','
2024-03-11 12:00:07: ' '
2024-03-11 12:00:08: 'w'
2024-03-11 12:00:09: 'o'
2024-03-11 12:00:10: 'r'
2024-03-11 12:00:11: 'l'
2024-03-11 12:00:12: 'd'
2024-03-11 12:00:13: '!'
Requirements:
Python 3.x
pynput library
Usage:
python main.py
Note: Ensure that you have Python installed on your system before running the program.

Disclaimer
This keylogger program is provided for educational purposes only. Do not use it for illegal activities. Respect the privacy and consent of others before using this software.

Contributors:
[https://github.com/karthicysec]
