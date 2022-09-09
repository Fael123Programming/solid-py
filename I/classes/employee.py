from I.classes.database import Database


class Employee:

    def __init__(self, name: str, identification: str, department: str, role: str, salary: float):
        self._name = name
        self._identification = identification
        self._department = department
        self._role = role
        self._salary = salary

    @property
    def name(self) -> str:
        return self._name

    @property
    def identification(self) -> str:
        return self._identification

    @property
    def department(self) -> str:
        return self._department

    @property
    def role(self) -> str:
        return self._role

    @property
    def salary(self) -> float:
        return self._salary

    def log_in_to_basic_system(self) -> bool:
        db = Database()
        if db.authorize(self._identification, self._department, self._role):
            print(f'{self.__class__.__name__} logged in.')
            return True
        else:
            return False


class Manager(Employee):

    def __init__(self, name: str, identification: str, department: str, role: str, salary: float):
        super().__init__(name, identification, department, role, salary)

    def log_in_to_manager_system(self) -> bool:
        db = Database()
        if db.authorize(self._identification, self._department, self._role):
            print('Manager logged in.')
            return True
        else:
            return False


class Director(Employee):

    def __init__(self, name: str, identification: str, department: str, role: str, salary: float):
        super().__init__(name, identification, department, role, salary)

    def log_in_to_director_system(self) -> bool:
        db = Database()
        if db.authorize(self._identification, self._department, self._role):
            print(f'{self.__class__.__name__} logged in.')
            return True
        else:
            return False


class CEO(Director):
    def __init__(self, name: str, identification: str, department: str, role: str, salary: float):
        super().__init__(name, identification, department, role, salary)

    def log_in_to_ceo_system(self) -> bool:
        db = Database()
        if db.authorize(self._identification, self._department, self._role):
            print('CEO logged in.')
            return True
        else:
            return False
