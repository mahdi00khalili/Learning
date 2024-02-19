import time
import random


start_number = 56804155
finish_number = 56804165


flag = False

# n = 100000000

while True:

    # Checks the difference between finish_number and start_number.if it is less than 5 or equal to 5 ...
    if (finish_number - start_number) <= 5:
        for i in range(start_number, finish_number +1):
                
                start_time = time.time()
                # code ...
                result = 3 ** i
                # ........
                # Record the end time
                end_time = time.time()
                # Calculate the difference (elapsed time)
                elapsed_time = end_time - start_time

                if elapsed_time >= 60:
                        print(f'the result is n={i}. running time is {elapsed_time} \n')
                        print(f'the power of your computer is is n={i-1}')
                        flag = True
                        break
                else:   
                        
                        print(f'the power of your computer is n={i}')
                        flag = True
                        break

    if flag:
        break

    # select random between 
    # Generate a random integer between 1 and 10 (inclusive)
    random_number = random.randint(start_number, finish_number)
    print(f'the selected random number in range {start_number} and {finish_number} is {random_number}')
    # Record the start time
    start_time = time.time()

    # code ...
    result = 3 ** random_number
    # ........

    # Record the end time
    end_time = time.time()
    # Calculate the difference (elapsed time)
    elapsed_time = end_time - start_time


    if elapsed_time >= 60:
        finish_number = random_number
        print(f'the result is n={random_number}. running time is {elapsed_time} \n')
    else:
        start_number = random_number
        print(f'the result is n={random_number}. running time is {elapsed_time} \n')



