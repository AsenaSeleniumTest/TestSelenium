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