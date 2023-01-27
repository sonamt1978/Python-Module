from graphModule import Graph
g=Graph()
x = ("Dzo", "Eng","Maths","Sci")
y=[]
for i in range(len(x)):
    marks=int(input(f'Enter marks for {x[i]}:'))
    y.append(marks)
print("What do you want to do")
print("1. Draw line graph")
print("2. Draw bar graph")
print("3. Draw pie chart")
print("4. Draw scattered graph")
print("5. Exit")
while True:
    option=int(input("Enter option:"))
    if option==1:
        g.draw_line_graph(x, y)
    elif option==2:
        g.draw_bar_graph(x, y)
    elif option==3:
        g.draw_pie_graph(x,y)
    elif option==4:
        g.draw_scattered_graph(x,y)
    else:
        print("See you")
        break
