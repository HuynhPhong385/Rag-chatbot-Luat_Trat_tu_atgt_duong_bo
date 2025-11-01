from src.loader import load_data
from src.matcher import SemanticMatcher
from src.chatbot import Chatbot

import src.matcher
import os
print(f"Đường dẫn file matcher: {src.matcher.__file__}")
print(f"Các hàm/lớp trong file: {dir(src.matcher)}")


data = load_data("data/Cau_hoi_thi+GPLX.json")

matcher = SemanticMatcher(data)
bot = Chatbot(matcher)

while True:
    q = input("Bạn: ")

    if q.lower() == "exit":
        break

    print("Bot:", bot.ask(q))