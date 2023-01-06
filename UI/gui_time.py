from configuraciones import *
from UI.gui_widget import Widget


class Time(Widget):
    def __init__(self, master):
        self.game_time = 0
        super().__init__(
            master_form=master,
            pos=POS_TIME,
            size=SIZE_TIME,
            text="{0}".format(self.game_time),
            font="IMPACT",
            font_size=SIZE_FONT_TIME,
            font_color=WHITE
        )
