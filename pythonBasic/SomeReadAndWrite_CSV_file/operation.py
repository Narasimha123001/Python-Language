with open("C://datapy//data.csv", "r") as f, open("C://datapy//output.csv","w") as out:
    out.write("Compamy Name,PE Ratio,PB Ratio\n")

    next(f) #skip the first line for headings

    for line in f:
        tokens = line.strip().split(",")
        company_name=tokens[0]
        price =float(tokens[1])
        eps=float(tokens[2])
        book_value=float(tokens[3])


        #calculations

        pe_ratio =round(price / eps,2)
        pb_ratio =round(price / book_value, 2)

        #write the calculations ratio in the output files
        out.write(f"{company_name},{pe_ratio},{pb_ratio}\n")
print(type(f))


