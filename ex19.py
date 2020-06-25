def cheese_and_crackers(cheese_count, boxes_of_crackers): # 定义函数cheese_and_crackers，有两个参数，cheese_count boxes_of_crackers
    print(f"You have {cheese_count} cheeses!") # 用变量打印一句话
    print(f"You have {boxes_of_crackers} boxes of crackers!") # 用变量打赢一句话
    print("Man that's enough for a party") # 打印一句话
    print("Get a blanket.\n") # 打印一句话，添加换行符\n


print("We can just give the function numbers directly:") # 打印一句话
cheese_and_crackers(20, 30) # 直接用数字做参数


print("OR, we can use variables from our script:") # 打印一句话
amount_of_cheese = 10 # 添加变量
amount_of_crackers = 50 # 添加变量

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # 用变量来导入参数


print("We can even do math inside too:") # 打印一句话
cheese_and_crackers(10 + 20, 5 + 6) # 用算术式来添加参数


print("And we can combine the two, variables and math:") # 打印一句话
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # 用变量和算术式来添加变量

