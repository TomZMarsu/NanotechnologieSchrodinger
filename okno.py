from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel, QComboBox, QSlider
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys

from grafy.potencialove_funkce.upravit_energii import Upravit_energii
from grafy.potencialove_funkce.vytvorit_parabolickou_jamu import Vytvorit_parabolickou_jamu
from grafy.situace import Situace

class Window(QDialog):
    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setGeometry(400, 400, 900, 900)
        plt.rcParams['text.usetex'] = True

        self.figure, self.ax = plt.subplots(layout='constrained')
        
        situace = self.nastrelit_situaci()
        self.vykreslit_graf(situace)
        
        self.canvas = FigureCanvas(self.figure)
        
        grid = QVBoxLayout()
        grid.addWidget(self.canvas)
        self.setLayout(grid)
        
    def nastrelit_situaci(self) -> Situace:
        situace = Situace(konec_osy=100,
                          posunout_psi_na_e=True,
                          normalizovat_vysledek=True,
                          pocet_vykreslenych_energetickych_hladin=30,
                          pocatek_osy=-10
                          )
        
        uprava_energie1 = Upravit_energii(situace, 10, 40, 0)
        uprava_energie2 = Vytvorit_parabolickou_jamu(situace, 40, 70, situace.energie)
        
        situace.funkce_upravujici_potencial.append(uprava_energie1)
        situace.funkce_upravujici_potencial.append(uprava_energie2)
        
        situace.prepocitat_pripravu()
        situace.vyresit_rovnici()
        
        return situace
    
    def vykreslit_graf(self, situace: Situace) -> None:
        for i in range(0,situace.pocet_vykreslenych_energetickych_hladin):
            matice_i = situace.psi.T[i]
            matice_i = situace.normalizovat_psi(matice_i)
            
            if situace.normalizovat_vysledek:
                matice_i = matice_i**2
            
            if situace.posunout_psi_na_e:
                matice_i += situace.E[i]

            if situace.hladiny_jsou_barevne_pruhy:
                heatmap_body_y = np.full(situace.pocet_prvku, situace.E[i])
                vyska = (situace.E[i+1] - situace.E[i])*situace.koeficient_vysky_pruhu
                self.ax.scatter(situace.osa_x,heatmap_body_y,c=matice_i, cmap="plasma", s=vyska)
            else:
                self.ax.plot(situace.osa_x,matice_i)

        if situace.bariera_na_sekundarni_ose:
            ax2 = self.ax.twinx()
            ax2.plot(situace.osa_x, situace.v0, color="black")
            ax2.set_ylabel("Energie bariery [-]")
            self.ax.set_ylabel(r"$\psi^2$ (Normalizováno) [-]")
        else:
            self.ax.plot(situace.osa_x, situace.v0, color="black")
            self.ax.set_ylabel(r"$\psi^2$ (Normalizováno) [-] / Potenciál $V$ [eV]")

        self.ax.set_xlabel("x [-]")
        
if __name__ == "__main__":
   # creating apyqt5 application
   app = QApplication(sys.argv)   # creating a window object
   main = Window()   # showing the window
   main.show()   # loop
   sys.exit(app.exec_())