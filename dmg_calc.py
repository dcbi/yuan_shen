import csv
import math
import sys

################################################################

#### EXAMPLE:
# Ganyu
# Aqua Simulacra
# 4pc Shimenawa
# melt team with Xiangling, Bennett, Zhongli
# melt team with Xiangling, Xilonen, Zhongli

CHARACTER_LEVEL = 90
CHARACTER_BASE_ATK = 334.85
CHARACTER_BASE_DEF = 630.21
CHARACTER_BASE_HP = 9796.73
WEAPON_BASE_ATK = 542

# for ATK, DEF, HP;
# put 0 if ability does not scale with those stats, otherwise this accounts for dual-scaling characters
SKILL_MULTIPLIERS = {
    "atk": 392, #Ganyu charged shot bloom abiliy multiplier
    "def": 0,
    "hp": 0,
}

# ARTIFACTS
 
FLOWER = {
    "HP": 4780,
    "ATK %": 10.5,
    "Energy Recharge": 5.8,
    "Crit Rate": 9.7,
    "Crit DMG": 12.4,
}
FEATHER = {
    "ATK": 311,
    "HP": 209,
    "ATK %": 4.1,
    "Crit Rate": 10.9,
    "Crit DMG": 19.4,
}
SANDS = {
    "ATK %": 46.6,
    "HP": 269,
    "DEF %": 12.4,
    "Crit Rate": 14.4,
    "Crit DMG": 6.2,
}
GOBLET = {
    "% DMG BONUS": 46.6,
    "ATK": 58,
    "ATK %": 10.5,
    "Crit Rate": 6.2,
    "Crit DMG": 5.4,
}
CIRCLET = {
    "Crit Rate": 31.1,
    "DEF": 32,
    "ATK %": 9.9,
    "Energy Recharge": 5.2,
    "Crit DMG": 21.8,
}

# include:
# ascenion stats
# weapon sub-stat and passive
# talents
# talents (teammates)
# artifact set effects
# artifact set effects (teammates)
# constellations
# constellations (teammates)
# team elemental resonance
FLAT_HP = [
]
FLAT_ATK = [
    1.12*(608+191), # lvl 90 bennett & skyward blade, burst lvl 12
]
FLAT_DEF = [
]
PERCENT_HP = [
    16, # aqua simulacra R1
]
PERCENT_ATK = [
    18, # shimenawa 2pc set bonus
    25, # pyro resonance
    20, # noblesse 4pc set bonus
]
PERCENT_DEF = [
]
ELEMENTAL_MASTERY = [
    0,
]
ENERGY_RECHARGE = [
]
CRIT_RATE = [
    20, # ganyu A4 passive talent
]
# do NOT include the base 50% crit damage
CRIT_DMG = [
    38.4, # character ascenion
    88.2, # aqua simulacra
]
PERCENT_DMG_BONUS = [
    20, # aqua simulacra R1
    46.6, # goblet main (goblet)
    50, # shimenawa 4pc bonus
    35, # archaic petra 4pc bonus
    #15, # geo resonance
    #40, # hero of cinder city 4pc bonus w/ xilonen
]
ADDITIVE_DMG_BONUS = [
]
# do NOT include the base 5% crit rate
PERCENT_REACTION_BONUS = [
]
BASE_DMG_MULTIPLIER = [
]

ENEMY_LEVEL = 100
ENEMY_RESISTANCE = 0.1 
ENEMY_RESISTANCE -= 0.15 # Ganyu C1
ENEMY_RESISTANCE -= 0.20 # Zhongli shield
#ENEMY_RESISTANCE -= 0.33 # Xilonen skill level 9

REACTION_TYPE = "cryo melt"
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


LEVEL_MULTIPLIER = {"character": [], "enemy":[]}
with open("genshin_level_multiplier.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        LEVEL_MULTIPLIER["character"].append(float(row[2]))
        LEVEL_MULTIPLIER["enemy"].append(float(row[1]))


################################################################

artifacts = (FLOWER, FEATHER, SANDS, GOBLET, CIRCLET)
for art in artifacts:
    for stat in art:
        if stat == "HP":
            FLAT_HP.append(art[stat]),
        elif stat == "HP %":
            PERCENT_HP.append(art[stat]),
        elif stat == "DEF":
            FLAT_DEF.append(art[stat]),
        elif stat == "DEF %":
            PERCENT_DEF.append(art[stat]),
        elif stat == "ATK":
            FLAT_ATK.append(art[stat]),
        elif stat == "ATK %":
            PERCENT_ATK.append(art[stat]),
        elif stat == "Energy Recharge":
            ENERGY_RECHARGE.append(art[stat]),
        elif stat == "Elemental Mastery":
            ELEMENTAL_MASTERY.append(art[stat]),
        elif stat == "Crit Rate":
            CRIT_RATE.append(art[stat]),
        elif stat == "Crit DMG":
            CRIT_DMG.append(art[stat]),

level_character = CHARACTER_LEVEL
hp_character = CHARACTER_BASE_HP * (1 + sum(PERCENT_HP)/100) + sum(FLAT_HP)
atk_character = (CHARACTER_BASE_ATK + WEAPON_BASE_ATK) * (1 + sum(PERCENT_ATK)/100) + sum(FLAT_ATK)
def_character = (CHARACTER_BASE_DEF) * (1 + sum(PERCENT_DEF)/100) + sum(FLAT_DEF)
elemental_mastery = sum(ELEMENTAL_MASTERY)
energy_recharge = (sum(ENERGY_RECHARGE)+100)
crit_rate_character = sum(CRIT_RATE) / 100 + 0.05
crit_dmg_character = sum(CRIT_DMG) / 100 + 0.5

print("HP:", round(hp_character))
print("ATK:", round(atk_character))
print("DEF:", round(def_character))
print("EM:", round(elemental_mastery))
print("Crit Rate:", round(100*crit_rate_character,1))
print("Crit DMG:", round(100*crit_dmg_character,1))

level_multiplier_char = LEVEL_MULTIPLIER["character"][CHARACTER_LEVEL-1]
#level_multiplier_enemy = LEVEL_MULTIPLIER["enemy"][ENEMY_LEVEL-1]

additive_dmg_bonus = sum(ADDITIVE_DMG_BONUS)
percent_reaction_bonus = sum(PERCENT_REACTION_BONUS)/100
percent_dmg_bonus = sum(PERCENT_DMG_BONUS)/100
base_dmg_multiplier = sum(BASE_DMG_MULTIPLIER)
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
