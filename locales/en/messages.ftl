### Bot Translation File to Russian
### Author: Shuwiku (shuwiku@gmail.com)
### License: MIT License


## Terms

-bot-name = 🤖 Prize Drawing Bot


## Bot Buttons

button-cancel = ❌ Cancel

button-register = ✅ Register


## Bot Responses

# Command or cancellation request (/cancel)
action-canceled = ❌ Action canceled.

# Command /language without arguments. Sent along with an inline keyboard listing languages
language-change = 📃 Please select a language from the list below:

# User did not press the buttons from the inline keyboard and wrote a message
language-change-default = Please use the buttons attached to the message.

    ❌ You can cancel the action with the command: <i>/cancel</i>.

    ⚠️ If you are unable to press a button, use the syntax: <i>/language language</i>.

    📃 You can get a list of available languages with the command: <i>/languages</i>.

# User changed language
language-change-successfully = Language set to - <b>{ $language }</b>

# User used the /language command with an argument but provided an incorrect language
language-not-found = ❌ Language <i>{ $language }</i> not found! Please choose a language from the list.
    You can view the list of available languages using the command: <i>/languages</i>.

# A nice list of bot locales. I haven't figured out how to generate it automatically yet
languages-list = List of bot locales:
    
    <b>en</b> - 🇺🇸 English
    <b>ru</b> - 🇷🇺 Русский

# Locale EN
locale-en = 🇺🇸 English

# Locale RU
locale-ru = 🇷🇺 Русский


# Message is not from a user
# Used by the filter filters.MessageFromUser()
message-not-from-user = ❌ Unable to process the message!
    The message did not come from a user.

# When receiving the /start command
start = <b>{-bot-name}</b> is a simple yet functional bot for conducting raffles.

    The bot can start, conduct raffles, and select winners using a referral link system, and it also has bot protection in the form of CAPTCHA.

# Additional message when receiving the /start command if the user is not registered
start-user-not-registered = ✅ By default, the bot does not store any information about you, so access to most features will be limited. Use the <i>/register</i> command to gain access to the bot's services.

# Sent from the filter filter.UserRegistered() if the user is not registered
user-not-registered = ❌ Access is only for registered users.
    Use the <i>/register</i> command to register with the bot.


# User registration in the bot
user-registration = ⚠️ After confirming your registration, the bot will save your Telegram ID in the database. Please note that the profile ID cannot be changed, so be careful when using any bots.

    ✅ At any time, you can request the deletion of your data from the bot, after which your profile will be removed from the current database <b>but not from backups</b>! Deleting your profile will also cancel your participation in all registered raffles.

# User used the /register command, but they are already in the database
user-registration-already-registered = ✅ You are already registered!

# User confirmed registration in the bot
user-registration-confirm-accept = ✅ You have been successfully registered!

# User declined registration in the bot
user-registration-confirm-decline = ❌ You canceled the registration.

# Confirmation of registration in the bot, but the user did not choose Yes or No and wrote something else
user-registration-confirm-default = ❌ Please use the buttons attached to the confirmation message. You can also cancel the action with the command <i>/cancel</i>.

