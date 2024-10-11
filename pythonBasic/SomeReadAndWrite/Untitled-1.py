f=open("C://datapy//book.txt","r")
s=f.read()
print(s)
print(type(s))

import json
book=json.loads(s)
print(book)
print(type(book))

print(book['Pop'])

print(book['Pop']['phone'])