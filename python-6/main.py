import abc

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    

class Employee(abc.ABC):
    def __init__(self, code, name, salary):
        self._code = code
        self._name = name
        self._salary = salary
        self._hours = 8
    
    @abc.abstractmethod
    def calc_bonus(self):
        pass

    def get_department(self):
        return self._department.name
    
    def set_department(self, name):
        self._department = Department(name)

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def get_hours(self):
        return self._hours


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('managers', 1)

    def calc_bonus(self):
        return float(self.get_salary()) * 0.15        


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('sellers', 2)
        self._sales = 0

    def calc_bonus(self):
        return self._sales * 0.15

    def get_sales(self):
        return self._sales
    
    def put_sales(self, sales):
        self._sales = self._sales + sales
