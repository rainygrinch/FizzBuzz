# Objective - generate numbers 1-100, but replace
# multiples of 3 with "fizz" and multiples of 5 with "buzz"
# and replace multiples of 3 AND 5 with "fizzbuzz"
# count the number of times each word occured



# define variables to count number of fizz, buzz, and fizzbuzz

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

# Number generator

for i in range(1, 101):

# if the number divides by 3 and 5, print fizzbuzz
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1

# if the number divides by 3 only, print fizz
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1

# if the number divides by 5 only, print buzz
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1

# if the number is not divisible by 3 or 5, print the number
    else:
        print(i)

# print the number of times each outcome occured
print("***************************************************************")
print("The number of times Fizz occured is: " + str(fizz_count))
print("The number of times Buzz occured is: " + str(buzz_count))
print("The number of times FizzBuzz occured is: " + str(fizzbuzz_count))
