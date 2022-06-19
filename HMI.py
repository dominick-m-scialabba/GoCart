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

# Theme Initialization #################################################################################################
display_resolution = (800, 480)
GUI.set_options(text_element_background_color='Black',
                background_color='Black',
                text_justification='center',
                text_color='White')


# Layout Initialization ################################################################################################
column_layout = [[GUI.Text('SOME INFO', expand_x=True, expand_y=True), GUI.Text('SOME INFO', expand_x=True, expand_y=True)],
                 [GUI.Text('SOME INFO', expand_x=True, expand_y=True), GUI.Text('SOME INFO', expand_x=True, expand_y=True)]]
home_layout = [[GUI.Text('SOME INFO', expand_x=True, expand_y=True), GUI.Column(column_layout, expand_x=True, expand_y=True, background_color='Gray', pad=(0, 0))],
               [GUI.Text('SOME INFO', expand_x=True, expand_y=True), GUI.Text('SOME INFO', expand_x=True, expand_y=True), GUI.Text('SOME INFO', expand_x=True, expand_y=True), GUI.Text('SOME INFO', expand_x=True, expand_y=True)]]
battery_layout = [[GUI.Text('SOME INFO', size=(10, 10))]]

motors_layout = [[GUI.Text('SOME INFO', size=(10, 10))]]

settings_layout = [[GUI.Text('SOME INFO', size=(10, 10))]]

# Define Tabs
tab_layout = [[GUI.Tab('          HOME          ', layout=home_layout, background_color='Gray', expand_x=True),
               GUI.Tab('          BATTERY          ', layout=battery_layout, background_color='Gray', expand_x=True),
               GUI.Tab('          MOTORS          ', layout=motors_layout, background_color='Gray', expand_x=True),
               GUI.Tab('          SETTINGS          ', layout=settings_layout, background_color='Gray', expand_x=True)]]

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

# Define Window ########################################################################################################
window = GUI.Window('HOME', layout=window_layout, size=display_resolution)

# Event Loop ###########################################################################################################
while True:
    event, values = window.read()
    print(event, values)
    if event == GUI.WIN_CLOSED or event == 'Exit':
        break

window.close()