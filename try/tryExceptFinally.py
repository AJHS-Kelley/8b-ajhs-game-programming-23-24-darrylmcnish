#This is a method for testing code and preventing crashes
#Try -- except -- else -- finally

try: # The code in this block is ALWAYS executed
    myVariable = 1
    print(myVariable)
    myString = "Five"
    print(float(myString))
except NameError:
    print("There is an incorrect variable name in your code.")
except: # This code will run IF there is an error (exeption)
    print("something has gone wrong!")
else: # This code runs if there are NO ERRORS
    print("code executed correctly with no exceptions.\n")
finally: #THIS CODE WILL ALWAYS RUN, ITS LIKE THE TERMINATOR
    print("I'll be back")

#except NameError:
#    pass