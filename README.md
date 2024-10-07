# Chatbot_Unstoppable
AIT Faculty Information Bot
Overview
The AIT Faculty Information Bot is a Telegram bot designed to help students and faculty at the Army Institute of Technology (AIT) quickly find the contact information of faculty members across various departments. The bot offers an intuitive menu-based interaction, allowing users to select their preferred theme (Day or Night Mode) and browse through departments and faculty members easily.

Features
🌞 Day Mode and 🌙 Night Mode options for user-friendly visual experiences.
📚 Information on departments including ASGE, Computer, IT, ENTC, and Mechanical.
👩‍🏫 Contact details of faculty members, including heads of departments, teaching staff, and non-teaching staff.
Simple and interactive menu-based navigation using Telegram inline buttons.
Prerequisites
Python 3.6+
A Telegram account
A Telegram bot token (obtained from BotFather)
Dependencies
The bot uses the following Python libraries:

pyTelegramBotAPI (also known as telebot) for interacting with the Telegram API.
You can install the dependencies using pip:

bash
Copy code
pip install pyTelegramBotAPI
Setup and Installation
1. Get the Bot Token
To create your own Telegram bot:

Talk to BotFather on Telegram.
Create a new bot and get the API token.
2. Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/ait-faculty-info-bot.git
cd ait-faculty-info-bot
3. Update the Bot Token
Open the bot.py file in a text editor and replace the placeholder YOUR_API_TOKEN with the token you received from BotFather:

python
Copy code
API_TOKEN = "YOUR_API_TOKEN"
4. Run the Bot
Run the bot using Python:

bash
Copy code
python bot.py
The bot will now be running and polling Telegram for updates. Make sure you are connected to the internet.

5. Interact with the Bot
Find your bot on Telegram by its username (created during the BotFather setup) and start a conversation by typing /start.

Project Structure
bash
Copy code
.
├── bot.py              # Main bot script containing the logic
├── README.md           # Instructions for setting up the bot
└── requirements.txt    # Python dependencies (optional)
Bot Commands
/start - Start the bot and initiate theme selection.
Interactions
Theme Selection: Choose between Day Mode and Night Mode.
Department Selection: After theme selection, choose the department you want information for.
Faculty Type Selection: Choose the type of faculty (Head of Department, Teaching, Non-Teaching).
Faculty Contact: View the contact details (email and phone) of the selected faculty member.
Future Improvements
Dynamic Data: Add more departments or update faculty details as needed.
Additional Features: Allow users to search for faculty by name or role.
Error Handling: Improve error messages and handling for invalid or incomplete interactions.
