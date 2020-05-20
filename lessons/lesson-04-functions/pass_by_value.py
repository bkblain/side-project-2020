array = ["cat", "dog", "rabbit", "turtle", "bird"]
integer = 0

def pass_by_value(integer, array):
    integer += 1
    array.append("fish")
    
    print("integer = ", integer)
    print(array)
    print("")


print("integer = ", integer)
print(array)
print("")

pass_by_value(integer, array)

print("integer = ", integer)
print(array)
print("")
