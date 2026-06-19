import System.Windows.Forms

from .base import SimpleProbe


class FrameProbe(SimpleProbe):
    native_class = System.Windows.Forms.GroupBox
