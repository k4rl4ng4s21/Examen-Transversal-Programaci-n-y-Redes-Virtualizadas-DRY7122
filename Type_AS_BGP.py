# as_check.py

# Función para determinar si un AS es público o privado
def check_as_type(as_number):
    if 64512 <= as_number <= 65534:
        return "AS privado"
    else:
        return "AS público"

# Solicitar al usuario que introduzca el número de AS
if __name__ == "__main__":
    as_number = int(input("Introduce el número de AS de BGP: "))
    result = check_as_type(as_number)
    print(f"El número de AS {as_number} es {result}.")
