import random
from typing import List, Dict, Optional, Tuple

from attachments.UnitsList import UNIT_BLUEPRINTS, get_units, Unit as BlueprintUnit
from attachments.NationsTags import NATIONS, get_nation_list, is_valid_nation
from attachments.MainCombatSYS import (
    GameEngine, Unit, UnitSorter, 
    TIERS, ERAS, MoveResult, TurnOrderEntry
)
from attachments.CivilWarTagGenerator import CivilWarTagGenerator

# =============================================================================
# CENTRAL GAME STATE / INTEGRATION LAYER
# =============================================================================

class GameManager:
    """
    Main orchestrator that connects all systems.
    """
    def __init__(self):
        self.engine = GameEngine()
        self.civil_war_generator = CivilWarTagGenerator()
        self.active_units: Dict[str, List[Unit]] = {}  # nation -> list of deployed units
        self.current_era = "WW1"

    def create_army(self, nation: str, era: str = None) -> List[Unit]:
        """Create full army from blueprints for a nation/era"""
        if era is None:
            era = self.current_era
        
        blueprints = get_units(nation, era)
        if not blueprints:
            raise ValueError(f"No units found for {nation} in {era}")
        
        army = []
        for bp in blueprints:
            # Convert blueprint to full combat Unit
            unit = Unit(
                name=bp.name,
                unit_type=bp.type,
                tier_key=bp.param1 or "LIGHT",
                armor_key=bp.param2 or "LIGHT",
                weapon_key=bp.param3 or "LIGHT",
                is_naval=bp.is_naval,
                era=era
            )
            army.append(unit)
        
        self.active_units[nation] = army
        return army

    def get_army_manifest(self, nation: str) -> str:
        """Get formatted army list"""
        units = self.active_units.get(nation, [])
        return UnitSorter.get_army_manifest(units)

    def simulate_battle(self, attacker_nation: str, defender_nation: str):
        """Simple battle demo"""
        att_units = self.active_units.get(attacker_nation, [])
        def_units = self.active_units.get(defender_nation, [])
        
        if not att_units or not def_units:
            return "Missing armies!"
        
        attacker = random.choice(att_units)
        defender = random.choice(def_units)
        
        damage = self.engine.calculate_damage(attacker, defender)
        defender.hp -= damage
        
        return f"{attacker.name} deals {damage} damage to {defender.name} (HP left: {defender.hp})"

    def generate_civil_war_tag(self) -> str:
        return self.civil_war_generator.get_next_faction_tag()

    def advance_era(self):
        """Cycle through eras"""
        try:
            idx = ERAS.index(self.current_era)
            self.current_era = ERAS[(idx + 1) % len(ERAS)]
        except ValueError:
            self.current_era = "WW1"
