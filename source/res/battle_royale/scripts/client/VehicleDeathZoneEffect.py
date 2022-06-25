# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleDeathZoneEffect.py
import BigWorld
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from death_zones_helpers import ZONE_STATE
from constants import DEATH_ZONES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE, DeathZoneTimerViewState
from battle_royale.gui.battle_control.battle_constants import BrTimerViewState
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleDeathZoneEffect(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _onAvatarReady(self):
        self.set_state()

    def set_state(self, _=None):
        leftTime, endTime = self.timeout()
        value = DeathZoneTimerViewState(DEATH_ZONES.STATIC, False, leftTime, BrTimerViewState.fromZone(self.state), endTime)
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.DEATHZONE_TIMER, value)

    def timeout(self):
        return (max(self.damageTime - BigWorld.serverTime(), 0.0), self.damageTime) if self.state == ZONE_STATE.CRITICAL else (0.0, 0.0)

    def onDamaged(self):
        value = DeathZoneTimerViewState(DEATH_ZONES.STATIC, True, -1.0, None, -1.0)
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.DEATHZONE_TIMER, value)
        return
