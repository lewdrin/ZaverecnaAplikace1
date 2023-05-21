from uzivatele import User

class UserRegistry:
    def __init__(self):
        self.users = []
        self.password = "PrahaJeDaleko"  # Your Password

    def register_user(self):
        name = input("Zadejte vaše Jměno: ")
        age = int(input("Zadejte váš věk: "))

        user = User(name, age)
        self.users.append(user)
        print("Úspěšně jste se zaregistrovali!")

    def register_phone_number(self):
        if not self.users:
            print("Nejsou registrováni žádní uživatelé. Nejprve prosím zaregistrujte uživatele.")
            return

        for i, user in enumerate(self.users):
            print(f"{i + 1}. {user.name}")

        user_choice = int(input("Vyberte uživatele: "))
        if user_choice < 1 or user_choice > len(self.users):
            print("Neplatná volba. Vyberte platného uživatele.")
            return

        phone_number = input("Vložte telefonní číslo: ")
        selected_user = self.users[user_choice - 1]
        selected_user.add_phone_number(phone_number)
        print("Telefonní číslo bylo úspěšně zaregistrováno!")

    def authenticate(self, password):
        return password == self.password

    def view_users(self, password):
        if not self.authenticate(password):
            print("Neplatné heslo. Přístup odepřen.")
            return

        if not self.users:
            print("Nejsou registrováni žádní uživatelé.")
        else:
            print("Seznam uživatelů:")
            for user in self.users:
                print(user)

    def search_users(self):
        if not self.users:
            print("Nejsou registrováni žádní uživatelé.")
            return

        search_term = input("Pro vyhledávání zadejte jméno nebo příjmení: ")
        found_users = []
        for user in self.users:
            if search_term.lower() in user.name.lower():
                found_users.append(user)

        if found_users:
            print(f"Nalezeno {len(found_users)} Uživatel/ů:")
            for user in found_users:
                print(user)
        else:
            print("Nenalezeni žádní uživatelé.")

