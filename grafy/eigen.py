import numpy as np # Knihovna pro lineární algebru, matice
import scipy
from typing import Final
from numbers import Real
import time

# Fyzika
m_e = 9.1093837139e-31
h_bar = 1.054571817e-34
eV = 1.602176634e-19
nm = 1e-9
FYZ_ALFA = (h_bar**2)/(2*m_e) # Pro nastavení fyzikálních veličin: (v sekci NASTAVENÍ) ALFA = FYZ_ALFA

# NASTAVENÍ (pod interními výpočty jsou tři případy, co lze například dělat)
# ===================================================================================================================================================
# Počáteční bod (v kódu je bug při nenulové hodnotě a DOPORUČUJI to prozatím nechat na 0)
POCATECNI_BOD: Final[Real] = 0.0

# Koncový bod mřížky
KONCOVY_BOD: Final[Real] = 40.0*nm

# Počet prvků/velikost matice (více prvků = přesnější výpočet, pomalejší program)
POCET_PRVKU: Final[int] = 100

# Fyzikalní konstanta (h_bar^2/2m), pro jednoduchost bývá nastavena jako 1
ALFA: Final[float] = FYZ_ALFA

# Základní potenciál bariéry. Pokud se neupraví (nevytvoří jáma) potenciál, bude v základu všude roven hodnotě této konstanty. 
# Pro parabolickou jámu je důležitá desetinná tečka (aby program to neuznal jako integer)
ENERGIE: Final[float] = 0.3*eV

# Normalizovat vlnovou funkci (umocnit na druhou?)
NORMALIZOVAT_VYSLEDEK: Final[bool] = True

# Zvednout vlnovou funkci na danou energetickou hladinu
POSUNOUT_PSI_NA_E: Final[bool] = False

# Pokud je bariéra velmi rozdílná od vlnové funkce/energetických hladin, lze přesunout bariéru na sekundární osu
BARIERA_NA_SEKUNDARNI_OSE: Final[bool] = True

# Počet vykreslených energetických hladin
POCET_VYKRESLENYCH_ENERGETICKYCH_HLADIN: Final[int] = 20

# Vykreslovat hladiny jako barevne pruhy
HLADINY_JSOU_BAREVNE_PRUHY: Final[bool] = False
KOEFICIENT_VYSKY_PRUHU: Final[float] = 10

# Nastavení PŘÍPADU 3
# -------------------------------
# Odstup od levé a pravé hrany simulace
offset = 100

# Šířka jedné mřížkové jámy
sirka = 10

# Rozestup/volný prostor mezi jámami
rozestup = 0
# -------------------------------
# ===================================================================================================================================================
# INTERNÍ VÝPOČTY (pod interními výpočty jsou tři případy, co lze například dělat)
# Vypocet ostatnich konstant
start = time.time()
osa_x = np.linspace(POCATECNI_BOD,KONCOVY_BOD,POCET_PRVKU)
dx = osa_x[1] - osa_x[0]
print(dx)
print(ALFA)

v0 = np.full(POCET_PRVKU, ENERGIE)

def x_pozice_v_poli(x: Real, velikost_pole: int = POCET_PRVKU, pocatek_osy: Real = POCATECNI_BOD, dx: float = dx) -> int:
    normalizacni_rozdil: float = -float(POCATECNI_BOD)
    x_normalizovano: float = float(x) + normalizacni_rozdil
    return int(x_normalizovano/dx)

def upravit_energii(pocatek, konec, energie):
    x_pocatek = int(pocatek*(1/dx))
    x_konec = int(konec*(1/dx))

    v0[x_pocatek:x_konec] = energie

def parabolicka_jama(pocatek, konec, energie_na_hrane):
    stred = pocatek+(konec-pocatek)/2
    x_stred = int(stred*(1/dx))
    x_pocatek = int(pocatek*(1/dx))
    x_konec = int(konec*(1/dx))
    strmost = energie_na_hrane/((x_pocatek-x_stred)**2)

    for x in range(x_pocatek,x_konec):
        v0[x] = strmost*(x-x_stred)**2

