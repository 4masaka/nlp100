from typing import Sequence

s = "I am an NLPer"

def ngram(seq: Sequence, n: int):
    return [seq[i:i+n] for i,_ in enumerate(seq)]

print(ngram(s, 2)) # 文字bi-gram
print(ngram(s.split(), 2)) # 単語bi-gram