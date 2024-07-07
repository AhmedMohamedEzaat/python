class Game():
    def __init__(self):
    
        user_input = int(input('''Enter namber game
        1 - remove_duplicate 
        2 - multiplication_tuble
        3 - divided_py
        4 - Exit the game 
        ''' ))

        if user_input == 1 :
            self.remove_duplicate()
        
        elif user_input == 2 :
            self.multiplication_table()
        
        elif user_input == 3 :
            self.divided_py()
        
        elif user_input == 4 :
            print("Goodbay")

        else :
            print("is not heer please choose feom 1 or 4 ")

        

    def remove_duplicate(self):
        lest=[]
        sentence = input("Enter your sentence : ")
        new_word = sentence.split(" ")
        for word in new_word :
            if word not in lest :
                lest.append(word)
        final = " ".join(lest)
        print(final)
        

    def multiplication_tuble(self , x ,y):
        for num in  range ( x , y + 1) :
            for numbers in range (1 , 11) :
                print(f"{num} * {numbers} = {num * numbers}")
            # print("____________________"



    def divided_py(self):
            



print(Game())