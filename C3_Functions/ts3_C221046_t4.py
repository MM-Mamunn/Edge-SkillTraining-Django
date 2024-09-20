
# Task 4 -

def sum_of_tuples(tup):
    sum = 0
    for i in tup:
        sum += i
    return sum

# to change an element of a tuple , we need to convert it to list first, then make changes, then convert the changed list into tuple again
def change_first_element(tup,num):
    list = []
    for i in tup:
        list.append(i)
    list[0] = num #change the first element of the list
    tup = tuple(list) #Now convert the changed list into tuple again
    return tup

# taking a tuple 
tup = (2, 3, 4, 5, 6)

print(sum_of_tuples(tup))

# change the first element of the tuple via 100
tup = change_first_element(tup,100)
print(tup)