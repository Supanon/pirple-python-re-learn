# Pirple homework assignment 4 (Python)

# Global scope variable
myUniqueList = [] 
myLeftOvers = [] 

def addList(add):
    if add in myUniqueList:       # Found this in Stackoverflow "If...in..."
        myLeftOvers.append(add)   # So I combine extra credit to this line not sure if I should write a new function or somtinh but I found that it more convinient and shorter
        return False              # just've been tried some  other methods using "=" and "==" but it didn't work out
    else:                         # check if the value is already existed first so it won't get add and return "False"
        myUniqueList.append(add)  # Then, I put add(parameter) inside "append" so any value that passed in will be add to "myUniqueList"
        return True               # after it get passed the condition then return "True"


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
