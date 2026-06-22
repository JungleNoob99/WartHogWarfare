from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import random
import math


# --- CONFIGURATION & DATA STRUCTURES ---
@dataclass
class TierData:
    slots: int
    weight: int
    penalty: int
    speed: int


@dataclass
class NavalData:
    weight: int
    speed: int


@dataclass
class ArmorData:
    weight: int
    penalty: int


@dataclass
class ArmamentData:
    slots: int
    weight: int


@dataclass
class WeightClass:
    label: str
    max_weight: int


@dataclass
class UnitStats:
    total_weight: int
    total_penalty: int
    speed: int


@dataclass
class MoveResult:
    success: bool
    reason: str
    distance_moved: float


@dataclass
class TurnOrderEntry:
    name: str
    score: int


# --- TIER CONFIGURATIONS ---
TIERS: Dict[str, TierData] = {
    "LIGHT": TierData(1, 1, 0, 40),
    "MEDIUM": TierData(2, 2, -4, 35),
    "HEAVY": TierData(4, 4, -8, 30),
    "SUPER_HEAVY": TierData(16, 16, -12, 25)
}

NAVAL_SLOTS: Dict[str, NavalData] = {
    "SUBMARINE": NavalData(6, 40),
    "LIGHT_DESTROYER": NavalData(6, 40),
    "BATTLESHIP": NavalData(12, 40),
    "AIRCRAFT_CARRIER": NavalData(10, 40)
}

ARMOR_BOOSTS: Dict[str, ArmorData] = {
    "LIGHT": ArmorData(1, -1),
    "MEDIUM": ArmorData(2, -2),
    "HEAVY": ArmorData(4, -3),
    "SUPER_HEAVY": ArmorData(8, -4)
}

ARMAMENT_BOOSTS: Dict[str, ArmamentData] = {
    "LIGHT": ArmamentData(1, 1),
    "MEDIUM": ArmamentData(1, 2),
    "HEAVY": ArmamentData(1, 4),
    "SUPER_HEAVY": ArmamentData(1, 8)
}

WEIGHT_CLASSES: List[WeightClass] = [
    WeightClass("ULTRALIGHT", 3),
    WeightClass("LIGHT-MID", 7),
    WeightClass("HEAVY", 15),
    WeightClass("SUPER-MASSIVE", 24),
    WeightClass("BEHEMOTH", float('inf'))
]

ERAS: List[str] = [
    "WW1", "Interwar", "Early WW2", "Late WW2", "Cold Transitions",
    "Early ColdWar", "Late Coldwar", "Transition Modern", "Modern"
]


# --- CORE CLASSES ---
class Unit:
    def __init__(self, name: str, unit_type: str, tier_key: str,
                 armor_key: str, weapon_key: str,
                 is_naval: bool = False, era: str = "WW1"):
        self.name = name
        self.type = unit_type
        self.tier_key = tier_key
        self.armor_key = armor_key
        self.weapon_key = weapon_key
        self.is_naval = is_naval
        self.era = era
        self.hp = 100
        self.supply = 100
        self.x = 0.0
        self.y = 0.0

        self.stats = self._calculate_final_stats()
        self.weight_class = self._get_weight_class(self.stats.total_weight)

    def _calculate_final_stats(self) -> UnitStats:
        # Base values
        if self.is_naval:
            naval = NAVAL_SLOTS.get(self.type, NavalData(1, 40))
            base_weight = naval.weight
            base_penalty = 0
            speed = naval.speed
        else:
            tier = TIERS.get(self.tier_key, TIERS["LIGHT"])
            base_weight = tier.weight
            base_penalty = tier.penalty
            speed = tier.speed

        # Armor
        armor = ARMOR_BOOSTS.get(self.armor_key, ArmorData(0, 0))
        # Weapon
        weapon = ARMAMENT_BOOSTS.get(self.weapon_key, ArmamentData(0, 0))

        total_weight = base_weight + armor.weight + weapon.weight
        total_penalty = base_penalty + armor.penalty

        return UnitStats(total_weight, total_penalty, speed)

    def _get_weight_class(self, weight: int) -> str:
        for wc in WEIGHT_CLASSES:
            if weight <= wc.max_weight:
                return wc.label
        return "BEHEMOTH"


class UnitSorter:
    @staticmethod
    def get_weight_class(weight: int) -> str:
        for wc in WEIGHT_CLASSES:
            if weight <= wc.max_weight:
                return wc.label
        return "BEHEMOTH"

    @staticmethod
    def sort_units_by_weight(units: List[Unit]) -> List[Unit]:
        return sorted(units, key=lambda u: u.stats.total_weight, reverse=True)

    @staticmethod
    def get_army_manifest(units: List[Unit]) -> str:
        sorted_units = UnitSorter.sort_units_by_weight(units)
        lines = []
        for u in sorted_units:
            lines.append(
                f"{u.name} | Weight: {u.stats.total_weight} | "
                f"Class: {u.weight_class} | Speed: {u.stats.speed}km"
            )
        return "\n".join(lines)


