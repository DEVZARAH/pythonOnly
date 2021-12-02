my_list = [1, 2, 3, 4, 5, 6, 7, 21, 33, 32, 2, 4]
# numbers =int(input("Enter any number: "))
# numbers=[numbers]
even_number=[]
odd_number=[]
for number in my_list: 
    if number % 2==0:
        # print(f"{numbers} is even number")

            even_number.append(number)
    else:
            # print(f"{numbers} is odd number")

            odd_number.append(number)
          
print(even_number)
print(odd_number)     