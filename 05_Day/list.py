# Exercises: List
# Level 1

# 1. Declare an empty list
# Solution 1
from curses.ascii import isupper


empty_list = []
print(empty_list)
                        # End.
# Solution 2
empty_list = list()
print(empty_list)
                        # End.

# 2. Declare a list with more than 5 items
items = ["TV", "Radio", "Monitor", "Mouse", "Charger"]
print(items)
                        # End.

# 3. Find the length of your list 
items = ["TV", "Radio", "Monitor", "Mouse", "Charger"]
print(len(items))
                        # End.

# 4. Get the first item, the middle item and the last item of the list
items = ["TV", "Radio", "Monitor", "Mouse", "Charger"]
first_item, second_item, third_item, fourth_item, fifth_item = items
print(items[0])
print(items[2])
print(items[4])
print("Or like this:")
print("=============")
print(first_item)
print(third_item)
print(fifth_item)
                        # End.

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Salah", 31, "178 cm", "married", "Egypt"]
print(mixed_data_types)
                        # End.

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
                        # End.

# 7. Print the list using print()
print(it_companies)
                        # End.

# 8. Print the number of companies in the list
print("The number of companies in the list is", len(it_companies))
                        # End.

# 9. Print the first, middle and last company
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_item, second_item, third_item, fourth_item, fifth_item, sixth_item, seventh_item = it_companies
print(first_item)
print(fourth_item)
print(seventh_item)
                        # End.

# 10. Print the list after modifying one of the companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[0] = "Twitter"
print(it_companies)
                        # End.

# 11. Add an IT company to it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("Paypal")
                        # End.

# 12. Insert an IT company in the middle of the companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle"]
it_companies.insert(3, "Amazon")
print(it_companies)
                        # End.

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ["facebook", "google", "microsoft", "apple", "oracle"]
it_companies[0] = it_companies[0].upper()
print(it_companies)
                         # End.

# 14. Join the it_companies with a string '#;  '
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
string = ["#; "]
joined = it_companies + string
print(joined)
                        # End.

# 15. Check if a certain company exists in the it_companies list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exist = "Facebook" in it_companies
print(does_exist)
does_exist = "Paypal" in it_companies
print(does_exist)
                        # End.
