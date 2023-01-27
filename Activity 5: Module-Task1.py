import matplotlib.pyplot as plt

def draw_line_graph(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()

def draw_bar_graph(x_values,y_values):
    plt.bar(x_values,y_values)
    plt.show()

def draw_pie_graph(x_values,y_values):
    plt.pie(y_values, labels=x_values)
    plt.show()

def draw_scattered_graph(x_values,y_values):
    plt.scatter(x_values,y_values)
    plt.show()
