import  read_csv


def find_country(country_to_find):
    data = read_csv.read_csv("./data.csv")
    country_dict = list(filter(lambda country: country_to_find == country["CCA3"], data))[0]
    return country_dict


def get_year_labels_from_header():
    years_labels = read_csv.get_header("./data.csv")[5:13]
    return years_labels


def get_population_from_year(dict_country):
    year_labels = get_year_labels_from_header()
    population_by_year = [int(dict_country[column]) for column in dict_country.keys() if column in year_labels]
    return population_by_year


def join_population_data(country_to_find):
    dict_country = find_country(country_to_find)
    population_by_year = get_population_from_year(dict_country)
    year_labels = get_year_labels_from_header()
    final_data = {year: population for year, population in zip(year_labels, population_by_year)}
    return final_data



def get_countries():
    data = read_csv.read_csv("./data.csv")
    data = list(filter(lambda dict: dict["Continent"] == "Oceania", data))
    countries = list(map(lambda dict: dict["Country/Territory"], data))
    return countries


def get_percentage():
    data = read_csv.read_csv("./data.csv")
    data = list(filter(lambda dict: dict["Continent"] == "Oceania", data))
    percentages = list(map(lambda dict: float(dict["World Population Percentage"]), data))
    return percentages