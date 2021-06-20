from bokeh.models import Paragraph, TextInput, PreText, Select
from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.core.properties import String


class CowsayPreText(PreText):
    __javascript__ = ["extensions/static/js/cowsay_lib.js"]
    __implementation__ = "cowsay.ts"

    cow_type = String("DEFAULT")

class CowsaySelect(Select):
    __javascript__ = ["extensions/static/js/cowsay_lib.js"]
    __implementation__ = "cowsay_select.ts"

cowsay = CowsayPreText(
    text="",
    cow_type="DEFAULT"
)
cow_input = TextInput()
select = CowsaySelect()

def on_cow_input_changed(attr, old, new):
    cowsay.text = new

def on_select_changed(attr, old, new):
    cowsay.cow_type = new

cow_input.on_change("value_input", on_cow_input_changed)
select.on_change("value", on_select_changed)

curdoc().add_root(column(cowsay, cow_input, select))