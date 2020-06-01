import os
import sys
import datetime

print("System")
print(sys.platform)
print(sys.version)
print(os.uname())
print("\n")

print("Directory")
print(os.getcwd())
print("\n")

print("Time")
print(datetime.datetime.now())

