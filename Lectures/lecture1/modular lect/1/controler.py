import lect3
import view

def button_click():
    value_a=view.get_value()
    value_b=view.get_value()
    lect3.init(value_a,value_b)
    result=lect3.summa()
    view.view(result)