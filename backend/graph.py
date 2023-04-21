import matplotlib.pyplot as plt

def graph():
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [4,6,7,4,23,5,6,23,7,3]

    plt.plot(x, y)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('a graph')

    plt.show()

def scatterPlot():

    x = [5,4,6,7,7,5,7]
    y = [400, 500, 378, 325, 340, 410, 330]

    plt.scatter(x, y, label = "stars", color = "red", marker = "*", s = 30)

    plt.xlabel('Hours Slept')
    plt.ylabel('Caffeine Consumed (mg)')

    plt.title('Hours Slept and Caffeine Consumed - Week 3')

    plt.show()

def pieChart():

    sources = ['coffee', 'energy drink', 'chocolate', 'tea']
    count   = [40, 3, 27, 12]

    colours = ['r', 'y', 'g', 'b']

    plt.pie(count, labels = sources, colors = colours, startangle = 90, shadow = True, explode = (0, 0, 0.1, 0), radius = 1.5, autopct = '%1.1f%%')

    plt.legend(loc = 'lower left')

    plt.savefig('pieChart.png')

    plt.show()

pieChart()