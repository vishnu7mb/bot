#import y as d
import random
j = 1
while j == 1:
    user = int(input("enter you user number"))
    name = int(input("enter your no1:"))

    name1 = int(input("enter your n02:"))
    name2 = int(input("enter your no3:"))
    h = open("r.txt")
    u = h.read()
    print(u)
    if u == "hello":
        hello = [name, name1, name2]

        h = random.choice(hello)
    if user == h:
        print("correct")
 #       print(h)
