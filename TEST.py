import PySimpleGUI as sg


def text(text):
    return sg.Text(text, size=(10, 10))


sg.set_options(text_element_background_color='Black')

column_layout = [[text('SOME INFO'), text('SOME INFO')], [text('SOME INFO'), text('SOME INFO')]]

layout = [[sg.Text('SOME INFO', expand_x=True, expand_y=True), sg.Column(column_layout, pad=(0, 0))],
          [text('SOME INFO'), text('SOME INFO'), text('SOME INFO'), text('SOME INFO')]]

window = sg.Window('TEST LAYOUT', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