# --- CORE GAME ENGINE ---
class GameEngine:
    def __init__(self):
        self.global_tension = 0
        self.rng = random.Random()

    def get_era_index(self, era: str) -> int:
        try:
            return ERAS.index(era)
        except ValueError:
            return 0

    # 1. TURN INITIATIVE SYSTEM
    def generate_turn_order(self, nations: List[Tuple[str, bool]]) -> List[TurnOrderEntry]:
        order = []
        for nation, in_crisis in nations:
            roll = self.rng.randint(1, 200)
            crisis_penalty = 50 if in_crisis else 0
            order.append(TurnOrderEntry(nation, roll + crisis_penalty))

        order.sort(key=lambda x: x.score)
        return order

    # 2. MOVEMENT / SUPPLY
    def move_unit(self, unit: Unit, target_x: float, target_y: float) -> MoveResult:
        distance = self.get_distance(unit.x, unit.y, target_x, target_y)
        max_speed = 40 if unit.is_naval else TIERS.get(unit.tier_key, TIERS["LIGHT"]).speed

        if distance > max_speed:
            return MoveResult(False, f"Distance exceeds max speed of {max_speed}km", 0.0)

        unit.x = target_x
        unit.y = target_y
        return MoveResult(True, "Move successful", distance)

    def calculate_supply(self, unit: Unit, hq_x: float, hq_y: float,
                        distance_moved: float, unit_nation_is_last_stand: bool,
                        province_is_isolated: bool):
        dist_to_hq = self.get_distance(unit.x, unit.y, hq_x, hq_y)
        if dist_to_hq > 500:
            drop = int(distance_moved / 10)
            unit.supply = max(0, unit.supply - drop)
        elif not unit_nation_is_last_stand:
            unit.supply = min(100, unit.supply + 1)

        if province_is_isolated:
            unit.supply = min(70, unit.supply)

    # 3. SHORE BOMBARDMENT
    def resolve_shore_bombardment(self, ship: Unit, land_unit: Unit) -> str:
        d20 = self.rng.randint(1, 20)
        d6 = self.rng.randint(1, 6)
        base_roll = d20 - d6

        if base_roll <= 0:
            return f"Miss! The shells splashed harmlessly (Roll: {base_roll})."

        weight_ratio = ship.stats.total_weight / (land_unit.stats.total_weight or 1)
        total_damage = int(base_roll * weight_ratio)

        land_unit.hp -= total_damage

        return (f"Bombardment Success! Roll: {base_roll} | Ratio: {weight_ratio:.2f}x | "
                f"Damage: {total_damage}")

    # 4. GOVERNMENT CRISIS CHECK
    def check_government_crisis(self, total_provinces: int,
                               disconnected_provinces: int,
                               capital_captured: bool) -> str:
        if total_provinces == 0:
            return "COLLAPSED"
        disconnection_ratio = disconnected_provinces / total_provinces
        if disconnection_ratio >= 0.75 or capital_captured:
            return "TRIGGER_CRISIS_PROMPT"
        return "STABLE"

    # 5. NAVAL DETECTION & COMBAT
    def resolve_naval_engagement(self, enemy_ship: Unit, sub_moved: bool) -> str:
        detect_chance = 0.25 if sub_moved else 0.15
        if self.rng.random() >= detect_chance:
            # First strike success
            damage = self.roll_dice(2, 10) * (TIERS["HEAVY"].weight / TIERS["SUPER_HEAVY"].weight)
            enemy_ship.hp -= int(damage)
            return f"First Strike! Sub dealt {damage:.1f} damage undetected."
        return "Standard Engagement: Sub spotted before strike."

    # 6. COMBAT CALCULATION
    def calculate_damage(self, attacker: Unit, defender: Unit) -> int:
        weight_ratio = attacker.stats.total_weight / (defender.stats.total_weight or 1)

        tier_penalty = self._get_tier_penalty(attacker, defender)

        attacker_idx = self.get_era_index(attacker.era)
        defender_idx = self.get_era_index(defender.era)
        era_penalty = -(defender_idx - attacker_idx) if attacker_idx < defender_idx else 0

        roll_a = self.rng.randint(1, 20) + tier_penalty + era_penalty
        roll_b = self.rng.randint(1, 20)
        margin = max(0, roll_a - roll_b)

        return int(margin * weight_ratio * 5)

    # --- HELPERS ---
    def roll_dice(self, count: int, sides: int) -> int:
        return sum(self.rng.randint(1, sides) for _ in range(count))

    def _get_tier_penalty(self, attacker: Unit, defender: Unit) -> int:
        att_penalty = TIERS.get(attacker.tier_key, TIERS["LIGHT"]).penalty
        def_penalty = TIERS.get(defender.tier_key, TIERS["LIGHT"]).penalty
        return att_penalty - def_penalty

    @staticmethod
    def get_distance(x1: float, y1: float, x2: float, y2: float) -> float:
        dx = x2 - x1
        dy = y2 - y1
        return math.sqrt(dx*dx + dy*dy)

    def has_path_to_capital(self, province_id: int, capital_id: int) -> bool:
        # Placeholder - implement pathfinding later if needed
        return True
