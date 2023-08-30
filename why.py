from typing import List
import json
import time
import random
import math

import numpy as np


def why(lists: list, email: str) -> List[dict]:
    # Создание списка с данными для тестов
    tests = [
        {
            #0
            "title": "Тест на простую зрительно-моторную реакцию",
            "avgSpeed": "",
            "minSpeed": "",
            "maxSpeed": "",
            "moda": "",
            "amoda": "",
            "sko": "",
            "advance": "",
            "skip": "",
            "variety": "",
            "variety_percent": "",
            "func_abil": "",
            "attempts": "",
            #"unique_id": "",
            "email": "",
            "first_name": "",
            "last_name": ""
        },
        {
            #1
            "title": "Тест на помехоустойчивость",
            "avgSpeed": "",
            "minSpeed": "",
            "maxSpeed": "",
            "moda": "",
            "amoda": "",
            "sko": "",
            "advance": "",
            "skip": "",
            "variety": "",
            "variety_percent": "",
            "func_abil": "",
            "hindrance":"23", #####   ????
            "attempts": "",
            #"unique_id": "",
            "email": "",
            "first_name": "",
            "last_name": ""
        },
        { 
            #2
            "title": "Тест на реакцию различения",
            "avgSpeed": "",
            "minSpeed": "",
            "maxSpeed": "",
            "moda": "",
            "amoda": "",
            "sko": "",
            "advance": "",
            "skip": "",
            "variety": "",
            "variety_percent": "",
            "func_abil": "",
            "choose":"23425", ############
            "podvizh":"11", ##############
            "attempts": "",
            #"unique_id": "",
            "email": "",
            "first_name": "",
            "last_name": ""
        },
        {
            #3
            "title": "Тест на реакцию выбора",
            "avgSpeed": "",
            "minSpeed": "",
            "maxSpeed": "",
            "moda": "",
            "amoda": "",
            "sko": "",
            "advance": "",
            "skip": "",
            "variety": "",
            "variety_percent": "",
            "func_abil": "",
            "attempts": "",
            #"unique_id": "",
            "email": "",
            "first_name": "",
            "last_name": ""
        },
        {
            #4
            "title": "Реакция на движущийся объект",
            "avgSpeed": "",
            "sko": "",
            "koef":"", ###########
            "attempts": "",
            #"unique_id": "",
            "email": "",
            "first_name": "",
            "last_name": ""
        },
        {
            #5
            "title": "Теппинг тест - Диагностика силы нервных процессов",
            "minSpeed": "",
            "maxSpeed": "",
            "attempts": "",
            #"unique_id": "",
            "email": "",
            "first_name": "",
            "last_name": "",
            "msg": "NICE" ############
        }
    ]

    def find_indexes(value, lists):
        res = []
        for i in range(len(lists)):
            if lists[i] == value:
                res.append(i)
        return res

    def results(clicks):
        minc = min(clicks)
        minc_index = find_indexes(minc, clicks)
        maxc = max(clicks)
        maxc_index = find_indexes(maxc, clicks)
        koef = maxc / minc
        msg = ""

        if (1 in maxc_index or 2 in maxc_index or 3 in maxc_index or 4 in maxc_index) and 0 in minc_index and minc - 10 < clicks[5] < minc + 10 and koef > 1.1:
            msg = "Характеризуется возрастанием темпа движений в первые 15 секунд обследования более чем на 10%; затем темп, как правило, снижается до исходного (±10%). Такой тип кривой свидетельствует о наличии у вас сильной нервной системы."
        elif 0 in maxc_index and koef > 1.1:
            msg = "Максимальное количество движений фиксируется в течение первого пятисекундного интервала, затем темп движений снижается более чем на 10%. Этот тип кривой свидетельствует о слабости нервной системы."
        elif (0 in maxc_index or 1 in maxc_index or 2 in maxc_index) and koef > 1.1:
            msg = "Максимальное число движений фиксируется в течение первых двух - трех пятисекундных интервалов, затем темп движений падает более чем на 10%. Такой тип кривой свидетельствует о наличии у вас нервной системы на границе между слабой и средней (средне-слабая нервная система). "
        elif 0 in minc_index and koef < 1.1:
            msg = "Темп движений вначале снижается, затем фиксируется кратковременное возрастание темпа до исходного уровня (±10%). Обследуемые с таким типом кривой также относятся к группе лиц со средне-слабой нервной системой)."
        else:
            msg = "Темп движений удерживается около исходного уровня с колебаниями ±10% на протяжении всего отрезка времени. Такой вариант кривой свидетельствует о наличии у вас средней силы нервной системы."
        
        return msg

    # Округление значения до двух знаков после запятой
    def round_two_decimals(value):
        return round(value, 2)

    # Генерация уникального идентификатора
    def generate_unique_id():
        return "apireactiontest" + str(int(time.time() * 1000))

    # Генерация случайного email
    def generate_random_email():
        return "example" + str(int(time.time())) + "@example.com"

    for i, test in enumerate(tests):
        if test["title"] == "Теппинг тест - Диагностика силы нервных процессов":
            avg_speed = round_two_decimals(sum(lists[i]) / len(lists[i]))
            min_speed = round_two_decimals(min(lists[i]))
            max_speed = round_two_decimals(max(lists[i]))
            attempts = ', '.join(str(int(x)) for x in lists[i])
            # email = generate_random_email()
            first_name = "John"
            last_name = "Doe"
            msg = results(lists[i])
            
            test["minSpeed"] = str(min_speed)
            test["maxSpeed"] = str(max_speed)
            test["attempts"] = attempts
            test["email"] = email
            test["first_name"] = first_name
            test["last_name"] = last_name
            test["msg"] = msg
            
            # Remove unnecessary keys
            test.pop("avgSpeed", None)
            test.pop("moda", None)
            test.pop("amoda", None)
            test.pop("sko", None)
            test.pop("advance", None)
            test.pop("skip", None)
            test.pop("variety", None)
            test.pop("variety_percent", None)
            test.pop("func_abil", None)
            test.pop("podvizh", None)
            
        elif test["title"] == "Тест на простую зрительно-моторную реакцию":
            avg_speed = round_two_decimals(sum(lists[i]) / len(lists[i]))
            min_speed = round_two_decimals(min(lists[i]))
            max_speed = round_two_decimals(max(lists[i]))
            moda = round_two_decimals(max(set(lists[i]), key=lists[i].count))
            amoda = round_two_decimals(lists[i].count(max(set(lists[i]), key=lists[i].count)))
            sko = round_two_decimals((sum((x - avg_speed)**2 for x in lists[i]) / len(lists[i]))**0.5)
            advance = sum(x < min_speed for x in lists[i])
            skip = sum(x == 0 for x in lists[i])
            variety = round_two_decimals(max_speed - min_speed)
            variety_percent = round_two_decimals((variety / avg_speed) * 100)
            hindrance =  np.abs(max_speed - avg_speed)
            if skip != 0:
                koef = round((30 - skip)/skip, 2)
            else:
                koef = 0  
            func_abil = round_two_decimals(45 - math.log(avg_speed) + 0.03*sko + 0.16*variety_percent - 0.06*moda + 0.08*amoda - 0.01*variety)
            attempts = attempts = ', '.join(str(int(x)) for x in lists[i])
            unique_id = generate_unique_id()
            # email = generate_random_email()
            
            test["avgSpeed"] = str(avg_speed)
            test["minSpeed"] = str(min_speed)
            test["maxSpeed"] = str(max_speed)
            test["moda"] = str(moda)
            test["amoda"] = str(amoda)
            test["sko"] = str(sko)
            test["advance"] = str(advance)
            test["skip"] = str(skip)
            test["variety"] = str(variety)
            test["variety_percent"] = str(variety_percent)
      
            test["func_abil"] = str(func_abil)
            test["attempts"] = attempts
            #test["unique_id"] = unique_id
            test["email"] = email
            
            # Remove unnecessary keys
            test.pop("hindrance", None)
            test.pop("koef", None)
            test.pop("unique_id", None)
            test.pop("msg", None)
            test.pop("podvizh", None)
            
        elif test["title"] == "Тест на помехоустойчивость":
            avg_speed = round_two_decimals(sum(lists[i]) / len(lists[i]))
            min_speed = round_two_decimals(min(lists[i]))
            max_speed = round_two_decimals(max(lists[i]))
            moda = round_two_decimals(max(set(lists[i]), key=lists[i].count))
            amoda = round_two_decimals(lists[i].count(max(set(lists[i]), key=lists[i].count)))
            sko = round_two_decimals((sum((x - avg_speed)**2 for x in lists[i]) / len(lists[i]))**0.5)
            advance = sum(x < min_speed for x in lists[i])
            skip = sum(x == 0 for x in lists[i])
            variety = round_two_decimals(max_speed - min_speed)
            variety_percent = round_two_decimals((variety / avg_speed) * 100)
            hindrance =  np.abs(max_speed - avg_speed)
            if skip != 0:
                koef = round((30 - skip)/skip, 2)
            else:
                koef = 0  
            func_abil = round_two_decimals(45 - math.log(avg_speed) + 0.03*sko + 0.16*variety_percent - 0.06*moda + 0.08*amoda - 0.01*variety)
            attempts = attempts = ', '.join(str(int(x)) for x in lists[i])
            unique_id = generate_unique_id()
            # email = generate_random_email()
            
            test["avgSpeed"] = str(avg_speed)
            test["minSpeed"] = str(min_speed)
            test["maxSpeed"] = str(max_speed)
            test["moda"] = str(moda)
            test["amoda"] = str(amoda)
            test["sko"] = str(sko)
            test["advance"] = str(advance)
            test["skip"] = str(skip)
            test["variety"] = str(variety)
            test["variety_percent"] = str(variety_percent)
            test["hindrance"] = str(hindrance)      
            test["func_abil"] = str(func_abil)
            test["attempts"] = attempts
            test["email"] = email
            
             # Remove unnecessary keys
           
            test.pop("koef", None)
            test.pop("unique_id", None)
            test.pop("msg", None)
            test.pop("podvizh", None)
            
        elif test["title"] == "Тест на реакцию различения":
            avg_speed = round_two_decimals(sum(lists[i]) / len(lists[i]))
            min_speed = round_two_decimals(min(lists[i]))
            max_speed = round_two_decimals(max(lists[i]))
            moda = round_two_decimals(max(set(lists[i]), key=lists[i].count))
            amoda = round_two_decimals(lists[i].count(max(set(lists[i]), key=lists[i].count)))
            sko = round_two_decimals((sum((x - avg_speed)**2 for x in lists[i]) / len(lists[i]))**0.5)
            advance = sum(x < min_speed for x in lists[i])
            skip = sum(x == 0 for x in lists[i])
            variety = round_two_decimals(max_speed - min_speed)
            variety_percent = round_two_decimals((variety / avg_speed) * 100)
            hindrance =  np.abs(max_speed - avg_speed)
            if skip != 0:
                koef = round((30 - skip)/skip, 2)
            else:
                koef = 0  
            func_abil = round_two_decimals(45 - math.log(avg_speed) + 0.03*sko + 0.16*variety_percent - 0.06*moda + 0.08*amoda - 0.01*variety)
            attempts = attempts = ', '.join(str(int(x)) for x in lists[i])
            unique_id = generate_unique_id()
            # email = generate_random_email()
            
            test["avgSpeed"] = str(avg_speed)
            test["minSpeed"] = str(min_speed)
            test["maxSpeed"] = str(max_speed)
            test["moda"] = str(moda)
            test["amoda"] = str(amoda)
            test["sko"] = str(sko)
            test["advance"] = str(advance)
            test["skip"] = str(skip)
            test["variety"] = str(variety)
            test["variety_percent"] = str(variety_percent)
            test["hindrance"] = str(hindrance)
            test["koef"] = str(koef)
            test["func_abil"] = str(func_abil)
            test["attempts"] = attempts
            test["unique_id"] = unique_id
            test["email"] = email
            test["podvizh"] = 11
            
            
             # Remove unnecessary keys
            test.pop("hindrance", None)
            test.pop("koef", None)
            test.pop("unique_id", None)
            test.pop("msg", None)
            
            
        elif test["title"] == "Тест на реакцию выбора":
            avg_speed = round_two_decimals(sum(lists[i]) / len(lists[i]))
            min_speed = round_two_decimals(min(lists[i]))
            max_speed = round_two_decimals(max(lists[i]))
            moda = round_two_decimals(max(set(lists[i]), key=lists[i].count))
            amoda = round_two_decimals(lists[i].count(max(set(lists[i]), key=lists[i].count)))
            sko = round_two_decimals((sum((x - avg_speed)**2 for x in lists[i]) / len(lists[i]))**0.5)
            advance = sum(x < min_speed for x in lists[i])
            skip = sum(x == 0 for x in lists[i])
            variety = round_two_decimals(max_speed - min_speed)
            variety_percent = round_two_decimals((variety / avg_speed) * 100)
            hindrance =  np.abs(max_speed - avg_speed)
            if skip != 0:
                koef = round((30 - skip)/skip, 2)
            else:
                koef = 0  
            func_abil = round_two_decimals(45 - math.log(avg_speed) + 0.03*sko + 0.16*variety_percent - 0.06*moda + 0.08*amoda - 0.01*variety)
            attempts = attempts = ', '.join(str(int(x)) for x in lists[i])
            unique_id = generate_unique_id()
            # email = generate_random_email()
            test["avgSpeed"] = str(avg_speed)
            test["minSpeed"] = str(min_speed)
            test["maxSpeed"] = str(max_speed)
            test["moda"] = str(moda)
            test["amoda"] = str(amoda)
            test["sko"] = str(sko)
            test["advance"] = str(advance)
            test["skip"] = str(skip)
            test["variety"] = str(variety)
            test["variety_percent"] = str(variety_percent)
            test["hindrance"] = str(hindrance)
            test["koef"] = str(koef)
            test["func_abil"] = str(func_abil)
            test["attempts"] = attempts
            test["unique_id"] = unique_id
            test["email"] = email
            
            test.pop("hindrance", None)
            test.pop("koef", None)
            test.pop("unique_id", None)
            test.pop("msg", None)
            test.pop("podvizh", None)
            
        elif test["title"] == "Реакция на движущийся объект":
            avg_speed = round_two_decimals(sum(lists[i]) / len(lists[i]))
            min_speed = round_two_decimals(min(lists[i]))
            max_speed = round_two_decimals(max(lists[i]))
            moda = round_two_decimals(max(set(lists[i]), key=lists[i].count))
            amoda = round_two_decimals(lists[i].count(max(set(lists[i]), key=lists[i].count)))
            sko = round_two_decimals((sum((x - avg_speed)**2 for x in lists[i]) / len(lists[i]))**0.5)
            advance = sum(x < min_speed for x in lists[i])
            skip = sum(x == 0 for x in lists[i])
            variety = round_two_decimals(max_speed - min_speed)
            variety_percent = round_two_decimals((variety / avg_speed) * 100)
            hindrance =  np.abs(max_speed - avg_speed)
            if skip != 0:
                koef = round((30 - skip)/skip, 2)
            else:
                koef = 0  
            func_abil = round_two_decimals(45 - math.log(avg_speed) + 0.03*sko + 0.16*variety_percent - 0.06*moda + 0.08*amoda - 0.01*variety)
            attempts = attempts = ', '.join(str(int(x)) for x in lists[i])
            unique_id = generate_unique_id()
            # email = generate_random_email()
            test["avgSpeed"] = str(avg_speed)
            test["sko"] = str(sko)
            test["koef"] = str(koef)
            test["attempts"] = attempts
            test["unique_id"] = unique_id
            test["email"] = email
            
          
           
           
            test["email"] = email
            
            # Remove unnecessary keys
            test.pop("minSpeed", None)
            test.pop("maxSpeed", None)
            test.pop("moda", None)
            test.pop("amoda", None)
            test.pop("advance", None)
            test.pop("hindrance", None)
            test.pop("skip", None)
            test.pop("unique_id", None)
            test.pop("msg", None)
            test.pop("podvizh", None) 
            test.pop("variety", None)
            test.pop("variety_percent", None)
            test.pop("skip", None)
            test.pop("func_abil", None)

    return tests