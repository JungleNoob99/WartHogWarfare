# =============================================================================
# ADVANCED MAP SYSTEM - Province Connections + Renderer
# map_system.py
# =============================================================================

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Set
import random
import math
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Circle, FancyArrowPatch

from attachments.NationsTags import is_valid_nation
from attachments.MainCombatSYS import GameEngine, Unit, MoveResult


@dataclass
class Province:
    id: int
    name: str
    owner: str
    capital: bool = False
    x: float = 0.0
    y: float = 0.0
    terrain: str = "PLAINS"
    supply_hub: bool = False


class GameMap:
    def __init__(self, width: int = 1000, height: int = 700):
        self.width = width
        self.height = height
        self.provinces: Dict[int, Province] = {}
        self.connections: Dict[int, Set[int]] = {}  # Adjacency list
        self.next_province_id = 1
        self.engine = GameEngine()

    def add_province(self, name: str, owner: str, x: float = None, y: float = None,
                     terrain: str = "PLAINS", capital: bool = False) -> int:
        if x is None: x = random.uniform(50, self.width - 50)
        if y is None: y = random.uniform(50, self.height - 50)

        if not is_valid_nation(owner):
            owner = "DEF"

        prov = Province(
            id=self.next_province_id,
            name=name,
            owner=owner,
            x=x, y=y,
            terrain=terrain,
            capital=capital
        )
        self.provinces[prov.id] = prov
        self.connections[prov.id] = set()
        self.next_province_id += 1
        return prov.id

    def connect_provinces(self, id1: int, id2: int, bidirectional: bool = True):
        """Create a connection (road/border) between provinces"""
        if id1 in self.provinces and id2 in self.provinces:
            self.connections[id1].add(id2)
            if bidirectional:
                self.connections[id2].add(id1)

    def get_connected_provinces(self, prov_id: int) -> List[int]:
        return list(self.connections.get(prov_id, set()))

    def is_connected(self, id1: int, id2: int) -> bool:
        return id2 in self.connections.get(id1, set())

    def move_unit_to_province(self, unit: Unit, target_prov_id: int, use_connections: bool = True) -> MoveResult:
        target = self.get_province(target_prov_id)
        if not target:
            return MoveResult(False, "Invalid province", 0.0)

        distance = self.engine.get_distance(unit.x, unit.y, target.x, target.y)

        if use_connections and not self.is_connected(int(unit.x), target_prov_id):  # rough check
            # Allow direct move but penalize if not connected
            pass

        max_speed = 40 if unit.is_naval else 35
        if distance > max_speed * 1.5:  # some flexibility
            return MoveResult(False, f"Too far ({distance:.1f}km)", 0.0)

        unit.x = target.x
        unit.y = target.y
        return MoveResult(True, f"Moved to {target.name}", distance)

    def generate_sample_map(self):
        """Generate a realistic Europe-style map with connections"""
        self.provinces.clear()
        self.connections.clear()
        self.next_province_id = 1

        # Major capitals
        capitals = {
            "BRT": ("London", 320, 180),
            "FRA": ("Paris", 380, 240),
            "GER": ("Berlin", 520, 190),
            "ITA": ("Rome", 480, 380),
            "RUS": ("Moscow", 720, 140),
            "USA": ("Washington", 120, 280),
            "CHN": ("Beijing", 820, 320),
            "JPN": ("Tokyo", 920, 340),
        }

        prov_ids = {}
        for nation, (name, x, y) in capitals.items():
            pid = self.add_province(name, nation, x, y, "URBAN", capital=True)
            prov_ids[nation] = pid

        # Add extra provinces
        extras = [
            ("Pacific Fleet Base", "USA", 100, 300, "COASTAL"),
            ("Normandy", "FRA", 340, 260, "COASTAL"),
            ("Ruhr", "GER", 500, 220, "URBAN"),
            ("Bavaria", "GER", 540, 260, "MOUNTAIN"),
            ("Siberia", "RUS", 780, 100, "MOUNTAIN"),
            ("Manchuria", "CHN", 840, 280, "PLAINS"),
            ("Scotland", "BRT", 280, 120, "PLAINS"),
        ]

        for name, owner, x, y, terrain in extras:
            pid = self.add_province(name, owner, x, y, terrain)
            # Connect to capital
            if owner in prov_ids:
                self.connect_provinces(prov_ids[owner], pid)

        # Create historical connections
        self.connect_provinces(prov_ids["BRT"], prov_ids["FRA"], True)   # Channel crossing
        self.connect_provinces(prov_ids["FRA"], prov_ids["GER"], True)
        self.connect_provinces(prov_ids["GER"], prov_ids["ITA"], True)
        self.connect_provinces(prov_ids["GER"], prov_ids["RUS"], True)

    def render_map(self, highlight_nation: str = None, show_connections: bool = True):
        """Visual map renderer using matplotlib"""
        plt.figure(figsize=(14, 9))
        ax = plt.gca()
        ax.set_facecolor('#1a2633')

        colors = {
            "BRT": "royalblue", "GER": "crimson", "FRA": "mediumblue",
            "ITA": "green", "RUS": "darkred", "USA": "navy",
            "CHN": "red", "JPN": "orange", "DEF": "gray"
        }

        # Draw provinces
        for prov in self.provinces.values():
            color = colors.get(prov.owner, "lightgray")
            size = 180 if prov.capital else 90

            circle = Circle((prov.x, prov.y), size, color=color, alpha=0.85, ec='white', lw=1.5)
            ax.add_patch(circle)

            # Label
            ax.text(prov.x, prov.y, prov.name, fontsize=9 if prov.capital else 8,
                    ha='center', va='center', color='white', weight='bold')

        # Draw connections
        if show_connections:
            for src_id, targets in self.connections.items():
                src = self.provinces[src_id]
                for tgt_id in targets:
                    if tgt_id > src_id:  # avoid double drawing
                        tgt = self.provinces[tgt_id]
                        ax.plot([src.x, tgt.x], [src.y, tgt.y],
                                color='white', alpha=0.4, linewidth=1.5, linestyle='--')

        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_title("Strategic World Map - Province Connections", fontsize=16, color='white')
        ax.axis('off')
        plt.tight_layout()
        plt.show()
