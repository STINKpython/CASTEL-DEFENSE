from configuraciones import *
from UI.gui_widget import Widget


class Unity(Widget):
    def __init__(self, master, pos, id):
        super().__init__(
            master_form=master,
            pos=pos,
            size=SIZE_FRAME_UNITY,
            color_border=GOLD4,
            image_bg=PATHS_UNITIES[id]
        )
