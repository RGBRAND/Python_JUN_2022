

class Person:

    def __init__(self, name, gender="female"):
        self.name = name
        self.gender = gender

    def show(self):
        print("My Details")
        print(f'Name: {self.name}')
        print(f'Gender: {self.gender}')

        print('---' * 10)

class Student(Person):
    def __init__(self, name, gender, klass, college, stream):
        super().__init__(name, gender)
        self.klass = klass
        self.college = college
        self.stream = stream

    def show_more(self):
        print("More Details")
        print(f'College: {self.college}')
        print(f'Class: {self.klass}')
        print(f'Stream: {self.stream}')

class Coder(Student):
    def __init__(self, name, gender, klass, college, stream, prog_langs=[]):
        super().__init__(name, gender, klass, college, stream)
        self.prglangs = prog_langs

    def coding_experience(self):
        if len(self.prglangs) == 0:
            print(f'I, {self.name} dont know any programming languages')
        else:
            print(f"I, {self.name} know following programming languages")
            for lang in self.prglangs:
                print(f"=> {lang}")
            print('---' * 10)

    def add_language(self, lang):
        self.prglangs.append(lang)

if __name__ == "__main__":

    p = Person("John Cena", gender="Male")
    p.show()

    std1 = Student('Ankit', 'Male', 'Python Class','Digipodium', 'Data Science')
    std1.show()
    std1.show_more()


    coder = Coder('Vijay Deenanath Chauhan', 'male', '12th','Mandawa','PCM')
    coder.show()
    coder.show_more()
    coder.coding_experience()
    print("Ek sal baad")
    coder.add_language('Python')
    coder.add_language('html')
    coder.add_language('c++')
    coder.add_language('Java')
    coder.coding_experience()
