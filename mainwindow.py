# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore as qtc
from PySide6.QtGui import QDoubleValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from grafy.potencialove_funkce.upravit_energii import Upravit_energii
from grafy.potencialove_funkce.vytvorit_parabolickou_jamu import Vytvorit_parabolickou_jamu
from grafy.situace import Situace
from ui_form import Ui_Form

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Grafy
        # ====================================================
        # Simulation
        plt.rcParams['text.usetex'] = True
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches

        self.figure, self.ax = plt.subplots(constrained_layout=True)
        situace = self.nastrelit_situaci()
        self.vykreslit_graf(situace)
        self.simulationCanvas = FigureCanvas(self.figure)
        self.ui.simulationLayout.addWidget(self.simulationCanvas)
        
        
        
        # Settings
        # ====================================================
        
        # Environment tab
        # ---------------------
        # POCET PRVKU
        # ---
        self.ui.pocetPrvkuSlider.valueChanged.connect(self.pocetPrvkuSliderValueChanged)
        
        # HMOTNOST CASTICE
        # ---
        self.ui.hmotnostCasticeComboBox.addItems(["Elektron (9.109e-31)", "Proton (1.673e-27)", "Vlastní částice"])
        self.ui.hmotnostCasticeComboBox.currentTextChanged.connect(self.hmotnostCasticeComboBoxCurrentTextChanged)
        self.vlastniHmotnostCasticeLineEditValidator = QDoubleValidator()
        self.vlastniHmotnostCasticeLineEditValidator.setRange(0,1.0e50)
        self.vlastniHmotnostCasticeLineEditValidator.setNotation(QDoubleValidator.Notation.ScientificNotation)
        self.ui.vlastniHmotnostCasticeLineEdit.setValidator(self.vlastniHmotnostCasticeLineEditValidator)

    @qtc.Slot()
    def pocetPrvkuSliderValueChanged(self, x:int):
        self.ui.pocetPrvkuCurrentLabel.setText(str(x))
        
    @qtc.Slot()
    def hmotnostCasticeComboBoxCurrentTextChanged(self, str):
        if(str=="Vlastní částice"):
            self.ui.vlastniHmotnostCasticeLineEdit.setEnabled(True)
        else:
            self.ui.vlastniHmotnostCasticeLineEdit.setEnabled(False)
        
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
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
