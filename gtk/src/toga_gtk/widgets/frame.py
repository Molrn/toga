from ..libs import GTK_VERSION, Gtk
from .base import Widget

_FRAME_PADDING = 3


class Frame(Widget):
    def create(self):
        self.native = Gtk.Frame()
        if GTK_VERSION < (4, 0, 0):
            # pragma: no-cover-if-gtk4
            self.native.label.set_line_wrap(False)
        else:  # pragma: no-cover-if-gtk3
            self.native.label.set_wrap(False)

    def get_title(self):
        return self.native.label.get_text()

    def set_title(self, value):
        self.native.label.set_text(value)
