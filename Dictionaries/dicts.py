

#import files
#fh = open('../Data/.txt')

# Dicts have key and values 
#they can be respresented as dicts literals 
#dicts literals == {'key':Value}
#initiate dict() constructor
# value = {}


#histogram 
#counts = dict()
# names = ['sxzhe','John','Bom','kim']
# for name in names:
#   if name not in names:
#       counts[name]= 1
#   else:
#       counts[names] = counts[name]+1
# print(counts)
# 

#However we can use 
# a get method instead of a loop
# x = counts.get(name,0) used to update the dict
#  

#reads a file and opens it
fname = input('Enter File name: ')
if len(fname)<1 : fname = 'clown.txt'
fhand = open(fname)

# loops through a file 
for line in fhand:
    line = line.rstrip()
   # print(line)
    words = line.split()
    print(words)

    count = 0
    di = dict()
    for word in words:
        #print('TTT:',word,di.get(word,-99))
    #    oldcount = di.get(word,0)
    #    print(word,'old',oldcount)
    #    newcount = oldcount+1
    #    di[word] = newcount
    #    print(word,'new', newcount)

        di[word] = di.get(word,0)+1
# The above line of code can replace the entire commented block
        # if word in di:
        #     di[word]= di[word]+1
        #     print('#exists#')
        # else:
        #     di[word]=1
        #     print('N**e***w')
        # count = count+1
        # print(word, di[word])
        # print(count)

print(di)
largest = -1
theword = None
for key,value in di.items():
    print(key,value)
    if value > largest:
        largest = value
        theword = key
print('Done: ', theword,largest)

