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
# General
display_resolution = (800, 480)

theme_font = ('Calibri', 24)
theme_text_color = 'White'
theme_element_color = 'Black'
theme_background_color = '#666666'
theme_justification = 'center'      # left, right, or center
theme_border_width = 2              # in pixels
theme_relief = 'solid'               # raised, sunken, flat, ridge, groove, solid
theme_padding = 2                   # in pixels



# Page Layouts #########################################################################################################
home_layout = [[GUI.Text(
                    text='20mph',                                        # "{} mph".format(IO.speed),
                    auto_size_text=True,
                    relief=theme_relief,
                    font=('Calibri', 64),
                    text_color=theme_text_color,
                    background_color=theme_element_color,
                    border_width=theme_border_width,
                    justification=theme_justification,
                    pad=theme_padding,
                    key='-SPEED-',
                    expand_x=True,
                    expand_y=True,
                    grab=True)]]

home_layout_2 = [[GUI.Text(
                    text='10mi',  # "{} mph".format(IO.speed),
                    auto_size_text=True,
                    relief=theme_relief,
                    font=('Calibri', 36),
                    text_color=theme_text_color,
                    background_color=theme_element_color,
                    border_width=theme_border_width,
                    justification=theme_justification,
                    pad=theme_padding,
                    key='-DISTANCE-TRAVELED-',
                    expand_x=True,
                    expand_y=True,
                    grab=True),

                GUI.Text(
                    text='48V',  # "{} mph".format(IO.speed),
                    auto_size_text=True,
                    relief=theme_relief,
                    font=('Calibri', 36),
                    text_color=theme_text_color,
                    background_color=theme_element_color,
                    border_width=theme_border_width,
                    justification=theme_justification,
                    pad=theme_padding,
                    key='-VOLTAGE-',
                    expand_x=True,
                    expand_y=True,
                    grab=True)],

                [GUI.Text(
                    text='85%',  # "{} mph".format(IO.speed),
                    auto_size_text=True,
                    relief=theme_relief,
                    font=('Calibri', 36),
                    text_color=theme_text_color,
                    background_color=theme_element_color,
                    border_width=theme_border_width,
                    justification=theme_justification,
                    pad=theme_padding,
                    key='-PERCENTAGE-',
                    expand_x=True,
                    expand_y=True,
                    grab=True),

                GUI.Text(
                    text='48A',  # "{} mph".format(IO.speed),
                    auto_size_text=True,
                    relief=theme_relief,
                    font=('Calibri', 36),
                    text_color=theme_text_color,
                    background_color=theme_element_color,
                    border_width=theme_border_width,
                    justification=theme_justification,
                    pad=theme_padding,
                    key='-AMPERAGE-',
                    expand_x=True,
                    expand_y=True,
                    grab=True)]]

home_layout = home_layout + home_layout_2

battery_layout = [[GUI.Text(
                        'Highest Qualfication',
                        size=(15, 1)),
                    GUI.Input(
                        '',
                        key='eQual')]]

motors_layout = [[GUI.Text(
                    'Last Job',
                    size=(10, 1)),
                GUI.Input(
                    '',
                    key='eLastJ')]]

settings_layout = [[GUI.Text(
                        'Last Job',
                        size=(10, 1)),
                    GUI.Input(
                        '',
                        key='eLastJ')]]

# Define Tabs
tab_layout = [[GUI.Tab(
                    'HOME',
                    layout=home_layout,
                    title_color=theme_text_color,
                    background_color=theme_background_color,
                    font=theme_font,
                    pad=theme_padding * 3,
                    border_width=0,
                    key='-HOME-TAB-',
                    expand_x=True,
                    expand_y=True,
                    element_justification=theme_justification),

                GUI.Tab(
                    'BATTERY',
                    layout=battery_layout,
                    title_color=theme_text_color,
                    background_color=theme_background_color,
                    font=theme_font,
                    pad=theme_padding * 3,
                    border_width=0,
                    key='-BATTERY-TAB-',
                    expand_x=True,
                    expand_y=True,
                    element_justification=theme_justification),

                GUI.Tab(
                    'MOTORS',
                    layout=motors_layout,
                    title_color=theme_text_color,
                    background_color=theme_background_color,
                    font=theme_font,
                    pad=theme_padding * 3,
                    border_width=0,
                    key='-MOTORS-TAB-',
                    expand_x=True,
                    expand_y=True,
                    element_justification=theme_justification),

                GUI.Tab(
                    'SETTINGS',
                    layout=settings_layout,
                    title_color=theme_text_color,
                    background_color=theme_background_color,
                    font=theme_font,
                    pad=theme_padding * 3,
                    border_width=0,
                    key='-SETTINGS-TAB-',
                    expand_x=True,
                    expand_y=True,
                    element_justification=theme_justification)]]

window_layout = [[GUI.TabGroup(
                    layout=tab_layout,
                    tab_location='topleft',    #left, right, top, bottom, and combinations
                    title_color=theme_text_color,
                    tab_background_color=theme_background_color,
                    selected_title_color=theme_text_color,
                    selected_background_color='#333333',
                    background_color=theme_element_color,
                    font=theme_font,
                    pad=0,
                    border_width=theme_border_width*3,
                    tab_border_width=theme_border_width*3,
                    key='-TAB-GROUP-',
                    size=display_resolution,
                    expand_x=True,
                    expand_y=True)]]

# Define Window
window = GUI.Window(
                    'HOME',
                    layout=window_layout,
                    default_element_size=None,
                    default_button_element_size=(None, None),
                    auto_size_text=True,
                    auto_size_buttons=True,
                    location=(None, None),
                    size=display_resolution,
                    element_padding=theme_padding,
                    margins=(None, None),
                    button_color=None,
                    font=theme_font,
                    progress_bar_color=(None, None),
                    background_color=theme_element_color,
                    border_depth=None,
                    icon=None,
                    return_keyboard_events=True,
                    use_default_focus=True,
                    text_justification=theme_justification,
                    no_titlebar=False,
                    keep_on_top=None,
                    resizable=True,
                    finalize=True,
                    element_justification = "center",
                    titlebar_background_color = theme_element_color,
                    titlebar_text_color=theme_text_color,
                    titlebar_font=theme_font,
                    titlebar_icon=None,
                    scaling=None)


# Read  values entered by user
event, values = window.read()
# access all the values and if selected add them to a string
window.close()