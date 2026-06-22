
#include <vector>
#include <string>
#include <map>

struct Unit {
    std::string name;
    std::string type;        // BATTLESHIP, INFANTRY, ARTILLERY, TANK, SUBMARINE, etc.
    std::string param1;      
    std::string param2;
    std::string param3;
    bool isNaval;            // true for major naval units

    Unit(std::string n, std::string t, std::string p1,
         std::string p2, std::string p3, bool naval)
        : name(std::move(n)), type(std::move(t)),
          param1(std::move(p1)), param2(std::move(p2)), param3(std::move(p3)),
          isNaval(naval) {}
};

using EraBlueprints = std::map<std::string, std::vector<Unit>>;
using NationBlueprints = std::map<std::string, EraBlueprints>;

// =============================================
// Main data - UNIT_BLUEPRINTS
// =============================================
const NationBlueprints UNIT_BLUEPRINTS = {
    {"BRT", {
        {"WW1", {
            Unit("HMS Dreadnought", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Tommy Infantry", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("QF 13-Pounder", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Mark 1 Tank", "TANK", "HEAVY", "MEDIUM", "HEAVY", false)
        }},
        {"Interwar", {
            Unit("Ironclad", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Vanguard", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Ordnance QF 2-Pounder", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Matilda A11", "TANK", "HEAVY", "MEDIUM", "HEAVY", false)
        }},
        {"Early WW2", {
            Unit("HMS Hood", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Home Guard", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("25-Pounder Gun", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Matilda II", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Late WW2", {
            Unit("HMS Ark Royal", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Commandos", "INFANTRY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("BL 5.5-inch Gun", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Churchill Tank", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("HMS Vanguard", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Paratroopers", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("25-Pounder Mk2", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("Centurion Mk3", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("HMS Eagle", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Royal Marines", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("FV433 Abbot", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Centurion Mk5", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("HMS Invincible", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("SAS", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("MLRS M270", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Challenger 1", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("HMS Illustrious", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Royal Marines Commando", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("AS90", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Challenger 2", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("HMS Queen Elizabeth", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("SAS Modern", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("M270A2 MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Challenger 3", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"GER", {
        {"WW1", {
            Unit("SMS Bayern", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Stormtrooper", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Big Bertha", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("A7V", "TANK", "HEAVY", "MEDIUM", "HEAVY", false)
        }},
        {"Interwar", {
            Unit("Deutschland", "LIGHT_DESTROYER", "", "HEAVY", "HEAVY", true),
            Unit("Reichswehr Infantry", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", false),
            Unit("10.5 cm leFH 18", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("Panzer I", "TANK", "MEDIUM", "LIGHT", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("Type VII U-boat", "SUBMARINE", "", "HEAVY", "HEAVY", true),
            Unit("Fallschirmjäger", "INFANTRY", "MEDIUM", "LIGHT", "HEAVY", false),
            Unit("88mm Pak 36", "ARTILLERY", "HEAVY", "MEDIUM", "SUPER_HEAVY", false),
            Unit("Panzer III", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Late WW2", {
            Unit("Bismarck", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Waffen-SS", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Nebelwerfer 41", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Tiger II", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("Type XXI U-boat", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Bundeswehr Infantry", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("Rheinmetall 105mm", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("M48 Patton", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("Brandenburg-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Fallschirmjäger", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("M109", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Leopard 1", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Type 206 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("KSK", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("PzH 2000", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Leopard 2A4", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Sachsen-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Bundeswehr Jaeger", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("PzH 2000", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Leopard 2A5", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Type 212 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("KSK Special Forces", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("PzH 2000 NG", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Leopard 2A7", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"ITA", {
        {"WW1", {
            Unit("Dante Alighieri", "BATTLESHIP", "", "HEAVY", "HEAVY", true),
            Unit("Arditi", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Cannone 149/13", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Fiat 2000", "TANK", "HEAVY", "MEDIUM", "HEAVY", false)
        }},
        {"Interwar", {
            Unit("Conte di Cavour", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Bersaglieri", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Obice 75/18", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("CV-33 Tankette", "TANK", "LIGHT", "LIGHT", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("Scire Submarine", "SUBMARINE", "", "HEAVY", "HEAVY", true),
            Unit("Alpini", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("Cannone 47/32", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("M13/40", "TANK", "MEDIUM", "MEDIUM", "HEAVY", false)
        }},
        {"Late WW2", {
            Unit("Aquila Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Decima Flottiglia", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Obice 210/22", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("P26/40", "TANK", "HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("Giuseppe Garibaldi", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Lagunari", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Obice 155/23", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("M47 Patton", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("Andrea Doria Cruiser", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Paracadutisti", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("M109 Italian", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Leopard 1", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Maestrale-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("9th Parachute Assault", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("FH-70", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Ariete", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Horizon-class", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Lagunari San Marco", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("FH-70 Modern", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Ariete PSO", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Trieste LHD", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Special Forces", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("VCA 155 PALM", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Ariete AMV", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"FRA", {
        {"WW1", {
            Unit("Courbet", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Poilu", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Canon de 155 C", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Renault FT", "TANK", "LIGHT", "LIGHT", "MEDIUM", false)
        }},
        {"Interwar", {
            Unit("Bretagne", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Chasseurs Alpins", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", false),
            Unit("Canon de 105 mle 1913", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("Char D1", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("Surcouf Submarine", "SUBMARINE", "", "HEAVY", "HEAVY", true),
            Unit("Senegalese Tirailleurs", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("Canon de 75", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Somua S35", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Late WW2", {
            Unit("Richelieu", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Free French Commandos", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Obusier de 6 pouces", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("M4 Sherman", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("Arromanches Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Paras", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("TRF1 155mm", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("AMX-13", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("La Fayette", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Légion Étrangère", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("AU F1", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("AMX-30", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Rubis-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("11th Parachute Brigade", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("TRF1", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Leclerc", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Charles de Gaulle", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Commandos Marine", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("CAESAR", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Leclerc Tropic", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Suffren-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("13th RDP", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("CAESAR NG", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Leclerc XLR", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"RUS", {
        {"WW1", {
            Unit("Gangut", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Imperial Guard", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Obusier de 305", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Russky Renault", "TANK", "LIGHT", "LIGHT", "LIGHT", false)
        }},
        {"Interwar", {
            Unit("Parizhskaya Kommuna", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Red Army Infantry", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", false),
            Unit("76mm M1902", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("MS-1 T-18", "TANK", "LIGHT", "LIGHT", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("Shchuka Sub", "SUBMARINE", "", "HEAVY", "HEAVY", true),
            Unit("Siberian Riflemen", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("ZiS-3", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("T-34/76", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Late WW2", {
            Unit("Kirov", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Naval Infantry", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("BM-13 Katyusha", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("IS-2", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("Kuznetsov Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("VDV Paratroopers", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("D-30", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("T-55", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("K-19 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Spetsnaz", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("2S1 Gvozdika", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("T-62", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Akula-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("VDV Modern", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("2S19 Msta", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("T-80", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Admiral Kuznetsov", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Spetsnaz GRU", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("2S35 Koalitsiya", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("T-90", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Yasen-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("VDV Elite", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Tornado-G", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("T-14 Armata", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"USA", {
        {"WW1", {
            Unit("USS New York", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Doughboy", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("75mm M1917", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Ford 3-Ton", "TANK", "MEDIUM", "LIGHT", "MEDIUM", false)
        }},
        {"Interwar", {
            Unit("USS Texas", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("National Guard", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", false),
            Unit("M1 75mm", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("Christie M1931", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("Yorktown Carrier", "AIRCRAFT_CARRIER", "", "HEAVY", "HEAVY", true),
            Unit("Marines", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("M2A1 105mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("M3 Stuart", "TANK", "MEDIUM", "MEDIUM", "HEAVY", false)
        }},
        {"Late WW2", {
            Unit("USS Iowa", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("101st Airborne", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("M1 155mm", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("M4 Sherman", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("USS Midway", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Rangers", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("M114", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("M48 Patton", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("USS Forrestal", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Green Berets", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("M109", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("M60", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Los Angeles-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Delta Force", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("M270 MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("M1 Abrams", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Nimitz-class", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("SEAL Team 6", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("M109A6", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("M1A1 Abrams", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Virginia-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("MARSOC Raiders", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("HIMARS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("M1A2 Abrams SEPv3", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"CHN", {
        {"WW1", {
            Unit("Yukiang", "BATTLESHIP", "", "LIGHT", "HEAVY", true),
            Unit("Beiyang Army", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Krupp 75mm", "ARTILLERY", "LIGHT", "LIGHT", "MEDIUM", false),
            Unit("None", "TANK", "LIGHT", "LIGHT", "LIGHT", false)
        }},
        {"Interwar", {
            Unit("Ning Hai", "LIGHT_DESTROYER", "", "LIGHT", "MEDIUM", true),
            Unit("Warlord Soldiers", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Type 41 75mm", "ARTILLERY", "LIGHT", "LIGHT", "MEDIUM", false),
            Unit("Vickers 6-Ton", "TANK", "LIGHT", "LIGHT", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("Type 035 Sub", "SUBMARINE", "", "MEDIUM", "MEDIUM", true),
            Unit("Guerrilla Fighters", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Type 59-1", "ARTILLERY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("Type 97 Chi-Ha", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", false)
        }},
        {"Late WW2", {
            Unit("Chao Ho", "BATTLESHIP", "", "MEDIUM", "HEAVY", true),
            Unit("PLA Infantry", "INFANTRY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("Type 45 105mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("T-34 Captured", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("Type 01 Sub", "SUBMARINE", "", "HEAVY", "HEAVY", true),
            Unit("PLA Marines", "INFANTRY", "MEDIUM", "MEDIUM", "MEDIUM", false),
            Unit("Type 59", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Type 58", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("Type 033 Sub", "SUBMARINE", "", "HEAVY", "HEAVY", true),
            Unit("PLA Airborne", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Type 66", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("Type 59", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Type 035G Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Special Forces", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("PLZ-05", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Type 80", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Type 039 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("PLA Snow Wolf", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("PLZ-05A", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Type 96", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Type 093 Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("PLASOF", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("PCL-181", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Type 99A", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"JPN", {
        {"WW1", {
            Unit("Fuso", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Imperial Army", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Type 38 75mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Type 97 Te-Ke", "TANK", "LIGHT", "LIGHT", "LIGHT", false)
        }},
        {"Interwar", {
            Unit("Nagato", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("IJA Infantry", "INFANTRY", "LIGHT", "LIGHT", "MEDIUM", false),
            Unit("Type 90 75mm", "ARTILLERY", "MEDIUM", "MEDIUM", "HEAVY", false),
            Unit("Type 89 I-Go", "TANK", "LIGHT", "LIGHT", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("I-400 Sub", "SUBMARINE", "", "HEAVY", "HEAVY", true),
            Unit("SNLF Marines", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("Type 92 70mm", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Type 95 Ha-Go", "TANK", "MEDIUM", "MEDIUM", "MEDIUM", false)
        }},
        {"Late WW2", {
            Unit("Yamato", "BATTLESHIP", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Kamikaze Pilots", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Type 4 15cm", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Type 97 Chi-Ha", "TANK", "HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("IJN Remnants", "LIGHT_DESTROYER", "", "HEAVY", "HEAVY", true),
            Unit("JSDF Infantry", "INFANTRY", "MEDIUM", "MEDIUM", "MEDIUM", false),
            Unit("Type 74", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Type 61", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("Oyashio Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("JGSDF Rangers", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("Type 99", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Type 74", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Harushio-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Special Forces Group", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Type 19", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Type 90", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Soryu-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Amphibious Rapid Deployment", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Type 19 155mm", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Type 10", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Taigei-class Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("JGSDF Elite", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Type 12 Rocket", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Type 10 Kai", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }},

    {"DEF", {
        {"WW1", {
            Unit("Dreadnought", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Rifleman", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Field Gun", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Early Tank", "TANK", "HEAVY", "MEDIUM", "HEAVY", false)
        }},
        {"Interwar", {
            Unit("Battleship", "BATTLESHIP", "", "HEAVY", "SUPER_HEAVY", true),
            Unit("Infantryman", "INFANTRY", "LIGHT", "LIGHT", "LIGHT", false),
            Unit("Howitzer", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Light Tank", "TANK", "MEDIUM", "LIGHT", "MEDIUM", false)
        }},
        {"Early WW2", {
            Unit("Destroyer", "LIGHT_DESTROYER", "", "HEAVY", "HEAVY", true),
            Unit("Regular Infantry", "INFANTRY", "MEDIUM", "LIGHT", "MEDIUM", false),
            Unit("Anti-Tank Gun", "ARTILLERY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Medium Tank", "TANK", "HEAVY", "HEAVY", "HEAVY", false)
        }},
        {"Late WW2", {
            Unit("Aircraft Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Veteran Infantry", "INFANTRY", "HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Heavy Artillery", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Heavy Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Cold Transitions", {
            Unit("Submarine", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Mechanized Infantry", "INFANTRY", "HEAVY", "MEDIUM", "HEAVY", false),
            Unit("Self-Propelled Gun", "ARTILLERY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("Main Battle Tank", "TANK", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false)
        }},
        {"Early ColdWar", {
            Unit("Destroyer Escort", "LIGHT_DESTROYER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Elite Infantry", "INFANTRY", "HEAVY", "HEAVY", "HEAVY", false),
            Unit("Rocket Artillery", "ARTILLERY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("Advanced Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Late Coldwar", {
            Unit("Attack Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Special Forces", "INFANTRY", "SUPER_HEAVY", "HEAVY", "SUPER_HEAVY", false),
            Unit("MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Super Heavy Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Transition Modern", {
            Unit("Modern Carrier", "AIRCRAFT_CARRIER", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Commando", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Precision Artillery", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Next-Gen Tank", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }},
        {"Modern", {
            Unit("Stealth Sub", "SUBMARINE", "", "SUPER_HEAVY", "SUPER_HEAVY", true),
            Unit("Tier 1 Operators", "INFANTRY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Hypersonic MLRS", "ARTILLERY", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false),
            Unit("Future MBT", "TANK", "SUPER_HEAVY", "SUPER_HEAVY", "SUPER_HEAVY", false)
        }}
    }}
};

// Helper function
const std::vector<Unit>* GetUnits(const std::string& nation, const std::string& era) {
    auto natIt = UNIT_BLUEPRINTS.find(nation);
    if (natIt == UNIT_BLUEPRINTS.end()) return nullptr;
    
    auto eraIt = natIt->second.find(era);
    if (eraIt == natIt->second.end()) return nullptr;
    
    return &(eraIt->second);
}
