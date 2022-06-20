# Go Cart HMI ##########################################################################################################
#
# Dominick M. Scialabba, 6/12/22
#
# This program will make a GUI to display relevant statistics and allow a portal for altering settings.


# Libraries ############################################################################################################
import PySimpleGUI as GUI
import matplotlib as MAT
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Code Connections #####################################################################################################
#import IO


# Methods ##############################################################################################################
def vert_data_block(name, data, decimal_places, units):
    data_string = "{data:.{decimal_places}f} {units}"
    data_block_layout = [[GUI.Text(name, expand_x=True, size=(10, 1), font='Calibri 12', background_color='DarkBlue')],
                         [GUI.Text(data_string.format(data=data, decimal_places=decimal_places, units=units), expand_x=True, expand_y=True, font='Calibri 18', size=(10, 1))]]
    return GUI.Column(data_block_layout, expand_x=True, expand_y=True, background_color='Gray', pad=(0, 0))


def big_vert_data_block(name, data, decimal_places, units):
    data_string = "{data:.{decimal_places}f} {units}"
    data_block_layout = [[GUI.Text(name, expand_x=True, size=(10, 1), font='Calibri 12', background_color='DarkBlue')],
                         [GUI.Text(data_string.format(data=data, decimal_places=decimal_places, units=units), expand_x=True, expand_y=True, font='Calibri 24', size=(10, 1))]]
    return GUI.Column(data_block_layout, expand_x=True, expand_y=True, background_color='Gray', pad=(0, 0))


def hor_data_block(name, data, decimal_places, units):
    data_string = "{data:.{decimal_places}f} {units}"
    data_block_layout = [[GUI.Text(name, expand_x=True, expand_y=True, size=(10, 1), font='Calibri 12', background_color='DarkBlue'),
                          GUI.Text(data_string.format(data=data, decimal_places=decimal_places, units=units), expand_x=True, expand_y=True, font='Calibri 18', size=(10, 1))]]
    return GUI.Column(data_block_layout, expand_x=True, expand_y=True, background_color='Gray', pad=(0, 0))


def update_plot_fields():
    return


def update_plot_data():
    return


# Theme Initialization #################################################################################################
display_resolution = (800, 480)
GUI.set_options(text_element_background_color='Black',
                background_color='Black',
                text_justification='center',
                text_color='White',
                font='Calibri 12')


# Layout Initialization ################################################################################################
home_column_layout = [[vert_data_block("Battery Voltage", 47.6, 1, "V"), vert_data_block("Battery Percentage", 92.3, 1, "%")],
                      [vert_data_block("Total Power", 1120, 0, "W"), vert_data_block("Motor #1 Power", 562, 0, "W"), vert_data_block("Motor #2 Power", 558, 0, "W")],
                      [vert_data_block("Total Current", 23.5, 1, "A"), vert_data_block("Motor #1 Current", 11.8, 1, "A"), vert_data_block("Motor #2 Current", 11.7, 1, "A")]]

home_layout = [[big_vert_data_block("Speed", 22.5, 1, "mph"), GUI.Column(home_column_layout, expand_x=True, expand_y=True, background_color='Gray', pad=(0, 0))],
               [vert_data_block("Distance Traveled", 2.32, 2, "mi"), vert_data_block("Range", 6.13, 2, "mi"), vert_data_block("Energy Consumed", 600.1, 1, "W•hr"), vert_data_block("Energy Generated", 52.3, 1, "W•hr")]]

