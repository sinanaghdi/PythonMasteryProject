"""
this is automation script-- to find patterns with regex
"""
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
mo = phoneNumRegex.search('My number is 918-734-7840.') # mo stands for match object
# print('Phone number found : ' + mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(3))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
# # print(mainNumber)

