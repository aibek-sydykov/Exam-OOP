
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

    def total_money(self):
        return f'Компании придется потратить {sum(self.list_of_salaries)} сом на оплату персонала'

    def __call__(self, *args):
        cls = type.__call__(self, *args)
        setattr(cls, "salary_calculator", self.salary_calculator)
        return cls


class Employee(object, metaclass=Company):
    def __init__(self, name, id_number, position, phonenumber, email, street, home_number, hours):
        self.information = PersonalInfo(name, id_number, phonenumber, email, street, home_number)
        self.position = position
        self.hours = hours
            
    def payout(self, fixed=None, sale_amount=None):
        salary = self.salary_calculator(self.position, fixed, sale_amount, self.hours)
        print(f'{self.information.name}, идентификационный номер {self.information._id_number}: {salary} сом')

    def efficiency(self):
        ef = (self.hours / 40) * 100
        print(f'{self.information.name}, продуктивность: {ef} %')


person1 = Employee('Барсбек Канаткулов', '1', 'Manager', '0550100001', 'iamaboss@gmail.com', 'Abdrahmanova', 75, 18)
person1.payout(45000)
person1.efficiency()

person2 = Employee('Алымкул Тилекбаев', '2', 'Secretary', '0550202020', 'iamabossassistant@gmail.com', 'Aitmatova', 124, 38)
person2.payout(20000)
person2.efficiency()

person3 = Employee('Айпери Шалымбекова', '3', 'Seller', '0550030303', 'iamaseller@gmail.com', 'Moskovskaya', 12, 38)
person3.payout(20000, 20)
person3.efficiency()

person4 = Employee('Бакыт Рустамов', '4', 'Shop worker', '0554444444', 'iamaworker@gmail.com', 'Bokonbaeva', 50, 25)
person4.payout(sale_amount = 20)
person4.efficiency()
	
person5 = Employee('Алтынай Ширинбаева', '5', 'Shop worker', '0550030303', 'iamaworkertoo@gmail.com', 'Jibek - Joly', 195, 40)
person5.payout(sale_amount = 20)
person5.efficiency()

person6 = Employee('Жанар Рыскулов', '6', 'Replacement Secretary', '0551234567', 'whereami@gmail.com', 'Gorkogo', 5, 33)
person6.payout()
person6.efficiency()

big = Company('', (), {})
print(big.total_money())