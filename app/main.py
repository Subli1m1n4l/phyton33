import utils
import readcsv
import charts as ch
import pandas as pd




def run():
  #  data= readcsv.read_csv()
  # data= list(filter(lambda item : item['Continent'] =='South America',data))

  # countries = list(map(lambda x: x['Country/Territory'],data))
  # percentages = list(map(lambda x: x['World Population Percentage'],data))

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] =='Africa']
  data= readcsv.read_csv('data.csv')
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  print(countries)
  print(percentages)
  country=input('Type Country =>')
  result = utils.population_by_country(data,country)
  
  country=result[0]
  labels,values= utils.get_population(country)
  ch.generate_bar_chart(country,countries,percentages)
  ch.generate_pie_chart(country,labels,values)



  result = utils.population_by_country(data,country)
  print(result)

if __name__ == '__main__':
  run()