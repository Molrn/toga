from ..container import TogaContainer
from ..libs import Gtk
from .base import Widget

_FRAME_PADDING = 3


class Frame(Widget):
    def create(self):
        self.native = Gtk.Frame()
        self.sub_container = TogaContainer()
        self.native.add(self.sub_container)

    def get_title(self):
        return self.native.get_label()

    def set_title(self, value):
        self.native.set_label(value)

    def set_content(self, widget):
        self.sub_container.content = widget
