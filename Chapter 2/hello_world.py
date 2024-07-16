"""-----------------------------
# Strings
-----------------------------"""

from decimal import Decimal

message = "hellO python world!"

print(message)  # hellO python world!
print(message.title())  # Hello Python World!
print(message.upper())  # HELLO PYTHON WORLD!
print(message.lower())  # hello python world!

"""-----------------------------
# Using variables in string
-----------------------------"""
first_name = "ada"
last_name = "lovelace"

# This is called f-string. f is for format
print(f"{first_name} {last_name}")  # ada lovelace

"""-----------------------------
# Stripping whitespace
-----------------------------"""
favorite_language = "     python "
print(favorite_language.lstrip())
print(favorite_language)

# interestingly, the original string is not changed.
# It is just the output that is changed
print(favorite_language.rstrip())
print(favorite_language.strip())

"""-----------------------------
# Removing prefix and suffix
-----------------------------"""
full_url = "https://www.google.com"
print(full_url.lstrip("https://"))  # output: www.google.com
print(full_url.removeprefix("https://"))  # output: www.google.com
print(full_url.removesuffix(".com"))  # output: https://www.google

# Multiple function can be used to achieve the same result.

"""-----------------------------
# Working with Numbers
-----------------------------"""
sum = 0.1 + 0.2
print(sum)  # 0.30000000000000004

sum2 = Decimal("0.1") + Decimal("0.2")
print(sum2)  # 0.3

# You can group large numbers using underscore
universe_age = 14_000_000_000
print(universe_age)  # 14000000000

"""-----------------------------
# Multiple assignment
-----------------------------"""
x, y, z = 0, 0, "what"
print(x, y, z)

"""-----------------------------
Constants  
-----------------------------"""
# No built in constant type
MAX_CONNECTIONS = 5000
