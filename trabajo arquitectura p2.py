# decimal_a_binario.py

def decimal_a_binario_8bits(numero_decimal):
    """
    Convierte un número decimal (00–99) a binario de 8 bits.
    """
    if not (0 <= numero_decimal <= 99):
        raise ValueError("El número debe estar entre 0 y 99.")
    binario = format(numero_decimal, '08b')  # Convierte a binario y rellena con ceros
    return binario


if __name__ == "__main__":
    print("Conversor de Decimal a Binario (8 bits)\n")
    try:
        numero = int(input("Ingrese un número decimal de dos cifras (00–99): "))
        resultado = decimal_a_binario_8bits(numero)
        print(f"El número {numero} en binario (8 bits) es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
