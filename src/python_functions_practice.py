def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def length_of_string(rope):
    return len(rope)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(integer_1):
    months = ["January", "February", "March", 
            "April", "May", "June", "July", "August", 
            "September", "October", "November", "December"]
    
    return months[integer_1 - 1]

def number_to_short_month_name(integer_1):    
    # Simple long way
    # months = ["Jan", "Feb", "Mar", 
    #         "Apr", "May", "Jun", "Jul", "Aug", 
    #         "Sep", "Oct", "Nov", "Dec"]
    # return months[integer_1 - 1]

    # shorter but reliant on another function - probably bad if we are testing individual functions
    # using string's list operator []
    # https://thispointer.com/python-how-to-get-first-n-characters-in-a-string/
    return number_to_full_month_name(integer_1)[0 : 3]


def volume_of_a_cube(length):
    # use ** for "to the power of"
    return length ** 3

def reverse_string(string):
    # https://www.w3schools.com/python/python_howto_reverse_string.asp (magic)
    # A slice that steps backwards [::-1]
    return string [::-1]

def fahrenheit_to_celsius(fh):
    # https://www.rapidtables.com/convert/temperature/how-fahrenheit-to-celsius.html
    return (fh - 32) * (5.0/9)
