#pragma once
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <random>
#include <sstream>

// --- CONFIGURATION & DATA STRUCTURES ---

struct TierData {
    int slots;
    int weight;
    int penalty;
    int speed;
};

struct NavalData {
    int weight;
    int speed;
};

struct ArmorData {
    int weight;
    int penalty;
};

struct ArmamentData {
    int slots;
    int weight;
};

struct WeightClass {
    std::string label;
    int max;
};

struct UnitStats {
    int totalWeight;
    int totalPenalty;
    int speed;
};

struct MoveResult {
    bool success;
    std::string reason;
    float distanceMoved;
};

struct TurnOrderEntry {
    std::string name;
    int score;
};

// --- TIER CONFIGURATIONS ---
static const std::map<std::string, TierData> TIERS = {
    {"LIGHT",       {1,  1,   0,   40}},
    {"MEDIUM",      {2,  2,  -4,   35}},
    {"HEAVY",       {4,  4,  -8,   30}},
    {"SUPER_HEAVY", {16, 16, -12, 25}}
};

static const std::map<std::string, NavalData> NAVAL_SLOTS = {
    {"SUBMARINE",        {6,  40}},
    {"LIGHT_DESTROYER",  {6,  40}},
    {"BATTLESHIP",       {12, 40}},
    {"AIRCRAFT_CARRIER", {10, 40}}
};

static const std::map<std::string, ArmorData> ARMOR_BOOSTS = {
    {"LIGHT",       {1, -1}},
    {"MEDIUM",      {2, -2}},
    {"HEAVY",       {4, -3}},
    {"SUPER_HEAVY", {8, -4}}
};

static const std::map<std::string, ArmamentData> ARMAMENT_BOOSTS = {
    {"LIGHT",       {1, 1}},
    {"MEDIUM",      {1, 2}},
    {"HEAVY",       {1, 4}},
    {"SUPER_HEAVY", {1, 8}}
};

static const std::vector<WeightClass> WEIGHT_CLASSES = {
    {"ULTRALIGHT",    3},
    {"LIGHT-MID",     7},
    {"HEAVY",         15},
    {"SUPER-MASSIVE", 24},
    {"BEHEMOTH",      INT_MAX}
};

static const std::vector<std::string> ERAS = {
    "WW1",
    "Interwar",
    "Early WW2",
    "Late WW2",
    "Cold Transitions",
    "Early ColdWar",
    "Late Coldwar",
    "Transition Modern",
    "Modern"
};

// --- CORE CLASSES ---

class Unit {
public:
    std::string name;
    std::string type;
    std::string tierKey;
    std::string armorKey;
    std::string weaponKey;
    bool isNaval;
    std::string era;
    int hp;
    int supply;
    UnitStats stats;
    std::string weightClass;
    float x, y;

    Unit(const std::string& name, const std::string& type, const std::string& tierKey,
         const std::string& armorKey, const std::string& weaponKey,
         bool isNaval = false, const std::string& era = "WW1")
        : name(name), type(type), tierKey(tierKey), armorKey(armorKey),
          weaponKey(weaponKey), isNaval(isNaval), era(era), hp(100), supply(100),
          x(0), y(0) {
        stats = calculateFinalStats();
        weightClass = getWeightClass(stats.totalWeight);
    }

private:
    UnitStats calculateFinalStats() {
        int baseWeight = 0;
        int basePenalty = 0;
        int speed = 0;

        if (isNaval) {
            auto it = NAVAL_SLOTS.find(type);
            if (it != NAVAL_SLOTS.end()) {
                baseWeight = it->second.weight;
                speed = it->second.speed;
            } else {
                baseWeight = 1;
                speed = 40;
            }
        } else {
            auto it = TIERS.find(tierKey);
            if (it != TIERS.end()) {
                baseWeight = it->second.weight;
                basePenalty = it->second.penalty;
                speed = it->second.speed;
            } else {
                auto light = TIERS.at("LIGHT");
                baseWeight = light.weight;
                basePenalty = light.penalty;
                speed = light.speed;
            }
        }

        int armorWeight = 0, armorPenalty = 0;
        auto armorIt = ARMOR_BOOSTS.find(armorKey);
        if (armorIt != ARMOR_BOOSTS.end()) {
            armorWeight = armorIt->second.weight;
            armorPenalty = armorIt->second.penalty;
        }

        int weaponWeight = 0;
        auto weaponIt = ARMAMENT_BOOSTS.find(weaponKey);
        if (weaponIt != ARMAMENT_BOOSTS.end()) {
            weaponWeight = weaponIt->second.weight;
        }

        return {
            baseWeight + armorWeight + weaponWeight,
            basePenalty + armorPenalty,
            speed
        };
    }

