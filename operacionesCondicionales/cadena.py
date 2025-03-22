# podemos acceder al caracter de cualquier cadena usando [n]

melissamaya = "Melissamaya"
print(melissamaya[1])

# podemos delimitar una  rebanada de cadena usando[:n]

melissamaya = "Melissamaya"
print(melissamaya[:4]) # imprime "Meli"

# delimitar fragmentos dentro de la palabra usando [n:m]

long_word = "parangaricutirimicuaro"
print(long_word[3:7]) # imprime 'anga', no imprime el 7mo caracter

# INDICES NEGATIVOS> se pueden incluir negativos para imprimir desde el ultimo caracter hacia atras:

long_word = "parangaricutirimicuaro"
print(long_word[-7]) #imprime la m contando desde la letra o hacia atras 7 caracteres (no cuenta desde cero)

# SALTAR CARACTERES: usamos [::n] para conseguir cada n numero de letras:
print(long_word[::3]) # imprime 'paacimuo' cada tercer letra de la palabra larga