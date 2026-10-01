from datetime import datetime, timezone, timedelta

print("Bot: Hi, I am PyBot. Type help to see what I can do.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Bye, see you later!")
        break

    elif user == "help":
        print("Bot: Try saying hello, asking my name, the time, or the date.")

    elif "hello" in user:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I'm good, thanks!")

    elif "name" in user:
        print("Bot: My name is PyBot.")

    elif "time" in user:
        now = datetime.now(timezone(timedelta(hours=5)))
        print("Bot: The time is", now.strftime("%H:%M"))

    elif "date" in user:
        now = datetime.now(timezone(timedelta(hours=5)))
        print("Bot: Today is", now.strftime("%d-%m-%Y"))

    else:
        print("Bot: I don't get that. Type help for ideas.")