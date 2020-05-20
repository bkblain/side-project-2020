globalVar = "Mr Worldwide!"

def think_globally():
    localVar = "act locally"

    print("inside function")
    print(globalVar)
    print(localVar)

print("start")
print(globalVar)
print("")

# print(localVar)

think_globally()

# print(localVar)

