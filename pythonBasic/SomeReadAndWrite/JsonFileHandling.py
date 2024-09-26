book ={ }

book['tom']={
    'name':'tom',
    'adderess':'Vja',
    'phone':45697
}

book['Pop']={
    'name':'Pop',
    'adderess':'hyd',
    'phone':98796
}

import json
s=json.dumps(book)  #dumps its as json file
print(s)

with open ("C://datapy//book.txt","w") as f:
    f.write(s)

