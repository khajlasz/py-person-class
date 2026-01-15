class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Clear the people dictionary
    Person.people = {}

    # First pass: create all Person instances
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_instance = Person(name, age)
        person_list.append(person_instance)

    # Second pass: establish relationships
    for i, person_data in enumerate(people):
        person = person_list[i]

        # Handle wife relationship
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]

        # Handle husband relationship
        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]

    return person_list


if __name__ == "__main__":
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]

    person_list = create_person_list(people)
    print(isinstance(person_list[0], Person))  # Should print: True
    print(person_list[0].name)  # Should print: Ross
    print(person_list[0].wife is person_list[2])  # Should print: True
    print(person_list[0].wife.name)  # Should print: Rachel

    print(person_list[1].name)  # Should print: Joey
    print(getattr(person_list[1], "wife", None))  # Should print: None

    print(isinstance(person_list[2], Person))  # Should print: True
    print(person_list[2].name)  # Should print: Rachel
    print(person_list[2].husband is person_list[0])  # Should print: True
    print(person_list[2].husband.name)  # Should print: Ross
    print(person_list[2].husband.wife is person_list[2])  # Should print: True

    print(Person.people)
