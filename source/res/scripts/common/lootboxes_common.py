# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/lootboxes_common.py
from constants import LOOTBOX_TOKEN_PREFIX
from soft_exception import SoftException

def makeLootboxTokenID(boxID):
    return LOOTBOX_TOKEN_PREFIX + str(boxID)


def makeLootboxID(tokenName):
    try:
        if tokenName.startswith(LOOTBOX_TOKEN_PREFIX):
            strID = tokenName[len(LOOTBOX_TOKEN_PREFIX):]
            return int(strID)
    except Exception:
        pass

    raise SoftException('Invalid tokenName: {}'.format(tokenName))


def isLootboxToken(tokenName):
    try:
        makeLootboxID(tokenName)
        return True
    except Exception:
        return False
