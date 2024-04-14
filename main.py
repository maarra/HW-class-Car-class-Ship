class Car:
    def __init__(self, model, yearOfRelease, manufacturer, engine, capacity, color, price):
        self.model = model
        self.yearOfRelease = yearOfRelease
        self.manufacturer = manufacturer
        self.engine = engine
        self.capacity = capacity
        self.color = color
        self.price = price

    def showInfo(self):
        #print('\nRECAPITULATION:\nManufacturer: {}\nCar model: {}\nYear of release: {}\nEngine: {}\nCapacity: {}\nColor: {}\nPrice: {}'
         #     .format(self.model, self.yearOfRelease, self.manufacturer, self.engine, self.capacity, self.color, self.price))
        print('\nRECAPITULATION:')
        print('Manufacturer: {}'.format(self.manufacturer))
        print('Model: {}'.format(self.model))
        print('Year of Release: {}'.format(self.yearOfRelease))
        print('Engine: {}'.format(self.engine))
        print('Capacity: {}'.format(self.capacity))
        print('Color: '.format(self.color))
        print('Price: {}'.format(self.price))

    # def getInfo(self):
    #     input('Enter car model: ')
    #     input('Enter year of release: ')
    #     input('Enter manufacturer: ')
    #     input('Enter engine: ')
    #     input('Enter capacity: ')
    #     input('Enter color: ')
    #     input('Enter price: ')

#car1 = Car(input('Enter car model: '), input('Enter year of release: '), input('Enter manufacturer: '), 'Diesel', 2.2, 'Grey', '500k')
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