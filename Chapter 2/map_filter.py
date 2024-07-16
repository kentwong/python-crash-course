def square(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Converting map object to a list to see the results
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)

number = 'a'

print(number*5)