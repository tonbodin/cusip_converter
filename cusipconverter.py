"""
READ THIS FIRST!!!

DESCRIPTION: 
This program takes a csv file of only CUSIPs (see only_Cusip.csv attached)
and appends a new column to the csv with the integer form of the CUSIP.
All manipulations of the csv file are performed using a dataframe through pandas. 

SCHEMA FOR CONVERSION:
All numbers in a CUSIP are maintained. All letters in the cusip are replaced by its ASCII value
Examples:
(this is directly from the dataframe when you run this program)
CUSIP         CUSIP_INT
0124285D6  -> 124285686
040484LE5  -> 4048476695
041431RG4  -> 4143182714

NEXT STEPS: 
When you run this program, you should get the first 1000 rows of the new dataframe (CUSIP -> CUSIP_INT)
I have yet to convert this dataframe back into a csv format, 
because I am not sure if the conversion was fully correct. 
Please check for any problems with the conversion (try accessing different rows in the dataframe)
and then the next step is to convert the dataframe into a csv. 

Hopefully you can then load this csv back into sql and perform joins :)

"""

# import the pandas library
import pandas as pd 

# create dataframe of from csv file
df = pd.read_csv("Only_Cusip.csv", dtype = {"CUSIP" : "string", "CUSIP_INT" : "int64"})

# function that takes a string Cusip and returns a int cusip
def converter(cusip_str):
    new_str = ""

    for char in range(0, len(cusip_str)):

        # this particular character is a number
        if(ord(cusip_str[char]) >= 48 and ord(cusip_str[char]) <= 59):
            new_str += cusip_str[char]
        # this particular character is a string
        else:
            new_str += str(ord(cusip_str[char]))
    
    # return the integer version of the string
    return int(new_str)

# initializes a new column in the dataframe
df["CUSIP_INT"] = 0

# iterates through the rows in the dataframe
for ind in df.index:
    
    # some string CUSIP values are in scientific notation (yikes)
    # only take the string CUSIP values that have 9 digits
    if(len(df["CUSIP"][ind]) == 9):
        df["CUSIP_INT"][ind] = converter(df["CUSIP"][ind])

#print the first 1000 rows of the dataframe
print(df.iloc[:1000])




