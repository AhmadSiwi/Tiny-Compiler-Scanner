f = open("tiny_sample_code.txt")
out = open("scanner_output.txt", "w")
FromOther = False
while True:
    if(not FromOther):
        c = f.read(1)
    FromOther = False
    str = ""
    if not c:
        break
    elif (c==" " or c=="\n"):
        continue
    elif (c=="{"):
        while(c!="}"):
            c = f.read(1)
    elif(c=="+" or c=="-" or c=="*" or c=="/" or c=="=" or c=="<" or c=="(" or c==")" or c==";"):
        out.write(c + ": special symbol\n")
    elif(c==":"):
        out.write(":= : special symbol\n")
        c = f.read(1)
    elif (c>="0" and c<="9"):
        while (c>="0" and c<="9"):
            str += c
            c = f.read(1)
        out.write(str + ": number\n")
        FromOther = True
    elif ((c>="A" and c<="Z") or (c>="a" and c<="z")):
        while ((c>="A" and c<="Z") or (c>="a" and c<="z")):
            str += c
            c = f.read(1)
        if(str=="if" or str=="then" or str=="else" or str=="end" or str=="repeat" or str=="until" or str=="read" or str=="write"):
            out.write(str + ": reserved word\n")
        else:
            out.write(str + ": identifier\n")
        FromOther = True
