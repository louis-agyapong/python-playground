def odd(n: int) -> bool:
    return n % 2 != 0


class Contact:
    all_contacts: list["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" f"{self.name!r}, {self.email!r}" f")"


if __name__ == "__main__":
    c_1 = Contact("Louis", "agyapong.louis@gmail.com")
    c_2 = Contact("Kofi", "fii.asamoah@mail.com")
    Contact.all_contacts
