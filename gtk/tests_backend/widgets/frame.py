from toga_gtk.libs import Gtk

from .base import SimpleProbe


class FrameProbe(SimpleProbe):
    native_class = Gtk.Frame
