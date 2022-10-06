class Person:
    def __init__(self, first_name, second_name, last_name, dict_phones: dict):
        self.phones = dict_phones
        self.FIO = [first_name, second_name, last_name]

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return " ".join(self.FIO)

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        return f"Уважаемый {self.FIO[0]} {self.FIO[1]}! Примите!"


class Company():
    def __init__(self, company_name, type_company, phone_number: dict, *args: Person):
        self.worker_list = list(args)
        self.company_name = company_name
        self.type = type_company
        self.phones_company = phone_number

    def get_name(self):
        return self.company_name

    def get_phone(self):
        if not self.phones_company.get("contact") is None:
            return self.phones_company.get("contact")
        else:
            for worker in self.worker_list:
                if not worker.get_work_phone() is None:
                    return worker.get_work_phone()
            return None

    def get_sms_text(self):
        return f"Уважаемый {self.company_name}! Примите {self.type}!"


def send_sms(*args):
    for el in args:
        if not el.get_phone() is None:
            print(f"Sms send to {el.get_phone()} with {el.get_sms_text()}")
        else:
            print(f'Sms did not send to {el.get_name()}')


def test():
    person1 = Person("Ivan", "Ivanovich", "Ivanov", {'private': 7543})
    person2 = Person("Alex", "Ivanovich", "Borisov", {'private': 73543, 'work': 15678})
    company1 = Company("Ozon", 'Marketplace', {'contact': 6789}, person1, person2)
    company2 = Company("Azon", 'Market', {'private': 6789}, person1)
    send_sms(person1, person2, company1, company2)
    print()
    person1 = Person("Ivan", "Ivanovich", "ivanov", {"private": 123, "worl": 456})
    person2 = Person("ivan", "Petrovich", "petrov", {"private": 789})
    person3 = Person("Ivan", "Fetrovich", "Sirnov", {"work": 789})
    person4 = Person("John", "unknown", "Doe", {})
    company1 = Company("Bell", "000", {"contact": 111}, person3, person4)
    company2 = Company('cell', "A0", {'non-contact': 333}, person2, person3)
    company3 = Company("Dell", 'Ltd', {'non_cotact': 333}, person2, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)

    print()
    person1 = Person("Степн", "Петрович", "Жобс", {"private": 555})
    person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, 'work':888})
    person3 = Person("Семен", "Роберитович", "Возняцик", {"work": 789})
    person4 = Person("Леонид", "Арсенович", "Торвальдс", {})
    company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person2)
    company2 = Company('ПластОкно', "АО", {'non-contact': 222}, person2)
    company3 = Company("Пингвинья ферма", 'Ltd', {'non_cotact': 333}, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)


test()


class MaxStat:
    def __init__(self):
        self.elements = []

    def add_number(self, num):
        self.elements.append(num)

    def result(self):
        return max(self.elements)


class MinStat:
    def __init__(self):
        self.elements = []

    def add_number(self, num):
        self.elements.append(num)

    def result(self):
        return min(self.elements)


class AverageStat:
    def __init__(self):
        self.elements = []

    def add_number(self, num):
        self.elements.append(num)

    def result(self):
        return sum(self.elements) / len(self.elements)


values = [1, 2, 3, 4]

minimal = AverageStat()
for i in values:
    minimal.add_number(i)
print(minimal.result())

