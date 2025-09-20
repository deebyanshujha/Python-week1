emoji_map = {
    "love" : "❤️",
    "happy" :"😊",
    "code" : "💻",
    "tea" : "🍵",
    "music" : "🎵",
    "food" : "🍔"
}

msg = input("enter your message : ")

updated_words = []

for word in msg.split():
    clean = word.lower().strip(".,!?")
    emoji = emoji_map.get(clean,"")
    if emoji:
        updated_words.append(f"{word} {emoji} ")
    else:
        updated_words.append(word)

updated_msg = " ".join(updated_words)
print("enhanced message:\n")
print(updated_msg)

