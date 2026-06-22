from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import random
import math

from attachments.NationsTags import NATIONS, is_valid_nation
from attachments.MainCombatSYS import GameEngine, Unit, MoveResult


@dataclass
class Province:
    id: int
    name: str
    owner: str                  # Nation code (e.g. "BRT", "GER")
    capital: bool = False
    x: float = 0.0
    y: float = 0.0
    terrain: str = "PLAINS"     # PLAINS, MOUNTAIN, FOREST, URBAN, COASTAL, etc.
    supply_hub: bool = False


class GameMap:
    """
    Simple 2D strategic map with provinces.
    Supports movement, ownership, distance calculations.
    """
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.provinces: Dict[int, Province] = {}
        self.next_province_id = 1
        self.engine = GameEngine()  # For distance calculations

    def add_province(self, name: str, owner: str, x: float = None, y: float = None,
                    terrain: str = "PLAINS", capital: bool = False) -> int:
        """Add a new province to the map"""
        if not is_valid_nation(owner):
            owner = "DEF"  # Default fallback

        if x is None:
            x = random.uniform(0, self.width)
        if y is None:
            y = random.uniform(0, self.height)

        prov = Province(
            id=self.next_province_id,
            name=name,
            owner=owner,
            x=x,
            y=y,
            terrain=terrain,
            capital=capital
        )
        self.provinces[prov.id] = prov
        self.next_province_id += 1
        return prov.id

    def get_province(self, prov_id: int) -> Optional[Province]:
        return self.provinces.get(prov_id)

    def get_owner_provinces(self, nation: str) -> List[Province]:
        return [p for p in self.provinces.values() if p.owner == nation]

    def change_owner(self, prov_id: int, new_owner: str) -> bool:
        prov = self.get_province(prov_id)
        if prov and is_valid_nation(new_owner):
            prov.owner = new_owner
            return True
        return False

    def distance_between(self, prov1_id: int, prov2_id: int) -> float:
        p1 = self.get_province(prov1_id)
        p2 = self.get_province(prov2_id)
        if not p1 or not p2:
            return float('inf')
        return self.engine.get_distance(p1.x, p1.y, p2.x, p2.y)

    def move_unit_to_province(self, unit: Unit, target_prov_id: int) -> MoveResult:
        target = self.get_province(target_prov_id)
        if not target:
            return MoveResult(False, "Invalid province", 0.0)

        distance = self.engine.get_distance(unit.x, unit.y, target.x, target.y)
        max_speed = 40 if unit.is_naval else 35  # rough default

        if distance > max_speed:
            return MoveResult(False, f"Too far ({distance:.1f} > {max_speed})", 0.0)

        unit.x = target.x
        unit.y = target.y
        return MoveResult(True, f"Moved to {target.name}", distance)

    def get_map_summary(self) -> str:
        owners = {}
        for p in self.provinces.values():
            owners[p.owner] = owners.get(p.owner, 0) + 1

        summary = ["=== WORLD MAP SUMMARY ==="]
        summary.append(f"Total Provinces: {len(self.provinces)}")
        for nation, count in sorted(owners.items(), key=lambda x: -x[1]):
            summary.append(f"  {nation}: {count} provinces")
        return "\n".join(summary)

    def generate_sample_map(self):
        """Generate a basic world map with major nations"""
        self.provinces.clear()
        self.next_province_id = 1

        # Major powers with capitals
        capitals = {
            "BRT": ("London", 400, 150),
            "GER": ("Berlin", 520, 140),
            "FRA": ("Paris", 380, 180),
            "USA": ("Washington", 150, 220),
            "RUS": ("Moscow", 680, 100),
            "CHN": ("Beijing", 750, 250),
            "JPN": ("Tokyo", 820, 280),
            "ITA": ("Rome", 480, 220),
        }

        for nation, (name, x, y) in capitals.items():
            self.add_province(name, nation, x, y, "URBAN", capital=True)

        # Add some extra provinces
        extras = [
            ("Normandy", "FRA", 360, 190, "COASTAL"),
            ("Ruhr", "GER", 510, 160, "URBAN"),
            ("Siberia", "RUS", 720, 80, "MOUNTAIN"),
            ("Manchuria", "CHN", 780, 230, "PLAINS"),
            ("Pacific Fleet Base", "USA", 100, 300, "COASTAL"),
        ]
        for name, owner, x, y, terrain in extras:
            self.add_province(name, owner, x, y, terrain)


# =============================================================================
# INTEGRATION WITH GAME MANAGER
# =============================================================================

class GameManagerWithMap:
    def __init__(self):
        self.map = GameMap()
        self.map.generate_sample_map()
        # ... (you can extend with previous GameManager logic)

    def print_map(self):
        print(self.map.get_map_summary())
        print("\nSample Provinces:")
        for p in list(self.map.provinces.values())[:8]:
            print(f"  {p.id}: {p.name} ({p.owner}) @ ({p.x:.0f}, {p.y:.0f})")


# =============================================================================
# DEMO
# =============================================================================
if __name__ == "__main__":
    gm = GameManagerWithMap()
    gm.print_map()

    # Example movement
    from attachments.UnitsList import get_units
    from attachments.MainCombatSYS import Unit

    # Create a test unit
    test_unit = Unit("Test Tank", "TANK", "HEAVY", "HEAVY", "HEAVY", False)
    prov_id = list(gm.map.provinces.keys())[0]
    result = gm.map.move_unit_to_province(test_unit, prov_id)
    print(f"\nMove result: {result.success} - {result.reason}")
