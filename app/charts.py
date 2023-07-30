import matplotlib.pyplot as plt

def generate_bar_chart(name,labels,Values):
  fig, ax = plt.subplots()
  ax.bar(labels,Values)
  plt.savefig(f'./imgs/{name["Country/Territory"]}.png')
  plt.close()
  #plt.show()

def generate_pie_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/{name["Country/Territory"]}pie.png')
    plt.close()
    #plt.show()
  


if __name__=='__main__':
  labels = ['a','b','c']
  Values=[100,200,80]
  #generate_bar_chart(labels,Values)
  generate_pie_chart(labels,Values)