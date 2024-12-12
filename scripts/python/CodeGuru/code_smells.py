def fetch_data_from_db():
    # Uso intencionado de una consulta sin parámetros (SQL Injection Vulnerable)
    user_input = input("Enter user ID: ")
    query = f"SELECT * FROM users WHERE id = {user_input}"  # Vulnerable
    print("Executing query:", query)
    return query

def inefficient_algorithm():
    # Uso intencionado de un algoritmo ineficiente (O(n^2))
    data = [i for i in range(1000)]
    for i in data:
        for j in data:
            if i == j:
                print(i, j)

fetch_data_from_db()
inefficient_algorithm()