# PŘÍPADY (lze vytvořit vlastní, nebo odkomentovat/zakomentovat dané případy)
# -------------------------------------------

# Pripad 1 (tunelování, hranatá potenciálová jáma)
upravit_energii(14*nm,20*nm,0)
upravit_energii(25*nm,31*nm,0)

# Pripad 2 (parabolická jáma)
#parabolicka_jama(20,50,ENERGIE)
#parabolicka_jama(70,90,ENERGIE)

# Pripad 3 (krystalová mřížka)
#pocet_jam = int((KONCOVY_BOD-2*offset)/(sirka+rozestup))
#for i in range(pocet_jam):
#    pos = offset + i*(sirka+rozestup)
#    parabolicka_jama(pos,pos+sirka,ENERGIE)

# Pripad 4 (6nm idealni jama)
#upravit_energii(0*nm,10*nm,0)

# -------------------------------------------
# KONEC PŘÍPADŮ, VÝPOČET MATICE, VYKRESLENÍ...
end_init = time.time()

matice = np.zeros([POCET_PRVKU, POCET_PRVKU])

# Je prvek v matici? (funkce)
def jeVMatici(cislo: int) -> bool:
    if cislo >= 0 and cislo <= POCET_PRVKU-1:
        return True
    
    return False
    

# Vypln matici
for y in range(POCET_PRVKU):
    x0 = y-1
    x1 = y
    x2 = y+1

    nasobic = (-ALFA/(dx**2))

    if jeVMatici(x0):
        matice[y,x0] = 1 * nasobic
    
    if jeVMatici(x1):
        matice[y,x1] = -2 * nasobic + v0[y]

    if jeVMatici(x2):
        matice[y,x2] = 1 * nasobic

print(matice)

end_matrix = time.time()

E,psi = scipy.linalg.eigh_tridiagonal(np.diag(matice),np.diag(matice, k=-1))
end_s = time.time()

# VYKRESLOVÁNÍ MATICE



def normalizovat(psi_matice: np.ndarray) -> np.ndarray:
    I = np.sum(dx*psi_matice**2)
    A = 1/np.sqrt(I)
    n_psi = A*psi_matice

    return n_psi



for i in range(0,POCET_VYKRESLENYCH_ENERGETICKYCH_HLADIN):
    if E[i] > ENERGIE: break
    matice_i = psi.T[i]
    matice_i = normalizovat(matice_i)
    
    if NORMALIZOVAT_VYSLEDEK:
        matice_i = matice_i**2
    
    if POSUNOUT_PSI_NA_E:
        matice_i += E[i]

    if HLADINY_JSOU_BAREVNE_PRUHY:
        heatmap_body_y = np.full(POCET_PRVKU, E[i])
        vyska = (E[i+1] - E[i])*KOEFICIENT_VYSKY_PRUHU
        ax.scatter(osa_x,heatmap_body_y,c=matice_i, cmap="plasma", s=vyska)
    else:
        ax.plot(osa_x,matice_i)

if BARIERA_NA_SEKUNDARNI_OSE:
    ax2 = ax.twinx()
    ax2.plot(osa_x, v0, color="black")
    ax2.set_ylabel("Energie bariery [-]")
    ax.set_ylabel(r"$\psi^2$ (Normalizováno) [-]")
else:
    ax.plot(osa_x, v0, color="black")
    ax.set_ylabel(r"$\psi^2$ (Normalizováno) [-] / Potenciál $V$ [eV]")

ax.set_xlabel("x [-]")


#ax.plot(osa_x,n_psi**2)

end_vykres = time.time()

print(f"Init {end_init-start}")
print(f"Matice {end_matrix-end_init}")
print(f"Solve {end_s-end_matrix}")
print(f"Vykres {end_vykres-end_s}")
print(f"Celkem {end_vykres-start}")

plt.show()
