'''
print(" number       square")
print("---------------------") 
for  x in range (1,11) :
    square = x * x
    print (x , '\t', '\t', square )
'''
'''
print('number           square')
print("-------------------")
for x in range(1 ,11):
    square = x * x 
    print (x ,  '\t', '\t' , square )

'''

'''
start =int (input("ferst number : "))
end =int( input ("end numper :   "))
print("numper           square")
print("------------------------")
for x in range (start , end+1 ):
    square =   x**2
    print(x,'\t',"\t",square)

'''
'''

rows =int(input('rows :'))
colums =int(input("colums:"))
for x in range (rows) :
    for y in range (colums) :
        print ('*',end= '')
    print()     

'''
'''

for x in range (8):
    for y in range (x+1):
        print ("*" , end='')
    print()
    
'''
'''
lists =[[1,2,3],[4,5,6],[7,8,9]]
for list in lists :
    
    for x in list :
        print(end="")
        print(x)
'''

