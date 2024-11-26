print('''
      
    COMPLEX CALC                                                                       
''')



while True:
    print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exponent
    6. Modulus
    7. Factorial
    8. Absolute value
    9. Factor finder
    10. Prime checker
    11. Degrees to rad
    12. Rad to degrees

    ''')


    def addition(first_num, sec_num):
        print(first_num + sec_num)

    def subtraction(first_num, sec_num):
        print(first_num - sec_num)

    def multiplication(first_num, sec_num):
        print(first_num * sec_num)

    def division(first_num, sec_num):
        print(first_num / sec_num)

    def exponent(first_num, sec_num):
        print(first_num ** (sec_num))

    def factorial(num):
        num = int(num)
        result = 1
        for i in range(1, num+1):
            result = result*i
        print(result)
    
    def modulus(first_num, sec_num):
        print(int(first_num) % int(sec_num))
    
    def abs_val(num):
        if num < 0:
            num = -num
        if num > 0:
            num = num
        print(num)

    def factors(num):
        factors = []
        for i in range(1, num+1):
            if num % i == 0:
                factors.append(i)
        print(factors)

    def check_if_prime(num):
        factors = []
        for i in range(1, num+1):
            if num % i == 0:
                factors.append(i)           
        if len(factors) == 2:
            print('Its a prime number! ')
        elif len(factors) > 2:
            print('Its not a prime number! ')

    def deg_to_rad(num):
        print(num *(3.14/180))

    def rad_to_deg(num):
        print((num) * (180/3.14))





    user_input = int(input('Choose: '))
    
    if user_input in [1,2,3,4,5,6]:
        first_num = input('First number: ')
        sec_num = input('Second number: ')

        if first_num.isdigit() and sec_num.isdigit():
                first_num = int(first_num)
                sec_num = int(sec_num)
                
                if user_input == 1:
                    addition(first_num, sec_num)

                elif user_input ==2:
                    subtraction(first_num, sec_num)

                elif user_input == 3:
                    multiplication(first_num, sec_num)

                elif user_input == 4:
                    division(first_num, sec_num)

                elif user_input == 5:
                    exponent(first_num, sec_num)

                elif user_input == 6:
                    modulus(first_num, sec_num)
    
    elif user_input in [7,8,9,10,11,12]:

        num = input('Enter a number: ')

        if num.isdigit():
            num = float(num)

            if user_input == 7: 
                factorial(num)

            elif user_input == 8:
                abs_val(num)

            elif user_input == 9:
                factors(num)

            elif user_input == 10:
                check_if_prime(num)

            elif user_input == 11:
                deg_to_rad(num)

            elif user_input == 12:
                rad_to_deg(num)

