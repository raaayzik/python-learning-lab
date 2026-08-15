# ============================================================
# PYTHON STRINGS — COMPLETE PRACTICE WORKBOOK
# FROM BEGINNER TO ADVANCED
# ============================================================
#
# IMPORTANT:
# Everything in this workbook is commented out on purpose.
# Rewrite the code yourself, remove the #, and run it.
#
# Goal:
# Master Python strings from absolute basics to advanced usage.
#
# ============================================================
# TABLE OF CONTENTS
# ============================================================
#
# 01. What is a string?
# 02. Creating strings
# 03. Single quotes
# 04. Double quotes
# 05. Triple single quotes
# 06. Triple double quotes
# 07. Empty strings
# 08. Strings containing quotes
# 09. Escape characters
# 10. New lines
# 11. Tabs
# 12. Backslashes
# 13. Raw strings
# 14. Unicode strings
# 15. String type
# 16. String length
# 17. Indexing
# 18. Positive indexing
# 19. Negative indexing
# 20. Slicing
# 21. Slice start
# 22. Slice stop
# 23. Slice step
# 24. Reverse a string
# 25. String immutability
# 26. Joining strings
# 27. Concatenation
# 28. Repetition
# 29. Membership
# 30. Comparing strings
# 31. String methods
#
# 32. lower()
# 33. upper()
# 34. capitalize()
# 35. title()
# 36. swapcase()
# 37. casefold()
#
# 38. strip()
# 39. lstrip()
# 40. rstrip()
#
# 41. removeprefix()
# 42. removesuffix()
#
# 43. replace()
# 44. split()
# 45. rsplit()
# 46. splitlines()
# 47. partition()
# 48. rpartition()
# 49. join()
#
# 50. find()
# 51. rfind()
# 52. index()
# 53. rindex()
# 54. count()
# 55. startswith()
# 56. endswith()
#
# 57. isalpha()
# 58. isalnum()
# 59. isdecimal()
# 60. isdigit()
# 61. isnumeric()
# 62. isascii()
# 63. isspace()
# 64. islower()
# 65. isupper()
# 66. istitle()
# 67. isidentifier()
# 68. isprintable()
#
# 69. center()
# 70. ljust()
# 71. rjust()
# 72. zfill()
#
# 73. String formatting
# 74. %-formatting
# 75. str.format()
# 76. f-strings
# 77. Format specifications
# 78. Alignment
# 79. Width
# 80. Precision
# 81. Number formatting
# 82. Dates inside strings
# 83. Expressions inside f-strings
# 84. Debugging with f-strings
#
# 85. Multiline strings
# 86. Docstrings
# 87. String concatenation across lines
# 88. Implicit concatenation
#
# 89. Escape sequences
# 90. Unicode
# 91. Unicode code points
# 92. ord()
# 93. chr()
#
# 94. Encoding
# 95. Decoding
# 96. UTF-8
# 97. bytes vs str
#
# 98. String translation
# 99. translate()
# 100. maketrans()
#
# 101. ASCII
# 102. Unicode normalization
# 103. Regular expressions
# 104. re.search()
# 105. re.match()
# 106. re.fullmatch()
# 107. re.findall()
# 108. re.finditer()
# 109. re.sub()
# 110. re.split()
#
# 111. String formatting advanced
# 112. Nested formatting
# 113. Custom formatting
#
# 114. Strings and lists
# 115. Strings and tuples
# 116. Strings and dictionaries
# 117. Strings and sets
#
# 118. String parsing
# 119. Cleaning user input
# 120. Normalizing text
# 121. Extracting information
# 122. Building text
#
# 123. Performance
# 124. StringBuilder-style patterns
# 125. join() vs +=
#
# 126. Advanced indexing
# 127. Extended slicing
# 128. String subclasses
# 129. __str__()
# 130. __repr__()
# 131. Custom string classes
#
# 132. Security considerations
# 133. SQL strings
# 134. Shell strings
# 135. HTML strings
# 136. JSON strings
#
# 137. Common mistakes
# 138. Practice challenges
# 139. Mastery challenges
#
# ============================================================



