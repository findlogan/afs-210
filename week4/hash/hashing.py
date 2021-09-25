# initializing objects
int_val = 4
str_val = 'PythonIsBest'
flt_val = 24.56

# Using hash method to print everything out
print('The integer hash value is:', hash(int_val))

# Note: the hash value for a string such as this is 
# never the same 2 times in a row, the other values stay consistent
# the reason for this, is that python uses a random hash seed to prevent 
# attackers from tar-pitting an application by sending you keys designed to collide
print('The string hash value is:', hash(str_val))

print('The float hash value is:', hash(flt_val))