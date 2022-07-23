import math
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BoardGame:
    id: int
    name: str
    type: str
    description: str
    minplayers: int
    maxplayers: int
    yearpublished: int
    averagerating: float
    complexity: float
    overallrank: Optional[float] = None
    thumbnail: Optional[str] = None
    image: Optional[str] = None

    def __post_init__(self):
        object.__setattr__(self, "id", int(self.id))
        object.__setattr__(self, "maxplayers", int(self.maxplayers))
        object.__setattr__(self, "minplayers", int(self.minplayers))
        object.__setattr__(self, "yearpublished", int(self.yearpublished))
        object.__setattr__(self, "averagerating", float(self.averagerating))
        object.__setattr__(self, "complexity", float(self.complexity))
        if self.overallrank == "Not Ranked":
            # Games without a rank have a string value for rank.  Setting these game's rank to infinity maintains
            # our type contract while setting to an obvious value we can filter for later on
            object.__setattr__(self, "overallrank", math.inf)
            object.__setattr__(self, "overallrank", float(self.overallrank))
        else:
            object.__setattr__(self, "overallrank", float(self.overallrank))
        # This bypasses frozen=true by modifying the object class which all objects inherent from including dataclasses

    # BoardGame object must be subscriptable in order to preform indexing on object's attributes
    def __getitem__(self, item):
        return getattr(self, item)
