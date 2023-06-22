 #9. What three functions can be used to get the integer, floating-point number, or string version of a value?

#int()   this function can be used to convert a value to an integer . it take a single argument and returns the
#integer representation of that value if the value can not be converted to an integer it will raise a 'valueerror'
#exception

value = "87"
integer_value = int(value)
print(value)
type(value)


# float() this function convert a value too a floting point number it also takes a single argument and returns 
# the floating point representation of the value if the value can not be converted to a flot it will raise a 
# value error exception

value = "8.8"
float_value = float(value)
print(value)
type(value)


# str() this function converts a value to a string it take a single argument and returns the 
# string representation of the value

value = 78
string_value = str(value)
print(value)
type(value)