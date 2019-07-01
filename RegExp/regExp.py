#Regex are used to do smart searching in strings mostly, things like find, search for specific information
# very powerful and quite  crypyic 
# fun once understood
#   its imported using import re

import re 
hand = open('../Data/mbox_short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:',line): 
#         print(line)

# ^ begining of the line
# X match the same itself
# . matches any character
# * matches many characters
# ^X-\S+:
# \S non white/ blank charatcter
# Greedy matching is when it can match more than one string itg chooses the largest string. 
# X = 'My favourrite numbers are  19 and 42'
# y = re.findall('[0-9]+',X)
# g = re.findall('[AOUEI]+',X)
# print(y,g)
# printing particular characters just prefix it with a forward slash 

##
#GREEDY MAYCHING
# import re

# x = 'From: Using the: character'
# y = re.findall('^F.+:', x)
# g = re.findall('^F.+?:',x)
# print(y,g)
# #NonGreedy
# ex = re.findall('\S+i\S+',x)
# ex1 = re.findall('\S+i\S+?', x)
# print(ex,ex1)

#String parsing using Regex
numlist = list()
for line in hand:
    line =line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) >= 1: continue
    num =float(stuff[0])
    numlist.append(num)
print('Max:',max(numlist))
