
file_name = input("Create a file: ")

text_file = open(file_name, "w")

text = input("Text of the file: ")

text_file.write(text)
text_file.flush()

text_file.close()
