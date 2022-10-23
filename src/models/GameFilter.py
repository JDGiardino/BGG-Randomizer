from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GameFilter:
    gametype: str = "boardgame"
    minplayers: Optional[int] = None
    maxplayers: Optional[int] = None
    playerrangetype: Optional[str] = None
    playstyle: Optional[str] = None

    def __post_init__(self):
        if self.minplayers is not None:
            object.__setattr__(self, "minplayers", int(self.minplayers))
        if self.maxplayers is not None:
            object.__setattr__(self, "maxplayers", int(self.maxplayers))
        if self.playerrangetype is not None:
            object.__setattr__(self, "playerrangetype", str(self.playerrangetype))
        if self.playstyle is not None:
            object.__setattr__(self, "playerstyle", str(self.playstyle))

    # This bypasses frozen=true by modifying the object class which all objects inherent from including dataclasses
