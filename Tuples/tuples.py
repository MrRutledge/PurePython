# Tuples just like list are used as data structures 
# They are initiated like a=(1,2,3,4,4,5,65,6)
# t1 = (12,23) t2=('a')
# types(t1)
# fh = open('mbox_short.txt')
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)

# d = {'a': 10, 'b': 1, 'c': 22}
# t = list(d.items())
# t


# t.sort()
# t
# for key, val in list(d.items()):
#     print(val, key)

# import string
# fhand = open('romeo-full.txt')
# counts = dict()
# for line in fhand:
# line = line.translate(str.maketrans('', '', string.punctuation))
# line = line.lower()
# words = line.split()
# for word in words:
# if word not in counts:
# counts[word] = 1
# else:
# counts[word] += 1
# # Sort the dictionary by value
# lst = list()
# for key, val in list(counts.items()):
# lst.append((val, key))
# lst.sort(reverse=True)
# for key, val in lst[:10]:
# print(key, val)


# fh  = open('../Data/mbox_short.txt')

# for line in fh:
#     line = line.rstrip()

#     words = line.strip()
#     print(words)

#     #count = 0
#     di = dict()
#     for word in words:
#         di[word] = di.get(word, 0)+1
# print(di)
# largest = -1
# theword = None
# for key,value in di.items():
#     print(key,value)
#     if value > largest:
#         largest = value
#         theword = key
# print('Done: ', theword,largest)       

# import the file 
inp = input('Enter the filename:')

#count = 0
#Total =0
try:
       fh = open('../Data/mbox_short.txt')
except FileNotFoundError:
        print('File not in the system', fh)
        quit()
        
lst = list()
di = dict()
for line in fh:
        line  = line.rstrip()
        if not line.startswith('From'):
                continue
        wrds = line.split()
        #print(line)
        #print(wrds)
        for word in wrds:
                #if  (quote.find('be,') != -1):
                if (word.find('@') != -1):
                         di[word] = di.get(word,0)+1
#print(di)    
#largest = -1
#theword =  None 
for key, value in list(di.items()):
        lst.append((value, key))
lst.sort(reverse=True)

for key, value in lst[:1]:
        print(key, value)
#print('Address:',lst.sort(reverse=True))
