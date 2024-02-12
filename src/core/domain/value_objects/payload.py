from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Payload:
    old: Dict[str, str] = field(default_factory=dict)
    new: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Dict[str, str]]:
        return {"old": self.old, "new": self.new}
