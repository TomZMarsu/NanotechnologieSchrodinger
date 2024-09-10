import numpy as np
import matplotlib.pyplot as plt
import math

# Konstanty
POCATECNI_BOD = 0
KONCOVY_BOD = 10
VELIKOST_MATICE = 200
ALFA = 1
E = 0.01

# Vypocet ostatnich konstant
h = math.sqrt((KONCOVY_BOD-POCATECNI_BOD)**2) / (VELIKOST_MATICE-1)
osa_x = np.zeros([VELIKOST_MATICE])
for y in range(VELIKOST_MATICE):
	osa_x[y] = POCATECNI_BOD + y*h

# Vyplneni prazdne matice A (AX=B)
A = np.zeros([VELIKOST_MATICE-2, VELIKOST_MATICE-2])

for y in range(0, VELIKOST_MATICE-2):
	x2 = y-1
	x1 = y
	x0 = y+1
	
	if x2>=0:
		A[y,x2] = 1
	
	A[y,x1] = -2
	
	if x0<=VELIKOST_MATICE-3:
		A[y,x0]=1

# Vyplneni prazdne matice B (AX=B)
B = np.zeros([VELIKOST_MATICE-2])

for y in range(1,VELIKOST_MATICE-1):
	B[y-1] = -ALFA*E*h**2
		

reseni_pocatecni_bod = 0
reseni_koncovy_bod = 0

print(reseni_pocatecni_bod)
print(reseni_koncovy_bod)

B[0] -= reseni_pocatecni_bod
B[VELIKOST_MATICE-3] -= reseni_koncovy_bod
print(B)

reseni = np.linalg.solve(A, B)

reseni = np.concatenate((np.array([reseni_pocatecni_bod]), reseni))
reseni = np.concatenate((reseni, np.array([reseni_koncovy_bod])))

plt.plot(osa_x,reseni)
plt.show()

