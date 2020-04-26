def main():
    num = int(input("Enter a number:"))
    print(fizz_buzz(num))

def fizz_buzz(input):
    input = int(input)
    if input % 3 == 0 and input % 5 == 0 :
        return ("FizzBuzz")
    elif input % 5 == 0 :
        return("Buzz")
    elif input % 3 == 0 :
        return("Fizz")

main()

