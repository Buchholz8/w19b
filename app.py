# i fist made the functions that will do their respective math questions
def add_numbers(num1 , num2):
    return num1 + num2
def subtract_numbers(num1 , num2):
    return num1 - num2
def multiply_numbers(num1 , num2):
    return num1 * num2
#for the divide i did a check for 0's
def divide_numbers(num1 , num2):
    try:
            return num1 / num2
#i did a zero division error
    except ZeroDivisionError:
        print('cannot be 0')
#i did a vlaue error to tell them they didn't choose a number
    except ValueError:
        print('must be a number')
#i did an error to check for anything else
    except:
        print('something else went wrong')
# and i did a finally that just says 'completed'
    finally:
        print('completed')
#i then printed out the different options for the equations 
print('please select an operation')
print('1. Adding')
print('2. Subtraction')
print('3. Multiplcation')
print('4. Division')
#i set a variable equal to the input of the 4 numbers
choice = int(input('Select an option (1, 2, 3, 4): '))
#i wrote an if statment that will make sure they choose a number between 1 and 4
if choice < 1 or choice > 4:
    print('invalid option')
    exit()
#i wrote a try statment that will follow some rules of making sure they choose a number
try:
    num1 = float(input('Please enter your first number : '))
    num2 = float(input('Please enetr your second number :'))
except ValueError:
    print('must be a number')
    exit()

result = 0
#i wrote some if elif to actaully select their number in relation to the equation they want
if choice == 1:
    result = add_numbers(num1 , num2)
elif choice == 2:
    result = subtract_numbers(num1 , num2)
elif choice == 3:
    result = multiply_numbers(num1 , num2)
elif choice == 4:
    result = divide_numbers(num1 , num2)
#this try statement just gives the result to them with a check making sure its not a value error
    try:
        result = divide_numbers(num1 , num2)
    except ValueError:
        print(str)
        exit()
#i then printed the results
print('result' , result)

#for the bonus part 1 all i did was makean input with some specific letters to do thefollowing 'quit' or 'restart'
exit_op = input("enter 'q' to quit or enter 'r' to re run :" )
#i then made an if to see if what was typed was a q, if it wasnt the calculator would restart 
if choice == 'q':
    exit()

user_numbers = []
while True:
    new_num = input("Enter a number (or 'c' to perform the calculation): ")
    if new_num == 'c':
        break
    user_numbers.append(float(new_num))

if not user_numbers:
    exit()

choice = int(input('Select an option (1: Add, 2: Subtract, 3: Multiply, 4: Divide): '))
result = user_numbers[0]

for i in range(1, len(user_numbers)):
    new_n = user_numbers[i]
    if choice == 1:
        result += new_n
    elif choice == 2:
        result -= new_n
    elif choice == 3:
        result *= new_n
    elif choice == 4:
        if new_n != 0:
            result /= new_n
        else:
            print("Error: Cannot divide by zero.")
            exit()
    else:
        print('Invalid option.')
        exit()

print("Result: ", result)