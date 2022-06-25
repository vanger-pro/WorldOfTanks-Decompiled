# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/arena_bonus_type_caps.py
from constants import ARENA_BONUS_TYPE, ARENA_BONUS_TYPE_NAMES, IS_EDITOR
from debug_utils import LOG_ERROR
from soft_exception import SoftException
from BonusCaps import BonusCapsConfig

class ARENA_BONUS_TYPE_CAPS():
    RESULTS = 'RESULTS'
    DAMAGE_VEHICLE = 'DAMAGE_VEHICLE'
    CREDITS = 'CREDITS'
    XP = 'XP'
    RANSOM_IN = 'RANSOM_IN'
    REWARD_FOR_ACHIEVEMENT = 'REWARD_FOR_ACHIEVEMENT'
    QUESTS = 'QUESTS'
    AVATAR_QUESTS = 'AVATAR_QUESTS'
    DOSSIER_TOTAL = 'DOSSIER_TOTAL'
    DOSSIER_KILL_LIST = 'DOSSIER_KILL_LIST'
    DOSSIER_15X15 = 'DOSSIER_15X15'
    DOSSIER_7X7 = 'DOSSIER_7X7'
    DOSSIER_CLAN = 'DOSSIER_CLAN'
    DOSSIER_ACHIEVEMENTS_15X15 = 'DOSSIER_ACHIEVEMENTS_15X15'
    DOSSIER_MARKS_ON_GUN = 'DOSSIER_MARKS_ON_GUN'
    DOSSIER_MARK_OF_MASTERY = 'DOSSIER_MARK_OF_MASTERY'
    DOSSIER_ACHIEVEMENTS_RANKED15X15 = 'DOSSIER_ACHIEVEMENTS_RANKED15X15'
    DOSSIER_ACHIEVEMENTS_7X7 = 'DOSSIER_ACHIEVEMENTS_7X7'
    DOSSIER_MAX15X15 = 'DOSSIER_MAX15X15'
    DOSSIER_MAX7X7 = 'DOSSIER_MAX7X7'
    RANKED = 'RANKED'
    DOSSIER_RANKED = 'DOSSIER_RANKED'
    DOSSIER_MAXRANKED = 'DOSSIER_MAXRANKED'
    CYBERSPORT_RATING = 'CYBERSPORT_RATING'
    TKILL_RATING = 'TKILL_RATING'
    DOSSIER_SORTIE = 'DOSSIER_SORTIE'
    DOSSIER_MAXSORTIE = 'DOSSIER_MAXSORTIE'
    DOSSIER_ACHIEVEMENTS_SORTIE = 'DOSSIER_ACHIEVEMENTS_SORTIE'
    DOSSIER_FORT_BATTLE = 'DOSSIER_FORT_BATTLE'
    DOSSIER_MAXFORTBATTLE = 'DOSSIER_MAXFORTBATTLE'
    REF_SYSTEM_BONUS = 'REF_SYSTEM_BONUS'
    DOSSIER_RATED7X7 = 'DOSSIER_RATED7X7'
    DOSSIER_MAXRATED7X7 = 'DOSSIER_MAXRATED7X7'
    DOSSIER_ACHIEVEMENTS_RATED7X7 = 'DOSSIER_ACHIEVEMENTS_RATED7X7'
    RESPAWN = 'RESPAWN'
    INTERACTIVE_STATS = 'INTERACTIVE_STATS'
    FLAG_MECHANICS = 'FLAG_MECHANICS'
    WIN_POINTS_MECHANICS = 'WIN_POINTS_MECHANICS'
    REPAIR_MECHANICS = 'REPAIR_MECHANICS'
    NO_ALLY_DAMAGE = 'NO_ALLY_DAMAGE'
    DAILY_MULTIPLIED_XP = 'DAILY_MULTIPLIED_XP'
    MULTITEAMS = 'MULTITEAMS'
    DOSSIER_GLOBAL_MAP = 'DOSSIER_GLOBAL_MAP'
    RAGE_MECHANICS = 'RAGE_MECHANICS'
    RESOURCE_POINTS = 'RESOURCE_POINTS'
    RANSOM_OUT = 'RANSOM_OUT'
    RENT_BATTLES_COUNTED = 'RENT_BATTLES_COUNTED'
    DOSSIER_FALLOUT = 'DOSSIER_FALLOUT'
    DOSSIER_MAXFALLOUT = 'DOSSIER_MAXFALLOUT'
    CREW_IMMUNE_TO_DAMAGE = 'CREW_IMMUNE_TO_DAMAGE'
    BOOSTERS = 'BOOSTERS'
    DOSSIER_ACHIEVEMENTS_FALLOUT = 'DOSSIER_ACHIEVEMENTS_FALLOUT'
    SQUADS = 'SQUADS'
    SQUAD_XP = 'SQUAD_XP'
    SQUAD_CREDITS = 'SQUAD_CREDITS'
    PREM_SQUAD_CREDITS = 'PREM_SQUAD_CREDITS'
    COMMON_CHAT = 'COMMON_CHAT'
    CREDITS_FACTOR_BOOTCAMP = 'CREDITS_FACTOR_BOOTCAMP'
    XP_FACTOR_BOOTCAMP = 'XP_FACTOR_BOOTCAMP'
    INFINITE_AMMO = 'INFINITE_AMMO'
    FREE_AMMO = 'FREE_AMMO'
    TEAM_HEALTH_BAR = 'TEAM_HEALTH_BAR'
    DOSSIER_30X30 = 'DOSSIER_30X30'
    DOSSIER_MAX30X30 = 'DOSSIER_MAX30X30'
    ACHIEVEMENT_CONDITIONS_EXT = 'ACHIEVEMENT_CONDITIONS_EXT'
    VICTORY_DEFEAT_MESSAGE = 'VICTORY_DEFEAT_MESSAGE'
    BOOTCAMP_MECHANICS = 'BOOTCAMP_MECHANICS'
    EPIC = 'EPIC'
    BATTLEROYALE = 'BATTLEROYALE'
    LOOT = 'LOOT'
    LOOT_DROP = 'LOOT_DROP'
    CONE_VISIBILITY = 'CONE_VISIBILITY'
    RADAR = 'RADAR'
    DEATH_ZONES = 'DEATH_ZONES'
    SPAWN_KEY_POINTS = 'SPAWN_KEY_POINTS'
    SECTOR_MECHANICS = 'SECTOR_MECHANICS'
    PROTECTION_ZONE = 'PROTECTION_ZONE'
    DESTRUCTIBLE_ENTITIES = 'DESTRUCTIBLE_ENTITIES'
    STEP_REPAIR_MECHANIC = 'STEP_REPAIR_MECHANIC'
    PLAYER_RANK_MECHANICS = 'PLAYER_RANK_MECHANICS'
    RECOVERY_MECHANIC = 'RECOVERY_MECHANIC'
    OVERTIME_MECHANIC = 'OVERTIME_MECHANIC'
    DOSSIER_EPIC_BATTLE = 'DOSSIER_EPIC_BATTLE'
    DOSSIER_MAX_EPIC_BATTLE = 'DOSSIER_MAX_EPIC_BATTLE'
    DOSSIER_ACHIEVEMENTS_EPIC_BATTLE = 'DOSSIER_ACHIEVEMENTS_EPIC_BATTLE'
    DETAILED_XP = 'DETAILED_XP'
    NO_REMOVE_RENTED_STYLE = 'NO_REMOVE_RENTED_STYLE'
    SUPPORT_AI = 'SUPPORT_AI'
    FORCE_AI = 'FORCE_AI'
    ROLE_SYSTEM = 'ROLE_SYSTEM'
    IN_BATTLE_XP = 'IN_BATTLE_XP'
    REFSYSTEM_20_BONUS = 'REFSYSTEM_20_BONUS'
    ADDITIONAL_XP_POSTBATTLE = 'ADDITIONAL_XP_POSTBATTLE'
    FREE_BATTLE_RESOURCES = 'FREE_BATTLE_RESOURCES'
    ALLY_STUN_PENALTY = 'ALLY_STUN_PENALTY'
    ALLY_STUN_TEAM_KILL = 'ALLY_STUN_TEAM_KILL'
    CUSTOM_ALLY_DAMAGE_EFFECT = 'CUSTOM_ALLY_DAMAGE_EFFECT'
    ALLY_TEAM_KILL = 'ALLY_TEAM_KILL'
    VEHICLE_NO_DAMAGE_FROM_STATICS = 'VEHICLE_NO_DAMAGE_FROM_STATICS'
    META = 'META'
    ALL_TRACERS_VISIBLE = 'ALL_TRACERS_VISIBLE'
    IN_BATTLE_UPGRADES = 'IN_BATTLE_UPGRADES'
    ARENA_INFO = 'ARENA_INFO'
    ANONYMIZER = 'ANONYMIZER'
    CUSTOMIZATION_PROGRESSION = 'CUSTOMIZATION_PROGRESSION'
    VEHICLES_SPAWN_LIST_STORAGE = 'VEHICLES_SPAWN_LIST_STORAGE'
    VEHICLE_REMOVAL = 'VEHICLE_REMOVAL'
    SAFE_TO_LEAVE = 'SAFE_TO_LEAVE'
    DOG_TAG = 'DOG_TAG'
    DISABLE_VISUAL_SCRIPT = 'DISABLE_VISUAL_SCRIPT'
    SPAM_PROTECTION = 'SPAM_PROTECTION'
    TRIGGERS = 'TRIGGERS'
    EXTERNAL_WINNER_PROCESSOR = 'EXTERNAL_WINNER_PROCESSOR'
    VEHICLES_AREA_MARKER = 'VEHICLES_AREA_MARKER'
    DEATHZONES = 'DEATHZONES'
    HEALTH_BROADCAST = 'HEALTH_BROADCAST'
    VISION_OVERRIDE = 'VISION_OVERRIDE'
    BATTLE_NOTIFIER = 'BATTLE_NOTIFIER'
    MATCHMAKER_STATS = 'MATCHMAKER_STATS'
    OBSERVER_SEES_ALL = 'OBSERVER_SEES_ALL'
    BECOME_AN_OBSERVER_AFTER_DEATH = 'BECOME_AN_OBSERVER_AFTER_DEATH'
    FOLLOW_WINNER = 'FOLLOW_WINNER'
    EXTENDED_SPG_MECHANICS = 'EXTENDED_SPG_MECHANICS'
    TEAMS_INFO = 'TEAMS_INFO'
    MAPBOX = 'MAPBOX'
    ARENA_COMMANDS = 'ARENA_COMMANDS'
    LASER_SIGHT = 'LASER_SIGHT'
    NO_ART_PREPARATION = 'NO_ART_PREPARATION'
    NO_PREBATTLE_MARKERS = 'NO_PREBATTLE_MARKERS'
    NO_RECONNECT = 'NO_RECONNECT'
    FORCE_DROWN = 'FORCE_DROWN'
    VPP_MODIFICATIONS = 'VPP_MODIFICATIONS'
    SWITCH_SETUPS = 'SWITCH_SETUPS'
    LOG_ALL_VEHICLES = 'LOG_ALL_VEHICLES'
    SSR = 'SSR'
    SSR_FORCE_RECORD = 'SSR_FORCE_RECORD'
    RTS_COMPONENT = 'RTS_COMPONENT'
    DOSSIER_ACHIEVEMENTS = frozenset((DOSSIER_ACHIEVEMENTS_15X15,
     DOSSIER_ACHIEVEMENTS_RANKED15X15,
     DOSSIER_ACHIEVEMENTS_7X7,
     DOSSIER_ACHIEVEMENTS_RATED7X7,
     DOSSIER_ACHIEVEMENTS_SORTIE,
     DOSSIER_ACHIEVEMENTS_EPIC_BATTLE))
    __RULES = (lambda caps: not set(ARENA_BONUS_TYPE_CAPS.DOSSIER_ACHIEVEMENTS) & set(caps) or ARENA_BONUS_TYPE_CAPS.MULTITEAMS not in caps,
     lambda caps: not set(ARENA_BONUS_TYPE_CAPS.DOSSIER_ACHIEVEMENTS) & set(caps) or ARENA_BONUS_TYPE_CAPS.RESPAWN not in caps or ARENA_BONUS_TYPE_CAPS.DOSSIER_ACHIEVEMENTS_EPIC_BATTLE in caps,
     lambda caps: ARENA_BONUS_TYPE_CAPS.CYBERSPORT_RATING not in caps or ARENA_BONUS_TYPE_CAPS.MULTITEAMS not in caps,
     lambda caps: ARENA_BONUS_TYPE_CAPS.WIN_POINTS_MECHANICS not in caps or ARENA_BONUS_TYPE_CAPS.INTERACTIVE_STATS in caps,
     lambda caps: (ARENA_BONUS_TYPE_CAPS.QUESTS in caps) != (ARENA_BONUS_TYPE_CAPS.AVATAR_QUESTS in caps) or ARENA_BONUS_TYPE_CAPS.QUESTS not in caps)
    _typeToCaps = {}
    OVERRIDE_BONUS_CAPS = None

    @staticmethod
    def init():
        if not ARENA_BONUS_TYPE_CAPS._typeToCaps:
            import bonus_caps_config
            ARENA_BONUS_TYPE_CAPS._typeToCaps = bonus_caps_config.readConfig()
        else:
            LOG_ERROR('re-init ARENA_BONUS_TYPE_CAPS')

    @staticmethod
    def check():
        for capsID in ARENA_BONUS_TYPE_CAPS._typeToCaps.iterkeys():
            for rule in ARENA_BONUS_TYPE_CAPS.__RULES:
                if not rule(ARENA_BONUS_TYPE_CAPS.get(capsID)):
                    raise SoftException('Caps is invalid for ARENA_BONUS_TYPE={}'.format(capsID))

    @staticmethod
    def get(arenaBonusType, **kwargs):
        overrideCaps = kwargs.get('specificOverrides', ARENA_BONUS_TYPE_CAPS.OVERRIDE_BONUS_CAPS)
        bonusCapsConfig = BonusCapsConfig(overrideCaps)
        bonusCaps = ARENA_BONUS_TYPE_CAPS._typeToCaps.get(arenaBonusType, frozenset())
        return bonusCapsConfig.getModifiedBonusCaps(arenaBonusType, bonusCaps)

    @staticmethod
    def checkAny(arenaBonusType, *args, **kwargs):
        caps = ARENA_BONUS_TYPE_CAPS.get(arenaBonusType, **kwargs)
        for cap in args:
            if isinstance(cap, str):
                if cap in caps:
                    return True
            if isinstance(cap, (set, frozenset)):
                if len(cap & caps) > 0:
                    return True

        return False

    @staticmethod
    def checkAll(arenaBonusType, *args, **kwargs):
        caps = ARENA_BONUS_TYPE_CAPS.get(arenaBonusType, **kwargs)
        for cap in args:
            if isinstance(cap, str):
                if cap not in caps:
                    return False
            if isinstance(cap, (set, frozenset)):
                if len(cap & caps) != len(cap):
                    return False
            return False

        return True


def parseArenaBonusType(parsedBonusTypes, bonusTypes, arenaBonusTypeCap):
    for k in bonusTypes:
        arenaBonusType = ARENA_BONUS_TYPE_NAMES[k]
        if not ARENA_BONUS_TYPE_CAPS.checkAny(arenaBonusType, arenaBonusTypeCap):
            raise SoftException('Wrong arena bonus type: %s is not enabled for %s' % (arenaBonusTypeCap, k))
        parsedBonusTypes.add(arenaBonusType)


def init():
    ARENA_BONUS_TYPE_CAPS.init()


ALLOWED_ARENA_BONUS_TYPE_CAPS = frozenset([ v for k, v in ARENA_BONUS_TYPE_CAPS.__dict__.iteritems() if not k.startswith('__') and isinstance(v, str) ])
if IS_EDITOR:
    init()