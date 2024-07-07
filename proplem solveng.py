# 1
def new_numbers(x, y):
    odd=[]
    even=[]
    for new_numbers in range (x , y+1):
        if new_numbers % 2 == 0 :
            even.append(new_numbers)
        else:
            odd.append(new_numbers)
            
    return f"odd :{odd} ,\n ,even : {even}" 

# print(new_numbers( 1 ,100))

def divided(x , y):
    resalt=[]
    for num in range (1,101):
        if  num % x == 0 and num % y == 0 :
            resalt.append(num)
    return resalt 

# print(divided(8 , 6))

def multiplication_table( x , y):
    for num in range(x , y+1):
        for mult in range (1 , 11):
            print(f"{num} * {mult} = { num *  mult}")
        print('--------------------')
# print(multiplication_table(1 ,3))

# 4
def  sentence(new_sentance):
    my_sen = new_sentance.split(" ")
    lest=[]
    for result in my_sen:
        if result not in  lest :
            lest.append(result)
    return lest

# print(sentence("ahmed mohamed ezaat ahmed"))

# 5

def  how_many_words(sentence):
    result = sentence.split(" ")
    print(result)
    lest= 0
    for words in result :
        if words == "" :
            continue
        lest += 1

    return lest

# print(how_many_words("ahmed  mohamed ezaat "))


# 6

def  remove(sentence , word ):
    # return sentence.replace(word, "")
    new_sentance = sentence.split(" ")
    new_word = word.split(" ")

    lest = []
    for word1 in new_sentance:
        for word2 in new_word:
            if word1 not in new_word and word1 != "" :
                lest.append(word1)
                break 
    final=" ".join(lest) 
    return final
# print(remove("ahmed mohamed ezaat hasaan", "ahmed mohamed") )   

# 7

def the_sentence ( sentence , word ):
    new_sentance = sentence.split(" ")
    result=0
    for new in new_sentance :
        if word == new:
            result +=1
    return result

# print(the_sentence("my name is is ahmed mohamed", "is")) 


# 8

def  divide ( x , y ):
    lest=[]
    for new in range( x ,101):
        if new % y  == 0 :
            lest.append(new)
    return lest
# print(divide(33 , 2))


lset_com=[ num for num in range (1,11) if num >=5 ]
# print(lset_com)







Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]

def num():
    new_name=[]
    for new in Names :
        n =new.upper()
        new_name.append(n)
    return new_name
# print(num())

def lest_com2():
    new=[ word.upper() for word in Names ]
    return new 
# print(lest_com2())

def upper(num):
    return num.upper()

زب_المنجا= list(map(upper , Names))

# print(زب_المنجا)


Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]

def contain_a():
    lest=[]
    for name in Names :
        if "a" in name  :
            lest.append(name)
            continue
    return lest 

# print(contain_a())


def lset_com3():
    lise=[ name for name in Names  if "a" in name]
    return lise

# print(lset_com3())



def name_map(num):
    if "t" in num :
        return num

new_name = list(filter(name_map , Names))

# print(new_name)




Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
    

def new_name():
    lest=[]
    for num in Names :
        if num[0] == "t" :
            lest.append(num)
    return lest 

# print(new_name())

def name():
    return [num for num in Names if num[0]=="t"]

# print(name())


def num(name):
    if name[0]== "t":
        return name

new_name= list(filter(num , Names ))

# print(new_name)



Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]

def name():
    lest=[]
    for num in Names:
        n1=num.count("a")
        if n1 >= 2 :
            lest.append(num)
    print(lest)

# print(name())

def name():
    return [num for num in Names  if num.count("a") >= 2 ]

# print(name())


def name(num):
    if num.count("a") >= 2 :
        return num 

new_name=list(filter(name , Names))

# print(new_name)




Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]

def num():
    lest=[]
    for num in Names:
        n1=len(num)
        lest.append(n1)
    print(lest)

# print(num())

def name():
    return [len(num) for num in Names ]

# print(name())

def name(num):
    return len(num)
new=list(map(name , Names))

# print(new)    




Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]

a, *b = Names
# print(a , b)

a , *_ , b = Names
# print(a,b )

a , b , *_ =Names
# print(a ,b )




