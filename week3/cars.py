import os
import csv

# TODO
# Открыть словарь с атрибутами класса можно с помощь метода __dict__:


class BaseCar:
    """This class describes machines"""

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try:
            self.body_length = float(body_whl.split("x")[0])
            self.body_width = float(body_whl.split("x")[1])
            self.body_height = float(body_whl.split("x")[2])
        except ValueError:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0


    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_file):
    car_list = []
    car_types = ["car", "truck", "spec_machine"]
    with open(csv_file, newline='') as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')
#         next(reader)
        for row in reader:

            if not row['photo_file_name']:
                continue

            if row['car_type'] not in car_types:
                continue

            if row['car_type'] == 'car':

                car = Car(row['car_type'], row['brand'], row['photo_file_name'], row['carrying'],
                          row['passenger_seats_count'])

            elif row['car_type'] == 'truck':

                car = Truck(row['car_type'], row['brand'], row['photo_file_name'], row['carrying'], row['body_whl'])

            elif row['car_type'] == 'spec_machine':

                car = SpecMachine(row['car_type'], row['brand'], row['photo_file_name'], row['carrying'], row['extra'])

            else:
                continue

            car_list.append(car)

        return car_list



