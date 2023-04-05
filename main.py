import station_list # импортируем список станций

# print (station_list.blue_line) -- печатаем список синей ветки

def main():
    # first_question = input("Введите первую станцию")
    # second_question = input("Введите вторую станцию")
    # first_station_id(first_question)
    # second_station_id(second_question)
    print("Введите название первой станции:")
    first_station_name = station_check()
    print(first_station_name)
#    result = firstStationid()
#    print (result[1])
#    firstStation = firstStationid()

def station_check():
    while True:
        station = input()
        if station in station_list.all_stations:
            return station
        else:
            print("Такой станции нету")
            print("Введите название еще раз")


# def first_station_id(first_station): # функция запрашивает название первой станции и выдает ее нумерацию 
#     while True:
# #        station = input("Введите первую станцию")
#         if first_station in station_list.blue_line:
#             line = "blue"
#             break
#         elif first_station in station_list.green_line:
#             line = "green"
#             break            
#         elif first_station in station_list.red_line:
#             line = "red"
#             break
#         elif first_station == "stop":
#             break
#         else:
#             return False
#     return line
    
# def second_station_id(second_station): # функция запрашивает название второй станции и выдает ее нумерацию 
#     while True:
# #        station = input("Введите вторую станцию")
#         if second_station in station_list.blue_line:
#             line = "blue"
#             break
#         elif second_station in station_list.green_line:
#             line = "green"
#             break            
#         elif second_station in station_list.red_line:
#             line = "red"
#             break
#         elif second_station == "stop":
#             break
#         else:
#             return False        
#     return line

if __name__ == "__main__":
    main()


