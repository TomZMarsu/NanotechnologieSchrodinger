from numbers import Real

import numpy as np

from typing import TYPE_CHECKING

from graph.potencialFunction.potencialFunction import PotencialFunction

if TYPE_CHECKING:
    from graph.situation import Situation

class CreateParabolicWell(PotencialFunction):
    def __init__(self, situation: 'Situation', start: Real, end: Real, potencialOnEdge: Real) -> None:
        super().__init__(situation)
        
        self.start = start
        self.end = end
        self.potencialOnEdge = potencialOnEdge
    
    def modifyPotencial(self, v0: np.ndarray) -> np.ndarray:
        v0_array = v0
        
        center = self.start+(self.end-self.start)/2
        xCenter = self.xPositionToArrayIndex(center)
        xStart = self.xPositionToArrayIndex(self.start)
        xEnd = self.xPositionToArrayIndex(self.end)
        steepness = self.potencialOnEdge/((xStart-xCenter)**2)

        for x in range(xStart,xEnd):
            v0_array[x] = steepness*(x-xCenter)**2
        
        return v0_array
    
