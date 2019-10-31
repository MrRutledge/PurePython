
# A class of partyAnimal

# class PartyAnimal:
#     x =0

#    # #constructors
#     def __init__(self):
#         print('I am constructed')
    
#    # #Paty method
#     def party(self):
#         self.x = self.x +1
#         print('so far ',self.x)
#     def __del__(self):
#         print('destructed',self.x)

# an = PartyAnimal()
# an.party()
# an.party()
# an.party()
# an = 45
# print('an contains:',an)

##*** INHERITANCE CLASS**
# class PartyAnimal:
#     x = 0
#     name =""

#     def __init__(self, z):
#         self.name = z
#         print(self.name,'I am constructed',self.x )
    
#     def party(self):
#         self.x = self.x +2
#         print(self.name,'Party:',self.x)
    
# s  = PartyAnimal('Sally')
# s.party()

#     #new objects instance

# j = PartyAnimal('Jim')
# j.party()

class PartyAnimal:
    """ Class for Party Animal"""
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print("Hey you just created me:", self.name)

    def party(self):
        self.x = self.x +1
        print(self.x,'Hey its a party', self.name)


    


