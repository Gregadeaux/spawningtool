BO_EXCLUDED = set([
    'MULE',
    'ReaperPlaceholder',
    'Interceptor'
    'AutoTurret',
    'PointDefenseDrone',
    'Mothership',
    'Baneling',
    'Locust',
    'Changeling',
    'InfestedTerran',
    'Overseer',
    'BroodLord',
    'Broodling',
    'Larva',
    'Creep Tumor'
    ])

BUILD_TIMES = {
        'SCV': 17,
        'Marine': 25,
        'Marauder': 30,
        'Reaper': 40,
        'Ghost': 40,
        'Hellion': 30,
        'Hellbat': 30,
        'WidowMine': 40,
        'SiegeTank': 45,
        'Thor': 60,
        'Viking': 42,
        'Medivac': 42,
        'Raven': 60,
        'Banshee': 60,
        'Battlecruiser': 90,
        'Probe': 17,
        'Zealot': 38,
        'Stalker': 42,
        'Sentry': 37,
        'MothershipCore': 30,
        'HighTemplar': 55,
        'DarkTemplar': 55,
        'Immortal': 55,
        'Colossus': 75,
        # 'Archon': ,
        'Observer': 30,
        'WarpPrism': 50,
        'Phoenix': 35,
        'VoidRay': 60,
        'Oracle': 50,
        'Tempest': 60,
        'Carrier': 120,
        'Drone': 17,
        'Queen': 50,
        'Zergling': 24,
        'Roach': 27,
        'Hydralisk': 33,
        'SwarmHost': 40,
        'Infestor': 50,
        'Ultralisk': 55,
        'NydusWorm': 20,
        'Overlord': 25,
        'Mutalisk': 33,
        'Corruptor': 40,
        'Viper': 40,
        # research
        'zerglingmovementspeed': 110,
        'GlialReconstitution': 110,
        'WarpGateResearch': 160,
        'BlinkTech': 170,
        'Stimpack': 170,
        'PunisherGrenades': 60,
        'ShieldWall': 110,  # ? Combat Shield?
        'TerranInfantryWeaponsLevel1': 160,
        'TerranInfantryWeaponsLevel2': 190,
        'TerranInfantryWeaponsLevel3': 220,
        'TerranInfantryArmorsLevel1': 160,
        'TerranInfantryArmorsLevel2': 190,
        'TerranInfantryArmorsLevel3': 220,
        }

for key, value in BUILD_TIMES.iteritems():
    BUILD_TIMES[key] = value * 16

