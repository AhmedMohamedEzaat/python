
# 1

def numbers(x,y):
    odd =[]
    even=[]
    for numbers in range(x , y+1):
        if numbers % 2 == 0 :
            even.append(numbers)
        else:
            odd.append(numbers)
    return odd,even
# print(numbers(1,100))  


# 2
def divided(x,y):
    result=[]
    for num in range(1,101):
        if num % x == 0 and num % y == 0 :
            result.append(num)
    return result 
# print(divided(5,7)) 

# 3
def  multiplication_table(x,y):
    for num in range(x,y+1):
        for nums in range(1,11):
            print(f"{num} * {nums} = {num * nums}")
        print("_________________")

print(multiplication_table(1,3))

# 4

def duplicated_words(sentance):
    old_sentance= sentance.split(" ")
    new_sentance=[]
    for word in old_sentance :
        if word in new_sentance :
            continue
        else:
            new_sentance.append(word)
    return new_sentance 

# print(duplicated_words("my name is is is ahmed"))


# 5

def words_in_the_sentence(sentence):
    result = sentence.split(" ")
    num_of_word = 0 
    for word in result :
        if word == "" :
            continue
        else:
            num_of_word += 1    
    return num_of_word


# print(words_in_the_sentence(" ahmed mohamed ezaat hasaan  "))
    


# 6
def remove_the_word(sentence, word ):
    # return sentence.replace(word, '')
    new = sentence.split(" ")
    new2= word.split(' ')
    result=[]
    for word1 in new :
        for word2 in new2 :
            if word1 not in new2 :
               result.append(word1)
               break
    return " ".join(result)

# print(remove_the_word("my name is ahmed mohamed ezaat" , "ahmed mohamed "))

# 7

def how_many_time_the_word(sentence , word ):
    # return sentence.count(word)
    new_sentance = sentence.split(" ")
    result = 0
    for word1 in new_sentance :
        if word == word1 :
            result += 1
    return result

print(how_many_time_the_word("ahmed mohamed ezaat ahmed ", "ahmed"))































































