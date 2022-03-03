def place_description(city_name, country_name, population=''):
    if population:
        full_description =  f"{city_name.title()}, {country_name.title()} - {population}"
    else:
        full_description =  f"{city_name.title()}, {country_name.title()}" 
    return full_description