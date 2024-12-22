# def greeting(name):
#     print("hello",+name)
# def sum(a,b):
#   result=a+b
#   print("result",result)
#   return result
# def diff(a,b):
# #    result=a-b
# #    print("result",result)
# #    return result
# # def mul(a,b):
# #    result=a*b
# #    print("result",result)
# #    return result
# # if __name__=="__main__":
# #    print("my module")
# #    a=1
# #    b=2
# #    result=a+b
# #    print("result",result)
# #    #next method
# #    from module import sum as sm,diff as df
# #    df(1,2)
# #    sm(1,2)  
# #    #sum,diff,mul,division,floor division and modulus
# # first_number=("input the first number")
# # second_number=("input the second number")
# # sum=first_number+second_number
# # mul=int(input("first_number*second_number") 
# # diff=first_number-second_number
# # div=first_number/second_number
# # floor=first_number//second_number
# # mod=first_number%second_number
# # print("first sum is",sum)
# # print("first sum is",diff)
# # print("first sum is",mul)
# # print("first sum is",div)
# # print("first sum is",floor)
# # print("first sum is",mod)# Importing the required math module (though math module is not strictly necessary for basic operations)
# # import operator

# # Functions to perform each operation
# def add(x, y):
#     return operator.add(x, y)

# def subtract(x, y):
#     return operator.sub(x, y)

# def multiply(x, y):
#     return operator.mul(x, y)

# def divide(x, y):
#     if y != 0:
#         return operator.truediv(x, y)
#     else:
#         return "Error! Division by zero."

# def floor_divide(x, y):
#     if y != 0:
#         return operator.floordiv(x, y)
#     else:
#         return "Error! Division by zero."

# def modulus(x, y):
#     if y != 0:
#         return operator.mod(x, y)
#     else:
#         return "Error! Division by zero."

# # Main function to drive the calculator
# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Floor Division")
#     print("6. Modulus")
    
#     # Taking input from the user
#     choice = input("Enter choice (1/2/3/4/5/6): ")

#     if choice in ['1', '2', '3', '4', '5', '6']:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(f"The result is: {add(num1, num2)}")
#         elif choice == '2':
#             print(f"The result is: {subtract(num1, num2)}")
#         elif choice == '3':
#             print(f"The result is: {multiply(num1, num2)}")
#         elif choice == '4':
#             print(f"The result is: {divide(num1, num2)}")
#         elif choice == '5':
#             print(f"The result is: {floor_divide(num1, num2)}")
#         elif choice == '6':
#             print(f"The result is: {modulus(num1, num2)}")
#     else:
#         print("Invalid input! Please select a valid operation.")

# # Run the calculator
# if __name__ == "__main__":
#     calculator()
    #introdution to sql in python
    #pandas
import pandas as pd
data={'name':['alice','bob','charlie'], 
'age':[25,30,35],
'city':['new york','paris','chicago']}
df=pd.DataFrame(data)
print(df)

df=pd.read_csv('data.csv')
print(df.head())
import pandas as pd