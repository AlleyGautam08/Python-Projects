def sub(x,y):
     return x - y

def add(x,y):
     return x + y

def multi(x,y):
     return x * y

def divide(x,y):
     return x / y

print("select option for calculator:")
print("1. Subtraction")
print("2. Addition")
print("3. Multiplication")
print("4. Divide")

while True:
     choice = input("Please Selection option 1,2,3,4")
      
     if str(choice ) in ('1', '2', '3', '4'):
          num1 = float(input("Input first number:"))
          num2 = float(input("Input second number:"))
          
          if str(choice) == '1':
               print(num1, "-", num2, "=", sub(num1, num2))
          elif str(choice) == '2':
               print(num1, "+", num2, "=", add(num1, num2))
          elif str(choice) == '3':
               print(num1, "*", num2, "=", multi(num1, num2))
          elif str(choice) == '4':
               print(num1, "/", num2, "=", divide(num1, num2))


          next_cal = input("Do you want to calculator another value? (yes/no):")
          if next_cal == 'no':
               break
     else:
          print("invalid input or wrong input")