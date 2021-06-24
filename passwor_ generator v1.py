#password generator base
import random
n=int(input("Enter the length of characters here "))
def password_generator():
    cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    small_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    spcl_char=['~','`','!','@','#','$','%','^','&','*','(',')','-','_','[',']','{','}',':',';','"',"'",'<','>',',','.','/','?','|']
    pwrd=""
    for i in range (0,(n-1),1):
        ch=""
        if i==0:
            r=random.randrange(1,5)
            if r==1:
               ch=random.choice(cap_letters)
            elif r==2:
                ch=random.choice(small_letters)
            elif r==3:
                ch=str (random.choice(num))
            elif r==4:
                ch=random.choice(spcl_char) 
            pwrd=pwrd+ch    
        elif i%2==1:
            if i%3==0:
                ch=random.choice(spcl_char)
            else:
                ch=random.choice(cap_letters)      
        elif i%2==0:
            if i%4==0:
                ch=random.choice(small_letters)
            else:
                ch=str(random.choice(num) )
        pwrd=pwrd+ch
    print (pwrd)

password_generator()
