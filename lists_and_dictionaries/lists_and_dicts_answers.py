# WGXC DC Python Lab
# Python Lists and Dictonaries

# -----------------------------------------------------------------------
# Let's make a list
# -----------------------------------------------------------------------
# this is the syntax for creating a new list called "days_of_the_week"
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# 1. what is in the list?
print("1. -----Days of the Week-----")
print(days_of_the_week)

# 1b. what is the index of Monday?
# hint... python starts counting at 0
# 0

# 1c. what is the index of Friday?
# hint... python starts counting at 0
# 4

# 2. what is the item stored at days_of_the_week[2]? Print it out.
print("2. -----Item stored at days_of_week[2]-----")
print(days_of_the_week[2])

# 2b. IndexError. What is the item stored at days_of_the_week[10]? 
# comment this one out when you are done. :)
print("2b. -----Item stored at days_of_week[10]-----")
print(days_of_the_week[10])

# ---------------------------------------------------------------
# oops... we forgot the weekend! 
# 3. Let's add Saturday.
days_of_the_week.append("Saturday")
print("3. -----Added Saturday-----")
print(days_of_the_week)

# 4. now add Sunday
days_of_the_week.append("Sunday")
print("4. -----Added Sunday-----")
print(days_of_the_week)

# 5. what is the length of the list?
number_of_days = len(days_of_the_week)
print("5. -----Length of list-----")
print("number of days: {0}".format(number_of_days))

# ---------------------------------------------------------------
# Let's slice the list
# the slicing goes up to (but does not include) the last number
# eg, [0: 3] will give you (0, 1, 2)
# eg, [1: 5] will give you (1, 2, 3, 4)
# think: last_index - first_index = number of items

# get just the week days slice
weekdays = days_of_the_week[0:5]
print("6. -----Week days-----")
print(weekdays)

# and what about just the weekend slice?
weekend = days_of_the_week[5:7]
print("7. -----Weekend days-----")
print(weekend)

# ---------------------------------------------------------------
# let's get rid of Wednesday!
least_fave_day = days_of_the_week.pop(2)
print("8. -----Removed that pesky Wednesday-----")
print(days_of_the_week)
print(least_fave_day)

# well, maybe we should put it back. 
days_of_the_week.insert(2, "Wednesday")
print("9. -----Just kidding, it's back-----")
print(days_of_the_week)

print("---------------------------------------------------------------")
# ----------------------------------------------------------------------
# Let's make a dictionary
# ----------------------------------------------------------------------
# this is the syntax for creating a new dictionary called "contacts"
contacts = {
	"stephanie": "703-555-6789",
	"heather": "813-555-8989",
	"gia": "321-555-1234"
}

# 1. what is in the dictionary?
print("1. -----Contacts Dictionary-----")
print(contacts)

# 2. how many items are in the dictionary?
print("2. -----Number of contacts-----")
print("Number of contacts is: {0}".format(len(contacts)))

# 3. what are the keys of the dictionary?
print("3. -----Contacts Keys-----")
print(contacts.keys())

# 4. What are the values?
print("4. -----Contacts Values-----")
print(contacts.values())

# 5. Let's add a new friend named 'sri'
contacts["sri"] = "202-555-2817"
print("5. -----Added a new item-----")
print(contacts)

# 6. Let's update gia's phone number. She moved to DC.
contacts["gia"] = "202-555-9999"
print("6. -----Updated a value")
print(contacts)

# 7. Let's remove stephanie. i know my own number
my_number = contacts.pop("stephanie")

print("7. -----Removed myself-----")
print(contacts)
print(my_number)

print("---------------------------------------------------------------")
# ----------------------------------------------------------------------
# Let's make a nested dictionary
# ----------------------------------------------------------------------
# 1. let's make a new contact list that can handle phone and email
# Notice that gia does NOT have an email key. keys are not required fields.
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

print("1. -----Nested dictionary example-----")
print(updated_contacts)

# 2. get stephanie's email
stephs_email = updated_contacts["stephanie"]["email"]

print("2. -----Stephanie's nested email-----")
print(updated_contacts)

# 3. update heather's phone number. She moved to DC, too.
updated_contacts["heather"]["phone"] = "202-555-8182"
print("3. -----Heather's new phone-----")
print(updated_contacts)

# 4. add sri's dictionary to this new phone book. 
# "sri" is the key, and the value is her dictionary of key/value pairs
# her number is 703-555-9999
# her email is "sri@sri.com"
# her twitter is @sri
updated_contacts["sri"] = {
	"phone": "703-555-9999",
	"email": "sri@sri.com",
	"twitter": "@sri"
}
print("4. -----Sri's new contact-----")
print(updated_contacts)

# 5. oops, remove sri's twitter. she doesn't want it in the contacts
# get sri's dictionary, then pop the twitter key
updated_contacts["sri"].pop("twitter")
print("5. -----Sri's new contact-----")
print(updated_contacts)

# 6. KeyError. Try to get gia's email using bracket syntax. 
# this one with raise an exception because gia doesn't have an email key
# comment this one out when you are done. :)
print("6. -----gia's email-----")
updated_contacts["gia"]["email"]

# 6b. Get gia's email with a default of "No email".
gias_email = updated_contacts["gia"].get("email", "No email")
print(gias_email)


