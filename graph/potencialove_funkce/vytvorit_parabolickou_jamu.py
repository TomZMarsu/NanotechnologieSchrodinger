from numbers import Real

import numpy as np

from typing import TYPE_CHECKING

from graph.potencialove_funkce.potencialova_funkce import Potencialova_funkce

if TYPE_CHECKING:
    from graph.situation import Situation

class Vytvorit_parabolickou_jamu(Potencialova_funkce):
    def __init__(self, situace: 'Situation', pocatek: Real, konec: Real, energie_na_hrane: Real) -> None:
        super().__init__(situace)
        
        self.pocatek = pocatek
        self.konec = konec
        self.energie_na_hrane = energie_na_hrane
    
    def modifyPotencial(self, v0: np.ndarray) -> np.ndarray:
        v0_pole = v0
        
        stred = self.pocatek+(self.konec-self.pocatek)/2
        x_stred = self.x_pozice_v_poli(stred)
        x_pocatek = self.x_pozice_v_poli(self.pocatek)
        x_konec = self.x_pozice_v_poli(self.konec)
        strmost = self.energie_na_hrane/((x_pocatek-x_stred)**2)

        for x in range(x_pocatek,x_konec):
            v0_pole[x] = strmost*(x-x_stred)**2
        
        return v0_pole
    
