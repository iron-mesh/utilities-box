

widgets=[]

def register_widget(widget):
    global widgets
    widgets.append(type(widget)())