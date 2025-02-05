class Timer:
    def __init__( self,hora,minuto,segundo ):
        self.__horas = hora
        self.__minute = minuto
        self.__second = segundo
    
    def __str__(self):
        
        cad1 =self.__horas
        cad2 = self.__minute
        cad3 = self.__second
        cad = str(cad1)+':'+ str(cad2)+':'+ str(cad3)
        if cad1 < 10: 
            h01 = '0' + str(cad1)
        else:
            h01 = str(cad1)    
        if cad2 < 10:
            h02 = '0' + str(cad1)
        else:
            h02 = str(cad2)
        if cad3 < 10:
            h03 = '0' + str(cad1)
        else:
            h03 = str(cad3)    
        cad = str(h01)+':' +str(h02)+':'+str(h03)        
        return cad
               

    def next_second(self):
                
        if self.__horas ==23 and self.__minute == 59 and self.__second == 59 :
            self.__horas = 0
            self.__minute = 0
            self.__second = 0            
        elif self.__minute == 59 and self.__second == 59:
            self.__horas +=1
            self.__minute = 0
            self.__second = 0
        elif self.__second == 59 :
            self.__minute += 1
            self.__second = 0
        else:
            self.__second += 1
                
            
    def prev_second(self):
        if self.__horas ==0 and self.__minute == 0 and self.__second == 0 :
            self.__horas = 23
            self.__minute = 59
            self.__second = 59            
        elif self.__minute == 0 and self.__second == 0:
            self.__horas -=1
            self.__minute = 59
            self.__second = 59
        elif self.__second == 0 :
            self.__minute -= 1
            self.__second = 59
        else:
            self.__second -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)