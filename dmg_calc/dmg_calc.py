import argparse
import csv
import math
import sys
import json

################################################################

LEVEL_MULTIPLIER = {
    "character": [
        17.165605,
        18.535048,
        19.904854,
        21.274903,
        22.6454,
        24.649613,
        26.640643,
        28.868587,
        31.367679,
        34.143343,
        37.201,
        40.66,
        44.446668,
        48.563519,
        53.74848,
        59.081897,
        64.420047,
        69.724455,
        75.123137,
        80.584775,
        86.112028,
        91.703742,
        97.244628,
        102.812644,
        108.409563,
        113.201694,
        118.102906,
        122.979318,
        129.72733,
        136.29291,
        142.67085,
        149.029029,
        155.416987,
        161.825495,
        169.106313,
        176.518077,
        184.072741,
        191.709518,
        199.556908,
        207.382042,
        215.3989,
        224.165667,
        233.50216,
        243.350573,
        256.063067,
        268.543493,
        281.526075,
        295.013648,
        309.067188,
        323.601597,
        336.757542,
        350.530312,
        364.482705,
        378.619181,
        398.600417,
        416.398254,
        434.386996,
        452.951051,
        472.606217,
        492.88489,
        513.568543,
        539.103198,
        565.510563,
        592.538753,
        624.443427,
        651.470148,
        679.49683,
        707.79406,
        736.671422,
        765.640231,
        794.773403,
        824.677397,
        851.157781,
        877.74209,
        914.229123,
        946.746752,
        979.411386,
        1011.223022,
        1044.791746,
        1077.443668,
        1109.99754,
        1142.976615,
        1176.369483,
        1210.184393,
        1253.835659,
        1288.952801,
        1325.484092,
        1363.456928,
        1405.097377,
        1446.853458,
        1488.215547,
        1528.444567,
        1580.367911,
        1630.847528,
        1711.197785,
        1780.453941,
        1847.322809,
        1911.474309,
        1972.864342,
        2030.071808
    ],
    "enemy": [
        17.165605,
        18.535048,
        19.904854,
        21.274903,
        22.6454,
        24.649613,
        26.640643,
        28.868587,
        31.367679,
        34.143343,
        37.201,
        40.66,
        44.446668,
        48.563519,
        53.74848,
        59.081897,
        64.420047,
        69.724455,
        75.123137,
        80.584775,
        86.112028,
        91.703742,
        97.244628,
        102.812644,
        108.409563,
        113.201694,
        118.102906,
        122.979318,
        129.72733,
        136.29291,
        142.67085,
        149.029029,
        155.416987,
        161.825495,
        169.106313,
        176.518077,
        184.072741,
        191.709518,
        199.556908,
        207.382042,
        215.3989,
        224.165667,
        233.50216,
        243.350573,
        256.063067,
        268.543493,
        281.526075,
        295.013648,
        309.067188,
        323.601597,
        336.757542,
        350.530312,
        364.482705,
        378.619181,
        398.600417,
        416.398254,
        434.386996,
        452.566797,
        471.426268,
        490.481663,
        509.50428,
        532.771793,
        556.393323,
        580.103031,
        607.894973,
        630.20133,
        652.866818,
        675.186325,
        697.782682,
        720.170325,
        742.454652,
        765.205477,
        784.374617,
        803.401172,
        830.920776,
        854.403332,
        877.759777,
        900.117232,
        923.766661,
        946.370258,
        968.634183,
        991.029365,
        1013.527108,
        1036.132954,
        1066.623598,
        1089.964198,
        1114.964489,
        1141.662656,
        1171.941798,
        1202.813736,
        1233.939915,
        1264.69967,
        1305.689483,
        1346.084383,
        1411.738173,
        1468.874501,
        1524.041318,
        1576.966305,
        1627.613082,
        1674.809242
    ],
}

