import pymongo
import datetime


class Logger:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]

    def insert_temperature(self, *sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for sensor in sensors:
            result[sensor.name] = sensor.value

        return self.db['Temperature'].insert_one(result)

    def insert_lightning(self, *sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for sensor in sensors:
            result[sensor.name] = sensor.value

        return self.db['Lightning'].insert_one(result)

    def insert_humidity(self, *sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for sensor in sensors:
            result[sensor.name] = sensor.value

        return self.db['Humidity'].insert_one(result)

    def insert_water(self, sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        #for sensor in sensors:
        result[sensors.name] = sensors.value
        return self.db['Water'].insert_one(result)

    def insert_seeds(self, *sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for sensor in sensors:
            result[sensor.name] = sensor.value

        return self.db['Seeds'].insert_one(result)

    def insert_fertilizer(self, *sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for sensor in sensors:
            result[sensor.name] = sensor.value

        return self.db['Fertilizer'].insert_one(result)

    def insert_components(self, *sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for sensor in sensors:
            result[sensor.name] = sensor.value

        return self.db['Components'].insert_one(result)

    def insert_air_condition(self, *sensors):
        result = {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for sensor in sensors:
            result[sensor.name] = sensor.value

        return self.db['Air_condition'].insert_one(result)

    def read_data(self, collection, value={}, field={}):
        return self.db[collection].find(value, field)

