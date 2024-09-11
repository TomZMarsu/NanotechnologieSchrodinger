# This Python file uses the following encoding: utf-8
import sys
import threading
import time
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from PySide6 import QtCore as qtc
from PySide6.QtGui import QDoubleValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from grafy.fyzika import eV, h_bar, nm
from grafy.potencialove_funkce.upravit_energii import Upravit_energii
from grafy.potencialove_funkce.vytvorit_parabolickou_jamu import Vytvorit_parabolickou_jamu
from grafy.situace import Situace
from ui import simulationStatus
from ui_form import Ui_Form

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        
        # Setup language
        self.translator = qtc.QTranslator(self)
        self.czechLocale = qtc.QLocale(qtc.QLocale.Language.Czech, qtc.QLocale.Country.CzechRepublic)
        self.englishLocale = qtc.QLocale(qtc.QLocale.Language.English, qtc.QLocale.Country.UnitedStates)
        self.setLocale(self.englishLocale)
        qtc.QLocale.setDefault(self.englishLocale)
        
        self.ui.setupUi(self)
        
        # Grafy
        # ====================================================
        # Simulation
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches

        self.figure, self.ax = plt.subplots(constrained_layout=True)
        self.ax2 = None
        self.simulationCanvas = FigureCanvas(self.figure)
        self.ui.simulationLayout.addWidget(self.simulationCanvas)
        
        # Resimulate button
        self.ui.resimulateButton.pressed.connect(self.resimulateButtonPressed)
        
        # Settings
        # ====================================================
        
        # Environment tab
        # ---------------------
        # MATRIX ELEMENT COUNT
        # ---
        self.ui.pocetPrvkuSlider.valueChanged.connect(self.pocetPrvkuSliderValueChanged)
        
        # PARTICLE WEIGHT
        # ---
        self.ui.particleWeightComboBox.currentTextChanged.connect(self.hmotnostCasticeComboBoxCurrentTextChanged)
        self.ui.customParticleWeightLineEdit.setValidator(self.createSpatialFloatValidator())
        
        # SIMULATION WIDTH
        # ---
        self.ui.simulationWidthLineEdit.setValidator(self.createSpatialFloatValidator())
        
        # BASE POTENTIAL
        # ---
        self.ui.basePotentialLineEdit.setValidator(self.createSpatialFloatValidator())
        
        # Situace
        # =====================================================
        self.situace: Situace = self.init_situace()
        self.resimulate()
       
        
        # Status bar
        # ====================================================
        # Language change
        # --- (events)
        self.ui.czechRadioButton.clicked.connect(self.czechRadioButtonPressed)
        self.ui.englishRadioButton.clicked.connect(self.englishRadioButtonPressed)
        
        self.ui.englishRadioButton.click()
    
    def getParticleWeight(self) -> float:
        weight_str = self.ui.particleWeightComboBox.currentText()
        
        if weight_str == qtc.QCoreApplication.translate("Form", "Elektron (9.109e-31)", None):
            return float(9.109e-31)
        elif weight_str == qtc.QCoreApplication.translate("Form", "Proton (1.673e-27)", None):
            return float(1.673e-27)
        else:
            return self.getLineEditFloat(self.ui.customParticleWeightLineEdit)
        
    def getLineEditFloat(self, lineEdit) -> float:
        return lineEdit.locale().toFloat(lineEdit.text())[0]
        
    def init_situace(self) -> Situace:
        situace = Situace()
        situace = self.getEnvironmentSettings(situace)
        
        return situace
        
    def getEnvironmentSettings(self, situace) -> Situace:
        situace.konec_osy = self.getLineEditFloat(self.ui.simulationWidthLineEdit)*nm
        situace.pocet_prvku = self.ui.pocetPrvkuSlider.value()
        situace.alfa = (h_bar**2)/(2*self.getParticleWeight())
        situace.energie = self.getLineEditFloat(self.ui.basePotentialLineEdit)*eV
        
        return situace
        

    @qtc.Slot()
    def pocetPrvkuSliderValueChanged(self, x:int):
        self.ui.pocetPrvkuCurrentLabel.setText(str(x))
        
    @qtc.Slot()
    def hmotnostCasticeComboBoxCurrentTextChanged(self, str):
        if(str=="Vlastní částice"):
            self.ui.customParticleWeightLineEdit.setEnabled(True)
        else:
            self.ui.customParticleWeightLineEdit.setEnabled(False)
            
    @qtc.Slot()
    def czechRadioButtonPressed(self, checked):
        if checked:
            self.translator.load("./lang/NanotechnologieSchrodinger_cs_CZ")
            QApplication.instance().installTranslator(self.translator)
            self.setLocale(self.czechLocale)
            self.translateUI()
            
    @qtc.Slot()
    def englishRadioButtonPressed(self, checked):
        if checked:
            self.translator.load("./lang/NanotechnologieSchrodinger_en_US")
            self.setLocale(self.englishLocale)
            self.translateUI()
    
    def translateFloatLineEdit(self, lineEdit:QLineEdit):
        lineEditLocale:qtc.QLocale = lineEdit.locale()
        lineEditValue:float = lineEditLocale.toFloat(lineEdit.text())[0]
        lineEdit.setLocale(self.locale())
        
        if lineEdit.validator():
            lineEdit.validator().setLocale(self.locale())
        
        if lineEdit.text() != "":
            lineEdit.setText(self.locale().toString(lineEditValue, format="g"))
        
        if lineEdit.text() == "inf":
            lineEdit.setText("")
    
    def translateUI(self):
        QApplication.instance().installTranslator(self.translator)
        # Retranslate rest
        self.ui.retranslateUi(self)
        simulationStatus.translateSimulationTime(self)
        simulationStatus.translateSimulationSize(self)
        
        # Set line edit decimals
        self.translateFloatLineEdit(self.ui.customParticleWeightLineEdit)
        self.translateFloatLineEdit(self.ui.basePotentialLineEdit)
        self.translateFloatLineEdit(self.ui.simulationWidthLineEdit)
        
        # Set locale for elements
        
    
    def createSpatialFloatValidator(self) -> QDoubleValidator:
        validator = QDoubleValidator()
        validator.setLocale(self.locale())
        validator.setRange(0,1.0e50)
        validator.setNotation(QDoubleValidator.Notation.ScientificNotation)
        
        return validator
    
    def resimulate(self):
        simulationStatus.setCurrentStatus(self, simulationStatus.SimulationStatus.IN_PROGRESS)
        thread = threading.Thread(target=self.resimulate_thread)
        thread.start()
    
    def resimulate_thread(self):
        
        self.situace = self.getEnvironmentSettings(self.situace)
        self.ax.clear()
        
        if self.ax2:
            self.ax2.clear()
        
        self.situace.prepocitat_pripravu()
        E,psi, computation_time = self.situace.vyresit_rovnici()
        
        plot_time_begin = time.time()
        self.vykreslit_graf(self.situace)
        self.simulationCanvas.draw()
        plot_time_end = time.time()
        
        total_time: float = (plot_time_end-plot_time_begin) + computation_time
        
        simulationStatus.setSimulationTime(self, total_time)
        simulationStatus.setSimulationSize(self, E, psi, self.situace.hlavni_diagonala, self.situace.vedlejsi_diagonala)
        simulationStatus.setCurrentStatus(self, simulationStatus.SimulationStatus.OK)
        
        
    
    @qtc.Slot()
    def resimulateButtonPressed(self):
        self.resimulate()
        
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
        self.osa_x_nm = situace.osa_x/nm
        self.v0_ev = situace.v0/eV
        
        for i in range(0,situace.pocet_vykreslenych_energetickych_hladin):
            matice_i = situace.psi.T[i]
            matice_i = situace.normalizovat_psi(matice_i)
            
            if situace.normalizovat_vysledek:
                matice_i = matice_i**2
            
            if situace.posunout_psi_na_e:
                matice_i += situace.E[i]/eV

            if situace.hladiny_jsou_barevne_pruhy:
                heatmap_body_y = np.full(situace.pocet_prvku, situace.E[i]/eV)
                vyska = (situace.E[i+1] - situace.E[i])*situace.koeficient_vysky_pruhu
                self.ax.scatter(self.osa_x_nm,heatmap_body_y,c=matice_i, cmap="plasma", s=vyska)
            else:
                self.ax.plot(self.osa_x_nm,matice_i)

        if situace.bariera_na_sekundarni_ose:
            if self.ax2 is None:
                self.ax2 = self.ax.twinx()
                
            self.ax2.plot(self.osa_x_nm, self.v0_ev, color="black")
            self.ax2.set_ylabel(qtc.QCoreApplication.translate("Form", "Potencial [eV]", None))
            self.ax.set_ylabel(qtc.QCoreApplication.translate("Form", "$Ψ^2$ [-]", None))
        else:
            self.ax.plot(self.osa_x_nm, self.v0_ev, color="black")
            self.ax.set_ylabel(f"{qtc.QCoreApplication.translate("Form", "$Ψ^2$ [-]", None)} / {qtc.QCoreApplication.translate("Form", "Potencial [eV]}", None)}")

        self.ax.set_xlabel(qtc.QCoreApplication.translate("Form", "x [nm]", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
