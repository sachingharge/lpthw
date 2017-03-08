"""
Numberes and Math Exercise
"""

print "I will now count my chicken:"

# It does addition and division
print "Hens", 25 + 30 / 6
'''
1. 30 / 6 = 5
2. 25 + 5 = 30
'''
print "------------------------------------"

# It does subtraction, multiply and modulus
print "Roosters", 100 - 25 * 3 % 4
'''
As per order: multiply and modulus comes first before addition or subtraction
1. 25 * 3 = 75
2. 75 % 4 = 3 (because 75/4 = 18 so remainder value 3)
3. 100 - 3 = 97 (result)
'''

print "------------------------------------"
print "Now I will count eggs without floating point:"
# It does addition, subtraction, modulus, divide
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
'''
1. 4 % 2 = 0 (because 4/2 has no remainder)
2. 1 / 4 = 0 (because no floating point)
3. 3 + 2 + 1 - 5 + 0 - 0 + 6 = 7 (rounded result due to no floating point)
'''
print "------------------------------------"
print "Now I will count eggs without floating point:"
# It does addition, subtraction, modulus, divide
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6
'''
1. 4 % 2 = 0 (because 4/2 has no remainder)
2. 1.0 / 4 = 0.25 (need .0 to make floating point)
3. 3 + 2 + 1 - 5 + 0 - "0.25" + 6 = 6.75 (used quotes to emphasize, do not type those)
'''

print "It is true that 3 + 2 < 5 -7 ?"
# It does addition, substraction and less than
print 3 + 2 < 5 - 7
print "------------------------------------"
# It does addition
print "What is 3 + 2?", 3 + 2
# It does substraction
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."
print "------------------------------------"

print "How about some more."
# It does more than comparison
print "It is greater?", 5 > -2
print "------------------------------------"

# It does greater than or equal comparison
print "It is greater or equal", 5 >= -2
print "------------------------------------"

# It does less than or equal comparison
print "It is less than or equal", 5 <= -2
print "------------------------------------"


# Few more code to understand integers and floating point Numberes
print "This show math with integers vs floating point numbers"

print "5/4 =", 5/4, "(The .25 got truncated)"
print "5.0/4 =", 5.0/4
print "5/4.0 =", 5/4.0
print "5.0/4.0 =", 5.0/4.0
