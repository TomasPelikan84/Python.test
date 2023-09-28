travel_diary = [
    {
        "country": "Spain",
        "cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5
    },
    {
        "country": "France",
        "cities": ["Paris", "Nice", "Rennes"],
        "visits": 2
    },
    {}
]

def add_country(country_name, towns_list, visits_number):
    new_dictionary = {}
    new_dictionary["country"] = country_name
    new_dictionary["cities"] = towns_list
    new_dictionary["visits"] = visits_number
    travel_diary.append(new_dictionary)
    
add_country("Italy", ["Rome", "Florence", "Milan"], 9)

print(travel_diary)