# Importa la clase Fernet del módulo cryptography.fernet para manejo de cifrado simétrico
from cryptography.fernet import Fernet

# Genera una clave secreta aleatoria que servirá para cifrar y descifrar datos
key = Fernet.generate_key()

# Abre (o crea) un archivo llamado 'secret.key' en modo escritura binaria
with open("secret.key", "wb") as key_file:
    # Escribe la clave generada dentro del archivo
    key_file.write(key)

# Imprime un mensaje indicando que la clave fue generada y guardada exitosamente
print("Clave generada y guardada en secret.key")
