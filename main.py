import station_list # импортируем список станций

# print (station_list.blue_line) -- печатаем список синей ветки

def main():
    print(f"First station info:{firstStationid()}")
    print(f"Second station info:{secondStationid()}")
#    result = firstStationid()
#    print (result[1])
#    firstStation = firstStationid()

def firstStationid(): # функция запрашивает название первой станции и выдает ее нумерацию 
    while True:
        station = input("Введите первую станцию")
        if station in station_list.blue_line:
            id = station_list.blue_line.index(station) + 1  
            line = "blue"
            break
        elif station in station_list.green_line:
            id = station_list.green_line.index(station) + 1  
            line = "green"
            break            
        elif station in station_list.red_line:
            id = station_list.red_line.index(station) + 1  
            line = "red"
            break
        elif station == "stop":
            break
        else:
            print("Станция не найдена")
    return id, line
    
def secondStationid(): # функция запрашивает название второй станции и выдает ее нумерацию 
    while True:
        station = input("Введите вторую станцию")
        if station in station_list.blue_line:
            id = station_list.blue_line.index(station) + 1  
            line = "blue"
            break
        elif station in station_list.green_line:
            id = station_list.green_line.index(station) + 1  
            line = "green"
            break            
        elif station in station_list.red_line:
            id = station_list.red_line.index(station) + 1  
            line = "red"
            break
        elif station == "stop":
            break
        else:
            print("Станция не найдена")
    return id, line
if __name__ == "__main__":
    main()


