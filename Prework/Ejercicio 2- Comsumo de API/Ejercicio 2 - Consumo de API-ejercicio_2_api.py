# Escribe tu solución aquí
import requests
from requests.exceptions import Timeout, HTTPError, RequestException

def obtener_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        usuarios = response.json()
        resultado = []
        for usuario in usuarios:
          resultado.append({
            "name": usuario.get("name"),
            "email": usuario.get("email"),
            "city": usuario.get("address", {}).get("city")
          })
        return resultado

    except Timeout:
      print("Error: La solicitud excedió el tiempo de espera.")
    except HTTPError as http_err:
      print(f"Error HTTP: {http_err}")
    except RequestException as err:
      print(f"Error en la solicitud: {err}")
    return []

if __name__ == "__main__":
  usuarios_limpios = obtener_usuarios()
  for u in usuarios_limpios:
    print(u)