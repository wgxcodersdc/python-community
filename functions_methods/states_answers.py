
# use the open , read, split functions to create a list of all the rows
with open('states.txt','r',encoding='utf-8') as file:
    states = file.read()
    states = states.split('\n')

#insert any missing data
#how do we check if we have only the 50 states that we need?
#There are 2 ways to do this

#print(len(states))

for index, i in enumerate(states):
	print(str(index) + " " + i)


#remove data we don't need

missing = []

missing.append(states.pop(40))
missing.append(states.pop(37))
missing.append(states.pop(8))
#print(missing)

#print(len(states))


# create 2 lists and use a for loop to append the state and abbrevations 
# in corresponding lists
abbvs = []

state = []


for i in states:
	i.split(",")
	abbvs.append(i[0:2])
	state.append(i[3:])

	
#clean the data

# lets make the data all lower case then revert back
# to pretend we got it all in lowercase

#Do the states first

state = [x.lower() for x in state]


#state = [x[0].upper() + x[1:] for x in state] 
state = [x.title() for x in state]


#Do the abbreviations 

abbvs = [x.lower() for x in abbvs]

abbvs = [x.upper() for x in abbvs]



# combine the 2 cleaned lists together and sort alphabetically

fifty_states = list(zip(abbvs,state))

# create a dictionary with the Abbrevation as the Key and State as the Value

d_50 = dict(fifty_states)
print(d_50)

#sort dictionary by key instead of value
from collections import OrderedDict
print(OrderedDict(sorted(d_50.items())))