# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewBottomPanelTradeInMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewBottomPanelTradeInMeta(BaseDAAPIComponent):

    def onBuyClick(self):
        self._printOverrideError('onBuyClick')

    def as_setDataS(self, data):
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None
