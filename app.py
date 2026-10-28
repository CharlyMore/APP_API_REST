#Nombre: Carlos Moreno
#Aplicacion API-REST

import requests

#JSON formatter

#API de productos de DummyJSON

BASE_URL = "https://dummyjson.com/products"

def mostrar_respuesta(respuesta):
    #mostrar el codigo HTTP y los datos recibidos
    print("Codigo HTTP",respuesta.status_code)

    if respuesta.text:
        print("Respuesta JSON")
        print(respuesta.json())
    else:
        print("la respuesta no tiene datos")

try:
    #===================================
    # 1.GET: CONSULTAR UN PRODUCTO 
    #===================================

    print ("\n GET --- Consultar un producto")
    
    respuesta = requests.get(
        f"{BASE_URL}/19",
        timeout=10
    )

    respuesta.raise_for_status()
    producto = respuesta.json()

    print("Producto",producto["title"])
    print("Precio",producto["price"])
    print("Categoria",producto["category"])


    #========================
    # 2. METODO POST
    #========================

    print ("\n POST --- Crear un producto")
    
    nuevo_producto = {
        "title": "Teclado mecanico gamer",
        "price": 90000,
        "description":"Teclado para juegos",
        "category":"electronics"
    }
    
    respuesta = requests.post(
        f"{BASE_URL}/add",
        json=nuevo_producto,
        timeout=10
    )
    
    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)
    
    #========================
    # 3. METODO PUT
    #========================
    
    print ("\n PUT --- Actualizando un producto ---")
    
    producto_actualizado = {
            "title": "Notebook",
            "price": 590000,
            "description":"Notebook para pogramar",
            "category":"laptops"
        }
    
    respuesta = requests.put(
        f"{BASE_URL}/1",
        json=producto_actualizado,
        timeout=10
    )
    
    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)

    #========================
    # 4. METODO PAST
    #========================

    print ("\n PATCH --- Modifica solo *precio ---")

    respuesta = requests.patch(
        f"{BASE_URL}/1",
        json={"price":590000},
        timeout=10
    )

    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)

    #========================
    # 4. METODO DELETE
    #========================

    print("\n DELETE --- Eliminar un producto ---")

    respuesta= requests.delete(
        f"{BASE_URL}/1",
        timeout=10
    )

    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)


except requests.exceptions.Timeout:
    print("Error: se agoto el tiempo de espera")

except requests.exceptions.HTTPError as error:
    print("Error HTTP",error)

except requests.exceptions.ConnectionError:
    print("Error: no fue  posible conectar con la API.")

except requests.exceptions.RequestException as error:
    print("Error en la solicitud:", error)

except (ValueError, KeyError) as error:
    print("Error al procesar los datos:",error)

    
