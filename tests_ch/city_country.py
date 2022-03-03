from city_functions import place_description

print("Enter 'q' to quit.")
while True:
    city = input("\n Enter city name: ")
    if city == 'q':
        break
    country = input("\n Enter country name: ")
    if country == 'q':
        break
    population = input("\n Enter population amount: ")
    if country == 'q':
        break

    formatted_description = place_description(city, country, population)
    print(f"\n\t That place: {formatted_description}.")