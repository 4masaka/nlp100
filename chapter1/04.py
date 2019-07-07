s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {n : e[0] if n+1 in l else e[:2] for n, e in enumerate(s.split())}
print(result)