import System.Windows.Forms as WinForms

from ..container import Container
from .base import Widget


class Frame(Widget, Container):
    def create(self):
        self.native = WinForms.GroupBox()
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
