import utils
import readcsv
import charts as ch




def run():
  data= readcsv.read_csv('data.csv')
  data= list(filter(lambda item : item['Continent'] =='South America',data))

  countries = list(map(lambda x: x['Country/Territory'],data))
  percentages = list(map(lambda x: x['World Population Percentage'],data))

  country=input('Type Country =>')

  result = utils.population_by_country(data,country)
  

  if len(result) >0:
    country=result[0]
    labels,values= utils.get_population(country)
    ch.generate_bar_chart(country,labels,values)
    ch.generate_pie_chart(country,labels,values)



  result = utils.population_by_country(data,country)
  print(result)

if __name__ == '__main__':
  run()