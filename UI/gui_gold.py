from configuraciones import *
from UI.gui_widget import Widget


class Gold(Widget):
    def __init__(self, master, pos, size):
        self.gold = 0
        super().__init__(
            master_form=master,
            pos=pos,
            size=size,
            text="{0}".format(self.gold),
            font="IMPACT",
            font_size=SIZE_FONT_GOLD,
            font_color=WHITE
        )
