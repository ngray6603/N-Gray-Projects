
class ElectricVehicle:
    def __init__(self):
        self.color = input('Enter the color of the vehicle: ')
        self.make = input('Enter the make of vehicle: ')
        self.model = input('Enter the model of vehicle: ')
        self.max_kilowatt_hours = int(input('Enter max charge hour:'))
        self.current_kilowatt_hours = int(input('Enter current charge hour:'))
        self.kilometers_per_kilowatt_hour = int(input('Enter kilometers per charge hour:'))

    # get methods

    def get_color(self):
        return self.color

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_max_kilowatt_hours(self):
        return self.max_kilowatt_hours

    def get_current_kilowatt_hours(self):
        return self.current_kilowatt_hours

    def get_kilometers_per_kilowatt_hour(self):
        return self.kilometers_per_kilowatt_hour


    def charge(self):

        inputted_charge = input('Enter the amount of time you want to charge: ')
        if int(inputted_charge) >= self.max_kilowatt_hours:
            print('Max Charged')
        else:
            print('Charging...')

    def drive(self):
        kilo_to_drive = input('Enter kilometers you want to drive: ')
        kilometers_can_drive = self.current_kilowatt_hours * self.kilometers_per_kilowatt_hour
        if kilometers_can_drive < int(kilo_to_drive):
            print('You do not have enough charge to drive that distance')
        if kilometers_can_drive == int(kilo_to_drive):
            print('You will be depleted when you reach the destination')
        if kilometers_can_drive > int(kilo_to_drive):
            print('Good to go!')




v = ElectricVehicle()
v.get_color()
v.get_current_kilowatt_hours()
v.get_make()
v.get_model()
v.get_max_kilowatt_hours()
v.get_kilometers_per_kilowatt_hour()
v.charge()
v.drive()
