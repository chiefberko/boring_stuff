# Write your code here :-)
import re

# reg = re.compile(r"\d+")
# mo = reg.search("I was born in 1986.")
# print(mo.group())

reg = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = reg.search("My details: First Name: Johnson Last Name: Berko")
print(mo.groups())
