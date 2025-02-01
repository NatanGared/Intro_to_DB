import mysql.connector

def create_database(db_name):
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Rodasabebe@11'
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()

            # Create database if it doesn't exist
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
            print(f"Database '{db_name}' created successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

create_database("alx_book_store")