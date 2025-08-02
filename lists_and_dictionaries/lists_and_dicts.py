# WGXC DC Python Lab
# Python Lists and Dictonaries

# -----------------------------------------------------------------------
# Let's make a list
# -----------------------------------------------------------------------
# this is the syntax for creating a new list called "days_of_the_week"
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# 1. what is in the list?
# let's print it out!
print("1. -----Days of the Week-----")
print(days_of_the_week)

# 1b. what is the index of Monday?
# hint... python starts counting at 0
# print your answer
print("1. -----Index of Monday-----")
print("")

print("your answer here")

# 1c. what is the index of Friday?
# hint... python starts counting at 0
# print your answer
print("")
print("1. -----Index of Friday-----")

print("your answer here")

# 2. what is the item stored at days_of_the_week[2]? 
# Print out your answer
print("")
print("2. -----Item stored at days_of_week[2]-----")

print("your answer here")

# 2b. IndexError. What is the item stored at days_of_the_week[10]? 
# This one will raise an exception. That's ok! :) 
# comment this one out when you are done. :)
print("")
print("2b. -----Item stored at days_of_week[10]-----")

print("your answer here")

# ---------------------------------------------------------------
# oops... we forgot the weekend! 
# 3. Let's add Saturday.
# print the updated list
print("")
print("3. -----Added Saturday-----")

print("your answer here")

# 4. now add Sunday
# print the updated list
print("")
print("4. -----Added Sunday-----")

print("your answer here")

# 5. what is the length of the list now?
# print your answer
print("")
print("5. -----Length of list-----")

print("your answer here")

# ---------------------------------------------------------------
# Let's slice the list
# the slicing goes up to (but does not include) the last number
# eg, [0: 3] will give you (0, 1, 2)
# eg, [1: 5] will give you (1, 2, 3, 4)
# think: last_index - first_index = number of items

# get just the week days slice
# print the slice
print("")
print("6. -----Week days-----")

print("your answer here")

# and what about just the weekend slice?
# print the slice
print("")
print("7. -----Weekend days-----")

print("your answer here")

# ---------------------------------------------------------------
# let's get rid of Wednesday! Pop it out of the list.
# print the updated list
print("")
print("8. -----Remove that pesky Wednesday-----")

print("your answer here")

# well, maybe we should put it back. Insert it back to its regular spot.
# print the updated list.
print("")
print("9. -----Just kidding, it's back-----")

print("your answer here")

# ----------------------------------------------------------------------
# Let's make a dictionary
# ----------------------------------------------------------------------
print("")
print("---------------------------------------------------------------")

# this is the syntax for creating a new dictionary called "contacts"
contacts = {
	"stephanie": "703-555-6789",
	"heather": "813-555-8989",
	"gia": "321-555-1234"
}

# 1. what is in the dictionary?
# print the dictionary
print("")
print("1. -----Contacts Dictionary-----")

print(contacts)

# 2. how many items are in the dictionary?
# print your answer
print("")
print("2. -----Number of contacts-----")

print("your answer here")

# 3. what are the keys of the dictionary?
# print your answer
print("")
print("3. -----Contacts Keys-----")

print("your answer here")

# 4. What are the values?
# print your answer
print("")
print("4. -----Contacts Values-----")

print("your answer here")

# 5. Let's add a new friend named 'sri'
# print the updated dictionary
print("")
print("5. -----Added a new item-----")

print("your answer here")

# 6. Let's update gia's phone number. She moved to DC.
# print the updated dictionary
print("")
print("6. -----Updated a value-----")

print("your answer here")

# 7. Let's remove stephanie. i know my own number. :)
# print the updated dictionary
print("")
print("7. -----Removed Stephanie-----")

print("your answer here")

# ----------------------------------------------------------------------
# Let's make a nested dictionary
# ----------------------------------------------------------------------
print("")
print("---------------------------------------------------------------")

# 1. let's make a new contact list that can handle phone and email
# Notice that Gia does NOT have an email key. keys are NOT required fields.
updated_contacts = {
	"stephanie": {
		"phone": "703-555-6789",
		"email": "steph@email.com"
		},
	"heather": {
		"phone": "321-555-1234",
		"email": "heather@gmail.com"
	},
	"gia": {
		"phone": "202-555-2917"
	}

}

print("")
print("1. -----Nested dictionary example-----")

print(updated_contacts)

# 2. get stephanie's email
# print the email
print("")
print("2. -----Stephanie's nested email-----")

print("your answer here")

# 3. update heather's phone number. She moved to DC, too.
# print the updated dictionary
print("")
print("3. -----Heather's new phone-----")

print("your answer here")

# 4. add sri's dictionary to this new phone book. 
# "sri" is the key, and the value is her dictionary of key/value pairs
# her number is 703-555-9999
# her email is "sri@sri.com"
# her twitter is @sri
# print the updated dictionary
print("")
print("4. -----Sri's new contact (with twitter)-----")

print("your answer here")

# 5. oops, remove sri's twitter. she doesn't want it in the contacts
# get sri's dictionary, then pop the twitter key
# print the updated dictionary
print("")
print("5. -----Sri's new contact (without twitter)-----")

print("your answer here")

# 6. KeyError. Try to get gia's email using bracket syntax. 
# this one will raise an exception because Gia doesn't have an email key
# comment this one out when you are done. :)
print("")
print("6. -----Gia's email (with an exception)-----")

print("your answer here -- it will raise an exception. that's ok!")

# 6b. Get gia's email with a default of "No email". Print it out.
print("")
print("6. -----Gia's email (with a default)-----")

print("your answer here")
