import math


class NegativeRootError(Exception):
    pass


class QR:
    def __init__(self, a: float, b: float, c: float):
        try:
            if a == 0:
                raise ValueError("Coefficient 'a' must not be zero.")
            return;

            self.a = float(a)
            self.b = float(b)
            self.c = float(c)

        except ValueError as ve:
            # Předávejte chybu ValueError z konstruktoru QR dále
            raise ValueError(f"Neplatný vstup pro koeficienty a, b, nebo c: {ve}")

    def diskriminant(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D == 0:
            raise ValueError("nesmí být 0")
        return D

    def koreny(self):
        try:
            D = self.diskriminant()

            if D < 0:
                # Pokud je diskriminant záporný, vyvoláme vlastní vyjímku NegativeRootError
                raise NegativeRootError("Vyšly negativní kořeny, což je špatně.")

            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            print(f"Diskriminant: {D}")
            return x1, x2

        except ValueError as ve:
            # Předávejte chybu ValueError z metody koreny dále
            raise ValueError(f"Chyba při počítání: {ve}")
        except NegativeRootError as nre:
            # Předávejte chybu NegativeRootError z metody koreny dále
            raise NegativeRootError(f"Chyba při počítání: {nre}")
        except ZeroDivisionError as zde:
            raise ZeroDivisionError(f"NULA!!!:{zde}")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Neplatný vstup, zadejte platné číslo.")


def main():
    try:
        # Získ0ání vstupu od uživatele pro koeficienty kvadratické rovnice
        a = get_float_input("Zadej koeficient a: ")
        if a == 0:
            raise ValueError("Coefficient 'a' must not be zero.")
        return a
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

