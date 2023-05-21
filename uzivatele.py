class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.phone_numbers = []

    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)

    def __str__(self):
        phone_numbers = "\n".join(self.phone_numbers) if self.phone_numbers else "Nejsou registrována žádná telefonní čísla."
        return f"Jméno: {self.name}, Věk: {self.age}\nTelefonní čísla:\n{phone_numbers}"

