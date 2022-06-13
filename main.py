# Go Cart HMI Main Routine #############################################################################################
#
# Dominick M. Scialabba, 6/12/22
#
# This program will read, interpret, and display statistics on a touchscreen display.


# Libraries ############################################################################################################
import numpy as NP
import PySimpleGUI as GUI
import matplotlib as MAT
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# GUI Methods ##########################################################################################################
def update_graph(data, figure, canvas):
    axes = figure.axes
    x = [i[1] for i in data]
    y = [i[2] for i in data]
    axes[0].plot(x, y, 'r-')
    canvas.draw()
    canvas.get_tk_widget().pack(side = 'top', fill = 'both', expand = True)


# GUI Initialization ###################################################################################################
ENTER_KEY_1 = 'special 16777220'
ENTER_KEY_2 = 'special 16777221'

font = 'roman'
text_color_1 = '#ffffff'
text_color_2 = '#000000'
background_color_1 = '#212121'
padding_1 = 2
border_width_1 = 2

menu_contents = [['MAIN'], ['BATTERY'], ['MOTORS'], ['SETTINGS']]
table_contents = []

layout =    [[GUI.Menu(
                menu_definition = menu_contents,
                background_color = '#212121',
                text_color = "black",
                font = None,
                pad = padding_1,
                key = '-MENU-')],

            [GUI.Table(
                headings = ['Number', 'X', 'Y'],
                values = table_contents,
                expand_x = True,
                expand_y = True,
                hide_vertical_scroll = True,
                key = '-TABLE-')],

            [GUI.Input(
                default_text = "X Values",
                size = (None, None),
                justification = None,
                background_color = None,
                text_color = None,
                font = None,
                border_width = None,
                key = '-X-INPUT-',
                pad = padding_1,
                expand_x = True,
                expand_y = False),

            GUI.Input(
                default_text = "Y Values",
                size = (None, None),
                justification = None,
                background_color = None,
                text_color = None,
                font = None,
                border_width = None,
                key = '-Y-INPUT-',
                pad = padding_1,
                expand_x = True,
                expand_y = False),

            GUI.Button(
                button_text = "SUBMIT",
                border_width = 2,
                size = (None, None),
                auto_size_button = None,
                button_color = '#212121',
                highlight_colors = None,
                mouseover_colors = (None, None),
                font = None,
                pad = padding_1,
                key = None,
                expand_x = True,
                expand_y = False)],

            [GUI.Canvas(
                expand_x = True,
                expand_y = True,
                key = '-GRAPH-')]]

GUI.theme('Dark')
window = GUI.Window('Home', layout, resizable = True, finalize = True, return_keyboard_events = True)

# Plot initialization
fig = MAT.figure.Figure()
fig.add_subplot(1, 1, 1)
figure_canvas = FigureCanvasTkAgg(fig, window["-GRAPH-"].TKCanvas)

# Loop #################################################################################################################
while True:
    event, values = window.read()
    if event == GUI.WINDOW_CLOSED:
        break
    if event == '-SUBMIT-':
        new_x_value = values['-X-INPUT-']
        new_y_value = values['-Y-INPUT-']
        if new_x_value.isnumeric() and new_y_value.isnumeric():
            table_contents.append([len(table_contents) + 1, float(new_x_value), float(new_y_value)])
            window['-TABLE-'].update(table_contents)
            window['-X-INPUT-'].update('')
            window['-Y-INPUT-'].update('')
            update_graph(table_contents, fig, figure_canvas)

    if event in ('\r', ENTER_KEY_1, ENTER_KEY_2):
        active_element = window.find_element_with_focus()
        if active_element.key == '-X-INPUT-':
            window['-Y-INPUT-'].SetFocus()
        if active_element.key == '-Y-INPUT-':
            window['-SUBMIT-'].Click()
            window['-X-INPUT-'].SetFocus()
        if active_element is not None and active_element.Type == GUI.ELEM_TYPE_BUTTON:  # click if it's a button element
            active_element.Click()
            window['-X-INPUT-'].SetFocus()


window.close()
