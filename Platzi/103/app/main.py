import utils
import charts
import read_csv
  

def run():
  data= read_csv.read_csv('data.csv')
  data= list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_char(countries, percentages)
  country = input('Type Country =>')
  result = utils.info_by_country(data, country)
  country_info = result[0]

  keys, values = utils.get_population(country_info)
  charts.generate_bar_char(country,keys, values)
  
  
  #Este if dice que si es ejecutado desde la terminal, entre al run y si es ejecutado desde otro archivo, no se ejecuta.  
  
if __name__ == "__main__":
  run()