text_file = open("text.txt", "r")

for line in text_file:
    print(line)
    print("-------------------")

text_file.close()
