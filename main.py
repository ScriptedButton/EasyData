data = input("File where data is stored: ")

content = open(data, 'r').readlines()

for i in content:
  first_name, last_name, dob = i
  print(first_name, last_name, dob)
  
  
