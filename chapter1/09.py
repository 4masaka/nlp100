import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

s_list = sentence.split()

result = []
for word in sentence.split():
    word_length = len(word)
    word = "{}{}{}".format(word[0], "".join(random.sample(word[1:-1], word_length-2)), word[-1]) if word_length > 4 else word
    result.append(word)

print(" ".join(result))