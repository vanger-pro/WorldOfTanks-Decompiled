# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MapsTrainingIngameHelpWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class MapsTrainingIngameHelpWindowMeta(AbstractWindowView):

    def clickSettingWindow(self):
        self._printOverrideError('clickSettingWindow')

    def as_setDataS(self, data):
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None
