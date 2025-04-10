import json

from flask import Flask, render_template, request
import datetime

from threading import Timer
import my_classes
import logger
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#Подключение библиотек

app = Flask(__name__)
# Подключение к бд
logger = logger.Logger('IOT')
# Объявление объектов датчика температуры
sensor_1 = my_classes.Sensor('temp_1')
sensor_2 = my_classes.Sensor('temp_2')
sensor_3 = my_classes.Sensor('temp_3')
sensor_4 = my_classes.Sensor('temp_4')
sensor_5 = my_classes.Sensor('temp_5')
# Объявление объектов датчика влажности
sensor_6 = my_classes.Sensor('humidity_1')
sensor_7 = my_classes.Sensor('humidity_2')
sensor_8 = my_classes.Sensor('humidity_3')
sensor_9 = my_classes.Sensor('humidity_4')
sensor_10 = my_classes.Sensor('humidity_5')
# Объявление объектов датчика освещения
sensor_11 = my_classes.Sensor('light_1')
sensor_12 = my_classes.Sensor('light_2')
sensor_13 = my_classes.Sensor('light_3')
# Объявление объектов датчика показателя CO2
sensor_14 = my_classes.Sensor('air_condition_1')
sensor_15 = my_classes.Sensor('air_condition_2')
sensor_16 = my_classes.Sensor('air_condition_3')
sensor_17 = my_classes.Sensor('air_condition_4')
# Объявление объектов датчиков склада
sensor_water = my_classes.Sensor('water')
sensor_seeds = my_classes.Sensor('seeds')
sensor_fertilizer = my_classes.Sensor('fertilizer')
sensor_components = my_classes.Sensor('components')

# Создание массивов
# Температура
sensors = (sensor_1, sensor_2, sensor_3, sensor_4, sensor_5)
# Влажность
sensors2 = (sensor_6, sensor_7, sensor_8, sensor_9, sensor_10)
# Освещение
sensors3 = (sensor_11, sensor_12, sensor_13)
# CO2
sensors4 = (sensor_14, sensor_15, sensor_16, sensor_17)

# Созддание фокусных значений
heater = my_classes.Heater('greenhouse_heater', 25)
humidifier = my_classes.Humidifier('greenhouse_humidifier', 80)
lightning = my_classes.Lightning('greenhouse_lightning', 1000, 500)
conditioner = my_classes.Conditioner('greenhouse_conditioner', 10)


def log_temperature():
    logger.insert_temperature(sensor_1, sensor_2, sensor_3, sensor_4, sensor_5)
    logger.insert_humidity(sensor_6, sensor_7, sensor_8, sensor_9, sensor_10)
    logger.insert_lightning(sensor_11, sensor_12, sensor_13)
    logger.insert_air_condition(sensor_14, sensor_15, sensor_16, sensor_17)
    logger.insert_seeds(sensor_seeds)
    logger.insert_water(sensor_water)
    logger.insert_fertilizer(sensor_fertilizer)
    logger.insert_components(sensor_components)
    Timer(5, log_temperature).start()

log_temperature()

def set_lights():
    if (datetime.datetime.now().strftime("%H:%M:%S") > '06:00:00') and (datetime.datetime.now().strftime("%H:%M:%S") < '21:00:00'):
        print('Day is comming')
        lightning.day_light_up(*sensors3)
    else:
        print('Night is here')
        lightning.night_light_up(*sensors3)
    Timer(60, set_lights).start()

set_lights()
def send_json(name, value):
    return json.dumps({'Показатель': name, 'Значение': value})

def send_json_2(name, value, condition):
    return json.dumps({'Показатель': name, 'Значение': value, 'Условие': condition})

# Синхронизирование данных с логирования и датчиков
def Sync(temp_res,*sensors):
    for i in range(0, len(temp_res)):
        if ((sensors[i].value - temp_res[i]) >= 5):
            while(sensors[i].value != temp_res[i]):
                sensors[i].value -= 1
        if ((sensors[i].value - temp_res[i]) <= -5):
            while (sensors[i].value != temp_res[i]):
                sensors[i].value += 1


