# Text files 
#Using Open() for reading and opening using a file handle. open(filename, r)
#
#n =2+3
#print(n)


# Open a file 
#fh = open('mbox_short.txt')
#count = 0
fh = open('../Data/mbox_short.txt')
#fh = open('..','Data','mbox_short.txt')
count = 0
for line in fh:
    liney = line.rstrip()
    print(liney.upper())

# READ THE WHOLE FILE
inp = fh.read()
print(len(inp))
print(inp[9:20]) 
print(inp[94600:])

#SEARCHING THE FILE
#count = 0
#for line in fh:
 #   if line.startswith('From'):
 #       count = count+1
  #      print(line)
#print('Count',count)

# Without new Lines

#for line in fh:
    #line = line.rstrip()
    #if line.startswith('From'):
     #   print(line)

#Skipping reading through lines without

#for line in fh:
 #   line = line.rstrip()
  #  if not line.startswith('From'):
   #     continue
    #print(line)

#Searching for a specific line in the middle

#for line in fh:
 #   line = line.rstrip()
  #  if not 'cwen@iupui.edu' in line:
   #     continue
    #print(line)

#USER INPUT
#inp = input('Enterfile: ')
#try:
 #   if inp == 'mbox': fh = open('../Data/mbox_short.txt')
#except:
 #   print('File non existant')
#    exit()
#for line in fh:
    #line = line.rstrip()
    #if not 'X-DSPAM-Confidence: 0.8475' in line:
    #    continue 
   # print(line)

inp = input('Enterfile: ')
try:
   if inp == 'mbox_short': 
       fh = open('../Data/mbox_short.txt')
   elif inp == 'mbox_big':
        fh = open('../Data/mbox.txt')
except: 
    print('File non existant')
    exit()

count =0
tot = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    str = line.find(':')
    Int_val = float(line[str+2:])
    print(Int_val)
    print(line)
    count = count + 1
    tot = tot + Int_val
average= tot/count

print('Count: ',count,'\nTotal: ',tot, '\nAverage: ',average)
#print(tot)
