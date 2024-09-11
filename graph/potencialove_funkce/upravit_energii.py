from numbers import Real
import numpy as np

from typing import TYPE_CHECKING

from graph.potencialove_funkce.potencialova_funkce import Potencialova_funkce

if TYPE_CHECKING:
    from situace import Situace

class Upravit_energii(Potencialova_funkce):
    def __init__(self, situace: 'Situace', pocatek: Real, konec: Real, energie: Real) -> None:
        super().__init__(situace)
    
        self.pocatek = pocatek
        self.konec = konec
        self.energie = energie
    
    def uprav_potencial(self, v0: np.ndarray) -> np.ndarray:
        v0_pole = v0
        
        x_pocatek = self.x_pozice_v_poli(self.pocatek)
        x_konec = self.x_pozice_v_poli(self.konec)

        v0_pole[x_pocatek:x_konec] = self.energie
        
        return v0_pole
        
