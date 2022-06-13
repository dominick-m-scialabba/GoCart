# Go Cart HMI ##########################################################################################################
#
# Dominick M. Scialabba, 6/12/22
#
# This program will read data over UART and I2C and compute and display statistics on a touchscreen display via a GUI.


# Libraries ############################################################################################################
import PySimpleGUI as GUI
import matplotlib as MAT
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# GUI Methods ##########################################################################################################
def update_graph(data, figure, key):
    axes = figure.axes
    x = [i[0] for i in  data]
    y = [i[1] for i in  data]
    axes[0].plot(x, y, 'r-')
    figure_canvas = FigureCanvasTkAgg(fig, window[key].TKCanvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side = 'top', fill = 'both', expand = True)


# GUI Initialization ###################################################################################################
GUI.theme('DarkBlue')
table_contents = []
layout =    [[GUI.Table(
                headings = ['Number', 'X', 'Y'],
                values = table_contents,
                expand_x = True,
                expand_y = True,
                hide_vertical_scroll = True,
                key = '-TABLE-')],

            [GUI.Input(
                expand_x = True,
                expand_y = False,
                key = '-INPUT-'),

            GUI.Button(
                'SUBMIT',
                expand_x = True,
                expand_y = False,
                key = '-SUBMIT-')],

            [GUI.Canvas(
                expand_x = True,
                expand_y = True,
                key = '-GRAPH-')]]

window = GUI.Window('Home', layout, resizable = True, finalize = True)


# Figure Initialization ################################################################################################
fig = MAT.figure.Figure()
fig.add_subplot(1, 1, 1)


# GUI Read and Display Loop ############################################################################################
while True:
    event, values = window.read()
    if event == GUI.WINDOW_CLOSED:
        break
    if event == '-SUBMIT-':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            table_contents.append([len(table_contents) + 1, float(new_value)])
            window['-TABLE-'].update(table_contents)
            window['-INPUT-'].update('')
            update_graph(table_contents, fig, '-GRAPH-')

window.close()
