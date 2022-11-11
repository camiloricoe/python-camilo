import matplotlib.pyplot as plt

def generate_bar_char(labels, values):
  fig,ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()

def generate_pie_char(labels, values):
  fig,ax = plt.subplots()
  ax.pie(values,labels=labels)
  plt.show()
  

if __name__ == '__main__':
  generate_pie_char(['a','b','c'],[100,200,300])

