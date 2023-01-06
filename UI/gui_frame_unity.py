from configuraciones import *
from UI.gui_widget import Widget


class FrameUnity(Widget):
    def __init__(self, master, pos, size):
        super().__init__(
            master_form=master,
            pos=pos,
            size=size,
            color_border=DORADO,
            image_bg=PATH_FRAME_UNIT_IMAGE
        )
