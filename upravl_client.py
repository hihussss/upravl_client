import psycopg2
import os
from dotenv import load_dotenv
   
load_dotenv()
names = os.getenv("NAME")
password = os.getenv("PASSWORD")
name_db = os.getenv("NAMEDB")

def create_table_client(cur):   
    cur.execute("""
            create table if not exists client(
                id serial primary key,  
                first_name varchar(40)  not null,
                last_name varchar(40)  not null,
                email varchar(40) unique not null                      
            );""")
    

def create_table_phone(cur):    
    cur.execute("""
            create table if not exists phone(
                id serial primary key,  
                number_phone varchar(20)   null,
                client_id integer references client(id) not null          
            );""")
    

def add_client(name,sunname,mail):
            cur.execute("""
            insert into client(first_name,last_name,email) values(%s,%s,%s);""",(name,sunname,mail,))
            

def add_client_phone(phone,client_id):
    cur.execute("""
            insert into phone(number_phone,client_id) values(%s,%s);""",(phone,client_id,))
    
def delete_data_phone(client_id=None,number_phone=None):
    if client_id!=None:
        cur.execute("""
            delete from phone where client_id=%s;""",(client_id,))
    if number_phone!=None:
        cur.execute("""
            delete from phone where number_phone=%s;""",(number_phone,))
    
def delete_data_client(client_id):
    delete_data_phone(client_id)   
    cur.execute("""
            delete from client where id=%s;""",(client_id,))
    

def update_data_client(client_id,first_name=None,last_name=None,email=None,number_phone=None):
    first_name=input("Введите имя: ")
    last_name=input("Введите фамилию: ")
    email=input("Введите email: ")
    number_phone=input("Введите номер телефона: ")
    if first_name!="":
        cur.execute("""
            update client set first_name=%s where id=%s;""",(first_name,client_id,))
    if last_name!="":
        cur.execute("""
            update client set last_name=%s where id=%s;""",(last_name,client_id,))
    if email!="":
        cur.execute("""
            update client set email=%s where id=%s;""",(email,client_id,))
    if number_phone!="":
        cur.execute("""
            update phone set number_phone=%s where client_id=%s;""",(number_phone,client_id,))
    
    

def get_data(first_name=None,last_name=None,email=None,number_phone=None):
    first_name=input("Введите имя: ")
    last_name=input("Введите фамилию: ")
    email=input("Введите email: ")
    number_phone=input("Введите номер телефона: ")
    if first_name!="":
        cur.execute("""
            select * from client where first_name=%s;""",(first_name,))
    if last_name!="":
        cur.execute("""
            select * from client where last_name=%s;""",(last_name,))
    if email!="":
        cur.execute("""
            select * from client where email=%s;""",(email,))
    if number_phone!="":
        cur.execute("""
            select * from phone where number_phone=%s;""",(number_phone,))
    return cur.fetchone()    
         
if __name__ == "__main__":   

    with psycopg2.connect(database=name_db, user=names, password=password) as conn:
        with conn.cursor() as cur:
            create_table_client(cur)
            create_table_phone(cur)
            # add_client("Ivan","Ivanov","Ivanov@ya.ru")
            # add_client("Petr","Petrov","Petrov@ya.ru")
            # add_client_phone("+7(999)999-99-99","3")
            # add_client_phone("+7(999)999-99-96","2")
            #delete_data_client(3)
            #update_data_client(3)
            #print(get_data())
    conn.close()        
