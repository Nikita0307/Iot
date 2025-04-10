import abc

class Thing(abc.ABC):
    @abc.abstractmethod
    def __init__(self, name):
        self.name = name
        print(f"Create thing {self.name}")

    @abc.abstractmethod
    def print_name(self):
        print(f'name this device is {self.name}')

class Sensor(Thing):
    def __init__(self, name):
        super().__init__(name)
        self.value = 0
        print(f"Create new device {self.name}")

    def print_name(self):
        super().print_name()

class Heater(Thing):
    def __init__(self, name, focus_temperature):
        super().__init__(name)
        self.focus_temperature = focus_temperature

    def print_name(self):
        super().print_name()

    def change_temperature(self, focus_temperature):
        self.focus_temperature = focus_temperature

    def heat(self, *sensors):
        for sensor in sensors:
            if sensor.value < self.focus_temperature:
                sensor.value += 1
            else:
                sensor.value -= 1

class Humidifier(Thing):
    def __init__(self, name, focus_humidity):
        super().__init__(name)
        self.focus_humidity = focus_humidity

    def change_humidity(self, focus_humidity):
        self.focus_humidity = focus_humidity

    def print_name(self):
        super().print_name()

    def humidify(self, *sensors):
        for sensor in sensors:
            if sensor.value < self.focus_humidity:
                sensor.value += 1
            else:
                sensor.value -= 1

class Lightning(Thing):
    def __init__(self, name, focus_day_light, focus_night_light):
        super().__init__(name)
        self.focus_day_light = focus_day_light
        self.focus_night_light = focus_night_light

    def print_name(self):
        super().print_name()

    def change_day_light(self, light):
        self.focus_day_light = light
        # for sensor in sensors:
        #     sensor.value = light

    def change_night_light(self, light):
        self.focus_night_light = light
        # for sensor in sensors:
        #     sensor.value = light

    def day_light_up(self, *sensors):
        for sensor in sensors:
            sensor.value = self.focus_day_light

    def night_light_up(self, *sensors):
        for sensor in sensors:
            sensor.value = self.focus_night_light

class Conditioner(Thing):
    def __init__(self, name, focus_air):
        super().__init__(name)
        self.focus_air = focus_air

    def print_name(self):
        super().print_name()

    def change_air_condition(self, focus_air):
        self.focus_air = focus_air

    def air_condition(self, *sensors):
        for sensor in sensors:
            if sensor.value < self.focus_air:
                sensor.value += 1
            else:
                sensor.value -= 1

class Warehouse(Thing):
    def __init__(self, name, vater_volume, seeds, fertilizer, components):
        super().__init__(name)
        self.vater_volume = vater_volume
        self.seeds = seeds
        self.fertilizer = fertilizer
        self.components = components

    def print_name(self):
        super().print_name()

    def add_vater_volume(self, sensor):
        sensor.value += 1

    def add_seeds(self, sensor):
        sensor.value += 1

    def add_fertilizer(self, sensor):
        sensor.value += 1

    def add_components(self, sensor):
        sensor.value += 1

    def lower_vater_volume(self, sensor):
        sensor.value -= 1

    def lower_seeds(self, sensor):
        sensor.value -= 1

    def lower_fertilizer(self, sensor):
        sensor.value -= 1

    def lower_components(self, sensor):
        sensor.value -= 1