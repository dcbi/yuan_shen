import random
import struct

DOMAINS = [
    "boss",
    "Clear Pool and Mountain Cavern",
    "Valley of Remembrance",
    "Domain of Guyun",
    "Midsummer Courtyard",
    "Hidden Palace of Zhou Formula",
    "Peak of Vindagnyr",
    "Ridge Watch",
    "Momiji-Dyed Court",
    "Slumbering Court",
    "The Lost Valley",
    "Spire of Solitary Enlightenment",
    "City of Gold",
    "Molten Iron Fortress",
    "Denouement of Sin",
    "Waterfall Wen",
    "Faded Theater",
    "Sanctum of Rainbow Spirits",
]

PIECE_TYPES = ("flower", "feather", "sands", "goblet", "circlet")
PIECE_NAMES = {
    "flower": "Flower of Life",
    "feather": "Plume of Death",
    "sands": "Sands of Eon",
    "goblet": "Goblet of Enonothem",
    "circlet": "Circlet of Logos",
}

SET_PIECES = {
    "Gladiator's Finale": {
        "flower"  : "Gladiator's Nostalgia",
        "feather" : "Gladiator's Destiny",
        "sands"   : "Gladiator's Longing",
        "goblet"  : "Gladiator's Intoxication",
        "circlet" : "Gladiator's Triumphus",
    },
    "Wanderer's Troupe": {
        "flower"  : "Troupe's Dawnlight",
        "feather" : "Bard's Arrow Feather",
        "sands"   : "Concert's Final Hour",
        "goblet"  : "Wanderer's String-Kettle",
        "circlet" : "Conductor's Top Hat",
    },
    "Noblesse Oblige": {
        "flower"  : "Royal Flora",
        "feather" : "Royal Plume",
        "sands"   : "Royal Pocket Watch",
        "goblet"  : "Royal Silver Urn",
        "circlet" : "Royal Mask",
    },
    "Bloodstained Chivalry": {
        "flower"  : "Bloodstained Flower of Iron",
        "feather" : "Bloodstained Black Plume",
        "sands"   : "Bloodstained Final Hour",
        "goblet"  : "Bloodstained Chevalier's Goblet",
        "circlet" : "Bloodstained Iron Mask",
    },
    "Maiden Beloved": {
        "flower"  : "Maiden's Distant Love",
        "feather" : "Maiden's Heart-Stricken Infatuation",
        "sands"   : "Maiden's Passing Youth",
        "goblet"  : "Maiden's Fleeting Leisure",
        "circlet" : "Maiden's Fading Beauty",
    },
    "Viridescent Venerer": {
        "flower"  : "In Remembrance of Viridescent Fields",
        "feather" : "Viridescent Arrow Feather",
        "sands"   : "Viridescent Venerer's Determination",
        "goblet"  : "Viridescent Venerer's Vessel",
        "circlet" : "Viridescent Venerer's Diadem",
    },
    "Archaic Petra": {
        "flower"  : "Flower of Creviced Cliff",
        "feather" : "Feather of Jagged Peaks",
        "sands"   : "Sundial of Enduring Jade",
        "goblet"  : "Goblet of Chiseled Crag",
        "circlet" : "Mask of Solitude Basalt",
    },
    "Retracing Bolide": {
        "flower"  : "Summer Night's Bloom",
        "feather" : "Summer Night's Finale",
        "sands"   : "Summer Night's Moment",
        "goblet"  : "Summer Night's Waterballoon",
        "circlet" : "Summer Night's Mask",
    },
    "Thundersoother": {
        "flower"  : "Thundersoother's Heart",
        "feather" : "Thundersoother's Plume",
        "sands"   : "Hour of Soothing Thunder",
        "goblet"  : "Thundersoother's Goblet",
        "circlet" : "Thundersoother's Diadem",
    },
    "Thundering Fury": {
        "flower"  : "Thunderbird's Mercy",
        "feather" : "Survivor of Catastrophe",
        "sands"   : "Hourglass of Thunder",
        "goblet"  : "Omen of Thunderstorm",
        "circlet" : "Thunder Summoner's Crown",
    },
    "Lavawalker": {
        "flower"  : "Lavawalker's Resolution",
        "feather" : "Lavawalker's Salvation",
        "sands"   : "Lavawalker's Torment",
        "goblet"  : "Lavawalker's Epiphany",
        "circlet" : "Lavawalker's Wisdom",
    },
    "Crimson Witch of Flames": {
        "flower"  : "Witch's Flower of Blaze",
        "feather" : "Witch's Ever-Burning Plume",
        "sands"   : "Witch's End Time",
        "goblet"  : "Witch's Heart Flames",
        "circlet" : "Witch's Scorching Hat",
    },
    "Blizzard Strayer": {
        "flower"  : "Snowswept Memory",
        "feather" : "Icebreaker's Resolve",
        "sands"   : "Frozen Homeland's Demise",
        "goblet"  : "Frost-Weaved Dignity",
        "circlet" : "Broken Rime's Echo",
    },
    "Heart of Depth": {
        "flower"  : "Gilded Corsage",
        "feather" : "Gust of Nostalgia",
        "sands"   : "Copper Compass",
        "goblet"  : "Goblet of Thundering Deep",
        "circlet" : "Wine-Stained Tricorne",
    },
    "Tenacity of the Millelith": {
        "flower"  : "Flower of Accolades",
        "feather" : "Ceremonial War-Plume",
        "sands"   : "Orichalceous Time-Dial",
        "goblet"  : "Noble's Pledging Vessel",
        "circlet" : "General's Ancient Helm",
    },
    "Pale Flame": {
        "flower"  : "Stainless Bloom",
        "feather" : "Wise Doctor's Pinion",
        "sands"   : "Moment of Cessation",
        "goblet"  : "Surpassing Cup",
        "circlet" : "Mocking Mask",
    },
    "Shimenawa's Reminiscence": {
        "flower"  : "Entangling Bloom",
        "feather" : "Shaft of Remembrance",
        "sands"   : "Morning Dew's Moment",
        "goblet"  : "Hopeful Heart",
        "circlet" : "Capricious Visage",
    },
    "Emblem of Severed Fate": {
        "flower"  : "Magnificent Tsuba",
        "feather" : "Sundered Feather",
        "sands"   : "Storm Cage",
        "goblet"  : "Scarlet Vessel",
        "circlet" : "Ornate Kabuto",
    },
    "Husk of Opulent Dreams": {
        "flower"  : "Bloom Times",
        "feather" : "Plume of Luxury",
        "sands"   : "Song of Life",
        "goblet"  : "Calabash of Awakening",
        "circlet" : "Skeletal Hat",
    },
    "Ocean-Hued Clam": {
        "flower"  : "Sea-Dyed Blossom",
        "feather" : "Deep Palace's Plume",
        "sands"   : "Cowry of Parting",
        "goblet"  : "Pearl Cage",
        "circlet" : "Crown of Watatsumi",
    },
    "Vermillion Hereafter": {
        "flower"  : "Flowering Life",
        "feather" : "Feather of Nascent Light",
        "sands"   : "Solar Relic",
        "goblet"  : "Moment of the Pact",
        "circlet" : "Thundering Poise",
    },
    "Echoes of an Offering": {
        "flower"  : "Soulscent Bloom",
        "feather" : "Jade Leaf",
        "sands"   : "Symbol of Felicitation",
        "goblet"  : "Chalice of the Font",
        "circlet" : "Flowing Rings",
    },
    "Deepwood Memories": {
        "flower"  : "Labyrinth Wayfarer",
        "feather" : "Scholar of Vines",
        "sands"   : "A Time of Insight",
        "goblet"  : "Lamp of the Lost",
        "circlet" : "Laurel Coronet",
    },
    "Gilded Dreams": {
        "flower"  : "Dreaming Steelbloom",
        "feather" : "Feather of Judgement",
        "sands"   : "The Sunken Years",
        "goblet"  : "Honeyed Final Feast",
        "circlet" : "Shadow of the Sand King",
    },
    "Desert Pavillion Chronicle": {
        "flower"  : "The First Day of the City of Kings",
        "feather" : "End of the Golden Realm",
        "sands"   : "Timepiece of the Lost Path",
        "goblet"  : "Defender of the Echanting Dream",
        "circlet" : "Legacy of the Desert High-Born",
    },
    "Flower of Paradise Lost": {
        "flower"  : "Ay-Khanoum's Myriad",
        "feather" : "Wilting Feast",
        "sands"   : "A Moment Congealed",
        "goblet"  : "Secret-Keeper's Magic Bottle",
        "circlet" : "Amethyst Crown",
    },
    "Nymph's Dream": {
        "flower"  : "Odyssean Flower",
        "feather" : "Wicked Mage's Plumule",
        "sands"   : "Nymph's Constancy",
        "goblet"  : "Heroes' Tea Party",
        "circlet" : "Fell Dragon's Monocle",
    },
    "Vorukasha's Glow": {
        "flower"  : "Stamen of Khvarena's Origin",
        "feather" : "Vibrant Pinion",
        "sands"   : "Ancient Abscission",
        "goblet"  : "Feast of Boundless Joy",
        "circlet" : "Heart of Khvarena's Brilliance",
    },
    "Marechaussee Hunter": {
        "flower"  : "Hunter's Brooch",
        "feather" : "Masterpiece's Overture",
        "sands"   : "Moment of Judgement",
        "goblet"  : "Forgotten Vessel",
        "circlet" : "Veteran's Visage",
    },
    "Golden Troupe": {
        "flower"  : "Golden Song's Variation",
        "feather" : "Golden Bird's Shedding",
        "sands"   : "Golden Era's Prelude",
        "goblet"  : "Golden Night's Bustle",
        "circlet" : "Golden Troupe's Reward",
    },
    "Song of Days Past": {
        "flower"  : "Forgotten Oath of Days Past",
        "feather" : "Recollection of Days Past",
        "sands"   : "Echoing Sound From Days Past",
        "goblet"  : "Promised Dream of Days Past",
        "circlet" : "Poetry of Days Past",
    },
    "Nighttime Whispers in the Echoing Woods": {
        "flower"  : "Selfless Floral Accessory",
        "feather" : "Honest Quill",
        "sands"   : "Faithful Hourglass",
        "goblet"  : "Magnanimous Ink Bottle",
        "circlet" : "Compassionate Ladies' Hat",
    },
    "Fragment of Harmonic Whimsy": {
        "flower"  : "Harmonious Symphony Prelude",
        "feather" : "Ancient Sea's Nocturnal Musing",
        "sands"   : "The Grand Jape of the Turning of Fate",
        "goblet"  : "Ichor Shower Rhapsody",
        "circlet" : "Whimsical Dance of the Withered",
    },
    "Unfinished Reverie": {
        "flower"  : "Dark Fruit of Bright Flowers",
        "feather" : "Faded Emerald Tail",
        "sands"   : "Moment of Attainment",
        "goblet"  : "The Wine-Flask Over Which the Plan Was Hatched",
        "circlet" : "Crownless Crown",
    },
    "Scroll of the Hero of Cinder City": {
        "flower"  : "Beast Tamer's Talisman",
        "feather" : "Mountain Ranger's Marker",
        "sands"   : "Mystic's Gold Dial",
        "goblet"  : "Wandering Scholar's Claw Cup",
        "circlet" : "Demon-Warrior's Feather Mask",
    },
    "Obsidian Codex": {
        "flower"  : "Reckoning of the Xenogenic",
        "feather" : "Root of the Spirit-Marrow",
        "sands"   : "Myth's of the Night Realm",
        "goblet"  : "Pre-Banquet of the Contenders",
        "circlet" : "Crown of the Saints",
    },
}

