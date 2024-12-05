### Bot Translation File to Russian
### Author: Shuwiku (shuwiku@gmail.com)
### License: MIT License


## Terms

-bot-name = 🤖 Prize Drawing Bot


## Bot Buttons

button-cancel = ❌ Cancel

button-language = 🏳️ Language

button-profile = 👤 Profile


## Bot Responses

# Command or cancellation request (/cancel)
action-canceled = ❌ Action canceled.

# Used by the filters.CallbackHaveMessage()
callback-have-not-message = ❌ Callback could not be processed!

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

# Bot Menu Message
menu = Main sections of the bot:

    <b>👤 Profile</b> - Displays your profile

    <b>🏳️ Language</b> - Change the language in the bot


# Message is not from a user
# Used by the filter filters.MessageFromUser()
message-not-from-user = ❌ Unable to process the message!
    The message did not come from a user.

# User Information Message
profile = 👤 User Profile <b>{ $username }</b>

    <b>Language:</b> { $language }
    <b>Draws Conducted:</b> { $draw_count }
    <b>Registered:</b> { $registration_date }

# When receiving the /start command
start = <b>{-bot-name}</b> is a simple yet functional bot for conducting raffles.

    The bot can start, conduct raffles, and select winners using a referral link system, and it also has bot protection in the form of CAPTCHA.
