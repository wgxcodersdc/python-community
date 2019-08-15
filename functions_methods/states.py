# use the open , read, split functions to create a list of all the rows
with open('states.txt','r',encoding='utf-8') as file:
    states = file.read()
    states = states.split('\n')

#insert any missing data
#how do we check if we have only the 50 states that we need?
#There are 2 ways to do this




#remove data we don't need




# create 2 lists and use a for loop to append the state and abbrevations 
# in corresponding lists
abbvs = []

state = []



	
#clean the data

# lets make the data all lower case then revert back
# to pretend we got it all in lowercase

#Do the states first




#Do the abbreviations 




# combine the 2 cleaned lists together and sort alphabetically



# create a dictionary with the Abbrevation as the Key and State as the Value



#sort dictionary by key instead of value
