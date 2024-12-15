def create_usernames(data): 
    #Clear inactive users from the data
    #Set starting iterator
    i = 0
    for value in data["active"]:
        if value == False:
           data["students"].pop(i)
           data["active"].pop(i)
        i+=1
    #-----------
    #Create a username consisting of first 5 letters of surename and first 3 letters of first name 
    #Start with an empty list
    data["usernames"] = []
    

    for value in data["students"]:
        #Split name to first name and last name and set everything to lower case
        #If you have more that first and last name, then thats a problem for someone else.
        splitName = str.split(str.lower(value))
        data["usernames"].append(splitName[1][:5] + splitName[0][:3])

    #Check for duplicates and change the last letter to number
    unique_usernames = set()
    for j, value in enumerate(data["usernames"]):  
        original_value = value  
        counter = 1
        
        while value in unique_usernames:  
            # Replace last character with increasing number
            value = original_value[:7] + str(counter)
            counter += 1
        
        # Update the username in the list
        data["usernames"][j] = value
        # Add the new unique username to the set
        unique_usernames.add(value)
                
            

  

    
# testing
data = {
    "students":["Adam Levine", "Monica Muller", "John Deere", "John Deere"],
    "active":[True, False, True, True]
}  
print(data)
create_usernames(data)
print(data)



assert create_usernames(data) == {
    "students":["Adam Levine", "John Deere", "John Deere"],
    "active":[True, True, True],
    "usernames":["levinada", "deerejoh", "deerejo1"]
}