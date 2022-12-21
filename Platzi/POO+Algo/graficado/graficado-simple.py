from bokeh.plotting import figure, output_file, show


if __name__ =='__main__':
    output_file('simplegraph.html')
    fig = figure()

    total_vars = int(input('Cuatos valores quieres graficar? '))
    x_vals = list(range(total_vars))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x} '))
        y_vals.append(val)

    fig.line(x_vals,y_vals,line_width=2)
    show(fig)
