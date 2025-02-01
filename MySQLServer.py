import mysql.connector

def create_database():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Rodasabebe@11'
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()

            # Create database if it doesn't exist
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
            print(f"Database alx_book_store created successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

create_database()