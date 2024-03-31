# for input 
FirstName='Arnob'
LastName='Sarkar'
home='Islampur, Philipnagar, Daulatpur, Kushtia'
dept='ICT'
uni='Islamic University, Kushtia'

bio="""I am Sarkar Tuhassinul Arnob
I am a student of ICT at Islamic University, Kushtia
I am learning python from IEEE IU SB python-bootcamp
thanks."""



# 1. Concatenate First_Name and last_name and print
fullName= FirstName +' '+ LastName #concatanate names
print("Your full name is ",fullName)

# 2. Convert the Concatenated text into both uppercase and lowercase and print
print("Upper case name: ",fullName.upper())
print("Lower case name: ",fullName.lower())

print('Home Address: ', home)

# 3. Print the length of the values of variable Home_Address
length=len(home)
print(f'Length of the home address is: {length}')

# 4. Print a substring of Bio using string slicing
print("substring of the bio: ",end='')
print(bio[4:20]) # Get a substring from the 5th character to the 20th character

# 5. Print Department and University in a formatted string
print(f'I am a student of {dept} at {uni}')