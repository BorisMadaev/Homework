class Product:
    name = ''
    weight = 0.0
    category = ''

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'
    products = []
    products_file = []
    schetchik = 0

    def __init__(self):
        pass

    def get_products(self):
        file = open(self.__file_name, 'r')
        self.products_file = file.readlines()
        for i in range(len(self.products_file)):
            self.products_file[i] = self.products_file[i][:-1]
        file.close()
        return self.products_file

    def add(self, *products):
        self.get_products()
        self.products = products
        for i in range(len(self.products)):
            self.schetchik = 0
            for j in range(len(self.products_file)):
                if str(self.products[i]) == str(self.products_file[j]):
                    self.schetchik = self.schetchik + 1
            if self.schetchik > 0:
                print(f'Продукт {str(self.products[i])} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{str(self.products[i])}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
