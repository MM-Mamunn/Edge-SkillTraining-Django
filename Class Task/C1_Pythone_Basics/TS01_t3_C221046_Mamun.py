#Task :3 - String Manupulation

strng = "my name is "
name = "Mamun Mahmud"

#concat two string
full_text = strng + name
print(full_text)

#convert to uppercase
print(f"converted the string ({full_text}) to upper {full_text.upper()}")

#Capitalization
print(f"Capitalize {full_text.capitalize()}")

#substring by slicing
print(f"The name is {full_text[11:len(name)]}")

#replace 
new_name = name.replace("Mamun Mahmud","Najmus Sakib")
print(f"{name} is replaced, New name is {new_name}")

#find starting index
index = full_text.find("Mamun")
print(f"find index {index}")

#Checking  starts with 
starts_with= strng.startswith("my")
print(f"starts with my is {starts_with}")

#convert to list
char_list = list(name)
print(f"{name} is divided in list, The list is ",char_list)

#join from a list 
joined_list = ''.join(char_list)
print(f"The {char_list} is joined that is {joined_list}")

#repeat a string
print(f"Repeat the name  three times {name  * 3}")
