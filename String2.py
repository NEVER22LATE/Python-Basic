

# Parsing an Extracting 

data = " From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

# Take the following python code that stores a string 

str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the
#colon character and then use the float function to convert the extracted
#string into a floating point number

index = str.find(":")

float_number = str[index+1:]

fn = float(float_number)

print(fn)