    std::string getWeightClass(int weight) {
        for (const auto& wc : WEIGHT_CLASSES) {
            if (weight <= wc.max) {
                return wc.label;
            }
        }
        return "BEHEMOTH";
    }
};

class UnitSorter {
public:
    static std::string getWeightClass(int weight) {
        for (const auto& wc : WEIGHT_CLASSES) {
            if (weight <= wc.max) {
                return wc.label;
            }
        }
        return "BEHEMOTH";
    }

    static std::vector<Unit> sortUnitsByWeight(const std::vector<Unit>& units) {
        auto sorted = units;
        std::sort(sorted.begin(), sorted.end(),
                  [](const Unit& a, const Unit& b) {
                      return a.stats.totalWeight > b.stats.totalWeight;
                  });
        return sorted;
    }

    static std::string getArmyManifest(const std::vector<Unit>& units) {
        auto sorted = sortUnitsByWeight(units);
        std::stringstream ss;
        for (const auto& u : sorted) {
            ss << u.name << " | Weight: " << u.stats.totalWeight
               << " | Class: " << u.weightClass
               << " | Speed: " << u.stats.speed << "km\n";
        }
        return ss.str();
    }
};

// --- CORE GAME ENGINE ---

class GameEngine {
private:
    std::mt19937 rng;

public:
    int globalTension;

    GameEngine() : globalTension(0), rng(std::random_device{}()) {}

    int getEraIndex(const std::string& era) {
        auto it = std::find(ERAS.begin(), ERAS.end(), era);
        return it != ERAS.end() ? std::distance(ERAS.begin(), it) : 0;
    }

    // 1. TURN INITIATIVE SYSTEM
    std::vector<TurnOrderEntry> generateTurnOrder(const std::vector<std::pair<std::string, bool>>& nations) {
        std::vector<TurnOrderEntry> order;
        std::uniform_int_distribution<> dis(1, 200);

        for (const auto& nation : nations) {
            int roll = dis(rng);
            int crisisPenalty = nation.second ? 50 : 0;
            order.push_back({nation.first, roll + crisisPenalty});
        }

        std::sort(order.begin(), order.end(),
                  [](const TurnOrderEntry& a, const TurnOrderEntry& b) {
                      return a.score < b.score;
                  });
        return order;
    }

    // 2. MOVEMENT / SUPPLY & REGEN LOGIC
    MoveResult moveUnit(Unit& unit, float targetX, float targetY) {
        float distance = getDistance(unit.x, unit.y, targetX, targetY);
        int maxSpeed = unit.isNaval ? 40 : TIERS.at(unit.tierKey).speed;

        if (distance > maxSpeed) {
            return {false, "Distance exceeds max speed of " + std::to_string(maxSpeed) + "km", 0};
        }

        unit.x = targetX;
        unit.y = targetY;
        return {true, "Move successful", distance};
    }

    void calculateSupply(Unit& unit, float hqX, float hqY, float distanceMoved, bool unitNationIsLastStand, bool provinceIsIsolated) {
        float dist = getDistance(unit.x, unit.y, hqX, hqY);
        bool isOutOfRange = dist > 500;

        if (isOutOfRange) {
            int drop = static_cast<int>(distanceMoved / 10);
            unit.supply = std::max(0, unit.supply - drop);
        } else if (!unitNationIsLastStand) {
            unit.supply = std::min(100, unit.supply + 1);
        }

        if (provinceIsIsolated) {
            unit.supply = std::min(70, unit.supply);
        }
    }

