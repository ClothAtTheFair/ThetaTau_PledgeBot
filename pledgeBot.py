from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hey|hello",
        ["Hello, thank you for coming in. What is your name?",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, where are you from?",]
    ],
    [
        r"i'm from (.*)",
        ["Oh cool, I've never been to %1 I'll have to go sometime! \nWhat year are you?",]
    ],
    [
        r"i'm a (.*)",
        ["ahhh, that's cool I guess. What are your plans?", "The end is almost near. What are you plans?"]
    ],
    [
        r"my plans are (.*)",
        ["ok okay.. well enough about that stuff. so why USC?",]
    ],
    [
        r"i picked usc (.*)",
        ["that's cool, not bad. I came here for...\nReasons.. What is your major?",]
    ],
    [
        r"my major is (.*)",
        ["Computer Engineering is where all the cool kids are at. \nThank you for your time. You can either say quit to end or redo this interview",]
    ],
    [
        r"quit",
        ["Goodbye, it was great meeting you!", "Talk to you soon!"]
    ],
]

def pledgeBot():
    print("Hi, I'm pledge bot! \nI was an old project brought back to life in memory of my original creator. \nPlease type in lowercase English. say hello to begin!")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    pledgeBot()