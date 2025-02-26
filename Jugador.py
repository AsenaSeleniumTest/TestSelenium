
class Person:
    """ _summary_ The constructor of the class """
    def __init__(self,name,age,height,genero):
        self.__name=name
        self.__age=age
        self.__height=height
        self.__gender=genero
    ##Method to show details of the person  
    def show_details(self):
        """_summary_
        ## Method to show details of the person

        Returns:
            _type_: Display details for the Person class
        """          
        return f"Name: {self.__name} \n Age: {self.__age} \nheight:  {self.__height} \n gender : {self.__gender}"
    
    ##properties getters for the Person       
    def get_person_name(self)->str:
        """ _summary_ Get the name of the person"""
        return self.__name
    def get_person_age(self)->int:
        """ _summary_ Get the age of the person"""
        return self.__age
    def get_person_height(self)->float:
        """ _summary_ Get the height of the person"""
        return self.__height
    def get_person_gender(self)->str:
        """ _summary_ Get the gender of the person"""
        return self.__gender

class Player(Person):
    """ _summary_ The constructor of the class Player"""
    def __init__(self,name,age,height,gender,tipo,intelligence,stamina,strenght,agility):
        super().__init__(name, age, height, gender )
        ##properties definition
        self.__type=tipo
        self.__intelligence=intelligence
        self.__stamina=stamina
        self.__strength=strenght
        self.__agility=agility
    ##properties getters for the Player
    def get_player_type(self)->str:
        """_summary_ Get the type of the player
            str: _description_
        """
        return self.__type  
    def get_player_intelligence(self)->int:
        """ _summary_ Get the intelligence of the player"""
        return self.__intelligence
    def get_player_stamina(self)->int:
        """ _summary_ Get the stamina of the player"""
        return self.__stamina
    def get_player_strength(self)->int:
        """ _summary_ Get the strength of the player"""
        return self.__strength
    def get_player_agility(self)->int:
        """_summary_ Get the agility of the player"""
        return self.__agility
    def set_player_type(self,new_type): 
        """_summary_ Set the type of the player"""
        self.__type=new_type    
    
    ## Methods that define actions of the player
    def change_class_type(self,new_type):
        """ _summary_ Change the class of the player """
        current_type = self.get_player_type()
        if current_type != new_type:
            self.set_player_type(new_type)
            return True
        else:
            print("The player already has this class or error to change the player type class")
            return False
        
            
    ## Method that shows the details of the player
    def show_stats(self):
        """ _summary_ Show the stats of the player"""
        return (f"{self.show_details()}, Type: {self.get_player_type()},Intelligence: {self.get_player_intelligence()},Stamina : {self.get_player_stamina()},"
                f"Strength : {self.get_player_strength()}, Agility : {self.get_player_agility()}")
    
    
class Mago(Player):
    def __init__(self,name,age,height,genero, tipo, intelligence, stamina, strenght, agility,mana,atributo):
        super().__init__(name,age,height,genero,tipo, intelligence, stamina, strenght, agility)
        self.__mana=mana
        self.__atributo=atributo
    ##properties getters for the Mago        
    def get_mago_mana(self)->int:
        """ _summary_ Get the mana of the Magician"""
        return self.__mana
    def get_mago_atributo(self)->list:
        """ _summary_ Get the atribute of the Magician"""
        return self.__atributo
    ## Methods that define actions of the Magician
    
    ## Method that shows the details of the Magician
    def show_mage_details(self):
        """ _summary_ Show the details of the Magician"""
        return (f"{self.show_stats()}\n, Mana : {self.get_mago_mana()},\n Atribute : {self.get_mago_atributo()}\n ")


class Knight(Player):
    def __init__(self,name,age,height,genero, tipo, intelligence, stamina, strenght, agility,aura):
        super().__init__(name,age,height,genero, tipo, intelligence, stamina, strenght, agility)
        self.__aura=aura  
    ##properties getters for the Knight
    def get_knight_aura(self)->int:
        """ _summary_ Get the aura of the Knight"""
        return self.__aura
    ## Methods that define actions of the Knight
    def level_up_aura(self,level):
        """ _summary_ Level up the aura of the Knight"""
        self.__aura+=level
    
        
    ## Method that shows the details of the Knight  
    def show_knight_details(self):
        """ _summary_ Show the details of the Knight"""
        return (f"{self.show_stats()},\n Aura : {self.get_knight_aura()} \n")
   

atributos_comunes = ["fire","water","earth","air"]
special_attributes = ["Metal","Wood","Poison","Space","light","dark","Time","Ice","Thunder","Sound","Magnetism",
                      "Gravity","Plasma","Lava","Sand","Crystal","Steam","Smoke","Acid","Radiation","Shadow","Wind",
                      "Plant"]
warrior_types = ["Dark night","SwordMaster","Paladin","Berserker","Valkyrie"]
mage_types = ["Spellcaster","Necromancer","Druid","Elementalist","Sorcerer","Wizard","Warlock","Enchanter","Illusionist",]


caballero1 = Knight("Dark night",15,1.85,"M",warrior_types[0],10,10,10,10,15)
caballero1.level_up_aura(5)

print(caballero1.show_knight_details())
mage1=Mago("Merlin",18,1.87,"M","Spellcaster",10,10,5,9,15,special_attributes)
print(mage1.show_mage_details())