class WeekDayError(Exception):
    pass
	

class Weeker:
    days_week =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    def __init__(self, day):
        self.__dia = day

    def __str__(self):
        
        if self.__dia not in self.days_week:
            return WeekDayError.__str__
        else:
            return self.__dia
        
    def add_days(self, n):
        dia_verdadero =''
        times_thru = int(n/7)
        jump_spaces = n%7
        windex = self.days_week.index(self.__dia) 
        if n>7:
            for val in self.days_week:
                if windex+n  > 7:
                    dia_verdadero = self.days_week[windex-jump_spaces]
                else:
                    dia_verdadero = self.days_week[windex+jump_spaces]
        
        self.__dia = dia_verdadero        
        
        
        
            
        return dia_verdadero

    def subtract_days(self, n):
        dia_verdadero =''
        windex = self.days_week.index(self.__dia) 
        for val in self.days_week:
            if val == self.__dia and n < 7:
                if windex ==0:
                   dia_verdadero = self.days_week[windex+n]
                elif windex ==1 and n < 6:
                    dia_verdadero = self.days_week[windex+n]
                elif windex ==2 and n < 5:
                    dia_verdadero = self.days_week[windex+n]
                elif windex ==3 and n < 4:
                    dia_verdadero = self.days_week[windex+n]
                elif windex ==4 and n < 3:
                    dia_verdadero = self.days_week[windex+n]
                elif windex ==5 and n < 2:
                    dia_verdadero = self.days_week[windex+n]
                elif windex ==6 and n < 1:                       
                    dia_verdadero = self.days_week[windex+n]
            else:
                dia_verdadero=self.__dia
            
        return dia_verdadero        


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")


if __name__ == "__main__":
    print(WeekDayError.__str__)    