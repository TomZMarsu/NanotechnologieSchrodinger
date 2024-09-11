from numbers import Real
import numpy as np

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph.situation import Situation

class Potencialova_funkce():
    def __init__(self, situace: 'Situation') -> None:
        self.situace = situace
    
    def x_pozice_v_poli(self, x: Real) -> int:
        normalizacni_rozdil: float = -float(self.situace.xAxisStart)
        x_normalizovano: float = float(x) + normalizacni_rozdil
        return int(x_normalizovano/self.situace.dx)
    
    def modifyPotencial(self, v0: np.ndarray) -> np.ndarray:
        return v0