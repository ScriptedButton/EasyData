data = input("File where data is stored: ")

content = open(data, 'r')
text = content.read()

option = input("Read or write: ")
if option == "read":
    for i in content.readlines():
        first_name, last_name, dob = i.split(",")
        print(first_name, last_name, dob)
    content.close()
elif option == "write":
    values = input("Enter the values: ")
    file = open(data, 'w')
    file.write(text + "\n" + values)
    file.close()
