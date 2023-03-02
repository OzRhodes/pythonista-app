import ui
import console

@ui.in_background
def button_tapped(sender):
    alert_result = console.alert('Title', 'Message', 'Button 1', 'Button 2')
    sender.title = 'Button ' + str(alert_result)

button = ui.Button(title='Tap me!')
button.action = button_tapped
button.present('sheet')
