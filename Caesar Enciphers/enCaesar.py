#Caesar Encipher Implemetation
print("Please input the name of your txt file")
print("Use the format abc.txt")
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
    if (65 <=elem <= 87)or( 97 <=elem <= 119):
        new_value = elem+3
        modified_list.append(new_value)
    elif ( elem in [ 88,89,90,120,121,122 ]):
        new_value = elem - 23
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
print("Use the format xyz.txt")
new_filename = input()
new_file = open(new_filename, "w")
new_file.write(descript)
new_file.close()


    
    
