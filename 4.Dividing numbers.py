while True:
    try:
        number = int(input("Enter a number to find out its divisors: ")) # convert the input to an integer

        if number <= 0: # raise an exception if the input is less than or equal to 0
            raise ValueError("The input number must be greater than 0")

        num_list = []
        number_list = list(range(1,number+1)) # list of numbers from 1 to the input number inclusive

        for num in number_list: # loop through the numbers in the list
            if num % 2 == 0: # check if the number is even
                num_list.append(num) # if the number is even, add it to the list of divisors

        if len(num_list) == 0: # if the list of divisors is empty, it means no divisors were found
            raise ValueError("No even divisors were found")
        
        num_list = str(num_list).replace('[','').replace(']','') # convert the list to a string and remove the brackets

        print(num_list) # print the divisorss

    except ValueError as error:
        print(error) # print the error message if an exception is raised
