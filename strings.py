# STRINGS LESSON
# How to Create Strings in Python?

# Python string examples - all assignments are identical.
String_var = 'Python'
String_var = "Python"
String_var = """Python"""

# with Triple quotes Strings can extend to multiple lines
String_var = """ This document will help you to
explore all the concepts
of Python Strings!!! """

# Replace "document" with "tutorial" and store in another variable
substr_var = String_var.replace("document", "tutorial")
print(substr_var)

# Index and Slice Strings in Python
# Access Individual Characters of a String
# Python allows to index from the zeroth position in Strings.
# But it also supports negative indexes.Index of ‘-1’ represents the last character of the String.

# String Representation in Python
sample_str = 'Python String'
print(sample_str[0])  # return 1st character
# output: P
print(sample_str[-1])  # return last character
# output: g
print(sample_str[-2])  # return last second character
# output: n

# Slice a String in Python
# To retrieve a range ofcharacters in a String, we use ‘slicing operator,’ the colon ‘:’ sign.
# With the slicing operator, we define the range as [a: b]. Print all the characters of the String starting
# from index ‘a’ up to char at index ‘b - 1’.So the char at index ‘b’ is not a part of the output.
sample_str = 'Python String'
print(sample_str[3:5])  # return a range of character
# ho
print(sample_str[7:])  # return all characters from index 7
# String
print(sample_str[:6])  # return all characters before index 6
# Python
print(sample_str[7:-4])
# St
# 1 - If we try to retrieve characters at out of range index, then ‘IndexError’ exception will be raised.
sample_str = "Python Supports Machine Learning."
# print(sample_str[1024])  # index must be in range
# IndexError: string index out of range
# 2 - String index must be of the integer data type.
sample_str = "Welcome post"
# print(sample_str[1.25])  # index must be an integer
# TypeError: string indices must be integers

# Modify / Delete a String in Python
# Python Strings are by design immutable. It suggests that once a String binds to a variable, it can’t be modified.
sample_str = 'Python String'
sample_str[2] = 'a'
# TypeError: 'str' object does not support item assignment
sample_str = 'Programming String'
print(sample_str)
# Output=> Programming String
sample_str = "Python is the best scripting language."
del sample_str[1]
# TypeError: 'str' object doesn't support item deletion
del sample_str
print(sample_str)
# NameError: name 'sample_str' is not defined

# String Operators in Python

# Concatenation(+) It combines two strings into one.
# example
var1 = 'Python'
var2 = 'String'
print(var1 + var2)
# PythonString

# Repetition(*) This operator creates a new string by repeating it a given number of times.
# example
var1 = 'Python'
print(var1 * 3)
# PythonPythonPython

# Slicing[] The slice operator prints the character at a given index.
# example
var1 = 'Python'
print(var1[2])
# t

# Range Slicing[x:y] It prints the characters present in the given range.
# example
var1 = 'Python'
print(var1[2:5])
# tho

# Membership( in) This operator returns ‘True’ value if the character is present in the given String.
# example
var1 = 'Python'
print('n' in var1)
# True

# Membership(not in) It returns ‘True’ value if the character is not present in the given String.
# example
var1 = 'Python'
print('N' not in var1)
# True

# Iterating( for ) With this operator, we can iterate through all the characters of a string.
# example
for var in var1: print(var, end="")
# Python

# Raw String(r / R) We can use it to ignore the actual meaning of Escape characters inside a string.
# For this, we add ‘r’ or ‘R’ in front of the String.
# example
print(r'\n')
# \n
print(R'\n')
# \n

# String Formatting Operators in Python
# Python Escape Characters
# An Escape sequence starts with a backslash (\), which signals the compiler to treat it differently.
# Python subsystem automatically interprets an escape sequence irrespective of it is in a single-quoted or double-quoted Strings.
# escape the double - quotes and single - quotes as:
# print("Python is a "widely" used language")
# SyntaxError: invalid syntax
# After escaping with double-quotes
print("Python is a \"widely\" used language")
# Output: Python is a "widely" used language

# List of Escape Characters
# Escape Char         Name
# \\                  Backslash(\)
# \”                  Double - quote(“)
# \a                  ASCII bell(BEL)
# \b                  ASCII backspace(BS)
# \cx or \Cx          Control - x
# \f                  ASCII Form feed(FF)
# \n                  ASCII linefeed(LF)
# \N                  {name} Character named name in the Unicode database(Unicode only)
# \r                  Carriage Return(CR)
# \t                  Horizontal Tab(TAB)
# \uxxxx              A character with 16 - bit hex value xxxx (Unicode only)
# \Uxxxxxxxx          A character with 32 - bit hex value xxxxxxxx (Unicode only)
# \v                  ASCII vertical tab(VT)
# \ooo                Characters with octal value ooo
# \xnn                A character with hex value nn where n can be anything from the range 0-9, a-f, or A-F.

# Python Format Characters
# String ‘ % ’ operator issued for formatting Strings.We often use this operator with the print() function.
print("Employee Name: %s,\nEmployee Age:%d" % ('Ashish', 25))
# Employee Name: Ashish,
# Employee Age: 25

