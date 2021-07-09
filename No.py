import random
a=random.randint(1,10)

chances=3
while(chances!=0):
    g=int(input("guess the number : "))
    if(g==a):
        print("YOU WON")
        break
    else:
        print("TRY AGAIN")
    chances=chances-1