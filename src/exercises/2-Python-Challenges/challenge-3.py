class Person:
    def __init__(self, name, age, gender, study_subject):
        self.name = name
        self.age = age
        self.gender = gender
        self.study_subject = study_subject

person1= Person("Juli", 25, "F", "World dominance")
print person1.name, person1.age, person1.gender, person1.study_subject
print vars(person1)
