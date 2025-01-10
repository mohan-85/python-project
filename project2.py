import random
import string

newwrd= [] 

def encoding(msg):
    words=msg.split()
    for word in words:
        if(len(word)>=3):
            s1=word[1:]+word[0]
            r1=''.join(random.choice(string.ascii_letters)for i in range(3))
            r2= ''.join(random.choice(string.ascii_letters)for i in range(3))  
            encoded=r1+s1+r2
            newwrd.append(encoded)
        else:
            newwrd.append(word[::-1])
    return ' '.join(newwrd)        

def decoding(encomsg):
    words=encomsg.split()
    for word in words:
        if (len(word)>6):
            rmr=word[3:-3]
            corew=rmr[-1]+rmr[:-1]
            newwrd.append(corew)
        else:
            newwrd.append(word[::-1]) 
    return " ".join(newwrd)  
            

user=input("enter your msg:")
choice=input("entr your choice e for encoding d for decoing e/d:")

if (choice == "e"):
    encod=encoding(user)
    print(encod)
elif(choice=="d"):
    decod=decoding(user)
    print(decod)
else:
    print("pleace enter right option")   


