import station_list # импортируем список станций

# print (station_list.blue_line) -- печатаем список синей ветки

def main():
    print(f"Под номером:{firstStationid()}")
    print(f"Под номером:{secondStationid()}")

#    firstStation = firstStationid()

def firstStationid():
    while True:
        station = input("Введите первую станцию")
        if station in station_list.blue_line:
            id = station_list.blue_line.index(station) + 1  
            print("Первая станция находится на синей ветке")
            break
        elif station in station_list.green_line:
            id = station_list.green_line.index(station) + 1  
            print("Первая станция находится на зеленой ветке")
            break            
        elif station in station_list.red_line:
            id = station_list.red_line.index(station) + 1  
            print("Первая станция находится на красной ветке")
            break
        elif station == "stop":
            break
        else:
            print("Станция не найдена")
    return id
def secondStationid():
    while True:
        station = input("Введите вторую станцию")
        if station in station_list.blue_line:
            id = station_list.blue_line.index(station) + 1  
            print("Вторая станция находится на синей ветке")
            break
        elif station in station_list.green_line:
            id = station_list.green_line.index(station) + 1  
            print("Вторая станция находится на зеленой ветке")
            break            
        elif station in station_list.red_line:
            id = station_list.red_line.index(station) + 1  
            print("Вторая станция находится на красной ветке")
            break
        elif station == "stop":
            break
        else:
            print("Станция не найдена")
    return id
if __name__ == "__main__":
    main()


