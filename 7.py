class Employee:
    def __init__(self, name, idd):
        self.name = name
        self.id = idd

    def get_info(self):

        return f"Имя: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name='', idd='', department=''):
        super().__init__( name, idd)
        self.department = department

    def manage_project(self):

        print(f"Менеджер {self.name} управляет проектом в отделе {self.department}")


class Technician(Employee):
    def __init__(self, name='', idd='', specialization=''):
        super().__init__(name, idd)
        self.specialization = specialization

    def perform_maintenance(self):

        print(f"Техник {self.name} выполняет техническое обслуживание в области {self.specialization}")


class TechManager(Manager, Technician):
    def __init__(self, name, idd, department, specialization):
       super().__init__( name, idd, department)
       super().__init__( name, idd, specialization)
       self.subordinates = []
    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        print(f"Команда {self.name} в отделе {self.department}:")
        for employee in self.subordinates:
            print(employee.get_info())

# Создание объектов
employee1 = Employee("Эльдар Джарахов", 123)
manager1 = Manager("Уолтер Уайт", 456, "IT")
technician1 = Technician("Эрен Йегер", 789, "Электр")
tech_manager1 = TechManager("Олеся Косякова", 1011, "Разраб", "Прог")

# функциональностm
print(employee1.get_info())
manager1.manage_project()
technician1.perform_maintenance()

# Добавление сотрудников в команду
tech_manager1.add_employee(employee1)
tech_manager1.add_employee(technician1)

# Вывод информации о команде
tech_manager1.get_team_info()