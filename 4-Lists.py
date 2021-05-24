# Pirple homework assignment 4 (Python)

# Global scope variable
myUniqueList = [] 
myLeftOvers = [] 

def addList(add):
    if add in myUniqueList:       
        myLeftOvers.append(add)   
        return False              
    else:                         
        myUniqueList.append(add)  
        return True               


print("")
# Push some data to "myUniqueList"
print(addList(1))                 
print(addList("Hello"))
print(addList("\"Sam\""))                 
print(addList(1234))
print(addList([1,2,3,]))

# Try to add the same value that already existed in "myUniqueListk", Then it will get push to "myLeftOvers"
print(addList(1234))
print(addList("Hello"))

# Print out the result
print("\n---------------------------------------")
print("\n::This is myUniqueList::\n")   # Since, it return "True" it mean that the data has been added to "myUniqueList"
print(myUniqueList)    
print("\n---------------------------------------")
print("\n::This is myLeftOvers::\n")    # And False mean the data get push to "myLeftOvers"
print(myLeftOvers)
print("\n---------------------------------------")