battery_layout = [[vert_data_block("Battery Voltage", 47.6, 1, "V"), vert_data_block("Maximum Battery Voltage", 48.4, 1, "V"), vert_data_block("Minimum Battery Voltage", 46.5, 1, "V")],
                  [vert_data_block("Battery Percentage", 99.2, 1, "%"), vert_data_block("Maximum Battery Percentage", 100.1, 1, "%"), vert_data_block("Minimum Battery Percentage", 96.9, 1, "%")],
                  [vert_data_block("Total Current", 23.5, 1, "A"), vert_data_block("Motor #1 Current", 11.8, 1, "A"), vert_data_block("Motor #2 Current", 11.7, 1, "A")],
                  [vert_data_block("Total Power", 1120, 0, "W"), vert_data_block("Motor #1 Power", 562, 0, "W"), vert_data_block("Motor #2 Power", 558, 0, "W")],
                  [vert_data_block("Total Power Consumed", 600.1, 1, "W•hr"), vert_data_block("Motor #1 Power Consumed", 301.2, 1, "W•hr"), vert_data_block("Motor #2 Power Consumed", 298.9, 1, "W•hr")],
                  [vert_data_block("Total Power Generated", 52.3, 1, "W•hr"), vert_data_block("Motor #1 Power Generated", 26.2, 1, "W•hr"), vert_data_block("Motor #2 Power Generated", 26.1, 1, "W•hr")]]

motors_column_layout_1 = [[GUI.Text('Motor #1', expand_x=True, expand_y=True, size=(20, 1), background_color='DarkBlue', font='Calibri 18')],
                          [hor_data_block("Power", 3001, 0, "W")],
                          [hor_data_block("Current", 3001, 0, "A")],
                          [hor_data_block("RPM", 3001, 0, "RPM")],
                          [hor_data_block("Torque", 3001, 0, "N•m")],
                          [hor_data_block("Motor Temperature", 3001, 0, "°F")],
                          [hor_data_block("ESC Temperature", 3001, 0, "°F")],
                          [hor_data_block("Power Consumed", 3001, 0, "W•hr")],
                          [hor_data_block("Power Generated", 3001, 0, "W•hr")]]

motors_column_layout_2 = [[GUI.Text('Motor #2', expand_x=True, expand_y=True, size=(20, 1), background_color='DarkBlue', font='Calibri 18')],
                          [hor_data_block("Power", 3001, 0, "W")],
                          [hor_data_block("Current", 3001, 0, "A")],
                          [hor_data_block("RPM", 3001, 0, "RPM")],
                          [hor_data_block("Torque", 3001, 0, "N•m")],
                          [hor_data_block("Motor Temperature", 3001, 0, "°F")],
                          [hor_data_block("ESC Temperature", 3001, 0, "°F")],
                          [hor_data_block("Power Consumed", 3001, 0, "W•hr")],
                          [hor_data_block("Power Generated", 3001, 0, "W•hr")]]

motors_layout = [[GUI.Column(motors_column_layout_1, expand_x=True, expand_y=True, background_color='Gray', pad=(0, 0)),
                  GUI.Column(motors_column_layout_2, expand_x=True, expand_y=True, background_color='Gray', pad=(0, 0))]]

plots_layout = [[GUI.Text('SOME INFO', size=(10, 10))]]

settings_layout = [[GUI.Text('SOME INFO', size=(10, 10))]]

tab_layout = [[GUI.Tab('           HOME           ', layout=home_layout, background_color='Gray', expand_x=True),
               GUI.Tab('           BATTERY           ', layout=battery_layout, background_color='Gray', expand_x=True),
               GUI.Tab('           MOTORS           ', layout=motors_layout, background_color='Gray', expand_x=True),
               GUI.Tab('           PLOTS           ', layout=plots_layout, background_color='Gray', expand_x=True),
               GUI.Tab('           SETTINGS           ', layout=settings_layout, background_color='Gray', expand_x=True)]]

window_layout = [[GUI.TabGroup(layout=tab_layout,
                               tab_location='topleft',
                               expand_x=True,
                               expand_y=True,
                               title_color='White',
                               tab_background_color='Black',
                               selected_background_color='Gray',
                               background_color='Black',
                               pad=(10, 10),
                               border_width=2,
                               tab_border_width=2)]]


# Window Initialization ################################################################################################
window = GUI.Window('HOME', layout=window_layout, size=display_resolution)


# Event Loop ###########################################################################################################
while True:
    event, values = window.read()
    print(event, values)
    if event == GUI.WIN_CLOSED or event == 'Exit':
        break

window.close()
