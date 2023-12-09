from polynomial import Polynomial
from getpass import getpass

shares = 10
minimum = 5

if __name__ == "__main__":
    p = Polynomial("pairs.txt")
    p.encrypt("foobar.txt", shares, minimum, getpass("Contraseña: "))
    # p.decrypt("foobar.aes")
