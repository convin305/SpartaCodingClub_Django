my_station=['야탑','모란','이매','선릉','한티','왕십리']

def station_list(station_list):
    for station in station_list:
        print(station)

station_list(my_station)

def station_point(station_list):
    for station in station_list:
        if station == '선릉':
            print(station)

station_point(my_station)