    // 3. SHORE BOMBARDMENT
    std::string resolveShoreBombardment(const Unit& ship, Unit& landUnit) {
        std::uniform_int_distribution<> d20Dis(1, 20);
        std::uniform_int_distribution<> d6Dis(1, 6);

        int d20 = d20Dis(rng);
        int d6 = d6Dis(rng);
        int baseRoll = d20 - d6;

        if (baseRoll <= 0) {
            return "Miss! The shells splashed harmlessly (Roll: " + std::to_string(baseRoll) + ").";
        }

        float weightRatio = static_cast<float>(ship.stats.totalWeight) / 
                           (landUnit.stats.totalWeight > 0 ? landUnit.stats.totalWeight : 1);
        int totalDamage = static_cast<int>(baseRoll * weightRatio);

        landUnit.hp -= totalDamage;

        std::stringstream ss;
        ss << "Bombardment Success! Roll: " << baseRoll << " | Ratio: " << weightRatio
           << "x | Damage: " << totalDamage;
        return ss.str();
    }

    // 4. GOVERNMENT CRISIS CHECK
    std::string checkGovernmentCrisis(int totalProvinces, int disconnectedProvinces, bool capitalCaptured) {
        if (totalProvinces == 0) return "COLLAPSED";

        float disconnectionRatio = static_cast<float>(disconnectedProvinces) / totalProvinces;
        if (disconnectionRatio >= 0.75f || capitalCaptured) {
            return "TRIGGER_CRISIS_PROMPT";
        }
        return "STABLE";
    }

    // 5. NAVAL DETECTION & COMBAT
    std::string resolveNavalEngagement(Unit& enemyShip, bool subMoved) {
        float detectChance = subMoved ? 0.25f : 0.15f;
        std::uniform_real_distribution<> randDis(0.0, 1.0);
        bool isDetected = randDis(rng) < detectChance;

        if (!isDetected) {
            float damage = rollDice(2, 10) * (static_cast<float>(TIERS.at("HEAVY").weight) / 
                                              TIERS.at("SUPER_HEAVY").weight);
            enemyShip.hp -= static_cast<int>(damage);
            std::stringstream ss;
            ss << "First Strike! Sub dealt " << damage << " damage undetected.";
            return ss.str();
        }
        return "Standard Engagement: Sub spotted before strike.";
    }

    // 6. COMBAT CALCULATION
    int calculateDamage(const Unit& attacker, const Unit& defender) {
        float weightRatio = static_cast<float>(attacker.stats.totalWeight) / 
                           (defender.stats.totalWeight > 0 ? defender.stats.totalWeight : 1);
        int tierPenalty = getTierPenalty(attacker, defender);

        int eraPenalty = 0;
        int attackerIndex = getEraIndex(attacker.era);
        int defenderIndex = getEraIndex(defender.era);
        if (attackerIndex < defenderIndex) {
            eraPenalty = -(defenderIndex - attackerIndex);
        }

        std::uniform_int_distribution<> d20Dis(1, 20);
        int rollA = d20Dis(rng) + tierPenalty + eraPenalty;
        int rollB = d20Dis(rng);

        int margin = std::max(0, rollA - rollB);
        return static_cast<int>(margin * weightRatio * 5);
    }

    // --- HELPERS ---

    int rollDice(int count, int sides) {
        std::uniform_int_distribution<> dis(1, sides);
        int total = 0;
        for (int i = 0; i < count; ++i) {
            total += dis(rng);
        }
        return total;
    }

    int getTierPenalty(const Unit& attacker, const Unit& defender) {
        int attackerPenalty = TIERS.at(attacker.tierKey).penalty;
        int defenderPenalty = TIERS.at(defender.tierKey).penalty;
        return attackerPenalty - defenderPenalty;
    }

    float getDistance(float x1, float y1, float x2, float y2) {
        float dx = x2 - x1;
        float dy = y2 - y1;
        return std::sqrt(dx * dx + dy * dy);
    }

    bool hasPathToCapital(int provinceId, int capitalId) {
        // Placeholder
        return true;
    }
};
