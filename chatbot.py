import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

responses = {
    "hello": [
        "Hello! 👋 How can I help you?",
        "Hi there! Nice to meet you!",
        "Hey! 😊 How are you doing?"
    ],
    "hi": [
        "Hi! 👋",
        "Hello! How are you?",
        "Hey there! 😊"
    ],
    "how are you": [
        "I'm doing great! Thanks for asking. 😊",
        "I'm fine and ready to chat!",
        "Doing well! How about you?"
    ],
    "your name": [
        "I'm SimpleBot 🤖.",
        "You can call me SimpleBot!"
    ],
    "who are you": [
        "I'm a simple Python chatbot designed for basic conversations.",
        "I'm SimpleBot, your friendly little chatbot! 🤖"
    ],
    "thank": [
        "You're welcome! 😊",
        "No problem!",
        "Happy to help!"
    ],
    "good morning": [
        "Good morning! ☀️ Have a wonderful day!",
        "Good morning! How can I help you?"
    ],
    "good night": [
        "Good night! 🌙 Sleep well!",
        "Good night! See you soon!"
    ],
    "what can you do": [
        "I can have basic conversations, tell you the time and date, and respond to common questions."
    ]
}

def get_response(user_message):
    message = user_message.lower().strip()

    if message in ["bye", "goodbye", "exit", "quit"]:
        return random.choice([
            "Goodbye! 👋 Have a great day!",
            "See you later! 😊",
            "Bye! Take care!"
        ])

    if "time" in message:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}. 🕐"

    if "date" in message or "today" in message:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}. 📅"

    for keyword, replies in responses.items():
        if keyword in message:
            return random.choice(replies)

    if "i am" in message or "i'm" in message:
        return "That's nice! Tell me more. 😊"

    if "good" in message:
        return "That's great to hear! 👍"

    if "sad" in message:
        return "I'm sorry you're feeling that way. I hope things get better. 💙"

    if "happy" in message:
        return "That's wonderful! 😊"

    if "help" in message:
        return "Sure! You can talk to me about basic everyday topics."

    return random.choice([
        "Interesting! Tell me more. 😊",
        "I understand. What else would you like to talk about?",
        "That's interesting!",
        "I'm still learning, but I'd love to continue chatting!",
        "Could you tell me a little more?"
    ])

def add_message(sender, message, sender_type):
    chat_area.config(state=tk.NORMAL)

    if sender_type == "user":
        chat_area.insert(tk.END, "\nYou\n", "user_name")
        chat_area.insert(tk.END, f"{message}\n", "user_message")
    else:
        chat_area.insert(tk.END, "\nSimpleBot 🤖\n", "bot_name")
        chat_area.insert(tk.END, f"{message}\n", "bot_message")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

def send_message(event=None):
    message = input_box.get().strip()
    if not message:
        return

    add_message("You", message, "user")
    input_box.delete(0, tk.END)

    response = get_response(message)
    window.after(300, lambda: add_message("SimpleBot", response, "bot"))

def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)
    chat_area.config(state=tk.DISABLED)
    add_message("SimpleBot", "Chat cleared! 👋 How can I help you?", "bot")

window = tk.Tk()
window.title("SimpleBot - AI Chatbot")
window.geometry("700x650")
window.minsize(600, 550)
window.configure(bg="#f5f7fb")

header = tk.Frame(window, bg="#ffffff", height=75)
header.pack(fill=tk.X)
header.pack_propagate(False)

title = tk.Label(
    header, text="🤖 SimpleBot",
    font=("Segoe UI", 22, "bold"),
    bg="#ffffff", fg="#222222"
)
title.pack(side=tk.LEFT, padx=25, pady=15)

subtitle = tk.Label(
    header, text="Basic Conversation Chatbot",
    font=("Segoe UI", 10),
    bg="#ffffff", fg="#777777"
)
subtitle.pack(side=tk.LEFT, pady=18)

chat_frame = tk.Frame(window, bg="#f5f7fb")
chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(15, 10))

chat_area = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="#ffffff",
    fg="#333333",
    relief=tk.FLAT,
    borderwidth=0,
    padx=15,
    pady=15
)
chat_area.pack(fill=tk.BOTH, expand=True)

chat_area.tag_config("user_name", font=("Segoe UI", 10, "bold"), foreground="#2563eb")
chat_area.tag_config("user_message", font=("Segoe UI", 11), foreground="#222222", spacing3=8)
chat_area.tag_config("bot_name", font=("Segoe UI", 10, "bold"), foreground="#16a34a")
chat_area.tag_config("bot_message", font=("Segoe UI", 11), foreground="#333333", spacing3=8)
chat_area.config(state=tk.DISABLED)

input_frame = tk.Frame(window, bg="#ffffff", height=70)
input_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
input_frame.pack_propagate(False)

input_box = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg="#f1f3f6",
    fg="#222222",
    relief=tk.FLAT,
    bd=0
)
input_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 8), pady=12, ipady=10)

send_button = tk.Button(
    input_frame,
    text="Send ➤",
    font=("Segoe UI", 10, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief=tk.FLAT,
    bd=0,
    cursor="hand2",
    command=send_message
)
send_button.pack(side=tk.LEFT, padx=(0, 8), pady=12, ipadx=12)

clear_button = tk.Button(
    input_frame,
    text="Clear",
    font=("Segoe UI", 10),
    bg="#e5e7eb",
    fg="#333333",
    activebackground="#d1d5db",
    relief=tk.FLAT,
    bd=0,
    cursor="hand2",
    command=clear_chat
)
clear_button.pack(side=tk.LEFT, padx=(0, 10), pady=12, ipadx=8)

input_box.bind("<Return>", send_message)

add_message(
    "SimpleBot",
    "Hello! 👋 I'm SimpleBot. How are you today?",
    "bot"
)

input_box.focus()
window.mainloop()
