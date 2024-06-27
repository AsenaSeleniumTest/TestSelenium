import os
import pypdf
import mysql.connector



def read_PDF():
    os.chdir('C:\\Users\\uziel.buendia\\Desktop\\uziel\\python\\usbwireshark\\')
    try: 
        with open('March052024.csv','r') as file:
            text = file.read()
            textlist = text.splitlines()
            
            print(text[0], str(len(textlist)))
    except:
        print(os.getcwd() + ':  going thru the exception flow')
    return textlist

read_PDF() 

def get_System_Info():
    #os.chdir('C:\\Users\\uziel.buendia\\Desktop\\uziel\\python\\usbwireshark\\')
    env = os.environ
    pc_config = dict(env)
    env_keys = pc_config.keys()
    output = []
    for i in env_keys:
        output.append( f'{i}:    {pc_config.get(i)}')
       # print(f'{i}:    {pc_config.get(i)}')
    try:
        with open('systeminfo.csv','w') as file:
            for k in output:
                file.write(k+'\n')
        file.close()        
    except:
        print(os.getcwd() + ':  going thru the exception flow')

def connect_MySQL():
    mydb=mysql.connector.connect(host='192.168.3.246',user='usbtestuser1',password='Testing1386!')
    return mydb
    
def create_usb_DB():
    #schema  = usbschema1
     mydb=mysql.connector.connect(host='192.168.3.246',user='usbtestuser1',password='Testing1386!')
     mycursor = mydb.cursor()
     result = mycursor.execute('CREATE DATABASE usbtestdb1')
     if result:
         print("successfully created")
     else:
         print('Data base cannot be created ' + result.__annotations__)       

def create_db_table(usb_query):
    connect_result =connect_MySQL()
    my_cursor = connect_result.cursor()
    use_db_result = my_cursor.execute('USE usbtestdb1')   
    create_table_result = my_cursor.execute(usb_query)
    print(use_db_result)
    print(create_table_result)


         
create_db_table('INSERT INTO Persons (PersonID ,LastName, FirstName ,Address ,City ) VALUES("00003","usbuser3","usertres","cto oleiros 140 ","Durango") ;')
create_db_table('commit;')