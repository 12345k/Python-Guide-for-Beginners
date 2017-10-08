def get_factorial(number):
    answer = 1  # We start with 1 as usual for finding factorial
    
    for i in range(1, (number+1)):  # 1 is added to second argument of range function since it ignores last value
        answer = answer * i

    return answer # answer now contains the calculated value



if __name__ == '__main__':
    number = input("Enter the number : ")
    number = int(number)
    factorial = get_factorial(number)
    print ("The factorial of " + str(number) + " is = " + str(factorial))

