from registrace import UserRegistry

def main():
    user_registry = UserRegistry()

    while True:
        print("\n1. Registrovat uživatele")
        print("2. Zaregistrujte telefonní číslo")
        print("3. Zobrazit uživatele")
        print("4. Hledat uživatele")
        print("5. Exit")

        choice = input("Zadejte svou volbu: ")

        if choice == "1":
            user_registry.register_user()
        elif choice == "2":
            user_registry.register_phone_number()
        elif choice == "3":
            password = input("Zadejte heslo pro přístup do seznamu uživatelů: ")
            user_registry.view_users(password)
        elif choice == "4":
            user_registry.search_users()
        elif choice == "5":
            break
        else:
            print("Neplatná volba. Vyberte platnou možnost.")


if __name__ == "__main__":
    main()

