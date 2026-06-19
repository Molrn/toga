from decimal import ROUND_DOWN

import System.Windows.Forms as WinForms

from ..container import Container
from .base import Widget

_FRAME_PADDING = 3


class Frame(Widget, Container):
    def create(self):
        self.native = WinForms.GroupBox()
        self.native.Padding = WinForms.Padding(_FRAME_PADDING)
        Container.__init__(self, self.native)

    def get_title(self):
        return self.native.Text

    def set_title(self, value):
        self.native.Text = value

    def set_font(self, font):
        super().set_font(font)
        # Rectangle in which the content can be displayed
        # varies according to the title font
        self.native_content.Location = self.native.DisplayRectangle.Location

    def set_bounds(self, x, y, width, height):
        super().set_bounds(x, y, width, height)
        padding = 2 * _FRAME_PADDING
        display_y = self.native.DisplayRectangle.Y
        self.resize_content(
            self.scale_in(width - padding, ROUND_DOWN),
            self.scale_in(height - padding - display_y, ROUND_DOWN),
        )
