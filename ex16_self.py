from sys import argv
script, file_name = argv

print(f"We will going to erase {file_name}")
print("If you don't want to do that click ctrl+c")
print("If you want to do that, click return.")

input(">")

print("Opening the file...")
target = open(file_name, "w")

print("We are going to truncate it...")
target.truncate
print("Truncate done!")

print("I'm going to ask you three lines.")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I'm going to write these to the file...")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
target.write(f"{line1} \n {line2} \n {line3} \n")
print("Write down!")

print("And finally, we will close it.")
target.close()


