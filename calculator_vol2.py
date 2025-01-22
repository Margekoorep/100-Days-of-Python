def add (n1, n2):
  return n1 + n2
  
def substract (n1, n2):
  return n1 - n2
  
def multyply (n1, n2):
  return n1 * n2
  
def divide (n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multyply,
  "/": divide
}
def calculator ():
  should_accumulate = True
  num1 = float(input("What is the first number?: "))
  while should_accumulate:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    choise = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    
    if choise == "y":
      num1 = answer
    else: 
      should_accumulate = False
      print("\n"*20) #to make a new page sort of 
      calculator()

calculator()
