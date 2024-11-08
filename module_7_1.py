class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        data = file.read()
        return (data)
        file.close()

    def add(self, *products):
        file = open(self.__file_name, 'a', encoding='utf-8')
        file.write('')  # Создание файла при первом запуске и добавление "ничего" при последующих
        file.close()
        for i in products:
            name_produkt = (str(i))
            file = open(self.__file_name, 'r', encoding='utf-8')
            prod_list = file.read()
            file.close()
            if name_produkt in prod_list:
                print(f'Продукт {name_produkt} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a', encoding='utf-8')
                file.write(f'{name_produkt}\n')
                file.close()


##########################################


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
