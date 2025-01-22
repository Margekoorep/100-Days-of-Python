
first_number = int(input("what is the first number?: \n"))
game_off = False
while game_off == False:
  
  
  operation = input ("+\n-\n*\n/\nPick an operation: \n")
 
  second_number = int(input("what is the second number?: \n"))
  
  
  def calculation(first_number, second_number, operation):
    """This function is the calculator"""
    if operation == "+":
      return first_number + second_number
    elif operation == "-":
      return first_number - second_number
    elif operation == "*":
      return first_number * second_number
    elif operation == "/":
      return first_number / second_number
    else:
      return f"{operation} is not valid"
  result = calculation(first_number, second_number, operation)
  print(f" The result is : {result}")
  option = input("if you want to continue with the result type Y, otherwise type N. If you want to end type E.\n")
  if option == "Y":
    first_number = result
  elif option == "N":
    first_number = int(input("what is the first number?: \n"))
  elif option == "E":
    print("Thank You!")
    game_off = True
  
  
  