REACTION_MULTIPLIER = {
    "pyro melt": 2,
    "cryo melt": 1.5,
    "hydro vape": 2,
    "pyro vape": 1.5,
    "swirl": 0.6,
    "overload": 2,
    "electro-charged": 1.2,
    "superconduct": 0.5,
    "burning": 0.25,
    "spread": 1.25,
    "aggravate": 1.15,
    "bloom": 2,
    "burgeon": 3,
    "hyperbloom": 3,
    "shattered": 1.5,
}

def calc_genshin_dmg(info_filepath):
    with open(info_filepath, 'r') as fr:
        info = json.load(fr)

    CHARACTER_LEVEL    = info["CHARACTER LEVEL"]
    CHARACTER_BASE_ATK = info["CHARACTER BASE ATK"]
    CHARACTER_BASE_DEF = info["CHARACTER BASE DEF"]
    CHARACTER_BASE_HP  = info["CHARACTER BASE HP"]
    WEAPON_BASE_ATK    = info["WEAPON BASE ATK"]

    SKILL_MULTIPLIERS = {
        "atk" : sum(info['SKILL MULTIPLIERS']['ATK']),
        "def" : sum(info['SKILL MULTIPLIERS']['DEF']),
        "hp"  : sum(info['SKILL MULTIPLIERS']['HP']),
    }

    FLAT_HP = sum(info['FLAT HP'])
    FLAT_ATK = sum(info['FLAT ATK'])
    FLAT_DEF = sum(info['FLAT DEF'])
    PERCENT_HP = sum(info['PERCENT HP'])
    PERCENT_ATK = sum(info['PERCENT ATK'])
    PERCENT_DEF = sum(info['PERCENT DEF'])
    ELEMENTAL_MASTERY = sum(info['ELEMENTAL MASTERY'])
    ENERGY_RECHARGE = sum(info['ENERGY RECHARGE'])
    CRIT_RATE = sum(info['CRIT RATE'])
    CRIT_DMG = sum(info['CRIT DMG'])
    PERCENT_DMG_BONUS = sum(info['PERCENT DMG BONUS'])
    ADDITIVE_DMG_BONUS = sum(info['ADDITIVE DMG BONUS'])
    PERCENT_REACTION_BONUS = sum(info['PERCENT REACTION BONUS'])
    BASE_DMG_MULTIPLIER = sum(info['BASE DMG MULTIPLIER'])

    ENEMY_LEVEL = info['ENEMY LEVEL']
    ENEMY_RESISTANCE = info['ENEMY BASE RESISTANCE'] / 100
    ENEMY_RESISTANCE -= sum(info['RESISTANCE DEBUFFS']) / 100

    REACTION_TYPE = info["REACTION TYPE"]

    ################################################################

    artifacts = info["ARTIFACTS"]
    for art in artifacts:
        for stat in artifacts[art]:
            if stat == "HP":
                FLAT_HP += artifacts[art][stat]
            elif stat == "HP %":
                PERCENT_HP += artifacts[art][stat]
            elif stat == "DEF":
                FLAT_DEF += artifacts[art][stat]
            elif stat == "DEF %":
                PERCENT_DEF += artifacts[art][stat]
            elif stat == "ATK":
                FLAT_ATK += artifacts[art][stat]
            elif stat == "ATK %":
                PERCENT_ATK += artifacts[art][stat]
            elif stat == "Energy Recharge":
                ENERGY_RECHARGE += artifacts[art][stat]
            elif stat == "Elemental Mastery":
                ELEMENTAL_MASTERY += artifacts[art][stat]
            elif stat == "Crit Rate":
                CRIT_RATE += artifacts[art][stat]
            elif stat == "Crit DMG":
                CRIT_DMG += artifacts[art][stat]
            elif stat == "% DMG BONUS":
                PERCENT_DMG_BONUS += artifacts[art][stat]

    level_character = CHARACTER_LEVEL
    hp_character = CHARACTER_BASE_HP * (1 + PERCENT_HP/100) + FLAT_HP
    atk_character = (CHARACTER_BASE_ATK + WEAPON_BASE_ATK) * (1 + PERCENT_ATK/100) + FLAT_ATK
    def_character = (CHARACTER_BASE_DEF) * (1 + PERCENT_DEF/100) + FLAT_DEF
    elemental_mastery = ELEMENTAL_MASTERY
    energy_recharge = ENERGY_RECHARGE+100
    crit_rate_character = CRIT_RATE / 100 + 0.05
    crit_dmg_character = CRIT_DMG / 100 + 0.5

    print("HP:", round(hp_character))
    print("ATK:", round(atk_character))
    print("DEF:", round(def_character))
    print("EM:", round(elemental_mastery))
    print("Crit Rate:", round(100*crit_rate_character,1))
    print("Crit DMG:", round(100*crit_dmg_character,1))

    level_multiplier_char = LEVEL_MULTIPLIER["character"][CHARACTER_LEVEL-1]
    #level_multiplier_enemy = LEVEL_MULTIPLIER["enemy"][ENEMY_LEVEL-1]

    additive_dmg_bonus = ADDITIVE_DMG_BONUS
    percent_reaction_bonus = PERCENT_REACTION_BONUS/100
    percent_dmg_bonus = PERCENT_DMG_BONUS/100
    base_dmg_multiplier = BASE_DMG_MULTIPLIER
    if base_dmg_multiplier == 0:
        base_dmg_multiplier = 1

    # there may be multiple stats and skill multipliers involved for dual-scaling characters
    base_dmg = (atk_character * SKILL_MULTIPLIERS['atk']/100)
    base_dmg += (def_character * SKILL_MULTIPLIERS['def']/100)
    base_dmg += (hp_character * SKILL_MULTIPLIERS['hp']/100)
    base_dmg *= base_dmg_multiplier

    if REACTION_TYPE in ("spread", "aggravate"):
        percent_EM_bonus = 5 * elemental_mastery / (elemental_mastery+1200)
        additive_dmg_bonus += (1 + percent_EM_bonus + percent_reaction_bonus) * REACTION_MULTIPLIER[REACTION_TYPE]

    outgoing_dmg = (base_dmg + additive_dmg_bonus) * (1 + percent_dmg_bonus)

    if REACTION_TYPE in ("pyro melt", "cryo melt", "pyro vape", "hydro vape"):
        percent_EM_bonus =  2.78 * elemental_mastery /(elemental_mastery + 1400)
        amplifying_multiplier = (1 + percent_EM_bonus + percent_reaction_bonus) * REACTION_MULTIPLIER[REACTION_TYPE]
        outgoing_dmg *= amplifying_multiplier

    def_enemy = 5 * ENEMY_LEVEL + 500
    def_multiplier = 1 - (def_enemy / (def_enemy + 5 * level_character + 500))

    res_multiplier = 1
    if ENEMY_RESISTANCE < 0:
        res_multiplier = 1 - ENEMY_RESISTANCE/2
    elif ENEMY_RESISTANCE < 0.75 :
        res_multiplier = 1 - ENEMY_RESISTANCE
    else:
        res_multiplier = 1/(4*ENEMY_RESISTANCE+1)

    if REACTION_TYPE in ("swirl", "burning", "superconduct", "electro-charged", "overload"):
        percent_EM_bonus = 1 + 16 * elemental_mastery / (elemental_mastery + 2000)
        outgoing_dmg = REACTION_MULTIPLIER[REACTION_TYPE] * level_multiplier_char (1 + percent_EM_bonus + percent_reaction_bonus) * ENEMY_RESISTANCE
        print("Reaction DMG:", outgoing_dmg)
        sys.exit()

    incoming_dmg = outgoing_dmg * def_multiplier * res_multiplier
    incoming_dmg_crit = incoming_dmg * (1+crit_dmg_character)
    incoming_dmg_avg = incoming_dmg * (1 + crit_dmg_character*crit_rate_character)

    print('-'*10)
    print("Damage (non crit):", round(incoming_dmg))
    print("Damage (crit):", round(incoming_dmg_crit))
    print("Average Damage:", round(incoming_dmg_avg))

    return incoming_dmg, incoming_dmg_crit, incoming_dmg_avg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()
    filepath = args.filepath
    
    dmgs = calc_genshin_dmg(filepath)

if __name__ == "__main__":
    main()
