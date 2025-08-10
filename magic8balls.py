import random

magic8ball_messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print("ASK A YES OR NO QUESTION!")
user_reply = input(">")
print(magic8ball_messages[random.randint(0, len(magic8ball_messages) - 1)])