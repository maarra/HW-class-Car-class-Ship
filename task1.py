class Car:
    def __init__(self, manufacturer, model, yearOfRelease, engine, capacity, color, price):
        self.model = model
        self.yearOfRelease = yearOfRelease
        self.manufacturer = manufacturer
        self.engine = engine
        self.capacity = capacity
        self.color = color
        self.price = price

    def showInfo(self):
        print('\nRECAPITULATION:')
        print('Manufacturer: {}'.format(self.manufacturer))
        print('Model: {}'.format(self.model))
        print('Year of Release: {}'.format(self.yearOfRelease))
        print('Engine: {}'.format(self.engine))
        print('Capacity: {}'.format(self.capacity))
        print('Color: {}'.format(self.color))
        print('Price: {}'.format(self.price))

    def editManufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def editModel(self, model):
        self.model = model

    def editYOR(self, yor):
        self.yearOfRelease = yor

car1 = Car(
    input('Enter manufacturer: '),
    input('Enter model: '),
    input('Enter year of release: '),
    input('Enter engine: '),
    input('Enter capacity: '),
    input('Enter color: '),
    input('Enter price: ')
    )

car1.showInfo()
car1.editManufacturer('Volvo')
car1.editModel('XC90')
car1.editYOR(2022)

car2 = Car('Astra',2012,'Opel','petrol',1.5,'white',123000)
car2.showInfo()
car1.showInfo()