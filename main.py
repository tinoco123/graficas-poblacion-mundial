import charts
import utils


def run():
    # Poblacion de un pais por años
    country_to_find = input("Write a country: ")
    data = utils.join_population_data(country_to_find)
    years = data.keys()
    population = data.values()
    charts.generate_bar_chart(years, population)
    # Porcentaje de poblacion mundial de paises del continente de oceania
    countries, percentages = utils.get_countries(), utils.get_percentage()
    charts.generate_pie_chart(countries, percentages)

if __name__ == "__main__":
    run()