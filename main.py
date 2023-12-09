import polynomial
import getpass

shares = 10
minimum = 5


def encrypt(pair_file: str, shares: int, minimum: int,
            clear_file: str) -> None:
    password = getpass.getpass("Contraseña: ")
    p = polynomial.Polynomial(pair_file)
    p.write_pairs(shares, minimum, password)
    p.encrypt_file(clear_file, password)


def decrypt(pair_file: str, encrypted_file: str) -> None:
    p = polynomial.Polynomial(pair_file)
    password = p.get_password().decode('utf-8')
    p.decrypt_file(encrypted_file, password)


if __name__ == "__main__":
    encrypt("pairs.txt", shares, minimum, "example.txt")
    # decrypt("pairs.txt", "foobar.aes")