# List of Format Symbols
# Symbol      Conversion
# %c          character
# %s          string conversion via str() before formatting
# % i         signed decimal integer
# % d         signed decimal integer
# % u         unsigned decimal integer
# % o         octal integer
# % x         hexadecimal integer(lowercase letters)
# % X         hexadecimal integer(UPPER - case letters)
# % e         exponential notation(with lowercase ‘e’)
# % E         exponential notation(with UPPER - case ‘E’)
# % f         floating - point real number
# % g         the shorter of % f and % e
# % G         the shorter of % f and % E

# Unicode String  support in Python
# Regular Strings stores as the 8 - bit ASCII value, whereas Unicode String follows the 16 - bit ASCII standard.
# In Python, the letter ‘u’ works as a prefix to distinguish between Unicode and usual strings.
print(u' Hello Python!!')
# Hello Python

# Built - in String Functions in Python
# Conversion Functions

# 1. capitalize() – Returns the string with the first character capitalized and rest of the characters in lower case.
var = 'PYTHON'
print(var.capitalize())
# Python
# 2. lower() – Converts all the characters of the String to lowercase
var = 'TechBeamers'
print(var.lower())
# techbeamers
# 3. upper() – Converts all the characters of the String to uppercase
var = 'TechBeamers'
print(var.upper())
# TECHBEAMERS
# 4. swapcase() – Swaps the case of every character in the String means that lowercase characters got converted to
# uppercase and vice - versa.
var = 'TechBeamers'
print(var.swapcase())
# tECHbEAMERS
# 5. title() – Returns the ‘titlecased’ version of String, which means that all words start with uppercase and
# the rest of the characters in words are in lowercase.
var = 'welcome to Python programming'
print(var.title())
# Welcome To Python Programming
# 6. count(str[, beg[, end]]) – Returns the number of times substring ‘str’ occurs in the range[beg, end] if beg
# and end index are given else the search continues in full String Search is case - sensitive.
var = 'TechBeamers'
str = 'e'
print(var.count(str))
# 3
var1 = 'Eagle Eyes'
print(var1.count('e'))
# 2
var2 = 'Eagle Eyes'
print(var2.count('E', 0, 5))
# 1

# Comparison Functions – Part1
# 1. islower() – Returns ‘True’ if all the characters in the String are in lowercase.If any of the char is in uppercase, it will return False.
var = 'Python'
print(var.islower())
# False
var = 'python'
print(var.islower())
# True
# 2. isupper() – Returns ‘True’ if all the characters in the String are in uppercase.If any of the char is in lowercase, it will return False.
var = 'Python'
print(var.isupper())
# False
var = 'PYTHON'
print(var.isupper())
# True
# 3. isdecimal() – Returns ‘True’ if all the characters in String are decimal.If any character in the String is of other data-type, it will return False.
# Decimal characters are those from the Unicode category Nd.
num = u'2016'
print(num.isdecimal())
# True
# 4. isdigit() – Returns ‘True’ for any char for which isdecimal() would return ‘True and some characters in the ‘No’ category.If there are any characters other than these, it will return False’.
# Precisely, digits are the characters for which Unicode property includes: Numeric_Type = Digit or Numeric_Type = Decimal.
# For example, superscripts are digits, but fractions not.
print('2'.isdigit())
# True
print('²'.isdigit())
# True

# Comparison Functions – Part2
# 1. isnumeric() – Returns ‘True’ if all the characters of the Unicode String lie in any one of the categories Nd, No, and NI.
# If there are any characters other than these, it will return False.
# Precisely, Numeric characters are those for which Unicode property includes: Numeric_Type = Digit, Numeric_Type = Decimal or Numeric_Type = Numeric.
num = u'2016'
print(num.isnumeric())
# True
num = u'year2016'
print(num.isnumeric())
# False
# 2. isalpha() – Returns ‘True’ if String contains at least one character (non-empty String), and all the characters are alphabetic, ‘False’ otherwise.
print('python'.isalpha())
# True
print('python3'.isalpha())
# False
# 3. isalnum() – Returns ‘True’ if String contains at least one character (non-empty String), and all the characters are either alphabetic or decimal digits, ‘False’ otherwise.
print('python'.isalnum())
# True
print('python3'.isalnum())
# True

# Padding Functions
# 1. rjust(width[, fillchar]) – Returns string filled with input char while pushing the original content on the right side.
# By default, the padding uses a space.Otherwise, ‘fillchar’ specifies the filler character.
var = 'Python'
print(var.rjust(10))
# Python
print(var.rjust(10, '-'))
# ----Python
# 2. ljust(width[, fillchar]) – Returns a padded version of String with the original String left-justified to a total of width columns
# By default, the padding uses a space.Otherwise, ‘fillchar’ specifies the filler character.
var = 'Python'
print(var.ljust(10))
# Python

