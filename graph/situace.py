import numpy as np # Knihovna pro lineární algebru, matice
import scipy.linalg
from typing import Final
from numbers import Real
import time

from graph.potencialove_funkce.potencialova_funkce import Potencialova_funkce

class Situace():
    def __init__(self, 
                 pocet_prvku: int = 500, 
                 pocatek_osy: Real = 0, 
                 konec_osy: Real = 1,
                 alfa: Real = 1.0,
                 energie: Real = 1.0,
                 normalizovat_vysledek: bool = False,
                 posunout_psi_na_e: bool = False,
                 bariera_na_sekundarni_ose: bool = True,
                 hladiny_jsou_barevne_pruhy: bool = False,
                 koeficient_vysky_pruhu: Real = 20,
                 pocet_vykreslenych_energetickych_hladin: int = 10,
                 funkce_upravujici_potencial: list[Potencialova_funkce] = []
                 ):
        
        # Zpracovani argumentu konstruktoru
        self.pocet_prvku = pocet_prvku
        self.pocatek_osy = pocatek_osy
        self.konec_osy = konec_osy
        self.alfa = alfa
        self.energie = energie
        self.normalizovat_vysledek = normalizovat_vysledek
        self.posunout_psi_na_e = posunout_psi_na_e
        self.bariera_na_sekundarni_ose = bariera_na_sekundarni_ose
        self.hladiny_jsou_barevne_pruhy = hladiny_jsou_barevne_pruhy
        self.koeficient_vysky_pruhu = koeficient_vysky_pruhu
        self.pocet_vykreslenych_energetickych_hladin = pocet_vykreslenych_energetickych_hladin
        self.funkce_upravujici_potencial = funkce_upravujici_potencial
        
        # Vypocet ostatnich konstant
        self.osa_x, self.dx = self.prepocitat_osu_x()
        
        self.v0 = self.prepocitat_potencial()
        
        self.hlavni_diagonala, self.vedlejsi_diagonala = self.priprav_matici()
        
        # Priprava prozatim nevypoctenych hodnot
        self.E = None
        self.psi = None
        
            
    def prepocitat_osu_x(self) -> tuple[np.ndarray, float]:
        self.osa_x = np.linspace(self.pocatek_osy,self.konec_osy,self.pocet_prvku)
        self.dx = self.osa_x[1] - self.osa_x[0]
        
        return self.osa_x, self.dx
    
    def prepocitat_potencial(self) -> np.ndarray:
        v0 = np.full(self.pocet_prvku, self.energie)
        
        for v0_fn in self.funkce_upravujici_potencial:
            v0 = v0_fn.uprav_potencial(v0)
        
        return v0
    
    def priprav_matici(self) ->  tuple[np.ndarray, np.ndarray]:
        hlavni_diagonala = np.full([self.pocet_prvku],-2)
        vedlejsi_diagonala = np.ones([self.pocet_prvku-1])  
        
        nasobic = (-self.alfa/(self.dx**2))
        hlavni_diagonala = hlavni_diagonala * nasobic
        vedlejsi_diagonala = vedlejsi_diagonala * nasobic
        
        hlavni_diagonala += self.v0
        
        return hlavni_diagonala, vedlejsi_diagonala
    
    def prepocitat_pripravu(self):
        self.osa_x, self.dx = self.prepocitat_osu_x()
        
        self.v0 = self.prepocitat_potencial()
        
        self.hlavni_diagonala, self.vedlejsi_diagonala = self.priprav_matici()
        
    def vyresit_rovnici(self) -> tuple[np.ndarray, np.ndarray, float]:
        cas_start = time.time()
        self.E, self.psi = scipy.linalg.eigh_tridiagonal(self.hlavni_diagonala,self.vedlejsi_diagonala)
        cas_konec = time.time()
        
        cas = cas_konec - cas_start
        
        return self.E, self.psi, cas

    def normalizovat_psi(self, psi_matice: np.ndarray) -> np.ndarray:
        I = np.sum(self.dx*psi_matice**2)
        A = 1/np.sqrt(I)
        n_psi = A*psi_matice

        return n_psi