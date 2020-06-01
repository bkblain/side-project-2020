import os

current_file = input("Enter the name of a file.")
new_name = input("Enter the new name of the file.")

os.rename(current_file, new_name)
