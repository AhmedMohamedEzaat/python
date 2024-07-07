
class student():
    def student_info(self,name,age):
        self.name =name
        self.age  =age
        print(f"my name is {self.name} and my age is {self.age}")

    def __init__(self):
        print("welcome")
        
# s1=student()
# s1.student_info("ahmed",25)
# print(s1)



class student():
    def __init__(self, name):
        self.name= name
        self.marks=[]
        print("welcome {} in the school". format (name))
    def add_marks(self, mark):
        self.marks.append(mark)
    def avg(self):
        return sum(self.marks)/len(self.marks)
  
# s1 = student('ahmed')
# print(s1.marks)
# s1.add_marks(40)
# s1.add_marks(55)
# s1.add_marks(87)
# s1.add_marks(74)
# print(s1.marks)
# print(s1.avg())
 



class calculator():
    def __init__ (self , a , b):
        self.a = a
        self.b = b
    def sum (self):
        return self.a + self.b 
    def mult (self):
        return self.a * self.b

# calc = calculator(10,20)
# print(calc.sum())
# print(calc.mult())






class animal():
    def __init__(self,name):
        self.name = name

    def lion (self):
        print(f"{self.name} is eating meet")

class cat (animal):
    def cat_eat(self):
        print(f"{self.name} is eating food")

class dog (animal):
    def fetch (self,thing):
        print(f"{self.name} get the {thing}")

        
# zoo = cat("sokar")
# print(zoo.cat_eat())
# zoo2= dog("kaled")
# print(zoo2.fetch("meet"))
# print(zoo2.lion())




class anemal ():
    def __init__ (self , name):
        self.name=name
    def eat (self , eat):
        print(f"{self.name} is eting {eat}")
class cat (anemal):
    def like (self, like):
        print (f"{self.name} he like {like}")
class doog (anemal):
    def love (self, love):
        print(f"{self.name} is love {love}")

# zoo=doog("meet")
# print(zoo.love("meet"))
# zoo1=cat("flfl")
# print(zoo1.like("fish"))
# zoo=doog("doog")
# print(zoo.eat("meet"))





class student ():
    def __init__ (self,name):
        self.name=name
    
    def ahmed (self):
        print (f"{self.name} is fool agre")

class school (student):
    def mohamed (self , age):
        print (f" is name {self.name} and is age {age}")

class library (student):
    def ali (self):
        print (f"{self.name} is old man")


# s1=school("ahmed")
# print(s1.mohamed(20))
# s2=library("ali")
# print(s2.ali())
# print(s2.ahmed())
# print(s1.ahmed())





class zoo():
    def __init__(self,name):
        self.name=name

class anemal ():
    def __init__(self,name):
        super (dog ,self ).__init__(name)
        self.food="meet"

    def horse (self):
        print(f"{name} is like a weeds")



class A ():
    def dothis (self):
        print("doing this in A")
class B (A):
    pass
class C ():
    def dothis (self):
        print("doing this in C")
class D(B,C):
    pass


# d = D()
# d.dothis()
# print(D.mro())

 


























