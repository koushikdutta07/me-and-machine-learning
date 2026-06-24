s = "hello world"
s.upper()        # 'HELLO WORLD'
s.lower()        # 'hello world'
s.capitalize()   # 'Hello world'
s.title()        # 'Hello World'
s.swapcase()     # 'HELLO WORLD'
s.casefold()     # stronger lower(), useful for comparisons
s.replace("world", "there")  # 'hello there'



#stripping whitespace and characters
s = "   hello   "
s.strip()      # 'hello'
s.lstrip()     # 'hello   '
s.rstrip()     # '   hello'

s = "###hello###"
s.strip("#")   # 'hello'

"Mr. John".removeprefix("Mr. ") # 'John'
"hello.py".removesuffix(".py") # 'hello'



# finding and counting substrings
s = "banana"
s.find("na")      # 2 locates the first occurrence from left (returns -1 if not found) 
s.rfind("na")     # 4 locates the first occurrence from right (returns -1 if not found) 
s.index("na")     # 2 same as find() (raises error if not found)
s.rindex("na")    # 4 same as rfind() (raises error if not found)
s.startswith("ba")  # True
s.endswith("py")   # False
s.count("a")      # 3 (counts occurrences of substring)



# checking string properties
"abc".isalpha()       # True (checks if all characters are alphabetic)
"123".isdigit()       # True (checks if all characters are digits)
"abc123".isalnum()    # True (checks if all characters are alphanumeric)
"hello".islower()     # True (checks if all characters are lowercase)
"HELLO".isupper()     # True (checks if all characters are uppercase)
"Hello".istitle()     # True (checks if the string is in title case)
"   ".isspace()       # True (checks if all characters are whitespace)



# formatting strings
s = "I like Java"
s.replace("Java", "Python")  # 'I like Python'
"aaa".replace("a", "b", 2) # 'bba' limits the number of replacements to 2



#splitting and joining strings
s = "apple,banana,mango"
s.split()  # ['apple,banana,mango'] 
# split() without arguments splits on whitespace
# no whitespace in the string, so it returns the whole string as a single element in a list
s.split(",")  # ['apple', 'banana', 'mango'] 


s.partition(",")  # ('apple', ',', 'banana,mango') splits the string into a tuple of three parts: the part before the separator, the separator itself, and the part after the separator
# useful for splitting a string into two parts based on the first occurrence of a separator


# join() is the opposite of split()
# separator.join(iterable) 
t = ("hi", "there")
joined_string =' '.join(t)  # 'hi there'
joined_string2 = '-'.join(t)  # 'hi-there'
joined_string3 = ''.join(t)  # 'hithere'
joined_string4 = s.join(t)  # 'hihello worldthere'