print(var.ljust(10, '-'))
# Python----
# 3. center(width[, fillchar]) – Returns string filled with the input char while pushing the original content into the center.
# By default, the padding uses a space.Otherwise, ‘fillchar’ specifies the filler character.
var = 'Python'
print(var.center(20))
# Python
print(var.center(20, '*'))
# *******Python*******
# 4. zfill(width) – Returns string filled with the original content padded on the left with zeros so that the total length of String becomes equal to the input size.
# If there is a leading sign(+ / -) present in the String, then with this function, padding starts after the symbol, not before it.
var = 'Python'
print(var.zfill(10))
# 0000Python
var = '+Python'
print(var.zfill(10))
# +000Python

# Search Functions
# 1. find(str[, i[, j]]) – Searches for ‘str’ in complete String ( if i and j not defined) or in a sub-string of String ( if i and j are defined).This function returns the index if ‘str’ is found else returns ‘-1’.
# Here, i = search starts from this index, j=search ends at this index.
var = "Tech Beamers"
str = "Beam"
print(var.find(str))
# 5
var = "Tech Beamers"
str = "Beam"
print(var.find(str, 4))
# 5
var = "Tech Beamers"
str = "Beam"
print(var.find(str, 7))
# -1
# 2. index(str[, i[, j]]) – This is same as ‘find’ method.The only difference is that it raises the ‘ValueError’ exception if ‘str’ doesn’t exist.
var = 'Tech Beamers'
str = 'Beam'
print(var.index(str))
# 5
var = 'Tech Beamers'
str = 'Beam'
print(var.index(str, 4))
# 5
var = 'Tech Beamers'
str = 'Beam'
print(var.index(str, 7))
# ValueError: substring not found
# 3. rfind(str[, i[, j]]) – This is same as find() just that this function returns the last index where ‘str’ is found.If ‘str’ is not found, it returns ‘-1’.
var = 'This is a good example'
str = 'is'
print(var.rfind(str, 0, 10))
# 5
print(var.rfind(str, 10))
# -1
# 4. count(str[, i[, j]]) – Returns the number of occurrences of substring ‘str’ in the String.
# Searches for ‘str’ in the complete String ( if i and j not defined) or in a sub-string of String ( if i and j are defined).
# Where: i = search starts from this index, j=search ends at this index.
var = 'This is a good example'
str = 'is'
print(var.count(str))
# 2 print(var.count(str, 4, 10)) # 1

# String Substitution Functions
# 1. replace(old, new[, count]) – Replaces all the occurrences of substring ‘old’ with ‘new’ in the String.
# If the count is available, then only ‘count’ number of occurrences of ‘old’ will be replaced with the ‘new’ var.
# Where old = substring to replace, new = substring
var = 'This is a good example'
str = 'was'
print(var.replace('is', str))
# Thwas was a good exampleprint (var.replace('is',str,1))
# Thwas is a good example
# 2. split([sep[, maxsplit]]) – Returns a list of substring obtained after splitting the String with ‘sep’ as a delimiter.
# Where, sep = delimiter, the default is space, maxsplit = number of splits to be done
var = "This is a good example"
print(var.split())
# ['This', 'is', 'a', 'good', 'example']print (var.split(' ', 3))
# ['This', 'is', 'a', 'good example']
# 3. splitlines(num) – Splits the String at line breaks and returns the list after removing the line breaks.
# Where num = if this is a positive value.It indicates that line breaks will appear in the returned list.
var = 'Print new line\nNextline\n\nMove again to new line'
print(var.splitlines())
# ['Print new line', 'Nextline', '', 'Move again to new line']print (var.splitlines(1))
# ['Print new line\n', 'Nextline\n', '\n', 'Move again to new line']
# 4. join(seq) – Returns a String obtained after concatenating the sequence ‘seq’ with a delimiter string.
# Where: the seq = sequence of elements to join
seq = ('ab', 'bc', 'cd')
str = '='
print(str.join(seq))
# ab=bc=cd

# Misc String Functions
# 1. lstrip([chars]) – Returns a string after removing the characters from the beginning of the String.
# Where: Chars = this is the character to be trimmed from the String. The default is whitespace character.
var = ' This is a good example '
print(var.lstrip())
# This is a good example
var = '*****This is a good example*****'
print(var.lstrip('*'))
# This is a good example**********
# 2. rstrip() – Returns a string after removing the characters from the End of the String.
# Where: Chars = this is the character to be trimmed from the String.The default is whitespace character.
var = ' This is a good example '
print(var.rstrip())
# This is a good example
var = '*****This is a good example*****'
print(var.lstrip('*'))
# *****This is a good example
# 3. rindex(str[, i[, j]]) – Searches for ‘str’ in the complete String ( if i and j not defined) or in a sub-string of String ( if i and j are defined).
# This function returns the last index where ‘str’ is available. If ‘str’ is not there, then it raises a ValueError exception.
# Where: i = search starts from this index, j=search ends at this index.
var = 'This is a good example'
str = 'is'
print(var.rindex(str, 0, 10))
# 5
print(var.rindex(str, 10))
# ValueError: substring not found
# 4. len(string) – Returns the length of given String
var = 'This is a good example'
print(len(var))
# 22

# In Python 3.6, a new style of strings got introduced, known as f-strings.