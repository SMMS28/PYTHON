# Take input from the user for birthdays in the format "name:dd-mm-yyyy"
data = input("Enter birthdays (name:dd-mm-yyyy separated by commas): ")

# Split the input string into a list of strings using comma as a delimiter
birthdays = data.split(",")

# Create an empty dictionary to store the name and birthday of each person
birthday_dict = {}

# Loop through each string in the birthdays list and extract the name and birthday
for birthday in birthdays:
    name, bday = birthday.split(":")
    birthday_dict[name] = bday.strip()

# Print the dictionary
print(birthday_dict)

# Take input from the user for a name to search in the dictionary
name = input("Enter a name to search: ")

# Join the name and birthday using the colon delimiter
if name in birthday_dict:
    print("The birthday of", name, "is", ":".join([name, birthday_dict[name]]))
else:
    print("No data found for", name)
