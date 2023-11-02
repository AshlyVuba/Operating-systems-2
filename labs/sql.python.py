import pyodbc

def connect_to_database():
    server = 'your_server_name'
    database = 'your_database_name'
    username = 'your_username'
    password = 'your_password'

    try:
        # Establish a connection to the SQL Server database
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
        )

        return connection
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        return None

def fetch_students_data():
    connection = connect_to_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            # Query the "students" table to fetch all records
            cursor.execute("SELECT * FROM students")

            # Fetch all records into a list of dictionaries
            students_data = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]

            return students_data
        except Exception as e:
            print(f"Error querying the database: {str(e)}")
        finally:
            connection.close()

    return None

if __name__ == "__main__":
    students_data = fetch_students_data()
    if students_data is not None:
        for student in students_data:
            print(student)