def readD (path_db):
    time = []
    temp = []
    temp_res = []
    last_time = ""
    print("Start sync")
    cursor = logger.read_data(path_db)
    for item in cursor:
        time.append(item['timeStamp'])
        temp.append(list(item.values())[2:])


    temp_res = temp[-1]


    return temp_res


def Syn_temp():
    light_path = 'Lightning'
    temp_path = 'Temperature'
    hum_path = 'Humidity'
    air_path = 'Air_condition'

    lp = readD(light_path)
    tp = readD(temp_path)
    hp = readD(hum_path)
    ap = readD(air_path)


    Sync(lp,*sensors3)
    Sync(tp,*sensors)
    Sync(hp,*sensors2)
    Sync(ap,*sensors4)


    Timer(30, Syn_temp).start()





Syn_temp()

#Warehouse

@app.route('/get_water')
def get_water():
    try:
        value = int(request.args.get('valueWater',''))
        sensor_water.value = value
        print('Установлено значение воды в баках')
    except:
        print('Value is not int')

    return send_json('Вода', request.args.get('valueWater', '') + ' л')

@app.route('/get_seed')
def get_seeds():
    try:
        value = int(request.args.get('valueSeeds',''))
        sensor_seeds.value = value
        print('Установлено значение Семян')
    except:
        print('Value is not int')

    return send_json('Семена', request.args.get('valueSeeds', '') + ' шт')

@app.route('/get_fertilizer')
def get_fertilizer():
    try:
        value = int(request.args.get('valueFert',''))
        sensor_fertilizer.value = value
        print('становлено значение воды в баках')
    except:
        print('Value is not int')

    return send_json('Удобрения', request.args.get('valueFert', '') + ' шт')

@app.route('/get_components')
def get_components():
    try:
        value = int(request.args.get('valueComp',''))
        sensor_components.value = value
        print('становлено значение воды в баках')
    except:
        print('Value is not int')

    return send_json('Компоненты', request.args.get('valueComp', '') + ' шт')



@app.route('/warehouse_water')
def warehouse_water():
    result = {}
    #for sensor_waters in sensor_water:
    result[sensor_water.name] = sensor_water.value
    return result

@app.route('/warehouse_seeds')
def warehouse_seeds():
    result = {}
    #for sensor_seeds in sensor_:
    result[sensor_seeds.name] = sensor_seeds.value
    return result

@app.route('/warehouse_fertilizer')
def warehouse_fertilizer():
    result = {}
    #for sensor_waters in sensor_water:
    result[sensor_fertilizer.name] = sensor_fertilizer.value
    return result

@app.route('/warehouse_components')
def warehouse_components():
    result = {}
    #for sensor_waters in sensor_water:
    result[sensor_components.name] = sensor_components.value
    return result

# End the WareHouse

@app.route('/get_temp')
def get_temp():
    heater.heat(*sensors)
    result = {}
    try:
        value = int(request.args.get('value1', ''))
        heater.change_temperature(value)
        print('Фокусное значение температуры установлено')
    except:
        print('Value is not int')

    return send_json('Температура', request.args.get('value1', '')+' гр')

@app.route('/get_humidity')
def get_humidity():
    humidifier.humidify(*sensors2)
    result = {}
    try:
        value = int(request.args.get('value2', ''))
        humidifier.change_humidity(value)
        print('Фокусное значение влажности установлено')
    except:
        print('Value is not int')

    return send_json('Влажность', request.args.get('value2', '')+' %')

@app.route('/get_air_condition')
def get_air_condition():
    conditioner.air_condition(*sensors4)
    result = {}
    try:
        value = int(request.args.get('value3', ''))
        conditioner.change_air_condition(value)
        print('Фокусное значение содержания CO2 установлено')
    except:
        print('Value is not int')

    condition = ''
    if request.args.get('check1', '') == '1':
        print('Кондиционер включен')
        condition = 'Кондиционер включен'
    else:
        print('Кондиционер выключен')
        condition = 'кондиционер выключен'
    return send_json_2('CO2', request.args.get('value3', '')+' ppm', condition)

