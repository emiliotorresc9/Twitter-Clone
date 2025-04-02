from HashMap import HashMap

def bmh_search(text, pattern):
    """
    Implementación del algoritmo Boyer-Moore-Horspool usando el HashMap del usuario.
    
    :param text: Texto donde se buscará el patrón.
    :param pattern: Patrón que se desea encontrar en el texto.
    :return: Índice donde comienza el patrón en el texto, o -1 si no se encuentra.
    """
    # Convertir ambos, el texto y el patrón, a minúsculas para hacer la búsqueda insensible a mayúsculas/minúsculas
    text = text.lower()
    pattern = pattern.lower()

    n = len(text)
    m = len(pattern)

    # Crear la tabla de "malos caracteres" usando el HashMap
    bad_char = HashMap()
    
    # Inicializar la tabla con el tamaño del patrón
    for char in set(text):  # Se inicializan solo los caracteres únicos del texto
        bad_char.put(char, m)

    # Actualizar las distancias según el patrón
    for i in range(m - 1):
        bad_char.put(pattern[i], m - 1 - i)

    # Buscar el patrón en el texto
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            return i  # Patrón encontrado en la posición i

        # Desplazar usando la tabla de "malos caracteres"
        char_to_check = text[i + j]
        shift = bad_char.get(char_to_check) if bad_char.get(char_to_check) is not None else m
        i += shift

    return -1  # Patrón no encontrado
