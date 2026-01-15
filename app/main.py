class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [Person(person_data["name"], person_data["age"]) for person_data in people]

    for i, person_data in enumerate(people):
        person = person_list[i]

        wife_name = person_data.get("wife")
        if wife_name is not None and wife_name in Person.people:
            person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name is not None and husband_name in Person.people:
            person.husband = Person.people[husband_name]

    return person_list
