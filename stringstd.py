from unidecode import unidecode

def standardize(text):
    return unidecode(text)

name = "Éric Ferreira"
std_name = standardize(name)

print(f"Seu nome é {name}. Seu nome sem acento é {std_name}")