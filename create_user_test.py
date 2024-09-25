import sender_stand_request
import data

# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

"""# Prueba 1. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene dos caracteres
#def test_create_user_2_letter_in_first_name_get_success_response():
    #user_body = get_user_body("Aa")
    #user_response = sender_stand_request.post_new_user(user_body)
    #Comprueba si el codigo de estado es 201
    #assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    #assert user_response.json()["authToken"] != ""
    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    #users_table_response = sender_stand_request.get_users_table()
    # El string que debe estar en el cuerpo de la respuesta para recibir datos de la tabla "users" se ve así
   # str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               #+ user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    #assert users_table_response.text.count(str_user) == 1
"""
# Función de prueba positiva
def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()

    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

#Prueba 2 creacion de un nuevo usuario
# numero de caracteres permitido (15)
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

#funcion de prueba negativa
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    #Comprueba si el codigo de estado es 400
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:


#Prueba 3 Error
#Parametro "first name" contiene un caracter
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

#Prueba 4 error
#Parametro "first name" contiene 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

#prueba 5 error
#no se permiten espacios en el parametro "first name"
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

#Prueba 6 error
#parametro "first name" permiten caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

#Prueba 7 error
#parametro "first name" no acepta numeros
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

#funcion de prueba negativa
def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400


#prueba 8 error
#La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_firstname(user_body)

#prueba 9
#parametro "First name" esta vacio
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)

#prueba 10
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400