SETS = [
    "Gladiator's Finale",
    "Wanderer's Troupe",
    "Noblesse Oblige",
    "Bloodstained Chivalry",
    "Maiden Beloved",
    "Viridescent Venerer",
    'Archaic Petra',
    'Retracing Bolide',
    'Thudersoother',
    'Thundering Fury',
    'Crimson Witch of Flames',
    "Lavawalker",
    'Blizzard Strayer',
    'Heart of Depth',
    'Tenacity of the Millelith',
    'Pale Flame',
    "Shimenawa's Reminiscence",
    "Emblem of Severed Fate",
    'Husk of Opulent Dreams',
    'Ocean-Hued Clam',
    'Vermillion Hereafter',
    'Echoes of an Offering',
    'Deepwood Memories',
    'Gilded Dreams',
    'Desert Pavillion Chronicle',
    'Flower of Paradise Lost',
    "Nymph's Dream",
    "Vorukasha's Glow",
    'Marechaussee Hunter',
    'Golden Troupe',
    'Song of Days Past',
    'Nighttime Whispers in the Echoing Woods',
    'Fragment of Harmonic Whimsy',
    'Unfinished Reverie',
    'Scroll of the Hero of Cinder City',
    'Obsidian Codex',
]

MAIN_STATS = {
    "sands"   : ("HP %", "ATK %", "DEF %", "Elemental Mastery", "Energy Recharge", ),
    "goblet"  : ("HP %", "ATK %", "DEF %", "Elemental Mastery",
                 "Pyro DMG Bonus", "Hydro DMG Bonus", "Cryo DMG Bonus", "Electro DMG Bonus",
                 "Anemo DMG Bonus", "Geo DMG Bonus", "Dendro DMG Bonus", "Physical DMG Bonus",),
    "circlet" : ("HP %", "ATK %", "DEF %", "Elemental Mastery",
                 "Crit Rate", "Crit DMG", "Healing Bonus"),
}
MAIN_DISTRIBUTION = {
    "sands"   : (0.8/3, 0.8/3, 0.8/3, 0.1, 0.1),
    "goblet"  : (0.1925, 0.1925, 0.19, 0.025,
                 0.05, 0.05, 0.05, 0.05, 
                 0.05, 0.05, 0.05, 0.05
                ),
    "circlet" : (0.22, 0.22, 0.22, 0.04, 0.1, 0.1, 0.1),
}
MAIN_VALUES = {
    "HP": (717, 1530, 2342, 3155, 3967, 4780),
    "ATK": (47, 100, 152, 205, 258, 311),
    "HP %": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "ATK %": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "DEF %": (8.7, 18.6, 28.6, 38.5, 48.4, 58.3),
    "Elemental Mastery": (28, 59.7, 91.4, 123.1, 154.8, 186.5),
    "Energy Recharge": (7.8, 16.6, 25.4, 34.2, 43.0, 51.8),
    "Pyro DMG Bonus": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "Cryo DMG Bonus": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "Hydro DMG Bonus": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "Electro DMG Bonus": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "Anemo DMG Bonus": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "Geo DMG Bonus": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "Dendro DMG Bonus": (7, 14.9, 22.8, 30.8, 38.7, 46.6),
    "Physical DMG Bonus": (8.7, 18.6, 28.6, 38.5, 48.4, 58.3),
    "Crit Rate": (4.7, 9.9, 15.2, 20.5, 25.8, 31.1),
    "Crit DMG": (9.3, 19.9, 30.5, 41.0, 51.6, 62.2),
    "Healing Bonus": (5.4, 11.5, 17.6, 23.7, 29.8, 35.9),
}

