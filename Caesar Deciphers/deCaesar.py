#Caesar Decipher Implemetation
print("Please input the name of your txt file")
print("Use the format xyz.txt")
file_name = input()
file = open(file_name, "r")
content = file.read()
file.close()

elements = list(content)
ascii_list = []
for ele in elements:
    value = ord(ele)
    ascii_list.append(value)
    continue  
modified_list = []
for elem in ascii_list:
    if (68 <=elem <= 90)or( 100 <=elem <= 122):
        new_value = elem-3
        modified_list.append(new_value)
    elif ( elem in [ 65,66,67,97,98,99 ]):
        new_value = elem + 23
        modified_list.append(new_value)
    else:
        modified_list.append(elem)
en_list = []
for eleme in modified_list:
    en_value = chr(eleme)
    en_list.append(en_value)

descript = ""
for elemen in en_list:
    descript += elemen

print("Please give encrypted file a name")
print("Use the format abc.txt")
new_filename = input()
new_file = open(new_filename, "w")
new_file.write(descript)
new_file.close()
