from numbers import Real
import numpy as np

from typing import TYPE_CHECKING

from graph.potencialFunction.potencialFunction import PotencialFunction

if TYPE_CHECKING:
    from graph.situation import Situation

class ModifyEnergy(PotencialFunction):
    def __init__(self, situation: 'Situation', start: Real, end: Real, potencial: Real) -> None:
        super().__init__(situation)
    
        self.start = start
        self.end = end
        self.potencial = potencial
    
    def modifyPotencial(self, v0: np.ndarray) -> np.ndarray:
        v0_array = v0
        
        xStart = self.xPositionToArrayIndex(self.start)
        xEnd = self.xPositionToArrayIndex(self.end)

        v0_array[xStart:xEnd] = self.potencial
        
        return v0_array
        