SUB_STATS = ("HP", "ATK", "DEF", "HP %", "ATK %", "DEF %", "Elemental Mastery", "Energy Recharge", "Crit Rate", "Crit DMG",)
SUB_WEIGHT = (6,    6,     6,     4,      4,       4,       4,                   4,                 3,           3 )
SUB_VALUES_BASE = {
    "HP": 298.75,
    "ATK": 19.45,
    "DEF": 23.15,
    "HP %": 5.83,
    "ATK %": 5.83,
    "DEF %": 7.29,
    "Elemental Mastery": 23.31,
    "Energy Recharge": 6.48,
    "Crit Rate": 3.89,
    "Crit DMG": 7.77,
}
SUB_VALUES_PERCENTAGE = (1.0, 0.9, 0.8, 0.7)

CUMULATIVE_EXP_REQUIRED = (0, 16300, 44725, 87150, 153300, 270475)

EMOJIS = {
    "flower": ":cherry_blossom:",
    "feather": ":feather:",
    "sands": ":hourglass:",
    "goblet": ":wine_glass:",
    "circlet": ":crown:",
}

def convertArtifactEXP(stars, rank=0):
    base = (1260, 2520, 3780)
    enhanced = CUMULATIVE_EXP_REQUIRED
    exp = base[stars-3] + enhanced[rank]*4/5
    return exp

