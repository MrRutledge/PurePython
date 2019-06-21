#Lists are important data structures in Python
#write a program to open a file read it and check if its got a specific word in it.

fh = open('../Data/mbox_short.txt')

# doesnt work because the if statment 
#for line in fh:
 #   line = line.rstrip()
  #  wds = line.split()
   # if wds[0] != 'From':
    #    continue
    #print(wds[2])


for line in fh:
    line = line.rstrip()
    wds = line.split()
    #gurdian line
   # if len(wds)<1: continue
    if len(wds)<3 or wds[0] != 'From':
        continue
    print(wds[2])



