# sample.py

password = "admin123"

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id={user_id}"
    return query
# q=get_user(101)
# print(q)