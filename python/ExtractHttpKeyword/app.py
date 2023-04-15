try:
    with open(input("readfile<links>: "),"r") as f:
        list = f.readlines()
        for l in list:
            char = l.split(" ")
            for c in char:
                if "http" in c:
                    with open("list.txt","a") as w:
                        w.writelines(c)
except: 
    print("invalid input")