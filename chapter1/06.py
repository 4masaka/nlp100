from typing import Sequence

def ngram(seq: Sequence, n: int):
    return [seq[i:i+n] for i,_ in enumerate(seq)]

x = set(ngram("paraparaparadise", 2))
y = set(ngram("paragraph", 2))

print(x|y) # 和集合
print(x&y) # 積集合
print(x-y) # 差集合

print("se" in x) # "se"がxに含まれるか
print("se" in y) # "se"がyに含まれるか
