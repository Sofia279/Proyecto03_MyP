from password import derive_key
import random


class Polynomial:
    def __init__(self, pair_file: str) -> None:
        self.pair_file = pair_file

    def write_pairs(self, shares: int, minimum: int, password: str) -> None:
        assert shares > 2, "El número total de datos debe ser mayor a dos."
        assert shares >= minimum, "El mínimo de datos no puede ser mayor" \
            "que el número total de datos."
        coefficients: list[int] = []

        def generate_coefficients(key: bytes) -> None:
            rand = random.SystemRandom()
            coefficients.append(int.from_bytes(key))
            for i in range(minimum - 1):
                coefficients.append(rand.randint(0, 2 ** 16))

        def polynomial(x: int) -> int:
            return sum(coefficients[i] * x ** i for i in range(minimum))

        generate_coefficients(derive_key(password))

        # https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing#Preparation
        with open(self.pair_file, 'w') as file:
            for point in range(1, shares + 1):
                file.write(f"{point} {polynomial(point)}\n")