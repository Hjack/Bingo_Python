# Bingo Generator

import random

picked_numbers = []
while len(picked_numbers) != 75:
    x = random.randrange(1,76)
    while x in picked_numbers:
        x = random.randrange(1,76)
    picked_numbers.append(x)    
    if x < 16:
        print "B",x
    if x > 15 and x < 31:
        print "I",x
    if x > 30 and x < 46:
        print "N",x
    if x > 45 and x < 61:
        print "G",x
    if x > 60 and x < 76:
        print "O",x
    raw_input('Press enter to continue')    
    

