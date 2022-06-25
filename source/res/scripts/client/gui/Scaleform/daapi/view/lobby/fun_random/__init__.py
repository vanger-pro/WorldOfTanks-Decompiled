# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fun_random/__init__.py
from gui.Scaleform.framework import WindowLayer, ScopeTemplates, ViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES

def getContextMenuHandlers():
    pass


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.fun_random.fun_random_prime_time_view import FunRandomPrimeTimeView
    return (ViewSettings(FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME, FunRandomPrimeTimeView, HANGAR_ALIASES.RANKED_PRIME_TIME, WindowLayer.SUB_VIEW, FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME, ScopeTemplates.LOBBY_SUB_SCOPE, True),)


def getBusinessHandlers():
    return (FunRandomPackageBusinessHandler(),)


class FunRandomPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME, self.loadViewByCtxEvent),)
        super(FunRandomPackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
