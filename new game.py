'''
make a game that do have 3 games:     
    1 - remove duplicate 
    2 - multiplication tuble
    3 - divided py
    4 - Exit the game 
    5 - play agin 
    
'''


class Games():
    def __init__(self):
        while True :
            User_input = int(input('''please choose number game :
            1 - remove duplicate
            2 - multiplication tuble
            3 - divided py
            4 - Exit the game
            '''))

            if User_input == 1 :
                self.remove_duplicate()

            elif User_input == 2 :
                self.multiplication_tuble()

            elif User_input == 3 :
                self.divided_py()

            elif User_input == 4 :
                print("goodbye......")
                return
            
            else :
                print("choose btwen 1 , 4")
        
            play_again = input("Do you want play again \n wrait yes to play again , no to exit: ")
            if play_again == "no" :
                print("goodbye....")
                break


    def remove_duplicate(self):
        sentanc = input("enter your sentance : ")
        new_sentanc = sentanc.split(" ")
        result = []
        for word in new_sentanc :
            if word not in result:
                result.append(word)
        final = " ".join(result)
        return print(final)




    def multiplication_tuble(self):
        x = int(input("input in first number : "))
        y = int(input("input in sacand number : "))


        for num1 in range(x , y+1):
            for num2 in range( 1 , 13):
                print(f"{num1} x {num2} = {num1 * num2}")
            print("_____________________")



    def divided_py(self):
        x = int(input("input in first number : "))
        y = int(input("input in sacand number : "))
        result = []
        for num in range(1 , 101):
            if num % x == 0 and num % y == 0 :
                result.append(num)
        return print(result)






#     def __str__(self):
#         return""
    
#     def __repr__(self):
#         return self.__str__()


# print(Games())









'''
make a game that do have 3 games:     
    1 - remove duplicate 
    2 - multiplication tuble
    3 - divided py
    4 - Exit the game 
    5 - play agin 
    
'''


class Games():
    def __init__(self):
        while True:
            User_input = int(input('''inter your game number : 
            1 - remove duplicate 
            2 - multiplication tuble
            3 - divided py
            4 - Exit the game   
             : '''))


            if User_input == 1 :
                self.remove_duplicate()
            
            if User_input == 2 : 
                self.multiplication_tuble()
            
            if User_input == 3 :
                self.divided_py()

            if User_input == 4 :
                print("goodbye....")
                return
            
            else :
                print("choose btwen 1 , 4")
            
            play_again = input("Do you want play again \n wrait yes to play again , no to exit: ")
            if play_again == "no" :
                print("goodbye........")
                break



    def remove_duplicate(self):
        sentanc = input("boot your sentanc : ")
        new_sentanc = sentanc.split(" ") 
        word = []


        for new_word in new_sentanc :
            if new_word not in word :
                word.append(new_word)
        final = " ".join(word)
        return print(final)




    def multiplication_tuble(self):
        x = int(input("boot your first number : " ))
        y = int(input("boot your sacand number : " ))


        for num1 in range( x , y+1 ):
            for num2 in range(1 , 13):
                print(f"{num1} x {num2} = {num1 * num2}")
            print ("________________")



    def divided_py(self):
        x = int(input("boot your first number : " ))
        y = int(input("boot your sacand number : " ))
        result = []
        for num in range( 1 , 101 ):
            if num % x == 0 and num % y == 0 :
                result.append(num)
        return print(result)



    def __str__(self):
        return ""
    def __repr__(self):
        return self.__str__

print(Games())