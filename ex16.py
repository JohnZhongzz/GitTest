from sys import argv

script, file_name = argv

print(f"We're going to erase {file_name}.") # 打印一句话，并且把之前获取的file_name变量导进去
print("If you don't want that, hit CTRL-C (^C).") # 打印一句话
print("If you do want that, hit RETURN") #打印一句话

input("?") #出现一个input的位置

print("Opening the file...") #打印一句话
target = open(file_name, 'w') #打开文件，并且将这个对象给到target，并且是以读写方式打开

print("Truncating the file. Goodbye!") #输出一句话
target.truncate() #清空txt文件

print("Now I'm going to ask you for three lines.") #输出一句话

line1 = input("line 1: ") #提供输入位置
line2 = input("line 2: ") #提供输入位置
line3 = input("line 3: ") #提供输入位置

print("I'm going to write these to the file.") #输出一句话

target.write(line1) #想txt第一行写入一句话
target.write("\n") #向txt文件写入换行符
target.write(line2) #向txt文件写入line2
target.write("\n") #向txt文件写入换行符
target.write(line3) #向txt 文件写入line3
target.write("\n") #向txt文件写入换行符

print("And finally, we close it.")
target.close()