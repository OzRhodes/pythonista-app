import ui

def button_tapped(sender):
	sender.title = 'Hello'

ui.load_view('UI_Basics-1a').present('sheet')
