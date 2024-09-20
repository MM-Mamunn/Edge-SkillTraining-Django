# Task 5
# Declare two set
set1 = {"Mamun","Seyam","Rayhan"}
set2 = {"Rayhan","Rafi","Nahian"}

# Set operations
union_set = set1 | set2
intersection = set1 & set2
diff = (set1 - set2) | (set2 - set1)
# this diff also can be done like this
diff = set1 ^ set2  # set1 ^ set2  is same as  (set1 - set2) | (set2 - set1)
print(f"The students in both sets are {intersection}")
print(f"The students in one sets are {diff}")