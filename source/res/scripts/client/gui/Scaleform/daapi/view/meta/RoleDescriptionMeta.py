# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RoleDescriptionMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RoleDescriptionMeta(BaseDAAPIComponent):

    def as_setDataS(self, data):
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

    def as_setVisibleS(self, isVisible):
        return self.flashObject.as_setVisible(isVisible) if self._isDAAPIInited() else None
