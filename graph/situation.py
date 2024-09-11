import numpy as np
import scipy.linalg
from typing import Final
from numbers import Real
import time

from graph.potencialFunction.potencialFunction import PotencialFunction

class Situation():
    def __init__(self, 
                 elementCount: int = 500, 
                 xAxisStart: Real = 0, 
                 xAxisEnd: Real = 1,
                 alpha: Real = 1.0,
                 basePotential: Real = 1.0,
                 isResultNormalized: bool = False,
                 isPsiOnSameLevelAsE: bool = False,
                 isPotentialOnSecondaryAxis: bool = True,
                 isLevelColorbar: bool = False,
                 colorbarHeightCoeff: Real = 20,
                 energyLevelDrawCount: int = 10,
                 functionsModifyingPotential: list[PotencialFunction] = []
                 ):
        
        # Zpracovani argumentu konstruktoru
        self.elementCount = elementCount
        self.xAxisStart = xAxisStart
        self.xAxisEnd = xAxisEnd
        self.alpha = alpha
        self.basePotencial = basePotential
        self.isResultNormalized = isResultNormalized
        self.isPsiOnSameLavelAsE = isPsiOnSameLevelAsE
        self.isPotentialOnSecondaryAxis = isPotentialOnSecondaryAxis
        self.isLevelColorbar = isLevelColorbar
        self.colorbarHeightCoeff = colorbarHeightCoeff
        self.energyLevelDrawCount = energyLevelDrawCount
        self.functionsModifyingPotential = functionsModifyingPotential
        
        # Vypocet ostatnich konstant
        self.xAxis, self.dx = self.recalculateXAxis()
        
        self.v0 = self.recalculatePotential()
        
        self.mainDiagonal, self.offDiagonal = self.prepareMatrix()
        
        # Priprava prozatim nevypoctenych hodnot
        self.E = None
        self.psi = None
        
            
    def recalculateXAxis(self) -> tuple[np.ndarray, float]:
        self.xAxis = np.linspace(self.xAxisStart,self.xAxisEnd,self.elementCount)
        self.dx = self.xAxis[1] - self.xAxis[0]
        
        return self.xAxis, self.dx
    
    def recalculatePotential(self) -> np.ndarray:
        v0 = np.full(self.elementCount, self.basePotencial)
        
        for v0_fn in self.functionsModifyingPotential:
            v0 = v0_fn.modifyPotencial(v0)
        
        return v0
    
    def prepareMatrix(self) ->  tuple[np.ndarray, np.ndarray]:
        mainDiagonal = np.full([self.elementCount],-2)
        offDiagonal = np.ones([self.elementCount-1])  
        
        modifier = (-self.alpha/(self.dx**2))
        mainDiagonal = mainDiagonal * modifier
        offDiagonal = offDiagonal * modifier
        
        mainDiagonal += self.v0
        
        return mainDiagonal, offDiagonal
    
    def recalculatePresolve(self):
        self.xAxis, self.dx = self.recalculateXAxis()
        
        self.v0 = self.recalculatePotential()
        
        self.mainDiagonal, self.offDiagonal = self.prepareMatrix()
        
    def solveMatrix(self) -> tuple[np.ndarray, np.ndarray, float]:
        cas_start = time.time()
        self.E, self.psi = scipy.linalg.eigh_tridiagonal(self.mainDiagonal,self.offDiagonal)
        cas_konec = time.time()
        
        cas = cas_konec - cas_start
        
        return self.E, self.psi, cas

    def normalizePsi(self, psiMatrix: np.ndarray) -> np.ndarray:
        I = np.sum(self.dx*psiMatrix**2)
        A = 1/np.sqrt(I)
        n_psi = A*psiMatrix

        return n_psi