import psycopg2
qwer = open("private/password.txt", "r").read()
   

with psycopg2.connect(database="netology_db", user="postgres", password=qwer) as conn:
    with conn.cursor() as cur:
        # cur.execute("""
        #     drop table phone;
        #     drop table client;        
        #             """)
        # conn.commit()
    # Первоначально хотел в функцию отправлять ИМЕНА СТОЛБЦОВ И ТИПЫ ДАННЫХ , ЧТОБ СОЗДАТЬ С ПОМОЩЬЮ ФУНКЦий создать таблицу с нуля.
        def create_table_client():
            cur.execute("""
            create table if not exists client(
                id serial primary key,  
                first_name varchar(40)  not null,
                last_name varchar(40)  not null,
                email varchar(40) unique not null                      
            );""")
        conn.commit()

        def create_table_phone():
            cur.execute("""
            create table if not exists phone(
                id serial primary key,  
                number_phone varchar(20)   null,
                client_id integer references client(id) not null          
            );""")
        conn.commit()

  # С помощью функции get_name_table хотел получать ИМЯ ТАБЛИЦЫ и имена  столбцов, чтоб не писать отдельную функцию для каждой таблицы. Но не получилось определить тип-данных названия таблицы (sql-identifier)
        
#         cur.execute("""
#             SELECT column_name FROM information_schema.columns
# WHERE table_schema NOT IN ('information_schema','pg_catalog');
#                     """)
#         print(cur.fetchall())

#         def get_name_table():
#             cur.execute("""
#             SELECT table_type FROM information_schema.tables
# WHERE table_schema NOT IN ('information_schema','pg_catalog');
#                     """)
#             return cur.fetchone()
        # Добавление данных



        def add_client(name,sunname,mail):
            cur.execute("""
            insert into client(first_name,last_name,email) values(%s,%s,%s);""",(name,sunname,mail,))
            conn.commit()
        def add_client_phone(phone,client_id):
            cur.execute("""
            insert into phone(number_phone,client_id) values(%s,%s);""",(phone,client_id,))
        conn.commit()
        # Удаление данных
        def delete_data_phone(value):
            cur.execute("""
            delete from phone where number_phone=%s;""",(value,))
            conn.commit()
        def delete_data_client(value):
            cur.execute("""
            delete from client where email=%s;""",(value,))
            conn.commit()
        
        # Обновление данных    
        def update_data_client_email(new_value,condition_value):
            cur.execute("""
            update client set email=%s where first_name=%s;""",(new_value,condition_value,))
        conn.commit()
        def update_data_client_first(new_value,condition_value):
            cur.execute("""
            update client set first_name=%s where email=%s;""",(new_value,condition_value,))
        conn.commit()
        def update_data_client_last(new_value,condition_value):
            cur.execute("""
            update client set last_name=%s where first_name=%s;""",(new_value,condition_value,))
        conn.commit()
        def update_data_phone(new_value,condition_value):
            cur.execute("""
            update phone set number_phone=%s where client_id=%s;""",(new_value,condition_value,))
        conn.commit()

        def get_data1(condition_value):
            cur.execute("""
            select * from client where email=%s;""",(condition_value,))
            return cur.fetchone()
        def get_data2(condition_value):
            cur.execute("""
            select * from client where first_name=%s;""",(condition_value,))
            return cur.fetchone()
        def get_data3(condition_value):
            cur.execute("""
            select * from client where last_name=%s;""",(condition_value,))
            return cur.fetchone()
        def get_all_data(condition_value):
            cur.execute("""
            select * from phone p join client c on p.client_id=c.id where number_phone=%s ;""",(condition_value,))        
            return cur.fetchone()
        # Посмотреть на таблицу
        def look_table_client():
            cur.execute("""
            select * from client;""")
            print(cur.fetchall())    
        def look_table_phone():
            cur.execute("""
            select * from phone;""")
            print(cur.fetchall()) 


        # create_table_client()
        # create_table_phone()
        # add_client("Ivan","Ivanov","Ivanov@ya.ru")
        # add_client("Petr","Petrov","Petrov@ya.ru")
        # add_client_phone("+7(999)999-99-99","1")
        # add_client_phone("+7(999)999-99-96","2")
        #delete_data_phone("+7(999)999-99-99")
        #delete_data_client("Ivanov@ya.ru")
        #update_data_client_email("Ivanov23@ya.ru","Ivan")
        #print(get_all_data("+7(999)999-99-96"))
        #look_table_client()
        #look_table_phone()