class Artifact():
    def __init__(self, art_set, piece, main_stat, sub_stats):
        self.rank = 0
        self.art_set = art_set
        self.piece = piece
        self.main_stat = main_stat
        self.sub_stats = sub_stats
        self.main_value = 0
        self.sub_values = []
        self.history = []
        self.generateValues()

    def generateValues(self):
        self.main_value = MAIN_VALUES[self.main_stat][0]
        for idx,stat in enumerate(self.sub_stats):
            upidx = random.choice((0,1,2,3))
            self.sub_values.append(SUB_VALUES_BASE[stat]*SUB_VALUES_PERCENTAGE[upidx])
            self.history.append((idx,upidx))

    def upgrade(self, exp_in=float('inf')):
        if self.rank == 5:
            return False
        exp_required = CUMULATIVE_EXP_REQUIRED[rank+1] - CUMULATIVE_EXP_REQUIRED[rank]
        if exp_in < exp_required:
            return False
        self.rank += 1
        self.main_value = MAIN_VALUES[self.main_stat][self.rank]
        if len(self.sub_stats) < 4:
            possible_substats = list(SUB_STATS)
            weights = list(SUB_WEIGHT)
            if self.main_stat in possible_substats:
                idx = possible_substats.index(main_stat)
                possible_substats.pop(idx)
                weights.pop(idx)
            for st in self.sub_stats:
                idx = possible_substats.index(st)
                possible_substats.pop(idx)
                weights.pop(idx)
            new_sub = random.choices(possible_substats, weights)[0]
            upidx = random.choice((0,1,2,3))
            new_sub_val = SUB_VALUES_BASE[new_sub] * SUB_VALUES_PERCENTAGE[upidx]
            self.sub_stats.append(new_sub)
            self.sub_values.append(new_sub_val)
            self.history.append((3,upidx))
        else:
            statidx = random.choice((0,1,2,3))
            upidx = random.choice((0,1,2,3))
            self.sub_values[statidx] += SUB_VALUES_BASE[self.sub_stats[statidx]]*SUB_VALUES_PERCENTAGE[upidx]
            self.history.append((statidx,upidx))
        return True

    @staticmethod
    def generateStats(piece, strongbox=False):
        if piece == "flower":
            main_stat = "HP"
        elif piece == "feather":
            main_stat = "ATK"
        else:
            main_stat = random.choices(MAIN_STATS[piece], MAIN_DISTRIBUTION[piece])[0]
    
        possible_substats = list(SUB_STATS)
        weights = list(SUB_WEIGHT)
    
        if main_stat in possible_substats:
            idx = possible_substats.index(main_stat)
            possible_substats.pop(idx)
            weights.pop(idx)
    
        if strongbox:
            n_subs = random.choices((3,4), (66,34))[0]
        else:
            n_subs = random.choices((3,4), (8,2))[0]

        sub_stats = []
        new_sub = None
        for jk in range(n_subs):
            if not new_sub is None:
                idx = possible_substats.index(new_sub)
                possible_substats.pop(idx)
                weights.pop(idx)
            new_sub = random.choices(possible_substats, weights)[0]
            sub_stats.append(new_sub)
        return main_stat, sub_stats

    @classmethod
    def generateTemplate(cls, strongbox=False):
        piece = random.choice(("flower", "feather", "sands", "goblet", "circlet"))
        main_stat, sub_stats = cls.generateStats(piece, strongbox)
        return piece, main_stat, sub_stats

    def __str__(self):
        set_piece_name = SET_PIECES[self.art_set][self.piece]
        piece_name = PIECE_NAMES[self.piece]
        s = f"**{self.art_set}**\n*{piece_name}:* {set_piece_name}\n"
        pct = '%' in self.main_stat or "bonus" in self.main_stat or self.main_stat in ("Energy Recharge", "Crit Rate", "Crit DMG")
        s += self.main_stat.replace(' %', '')
        s += '    ' + str(self.main_value)*(not pct) + str(round(self.main_value, 1))*pct + ' %'*pct
        for idx,stat in enumerate(self.sub_stats):
            pct = '%' in stat or stat in ("Energy Recharge", "Crit Rate", "Crit DMG")
            if pct: val = str(round(self.sub_values[idx], 1))
            else: val = str(int(round(self.sub_values[idx], 0)))
            s += '\n> ' + stat.replace(' %', '') + '+' + val + '%'*pct
        return s

    @classmethod
    def decompress(cls, bstr):
        ints = struct.unpack("<BBbbbbb", bstr[:7])
        art_set_idx = ints[0]
        piece_idx = ints[1] & 15
        rank_idx = (ints[1] & 240)>>4
        main_stat_idx = ints[2]
        substat_idxs = ints[3:]
        if substat_idxs[-1] == -1:
            substat_idxs.pop(-1)

        hist_ints = struct.unpack("<9B", bstr[7:])
        history = []
        for hi in hist_ints:
            line_idx = hi & 15
            val_idx = (hi & 240)>>4
            if stat_idx < 4:
                history.append( ( stat_idx , val_idx ) )

        piece = PIECE_TYPES[piece_idx]
        if piece_idx==0:
            main_stat = "HP"
        elif piece_idx==1:
            main_stat = "ATK"
        else:
            main_stat = MAIN_STATS[piece][main_stat_idx]
        sub_stats = [SUB_STATS[i] for i in substat_idxs]
        new_art = cls(SETS[art_set_idx], piece, main_stat, sub_stats)
        new_art.rank = rank_idx
        new_art.main_value = MAIN_VALUES[piece][rank_idx]
        new_art.history.clear()
        new_art.history = history
        new_art.sub_values = [0]*len(sub_stats)
        for h in history:
            new_art.sub_values[h[0]] += SUB_VALUES_BASE[new_art.sub_stats[h[0]]]*SUB_VALUES_PERCENTAGE[h[1]]
        return new_art

    def compress(self):
        psls = ('flower', 'feather', 'sands', 'goblet', 'circlet')
        p = psls.index(self.piece)

        cbs = struct.pack('<B', SETS.index(self.art_set)) 
        cbs += struct.pack('<B', p + (self.rank<<4))

        if p==0 or p==1:
            m = int(-1)
        else:
            m = int(MAIN_STATS[self.piece].index(self.main_stat))
        cbs += struct.pack('<b', m)

        for k in range(len(self.sub_stats)):
            cbs += struct.pack('<b', SUB_STATS.index(self.sub_stats[k]))

        if len(self.sub_stats) < 4:
            cbs += struct.pack('<b', -1)

        for h in self.history:
            cbs += struct.pack('<B', h[0] + (h[1]<<4) )

        if len(self.history) < 9:
            cbs += struct.pack('<B', 15)

def collectDomainArtifacts(domain=None):
    if domain is None:
        domain = random.choice(DOMAINS)
    idx = DOMAINS.index(domain)

    N = random.choices((1,2), (0.935, 0.065))[0]
    artifacts = []
    fodder4 = 2 + random.choices((0,1), (0.515,0.485))[0]
    fodder3 = 3 + random.choices((0,1), (0.45,0.55))[0]
    exp = convertArtifactEXP(3)*fodder3 + convertArtifactEXP(4)*fodder4
    for i in range(N):
        art_set = random.choice(SETS[idx*2:2*idx+2])
        piece, main_stat, sub_stats = Artifact.generateTemplate()
        artifacts.append(Artifact(art_set, piece, main_stat, sub_stats))
    return artifacts, exp

def collectStrongboxArtifacts(art_set, N):
    artifacts = []
    for i in range(N):
        piece, main_stat, sub_stats = Artifact.generateTemplate(strongbox=True)
        artifacts.append(Artifact(art_set, piece, main_stat, sub_stats))
    return artifacts
