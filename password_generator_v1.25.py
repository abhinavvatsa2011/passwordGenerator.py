import random
def password_generator(x):
    cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    small_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    spcl_char=['~','`','!','@','#','$','%','^','&','*','(',')','-','_','[',']','{','}',':',';','"',"'",'<','>',',','.','/','?','|']
    pwrd=""
    for i in range(0,(x+1),1):
        l=[1,2,3,4]
        ch=random.choice(l)
        if ch==1:
            pw=random.choice(cap_letters)
        elif ch==2:
            pw=random.choice(small_letters)
        elif ch==3:
            pw=str(random.choice(num))
        elif ch==4:
            pw=random.choice(spcl_char)
        pwrd=pwrd+pw
    print(pwrd)
            

n=int(input("Enter the length of characters here "))
password_generator(n)