# ============================================================
# 01 — WHAT IS A STRING?
# ============================================================

# A string is a sequence of characters.

# a = "Python"
# print(a)

# b = "Hello World"
# print(b)

# c = "12345"
# print(c)

# IMPORTANT:
# "12345" is a string.
# 12345 is an integer.

# a = "12345"
# b = 12345
#
# print(type(a))
# print(type(b))



# ============================================================
# 02 — CREATING STRINGS
# ============================================================

# Single quotes
# name = 'Python'

# Double quotes
# name = "Python"

# Triple single quotes
# text = '''Python'''

# Triple double quotes
# text = """Python"""



# ============================================================
# 03 — SINGLE QUOTES
# ============================================================

# a = 'Hello'
# print(a)

# a = 'Python programming'
# print(a)



# ============================================================
# 04 — DOUBLE QUOTES
# ============================================================

# a = "Hello"
# print(a)

# a = "Python programming"
# print(a)



# ============================================================
# 05 — TRIPLE SINGLE QUOTES
# ============================================================

# Triple quotes are useful for multiline strings.

# text = '''
# This is line one.
# This is line two.
# This is line three.
# '''

# print(text)



# ============================================================
# 06 — TRIPLE DOUBLE QUOTES
# ============================================================

# text = """
# This is line one.
# This is line two.
# This is line three.
# """

# print(text)



# ============================================================
# 07 — EMPTY STRING
# ============================================================

# empty = ""
# print(empty)

# print(len(empty))

# Empty string is still a string.

# print(type(empty))



# ============================================================
# 08 — STRINGS CONTAINING QUOTES
# ============================================================

# Single quote inside double quotes

# text = "Python's syntax"
# print(text)

# Double quote inside single quotes

# text = 'He said "Hello"'
# print(text)



# ============================================================
# 09 — ESCAPE CHARACTERS
# ============================================================

# Backslash is used for escape sequences.

# text = "Hello\nWorld"
# print(text)

# \n = newline

# text = "Hello\tWorld"
# print(text)

# \t = tab

# text = "Hello\\World"
# print(text)

# \\ = backslash

# text = "He said \"Hello\""
# print(text)

# \" = double quote

# text = 'It\'s Python'
# print(text)

# \' = single quote



# ============================================================
# 10 — NEWLINE
# ============================================================

# text = "Python\nJava\nC++"
# print(text)



# ============================================================
# 11 — TAB
# ============================================================

# text = "Name\tAge\tCity"
# print(text)



# ============================================================
# 12 — BACKSLASH
# ============================================================

# path = "C:\\Users\\Admin\\Documents"
# print(path)



# ============================================================
# 13 — RAW STRINGS
# ============================================================

# Raw strings treat backslashes mostly literally.

# path = r"C:\Users\Admin\Documents"
# print(path)

# Compare:

# normal = "C:\\Users\\Admin\\Documents"
# raw = r"C:\Users\Admin\Documents"

# print(normal)
# print(raw)

# Raw strings are particularly useful for regular expressions
# and Windows paths.



# ============================================================
# 14 — UNICODE STRINGS
# ============================================================

# Python 3 strings are Unicode.

# text = "Hello"
# print(text)

# text = "こんにちは"
# print(text)

# text = "你好"
# print(text)

# text = "مرحبا"
# print(text)

# text = "नमस्ते"
# print(text)

# text = "🙂"
# print(text)



# ============================================================
# 15 — STRING TYPE
# ============================================================

# text = "Python"

# print(type(text))

# Expected:
# <class 'str'>



# ============================================================
# 16 — STRING LENGTH
# ============================================================

# text = "Python"

# print(len(text))

# P y t h o n
# 1 2 3 4 5 6

# len() counts characters.



# ============================================================
# 17 — INDEXING
# ============================================================

# A string is a sequence.

# text = "Python"

# Each character has an index.

# P y t h o n
# 0 1 2 3 4 5

# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])



# ============================================================
# 18 — POSITIVE INDEXING
# ============================================================

# text = "Python"

# print(text[0])
# print(text[1])
# print(text[2])



# ============================================================
# 19 — NEGATIVE INDEXING
# ============================================================

# Negative indexes start from the end.

# P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

# text = "Python"

# print(text[-1])
# print(text[-2])
# print(text[-3])
# print(text[-6])



# ============================================================
# 20 — SLICING
# ============================================================

# Syntax:
#
# string[start:stop]
#
# stop is NOT included.

# text = "Python"

# print(text[0:2])

# Result:
# Py



# ============================================================
# 21 — SLICE START
# ============================================================

# text = "Python"

# print(text[2:])
# print(text[3:])
# print(text[0:])



# ============================================================
# 22 — SLICE STOP
# ============================================================

# text = "Python"

# print(text[:2])
# print(text[:4])
# print(text[:6])



# ============================================================
# 23 — SLICE STEP
# ============================================================

# Syntax:
#
# string[start:stop:step]

# text = "Python"

# print(text[0:6:1])
# print(text[0:6:2])
# print(text[0:6:3])



# ============================================================
# 24 — REVERSE A STRING
# ============================================================

# text = "Python"

# print(text[::-1])

# This is one of the most common Python string tricks.



# ============================================================
# 25 — STRING IMMUTABILITY
# ============================================================

# Strings are immutable.

# text = "Python"

# This does NOT work:

# text[0] = "J"

# You cannot directly change one character.

# Instead:

# text = "J" + text[1:]

# print(text)



# ============================================================
# 26 — CONCATENATION
# ============================================================

# first = "Hello"
# second = "World"

# result = first + second

# print(result)

# Add a space:

# result = first + " " + second
# print(result)



# ============================================================
# 27 — STRING REPETITION
# ============================================================

# text = "Python"

# print(text * 3)

# print("-" * 30)

# print("=" * 50)



# ============================================================
# 28 — MEMBERSHIP
# ============================================================

# text = "Python programming"

# print("Python" in text)
# print("Java" in text)

# print("Python" not in text)
# print("Java" not in text)



# ============================================================
# 29 — STRING COMPARISON
# ============================================================

# a = "apple"
# b = "banana"

# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)

# String comparison is lexicographical.



# ============================================================
# 30 — CASE-SENSITIVE COMPARISON
# ============================================================

# a = "Python"
# b = "python"

# print(a == b)

# They are different strings.



# ============================================================
# 31 — LOWER
# ============================================================

# text = "PYTHON"

# print(text.lower())



# ============================================================
# 32 — UPPER
# ============================================================

# text = "python"

# print(text.upper())



# ============================================================
# 33 — CAPITALIZE
# ============================================================

# text = "python programming"

# print(text.capitalize())



# ============================================================
# 34 — TITLE
# ============================================================

# text = "python programming language"

# print(text.title())



# ============================================================
# 35 — SWAPCASE
# ============================================================

# text = "PyThOn"

# print(text.swapcase())



# ============================================================
# 36 — CASEFOLD
# ============================================================

# casefold() is stronger than lower() for
# case-insensitive text comparisons.

# a = "HELLO"
# b = "hello"

# print(a.casefold() == b.casefold())



# ============================================================
# 37 — STRIP
# ============================================================

# text = "   Python   "

# print(text.strip())



# ============================================================
# 38 — LSTRIP
# ============================================================

# text = "   Python   "

# print(text.lstrip())



# ============================================================
# 39 — RSTRIP
# ============================================================

# text = "   Python   "

# print(text.rstrip())



# ============================================================
# 40 — STRIP SPECIFIC CHARACTERS
# ============================================================

# text = "...Python..."

# print(text.strip("."))

# IMPORTANT:
# strip() does not mean "remove this exact substring".
# It removes characters from the ends.



# ============================================================
# 41 — REMOVEPREFIX
# ============================================================

# text = "Mr. John"

# print(text.removeprefix("Mr. "))

