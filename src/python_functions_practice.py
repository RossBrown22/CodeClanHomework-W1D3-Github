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
    months = ["Jan", "Feb", "Mar", 
            "Apr", "May", "Jun", "Jul", "Aug", 
            "Sep", "Oct", "Nov", "Dec"]
    
    return months[integer_1 - 1]