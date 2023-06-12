import mysql.connector

def get_user_data(user_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="database"
    )
    cursor = conn.cursor()
    
    # Parametreli sorgu kullanımı
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    
    user_data = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return user_data
