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
