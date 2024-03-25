import math


class NegativeRootError(Exception):
    pass


class QR:
    def __init__(self, a: float, b: float, c: float) -> object:
        try:
            # funkce pro zkontrolování vstupu pro 0
            if a == 0:
                raise ValueError("Koefficient 'a' nesmí být nula.")

            self.a = float(a)
            self.b = float(b)
            self.c = float(c)

        except ValueError as ve:
            # Předávejte chybu ValueError z konstruktoru QR dále
            raise ValueError(f"Neplatný vstup pro koeficienty a, b, nebo c: {ve}")

    def diskriminant(self):
        D = self.b ** 2 - 4 * self.a * self.c
        return D

    def roots(self):
        discriminant = self.b**2 - 4*self.a*self.c
        if discriminant > 0:
            root1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)
            return root1, root2
        elif discriminant == 0:
            root = -self.b / (2*self.a)
            return root,
        else:
            raise NegativeRootError("kořeny jsou složité.")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value == 0:
                raise ValueError("Zadaná hodnota nesmí být nula.")
            return value
        except ValueError as ve:
            print(f"Neplatný vstup: {ve}. Zadejte platné číslo.")



def main():
    try:
        # Získání vstupu od uživatele pro koeficienty kvadratické rovnice
        a = get_float_input("Zadej koeficient a: ")
        b = get_float_input("Zadej koeficient b: ")
        c = get_float_input("Zadej koeficient c: ")

        # Vytvoření instance QR a výpočet kořenů
        quadratic_solver = QR(a, b, c)
        roots = quadratic_solver.koreny()
        print(f"Hodnoty jsou: {roots}")

    except ValueError as ve:
        print(f"Chyba: {ve}")

    except NegativeRootError as nre:
        print(f"Chyba: {nre}")


if __name__ == "__main__":
    main()