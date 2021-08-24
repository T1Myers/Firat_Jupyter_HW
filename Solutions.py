# Q1
def isConsecutive(arr, a, b):

    index_a = None
    index_b = None

    for idx, item in enumerate(arr):
        if item == a:
            index_a = idx
        elif item == b:
            index_b = idx

    difference = index_a - index_b

    print(index_a, index_b)
    return difference == 1 or difference == -1

# Q2

# Option 1:
def create_pyramid(n):
    for i in range(n):
        print(' ' * (n-i-1) + "X"*(2*i+1))
create_pyramid(5)

# Option 2:
def create_pyramid():
    rows = int(input("Enter the number of rows: ")) 
    for row in range (0,rows): 
        for _ in range(0,rows-row-1): 
            print(end=' ') 
        for _ in range(0,row+1): 
            print('x',end=' ') 
        print(' ')
create_pyramid()

# Option 3:
def create_pyramid(n):
    for i in range(1,n):
        print (" "*(n-i)+"X"*i+"X"*(i-1))
create_pyramid(15)

# Option 4:
def print_pyramid(n):
    for i in range(n):
        print(('X'*(i*2+1)).center(n*2+1))

# Option 5:
def print_pyramid(n):
    total_space_width = n*2+1
    for i in range(n):
        curr_level_xs = i*2+1
        curr_xs = 'X'*(curr_level_xs)
        print(curr_xs.center(total_space_width))