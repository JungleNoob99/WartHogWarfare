from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Unit:
    name: str
    type: str  # BATTLESHIP, INFANTRY, ARTILLERY, TANK, SUBMARINE, etc.
    param1: str
    param2: str
    param3: str
    is_naval: bool  # true for major naval units

# =============================================
# Main data - UNIT_BLUEPRINTS
# =============================================
UNIT_BLUEPRINTS: Dict[str, Dict[str, List[Unit]]] = {
    "BRT": {
        "WW1": [
            Unit("HMS Dreadnought", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Tommy Infantry", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("QF 13-Pounder", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Mark 1 Tank", "TANK", "HEAVY", "MEDIUM", "HEAVY", False)
        ],
        "Interwar": [
            Unit("Ironclad", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Vanguard", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Ordnance QF 2-Pounder", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Matilda A11", "TANK", "HEAVY", "MEDIUM", "HEAVY", False)
        ],
        "Early WW2": [
            Unit("HMS Hood", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Home Guard", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("25-Pounder Gun", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Matilda II", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Late WW2": [
            Unit("HMS Ark Royal", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Commandos", "INFANTRY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("BL 5.5-inch Gun", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Churchill Tank", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("HMS Vanguard", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Paratroopers", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("25-Pounder Mk2", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("Centurion Mk3", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("HMS Eagle", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Royal Marines", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("FV433 Abbot", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Centurion Mk5", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("HMS Invincible", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("SAS", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("MLRS M270", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Challenger 1", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("HMS Illustrious", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Royal Marines Commando", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("AS90", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Challenger 2", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("HMS Queen Elizabeth", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("SAS Modern", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("M270A2 MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Challenger 3", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "GER": {
        "WW1": [
            Unit("SMS Bayern", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Stormtrooper", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Big Bertha", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("A7V", "TANK", "HEAVY", "MEDIUM", "HEAVY", False)
        ],
        "Interwar": [
            Unit("Deutschland", "LIGHT_DESTROYER", "", "HEAVY", "HEAVY", True),
            Unit("Reichswehr Infantry", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", False),
            Unit("10.5 cm leFH 18", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("Panzer I", "TANK", "MEDIUM", "LIGHT", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("Type VII U-boat", "SUBMARINE", "", "HEAVY", "HEAVY", True),
            Unit("Fallschirmjäger", "INFANTRY", "MEDIUM", "LIGHT", "HEAVY", False),
            Unit("88mm Pak 36", "ARTILLERY", "HEAVY", "MEDIUM", "SUPER_HEAVY", False),
            Unit("Panzer III", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Late WW2": [
            Unit("Bismarck", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Waffen-SS", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Nebelwerfer 41", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Tiger II", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("Type XXI U-boat", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Bundeswehr Infantry", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("Rheinmetall 105mm", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("M48 Patton", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("Brandenburg-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Fallschirmjäger", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("M109", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Leopard 1", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Type 206 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("KSK", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("PzH 2000", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Leopard 2A4", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Sachsen-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Bundeswehr Jaeger", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("PzH 2000", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Leopard 2A5", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Type 212 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("KSK Special Forces", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("PzH 2000 NG", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Leopard 2A7", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "ITA": {
        "WW1": [
            Unit("Dante Alighieri", "BATTLESHIP", "", "HEAVY", "HEAVY", True),
            Unit("Arditi", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Cannone 149/13", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Fiat 2000", "TANK", "HEAVY", "MEDIUM", "HEAVY", False)
        ],
        "Interwar": [
            Unit("Conte di Cavour", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Bersaglieri", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Obice 75/18", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("CV-33 Tankette", "TANK", "LIGHT", "LIGHT", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("Scire Submarine", "SUBMARINE", "", "HEAVY", "HEAVY", True),
            Unit("Alpini", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("Cannone 47/32", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("M13/40", "TANK", "MEDIUM", "MEDIUM", "HEAVY", False)
        ],
        "Late WW2": [
            Unit("Aquila Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Decima Flottiglia", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Obice 210/22", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("P26/40", "TANK", "HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("Giuseppe Garibaldi", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Lagunari", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Obice 155/23", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("M47 Patton", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("Andrea Doria Cruiser", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Paracadutisti", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("M109 Italian", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Leopard 1", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Maestrale-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("9th Parachute Assault", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("FH-70", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Ariete", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Horizon-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Lagunari San Marco", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("FH-70 Modern", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Ariete PSO", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Trieste LHD", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Special Forces", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("VCA 155 PALM", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Ariete AMV", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "FRA": {
        "WW1": [
            Unit("Courbet", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Poilu", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Canon de 155 C", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Renault FT", "TANK", "LIGHT", "LIGHT", "MEDIUM", False)
        ],
        "Interwar": [
            Unit("Bretagne", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Chasseurs Alpins", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", False),
            Unit("Canon de 105 mle 1913", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("Char D1", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("Surcouf Submarine", "SUBMARINE", "", "HEAVY", "HEAVY", True),
            Unit("Senegalese Tirailleurs", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("Canon de 75", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Somua S35", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Late WW2": [
            Unit("Richelieu", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Free French Commandos", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Obusier de 6 pouces", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("M4 Sherman", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("Arromanches Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Paras", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("TRF1 155mm", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("AMX-13", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("La Fayette", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Légion Étrangère", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("AU F1", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("AMX-30", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Rubis-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("11th Parachute Brigade", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("TRF1", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Leclerc", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Charles de Gaulle", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Commandos Marine", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("CAESAR", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Leclerc Tropic", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Suffren-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("13th RDP", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("CAESAR NG", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Leclerc XLR", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "RUS": {
        "WW1": [
            Unit("Gangut", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Imperial Guard", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Obusier de 305", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Russky Renault", "TANK", "LIGHT", "LIGHT", "LIGHT", False)
        ],
        "Interwar": [
            Unit("Parizhskaya Kommuna", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Red Army Infantry", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", False),
            Unit("76mm M1902", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("MS-1 T-18", "TANK", "LIGHT", "LIGHT", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("Shchuka Sub", "SUBMARINE", "", "HEAVY", "HEAVY", True),
            Unit("Siberian Riflemen", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("ZiS-3", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("T-34/76", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Late WW2": [
            Unit("Kirov", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Naval Infantry", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("BM-13 Katyusha", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("IS-2", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("Kuznetsov Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("VDV Paratroopers", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("D-30", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("T-55", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("K-19 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Spetsnaz", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("2S1 Gvozdika", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("T-62", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Akula-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("VDV Modern", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("2S19 Msta", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("T-80", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Admiral Kuznetsov", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Spetsnaz GRU", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("2S35 Koalitsiya", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("T-90", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Yasen-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("VDV Elite", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Tornado-G", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("T-14 Armata", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "USA": {
        "WW1": [
            Unit("USS New York", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Doughboy", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("75mm M1917", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Ford 3-Ton", "TANK", "MEDIUM", "LIGHT", "MEDIUM", False)
        ],
        "Interwar": [
            Unit("USS Texas", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("National Guard", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", False),
            Unit("M1 75mm", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("Christie M1931", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("Yorktown Carrier", "AIRCRAFT_CARRIER", "", "HEAVY", "HEAVY", True),
            Unit("Marines", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("M2A1 105mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("M3 Stuart", "TANK", "MEDIUM", "MEDIUM", "HEAVY", False)
        ],
        "Late WW2": [
            Unit("USS Iowa", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("101st Airborne", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("M1 155mm", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("M4 Sherman", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("USS Midway", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Rangers", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("M114", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("M48 Patton", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("USS Forrestal", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Green Berets", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("M109", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("M60", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Los Angeles-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Delta Force", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("M270 MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("M1 Abrams", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Nimitz-class", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("SEAL Team 6", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("M109A6", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("M1A1 Abrams", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Virginia-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("MARSOC Raiders", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("HIMARS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("M1A2 Abrams SEPv3", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "CHN": {
        "WW1": [
            Unit("Yukiang", "BATTLESHIP", "", "LIGHT", "HEAVY", True),
            Unit("Beiyang Army", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Krupp 75mm", "ARTILLERY", "LIGHT", "LIGHT", "MEDIUM", False),
            Unit("None", "TANK", "LIGHT", "LIGHT", "LIGHT", False)
        ],
        "Interwar": [
            Unit("Ning Hai", "LIGHT_DESTROYER", "", "LIGHT", "MEDIUM", True),
            Unit("Warlord Soldiers", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Type 41 75mm", "ARTILLERY", "LIGHT", "LIGHT", "MEDIUM", False),
            Unit("Vickers 6-Ton", "TANK", "LIGHT", "LIGHT", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("Type 035 Sub", "SUBMARINE", "", "MEDIUM", "MEDIUM", True),
            Unit("Guerrilla Fighters", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Type 59-1", "ARTILLERY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("Type 97 Chi-Ha", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", False)
        ],
        "Late WW2": [
            Unit("Chao Ho", "BATTLESHIP", "", "MEDIUM", "HEAVY", True),
            Unit("PLA Infantry", "INFANTRY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("Type 45 105mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("T-34 Captured", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("Type 01 Sub", "SUBMARINE", "", "HEAVY", "HEAVY", True),
            Unit("PLA Marines", "INFANTRY", "MEDIUM", "MEDIUM", "MEDIUM", False),
            Unit("Type 59", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Type 58", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("Type 033 Sub", "SUBMARINE", "", "HEAVY", "HEAVY", True),
            Unit("PLA Airborne", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Type 66", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("Type 59", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Type 035G Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Special Forces", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("PLZ-05", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Type 80", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Type 039 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("PLA Snow Wolf", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("PLZ-05A", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Type 96", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Type 093 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("PLASOF", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("PCL-181", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Type 99A", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "JPN": {
        "WW1": [
            Unit("Fuso", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Imperial Army", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Type 38 75mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Type 97 Te-Ke", "TANK", "LIGHT", "LIGHT", "LIGHT", False)
        ],
        "Interwar": [
            Unit("Nagato", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("IJA Infantry", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", False),
            Unit("Type 90 75mm", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", False),
            Unit("Type 89 I-Go", "TANK", "LIGHT", "LIGHT", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("I-400 Sub", "SUBMARINE", "", "HEAVY", "HEAVY", True),
            Unit("SNLF Marines", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("Type 92 70mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Type 95 Ha-Go", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", False)
        ],
        "Late WW2": [
            Unit("Yamato", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Kamikaze Pilots", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Type 4 15cm", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Type 97 Chi-Ha", "TANK", "HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("IJN Remnants", "LIGHT_DESTROYER", "", "HEAVY", "HEAVY", True),
            Unit("JSDF Infantry", "INFANTRY", "MEDIUM", "MEDIUM", "MEDIUM", False),
            Unit("Type 74", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Type 61", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("Oyashio Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("JGSDF Rangers", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("Type 99", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Type 74", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Harushio-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Special Forces Group", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Type 19", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Type 90", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Soryu-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Amphibious Rapid Deployment", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Type 19 155mm", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Type 10", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Taigei-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("JGSDF Elite", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Type 12 Rocket", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Type 10 Kai", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    },
    "DEF": {
        "WW1": [
            Unit("Dreadnought", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Rifleman", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Field Gun", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Early Tank", "TANK", "HEAVY", "MEDIUM", "HEAVY", False)
        ],
        "Interwar": [
            Unit("Battleship", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", True),
            Unit("Infantryman", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", False),
            Unit("Howitzer", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Light Tank", "TANK", "MEDIUM", "LIGHT", "MEDIUM", False)
        ],
        "Early WW2": [
            Unit("Destroyer", "LIGHT_DESTROYER", "", "HEAVY", "HEAVY", True),
            Unit("Regular Infantry", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", False),
            Unit("Anti-Tank Gun", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Medium Tank", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
        ],
        "Late WW2": [
            Unit("Aircraft Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Veteran Infantry", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Heavy Artillery", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Heavy Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Cold Transitions": [
            Unit("Submarine", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Mechanized Infantry", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", False),
            Unit("Self-Propelled Gun", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("Main Battle Tank", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False)
        ],
        "Early ColdWar": [
            Unit("Destroyer Escort", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Elite Infantry", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", False),
            Unit("Rocket Artillery", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("Advanced Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Late Coldwar": [
            Unit("Attack Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Special Forces", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", False),
            Unit("MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Super Heavy Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Transition Modern": [
            Unit("Modern Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Commando", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Precision Artillery", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Next-Gen Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ],
        "Modern": [
            Unit("Stealth Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", True),
            Unit("Tier 1 Operators", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Hypersonic MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False),
            Unit("Future MBT", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", False)
        ]
    }
}

# Helper function
def get_units(nation: str, era: str) -> Optional[List[Unit]]:
    """Get units for a specific nation and era."""
    nation_data = UNIT_BLUEPRINTS.get(nation)
    if nation_data is None:
        return None
    return nation_data.get(era)
