#!/usr/bin/python3

def generate(keywords, i, s, len):
 
    # base case
    if (i == 0): # when len has
                 # been reached
     
        # print it out
        print(s)
        return
     
    # iterate through the keywordsay
    for j in range(0, len):
 
        # Create new string with
        # next character Call
        # generate again until
        # string has reached its len
        appended = s + keywords[j]
        generate(keywords, i - 1, appended, len)
 
    return
 
# function to generate
# all possible passwords
def crack(keywords, len):
 
    # call for all required lengths
    for i in range(1 , len + 1):
        generate(keywords, i, "", len)

keywords = ['INPUTS']
len = len(keywords)
crack(keywords, len)

''' You can edit keywords=[] and add any data you like about your victim,
as the following keyword = ['BIRTHDATE', 'NAME', 'LASTNAME','ZIP'] ANY info you have about your victim '''