@app.route('/get_light')
def get_light():
    # lightning.day_light_up(*sensors3)
    result = {}
    try:
        value = int(request.args.get('value4', ''))
        # for sensor in sensors3:
        #     sensor.value = value
        print(request.args.get('check2', ''))
        if request.args.get('check2', '') == '1':
            print('Дневное освещение')
            condition = 'Дневное освещение'
            lightning.change_day_light(value)
        else:
            print('Ночное освещение')
            condition = 'Ночное освещение'
            lightning.change_night_light(value)
        print('Фокусное значение освещения установлено')
    except:
        print('Value is not int')


    return send_json_2('Освещение', request.args.get('value4', '')+' лк', condition)


@app.route('/interface')
def show_interface():
    return 'interface'

@app.route('/new_value/<value>')
def save_value(value):
    print(value)
    return {}

@app.route('/sensor/<int:temp>')
def show_sensor(temp):
    save_value(temp)
    return f'текущая температура: {temp}'

def analysis(cursor, name):
    time = []
    avg_val = []
    max_val = []
    min_val = []
    for item in cursor:
        time.append(item['timeStamp'])
        avg_val.append(np.average(list(item.values())[2:]))
        max_val.append(np.max(list(item.values())[2:]))
        min_val.append(np.min(list(item.values())[2:]))
        if (np.max(list(item.values())[2:]) > np.average(list(item.values())[2:]) + 10) or (
                np.min(list(item.values())[2:]) < np.average(list(item.values())[2:]) - 10):
            print('Возможно присутствие ошибки в работе одного или более датчиков температуры')
    max_max_val = max(max_val)
    print(avg_val)
    print(max_val)
    print(min_val)
    # x = np.arange(0, len(time)).reshape((-1, 1))
    x = np.arange(0, len(time))
    y = np.array(avg_val)

    plt.plot(x, y)
    plt.xticks(rotation=90)
    plt.ylim(0, max_max_val*1.1)

    x = np.arange(len(time), len(time) * 2)
    y_pred = np.poly1d(np.polyfit(x, y, 30))

    # if (max_temp > y_pred + 10) or (min_temp < y_pred - 10):
    #     print('Возможно присутствие ошибки в работе одного или более датчиков температуры')

    plt.plot(x, y_pred(x))
    plt.xticks(rotation=90)
    plt.ylim(0, max_max_val*1.1)
    plt.xlabel('Time')
    plt.ylabel('Average indicator')
    plt.title(name)
    plt.show()

@app.route('/connect')
def connect():

    # Расчёт и построение графика прогнозирующего дальнейшее показание датчиков температуры
    cursor = logger.read_data('Temperature')
    print(cursor)
    analysis(cursor, 'Temperature')

    # Расчёт и построение графика прогнозирующего дальнейшее показание датчиков света
    cursor2 = logger.read_data('Lightning')
    print(cursor2)
    analysis(cursor2, 'Lightning')

    # Расчёт и построение графика прогнозирующего дальнейшее показание датчиков влажности
    cursor3 = logger.read_data('Humidity')
    print(cursor3)
    analysis(cursor3, 'Humidity')

    # Расчёт и построение графика прогнозирующего дальнейшее показание датчиков кондиционирования
    cursor4 = logger.read_data('Air_condition')
    print(cursor4)
    analysis(cursor4, 'Air_condition')

    return {}

@app.route('/connect_2')
def connect_2():
    print(request.args.get('value', ''))
    return send_json_2(request.args.get('value', ''))

@app.route('/greenhouse_temperature')
def greenhouse_temperature():
    heater.heat(*sensors)
    result = {}
    for sensor in sensors:
        result[sensor.name] = sensor.value
    return result

@app.route('/greenhouse_humidity')
def greenhouse_humidity():
    humidifier.humidify(*sensors2)
    result = {}
    for sensor in sensors2:
       result[sensor.name] = sensor.value
    return result

@app.route('/greenhouse_air_condition')
def greenhouse_air_condition():
    conditioner.air_condition(*sensors4)
    result = {}
    for sensor in sensors4:
        result[sensor.name] = sensor.value
    return result

@app.route('/greenhouse_lightning')
def greenhouse_lightning():
    result = {}
    for sensor in sensors3:
        result[sensor.name] = sensor.value
    return result

@app.route('/greenhouse')
def hello_world():  # put application's code here
    return render_template('new_window.html')

@app.route('/warehouse')
def warehouse():  # put application's code here
    return render_template('warehouse_window.html')

# Второй интерфейс


if __name__ == '__main__':
    app.run()
