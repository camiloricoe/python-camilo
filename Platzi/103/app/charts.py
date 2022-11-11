import matplotlib.pyplot as plt

def generate_bar_char(countryname, labels, values):
  fig,ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'{countryname}_bar.png')
  plt.close()

def generate_pie_char(labels, values):
  fig,ax = plt.subplots()
  ax.pie(values,labels=labels)
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  generate_pie_char(['a','b','c'],[100,200,300])

