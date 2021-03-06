# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/ArenaInfoAbilityNotifier.py
import functools
import BigWorld
import CGF
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from items import vehicles
import GenericComponents
from skeletons.gui.battle_session import IBattleSessionProvider

class ArenaInfoAbilityNotifier(BigWorld.DynamicScriptComponent, CallbackDelayer):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        CallbackDelayer.__init__(self)

    def onLeaveWorld(self, *args):
        self.destroy()

    def notifyLaunchPosition(self, equipmentId, position, launchTime, duration):
        delay = launchTime - BigWorld.serverTime()
        equipment = vehicles.g_cache.equipments()[equipmentId]
        self.__showGuiMarker(equipment, position, delay)
        self.delayCallback(delay, functools.partial(self.__launch, equipment, position, duration))

    def __showGuiMarker(self, equipment, position, delay):
        ctrl = self.__guiSessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.showMarker(equipment, position, (0, 0, 0), delay)
        return

    def __launch(self, equipment, position, duration):

        def postloadSetup(go):
            go.addComponent(equipment)
            go.createComponent(GenericComponents.RemoveGoDelayedComponent, duration)

        CGF.loadGameObject(equipment.usagePrefab, self.entity.spaceID, position, postloadSetup)
