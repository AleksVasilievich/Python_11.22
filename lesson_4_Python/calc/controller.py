import model
import view

def dutton_click():
    a = view.get_value()
    b = view.get_value()
    model.init(a, b)
    result = model.sum()
    view.view_data(result)
