import os
import hashlib
from datetime import datetime
import logging
import socket

def lista_Algoritmos_disponibles():
    lista=hashlib.algorithms_available
    return '\n'.join(lista)

def lista_algoritmos_garantizados():
    lista= hashlib.algorithms_guaranteed
    return '\n'.join(lista)


    
def encript_object(test_object,encription_method):
    if type(test_object)!= str:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        raise Exception("The input to encode is not string type: "+ str(type(test_object)))
    
    encription_list = lista_algoritmos_garantizados()
    if encription_method in encription_list:
        if encription_method == 'sha512':
            hash1 = hashlib.sha512()
            hash1.update(test_object.encode('UTF-8'))
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
            result_code = hash1.hexdigest()
        elif encription_method == 'sha256':
            hash1 = hashlib.sha256()
            hash1.update(test_object.encode('UTF-8'))
            result_code = hash1.hexdigest() 
        elif encription_method == 'md5':    
            hash1 = hashlib.md5()
            hash1.update(test_object.encode('UTF-8'))
            result_code = hash1.hexdigest()
        elif encription_method == 'blake2b':    
            hash1 = hashlib.blake2b()
            hash1.update(test_object.encode('UTF-8'))
            result_code = hash1.hexdigest()
        elif encription_method == 'blake2s':    
            hash1 = hashlib.blake2s()
            hash1.update(test_object.encode('UTF-8'))
            result_code = hash1.hexdigest()
        elif encription_method == 'sha224':    
            hash1 = hashlib.sha224()
            hash1.update(test_object.encode('UTF-8'))
            result_code = hash1.hexdigest()    
        elif encription_method == 'sha384':    
            hash1 = hashlib.sha384()
            hash1.update(test_object.encode('UTF-8'))
            result_code = hash1.hexdigest() 
        elif encription_method == 'shake_256':    
            hash1 = hashlib.shake_256()
            hash1.update(test_object.encode('UTF-8'))
            result_code = hash1.hexdigest(30)           
        else:
            result_code='Encription not found'       
    else:
        print("Validate provided encript method is available on Python :" + encription_list)   
        result_code = "Invalid encription method"
             
    return result_code


def print_on_file(text_to_print):
    working_path = os.getcwd()
    outputh_path = working_path+'/results'+ str(datetime.now().day)+'.txt'
    try:
        with open(outputh_path,'a') as file:
            file.write(text_to_print+'\n')
      
    except:
        print(outputh_path)
        raise OSError('Could not create the file, path not found:')
        
    return outputh_path    

def getlocalIP():
    local_name = socket.gethostname()
    
    return str(socket.gethostbyname(local_name))


def getIPScann():
    red = input("IP of the network: ")
    red1 = red.split('.')
    red2 = red1[0]+'.'+red1[1]+'.'+red1[2]+'.'
    st1 = int(input("First network input : "))
    en1 = int(input("Last network input : "))
    en1=en1+1
    ping = 'ping -n 1'
    inicio = datetime.now()
    print('scanning... ')
    for  ip in range(st1,en1):
        addr = red2+str(ip)
        comm = ping + addr
        response = os.popen(comm)
        for line in response.readlines():
            if line.count('TTL'):
                break
        if(line.count('TTL')):
            print(addr,'  : addr active' )
    fin = datetime.now()
      
    print('Ending of scanning : ' + addr) 
          
       
salida_encriptada = encript_object(lista_algoritmos_garantizados(),'sha256')   

#print(lista_Algoritmos_disponibles())
print_on_file(str(salida_encriptada))
print(getlocalIP)
getIPScann()


year = 1960
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year %100 != 0:
        return True
    elif year %400 !=0:
        return False
    else:
        return True

def days_in_month(year, month):
    #
    # Write your new code here.
    months_with30_days =[4,6,9,11]
    months_with31_days =[1,3,5,7,8,12]
    
    if month in months_with30_days:
        return 30
    elif month in months_with31_days:
        return 31
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else: 
        return None
    
def day_of_year(year, month, day):
    #
    # Write your new code here.
    leapy = is_year_leap(year)
    num_days= days_in_month(year,month)
    days_no_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
    days_leap =[31,29,31,30,31,30,31,31,30,31,30,31]
    suma =0
    if leapy:
        for i in range(month):
            suma +=days_leap[i]
        return suma
    elif month <= 12 and not leapy:
        for i in range(month):
            suma +=days_no_leap[i]
        return suma    
    else:
        return "invalid Date provided"    



a_mile = 1609.344
a_gallon = 3.785411784
def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    gals = float(liters/a_gallon)
    miles = float(100000 /a_mile)
    return float(miles / gals)
    
    #

def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here.
    km = 100000/(miles*a_mile)
    
    return  float( a_gallon * km)

  