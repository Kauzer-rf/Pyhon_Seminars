# Связующее звено между model и view

import model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.sum()
    view.view_data(result)

# Умножение
# import model_mult as model
# import view

# def button_click():
#     value_a = view.get_value()
#     value_b = view.get_value()
#     model.init(value_a, value_b)
#     result = model.mult()
#     view.view_data(result)
