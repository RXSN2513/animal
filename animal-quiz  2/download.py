# -*- coding: utf-8 -*-
import os, urllib.request

base = r"C:\Users\liuha\Doubao\chats\2026-09-18\new-chat\animal-quiz\assets"
os.makedirs(base, exist_ok=True)

items = [
    ("hero.jpg", "https://aka.doubaocdn.com/s/EaATE8jbh1"),
    ("cat.jpg", "https://aka.doubaocdn.com/s/7uhqc4xIsq"),
    ("dog.jpg", "https://aka.doubaocdn.com/s/SwvxREEb16"),
    ("rabbit.jpg", "https://aka.doubaocdn.com/s/tBVx202lzS"),
    ("turtle.jpg", "https://aka.doubaocdn.com/s/qMV4EvPodD"),
    ("fox.jpg", "https://aka.doubaocdn.com/s/YNlSjRlAh1"),
]

for name, url in items:
    path = os.path.join(base, name)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
            f.write(r.read())
        print("OK", name, os.path.getsize(path))
    except Exception as e:
        print("FAIL", name, repr(e))