# Useful when you know the exact prefix.



# ============================================================
# 42 — REMOVESUFFIX
# ============================================================

# filename = "report.txt"

# print(filename.removesuffix(".txt"))



# ============================================================
# 43 — REPLACE
# ============================================================

# text = "I like Java"

# text = text.replace("Java", "Python")

# print(text)



# ============================================================
# 44 — REPLACE WITH COUNT
# ============================================================

# text = "apple apple apple"

# print(text.replace("apple", "orange", 1))

# print(text.replace("apple", "orange", 2))

# print(text.replace("apple", "orange", 3))



# ============================================================
# 45 — SPLIT
# ============================================================

# text = "Python Java C++"

# result = text.split()

# print(result)

# split() converts a string into a list.



# ============================================================
# 46 — SPLIT USING A DELIMITER
# ============================================================

# text = "apple,banana,orange"

# result = text.split(",")

# print(result)



# ============================================================
# 47 — SPLIT WITH MAXSPLIT
# ============================================================

# text = "one-two-three-four"

# print(text.split("-", 1))

# print(text.split("-", 2))

# print(text.split("-", 3))



# ============================================================
# 48 — RSPLIT
# ============================================================

# text = "one-two-three-four"

# print(text.rsplit("-", 1))

# print(text.rsplit("-", 2))



# ============================================================
# 49 — SPLITLINES
# ============================================================

# text = """Python
# Java
# C++
# JavaScript"""

# print(text.splitlines())



# ============================================================
# 50 — PARTITION
# ============================================================

# text = "name=John"

# print(text.partition("="))

# partition() returns:
#
# (before, separator, after)



# ============================================================
# 51 — RPARTITION
# ============================================================

# text = "one=two=three"

# print(text.rpartition("="))



# ============================================================
# 52 — JOIN
# ============================================================

# words = ["Python", "is", "powerful"]

# result = " ".join(words)

# print(result)



# ============================================================
# 53 — JOIN WITH COMMA
# ============================================================

# words = ["Python", "Java", "C++"]

# result = ", ".join(words)

# print(result)



# ============================================================
# 54 — JOIN WITH NEWLINE
# ============================================================

# lines = ["Line one", "Line two", "Line three"]

# result = "\n".join(lines)

# print(result)



# ============================================================
# 55 — FIND
# ============================================================

# text = "Python programming"

# print(text.find("Python"))
# print(text.find("programming"))
# print(text.find("Java"))

# find() returns -1 if not found.



# ============================================================
# 56 — RFIND
# ============================================================

# text = "one two one two"

# print(text.rfind("one"))



# ============================================================
# 57 — INDEX
# ============================================================

# text = "Python programming"

# print(text.index("Python"))

# Difference:
#
# find() -> -1 if missing
# index() -> ValueError if missing



# ============================================================
# 58 — RINDEX
# ============================================================

# text = "one two one"

# print(text.rindex("one"))



# ============================================================
# 59 — COUNT
# ============================================================

# text = "banana"

# print(text.count("a"))
# print(text.count("an"))
# print(text.count("banana"))



# ============================================================
# 60 — STARTSWITH
# ============================================================

# text = "Python programming"

# print(text.startswith("Python"))
# print(text.startswith("Java"))



# ============================================================
# 61 — ENDSWITH
# ============================================================

# filename = "document.pdf"

# print(filename.endswith(".pdf"))
# print(filename.endswith(".txt"))



# ============================================================
# 62 — ISALPHA
# ============================================================

# print("Python".isalpha())
# print("Python123".isalpha())
# print("123".isalpha())



# ============================================================
# 63 — ISALNUM
# ============================================================

# print("Python123".isalnum())
# print("Python".isalnum())
# print("123".isalnum())
# print("Python 123".isalnum())



# ============================================================
# 64 — ISDECIMAL
# ============================================================

# print("123".isdecimal())
# print("12.3".isdecimal())
# print("-123".isdecimal())



# ============================================================
# 65 — ISDIGIT
# ===============================
