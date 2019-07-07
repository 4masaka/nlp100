s = "All legislative powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives."

def cipher(sentence: str):
    return "".join([chr(219-ord(s)) if s.islower() else s for s in sentence])

encrypted = cipher(s) # 暗号化
decrypted = cipher(encrypted) # 複号化
print(encrypted)
print(decrypted)