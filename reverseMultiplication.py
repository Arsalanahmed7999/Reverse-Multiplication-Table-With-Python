# Reverse Multiplication Table

num = int(input('Enter Your Number: \n'))

for i in range(10, 0, -1):
    print(f'{num} x {i} = {num * i}')


