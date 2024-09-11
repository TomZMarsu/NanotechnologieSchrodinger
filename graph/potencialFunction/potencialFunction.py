from numbers import Real
import numpy as np

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph.situation import Situation

class PotencialFunction():
    def __init__(self, situation: 'Situation') -> None:
        self.situation = situation
    
    def xPositionToArrayIndex(self, x: Real) -> int:
        normalizationDelta: float = -float(self.situation.xAxisStart)
        xNormalized: float = float(x) + normalizationDelta
        return int(xNormalized/self.situation.dx)
    
    def modifyPotencial(self, v0: np.ndarray) -> np.ndarray:
        return v0