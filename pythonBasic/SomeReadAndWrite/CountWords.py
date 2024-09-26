with open("C://datapy//book.txt","r") as f:

    total_words=0
    for line in f:
        words=line.split()
        total_words+=len(words)

with open("C://datapy//book.txt",'a') as f:
    f.write("\n Total words:" +str(total_words))
