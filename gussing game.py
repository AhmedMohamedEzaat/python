
print("Welcome in the Even-Odd Game ")
print("If you Wanna Close the Game Enter X")


while True :
    number = (input(" Drop your number : "))
    if number == "x" :
        print("closing the game ")
        break

    try :
        number = int(number)
        if number % 2 == 0 :
            print ("Your Number Is Ood ")
        else :
            print ("Your Number In Even") 
        
    except ValueError :
        print("Please Enter A Valid Number")
    print("________________________")