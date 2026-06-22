import re
from typing import Set


class CivilWarTagGenerator:
    def __init__(self):
        self.next_index: int = 1
        self.used: Set[str] = set()

    def get_next_faction_tag(self) -> str:
        """Generate next civil war faction tag in format A01, B42, ..., Z99"""
        index = self.next_index
        while True:
            letter_code = (index - 1) // 99
            number = ((index - 1) % 99) + 1

            if letter_code > 25:  # Beyond Z
                raise RuntimeError("Civil war faction tags exhausted (A01–Z99)")

            letter = chr(65 + letter_code)  # A=65
            tag = f"{letter}{number:02d}"

            if tag not in self.used:
                self.used.add(tag)
                self.next_index = index + 1
                return tag

            index += 1  # Skip used tags

    def reset(self) -> None:
        """Reset generator to start from A01"""
        self.next_index = 1
        self.used.clear()

    @staticmethod
    def is_faction_tag(tag: str) -> bool:
        """Check if string matches faction tag format (e.g. A01, Z99)"""
        return bool(re.match(r'^[A-Z][0-9]{2}$', tag))
