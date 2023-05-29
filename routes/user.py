#Package FastAPI
from fastapi import APIRouter

#Modulos Internos
from config.base_datos import conexion, cursor
from schemas.user import User

user = APIRouter()


@user.get("/users")
def all_users():
    cursor.execute("SELECT * FROM tbl_users")
    result = cursor.fetchall()
    
    return result

@user.get("/users/{id}")
def get_user(id):
    cursor.execute(f"SELECT * from tbl_users where User_id = '{id}'")
    result = cursor.fetchone()
    
    return result


@user.post("/users")
def create_user(user: User):
    cursor.execute(f"INSERT INTO tbl_users(Name, Last_name, Email, Password) VALUES('{user.name}', '{user.last_name}', '{user.email}', '{user.password}')")
    result = cursor.fetchone()
    conexion.commit()
    
    return f"User created: {result}"

@user.put("/users/{id}")
def update_user(user: User, id):
    cursor.execute(f"UPDATE tbl_users SET Name = '{user.name}', Last_name = '{user.last_name}', Email = '{user.email}', Password = '{user.password}' WHERE User_id = {id}")
    conexion.commit()
    result = cursor.fetchone()
    
    return f"User updated: {result}"


@user.delete("/users/{id}")
def delete_user(id):
    cursor.execute(f"SELECT * FROM tbl_users WHERE User_id = {id}")
    result = cursor.fetchone()
    cursor.execute(f"DELETE FROM tbl_users WHERE User_id = {id}")
    conexion.commit()
    
    return f"User deleted successfully: {result}"