from datetime import datetime
import os
a = "NEZUKO  "
my = open("h.txt","r")
i = my.read()
print(i)
my = open("s.txt","r")
s1 = my.read()
print(s1)
J = open("maaz.txt","r")
J1 = J.read()
print(J1)

#i = my.read()


#for i in range(0,10):
 #    print(i)
def sample_respons(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi","hey" ):

        return "hi"

    if user_message in ("manish", "i love you",):
        return i
    if user_message in ("somesh", "i love you",):
        return s1
    if user_message in ("maaz", "JNTU",):
        return J1



    if user_message in ("who are you", "who are you?" ):
        return a





#    if user_message in ("fuck you", "who are you?"):
 #       return "i am nezuko"
    if user_message in ("time", "time?",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y,%H:%M:%S")
        return str(date_time)
    return "i cannot understand"

