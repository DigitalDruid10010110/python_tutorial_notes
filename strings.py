# Notes: This file contains examples of strings in Python

message = "Hello World"  # string

print(message)  # Hello World

# escape method  (backslash)  (\)  (escape character)

message2 = "Hello \"World\""  

print(message2)  # Hello "World"

# different quote methods (double quote)  (single quote)  (triple quote)
message3 = 'Hello "World"'  # Hello "World"
message3 = "Hello 'World'"  # Hello 'World'
message3 = """Hello "World" """  # Hello "World"

print(message3)  # Hello "World"

# len method (length)

print(len(message))  # 11 (spaces count)

# len function for index  (0 to 10 = 11 characters)

print(message[0])  # H

# range of index and slicing  (colon)  (:)  (start:stop)  (start:stop:step)  (stop is not included in the range of index and slicing)

print(message[0:5])  # Hello
print(message[:5])  # Hello
print(message[6:])  # World
print(message.lower())  # hello world
print(message.upper())  # HELLO WORLD
print(message.count("Hello"))  # 1
print(message.count("l"))  # 3
print(message.find("World"))  # 6
print(message.find("Universe"))  # -1 (not found)
new_message = message.replace("World", "Universe")  # Hello Universe
print(new_message)  # Hello Universe

# concatenation   (string+string    string+variable   variable+variable  string+string+variable+variable)

greeting = "Hello"
name = "Michael"

message4 = greeting + ", " + name + ". Welcome!"

print(message4) # Hello, Michael. Welcome!

# formatted string (f string)  (f"{}")  (f"{variable}")  (f"{variable.method()}")  (f"{variable.upper()}")

message5 = "{}, {}. Welcome!".format(greeting, name)

print(message5) # Hello, Michael. Welcome!

# f string (formatted string) (f"{}")  (f"{variable}")  (f"{variable.method()}")  (f"{variable.upper()}")

message6 = f"{greeting}, {name.upper()}. Welcome!"

print(message6) # Hello, MICHAEL. Welcome!

# dir function (directory)  (methods)  (attributes)

print(dir(name))  # list of methods and attributes for the variable name

print(help(str)) # list of methods and attributes for the string data type (press q to exit)

# string methods (methods)  (attributes) (functions)

print(message.title()) # Hello World

