class Contact:

    def __init__(self, name, year_birth, is_programmer):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return (
            f'{self.name}, '
            f'возраст: {self.age_define()}, '
            f'статус: {self.programmer_define()}'
        )

# Создайте экземпляр класса Contact с необходимыми параметрами.
# Например, test_old_none_programmer = Contact('Пушкин', 1799, False).
test_old_none_programmer = Contact('Пушкин', 1799, False)
# Напишите assert и в нём проверьте,
# что метод programmer_define() этого экземпляра возвращает строку "Нормальный".
assert test_old_none_programmer.programmer_define() == 'Нормальный', 'ок'
# Во втором assert проверьте, возвращает ли метод age_define() значение "Старейшина".
assert test_old_none_programmer.age_define() == 'Старейшина', 'ок'
# Создайте новый экземпляр с другими параметрами;
# через assert проверьте, вернут ли и его методы ожидаемый результат.
test_programmer = Contact('Маяковский', 1950, True)
# Создайте столько экземпляров, сколько нужно,
# чтобы через разные assert проверить все методы во всех вариантах.
assert test_programmer.programmer_define() == 'Программист', 'ок'
assert test_programmer.age_define() == 'Олдскул', 'ок'
test_programmer = Contact('Роуллинг', 1980, True)
assert test_programmer.age_define() == 'Молодой', 'ок'