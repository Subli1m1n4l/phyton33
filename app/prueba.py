import readcsv
import charts

def run():
  data = readcsv.read_csv('./app/data.csv')
  data = list(filter(lambda item: item['Continent']== 'South America',data))
  values = list(map(lambda item:item['World Population Percentage'],data))
  labels= list(map(lambda item:item['Country/Territory'],data))
  charts.generate_bar_chart(labels,values)





if __name__ == '__main__':
  run()
