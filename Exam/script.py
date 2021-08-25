class PersonalInfo:
    def __init__(self, name, id_number, phonenumber, email, street, home_number):
        self.name = name
        self._id_number = id_number
        self.phonenumber = phonenumber
        self.email = email
        self.street = street
        self.home_number = home_number


class Company(type):
    list_of_salaries = []
    employers = []

    def total_money(self):
        name_list = []
        eff_list = []
        for employee in self.employers:
            employee.payout()
            eff_value = employee.efficiency()
            name_list.append(employee.information.name)
            eff_list.append(eff_value)
        eff_dict = dict(zip(name_list, eff_list))
        max_key = max(eff_dict, key=eff_dict.get)
        min_key = min(eff_dict, key=eff_dict.get)
        print(f'{max_key} имеет самую высокую продуктивность в {eff_dict.get(max_key)} %')
        print(f'{min_key} имеет самую низкую продуктивность в {eff_dict.get(min_key)} %')
        return f'Компании придется потратить {sum(self.list_of_salaries)} сом на оплату персонала'

    def salary_calculator(self, position, fixed=None, sale_amount=None, hours=None):
        if position == 'Manager' or position == 'Secretary':
            salary = fixed
        elif position == 'Seller':
            salary = fixed + sale_amount * 50
        elif position == 'Shop worker':
            salary = hours * 400
        elif 'Replacement' in position:
            salary = hours * 400
        self.list_of_salaries.append(salary)
        return salary

    def __call__(self, *args, **kwargs):
        cls = type.__call__(self, *args)
        setattr(cls, "salary_calculator", self.salary_calculator)
        return cls


class Employee(object, metaclass=Company):
    def __init__(self, name, id_number, position, phonenumber, email, street, home_number, hours, fixed=None, sale_amount=None):
        self.information = PersonalInfo(name, id_number, phonenumber, email, street, home_number)
        self.position = position
        self.hours = hours
        self.fixed = fixed
        self.sale_amount = sale_amount
            
    def payout(self):
        salary = self.salary_calculator(self.position, self.fixed, self.sale_amount, self.hours)
        print(f'{self.information.name}, идентификационный номер {self.information._id_number}: {salary} сом')

    def efficiency(self):
        ef = (self.hours / 40) * 100
        print(f'{self.information.name}, продуктивность: {ef} %\n')
        return ef


person1 = Employee('Барсбек Канаткулов', '1', 'Manager', '0550100001', 'iamaboss@gmail.com', 'Abdrahmanova', 75, 18, 45000)
person2 = Employee('Алымкул Тилекбаев', '2', 'Secretary', '0550202020', 'iamabossassistant@gmail.com', 'Aitmatova', 124, 38, 20000)
person3 = Employee('Айпери Шалымбекова', '3', 'Seller', '0550030303', 'iamaseller@gmail.com', 'Moskovskaya', 12, 38, 20000, 20)
person4 = Employee('Бакыт Рустамов', '4', 'Shop worker', '0554444444', 'iamaworker@gmail.com', 'Bokonbaeva', 50, 25, None, 20)
person5 = Employee('Алтынай Ширинбаева', '5', 'Shop worker', '0550030303', 'iamaworkertoo@gmail.com', 'Jibek - Joly', 195, 40, None, 20)
person6 = Employee('Жанар Рыскулов', '6', 'Replacement Secretary', '0551234567', 'whereami@gmail.com', 'Gorkogo', 5, 33)

big = Company('', (), {})
big.employers.append(person1)
big.employers.append(person2)
big.employers.append(person3)
big.employers.append(person4)
big.employers.append(person5)
big.employers.append(person6)
print(big.total_money())