
class Person:
    pass

class Player(Person):
    def __init__(self):
        ##properties definition
        __name:str
        __age:int
        __gender:str
        __race:str
    
class Snake:
    def __init__(self,victimdefault = 1):
        self.victims = victimdefault
    
    def increment(self,isVictim):
        if isVictim:
            self.victims +1
        return self.victims    
                    
            
       
    
## End of class Player    

my_player = Player()
my_player.a = 1
my_player.b = 2
my_player.c = 3
my_player.inumero = 5
my_player.ireal = 5.5
my_player.itipo ='dragon'
my_player.z = 7

def incIntsI(my_player):
    for name in my_player.__dict__.keys():
        if name.startswith('__n'):
            val = getattr(my_player, name)
            if isinstance(val, str):
                setattr(my_player, name, val + str(2))
stack=[]
stack.append(my_player)
incIntsI(my_player)
print(my_player.__dict__)