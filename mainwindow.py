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
from graph.physics import eV, h_bar, nm
from graph.potencialFunction.modifyPotential import ModifyEnergy
from graph.potencialFunction.createParabolicWell import CreateParabolicWell
from graph.situation import Situation
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
        self.ui.elementCountSlider.valueChanged.connect(self.elementCountSliderValueChanged)
        
        # PARTICLE WEIGHT
        # ---
        self.ui.particleMassComboBox.currentTextChanged.connect(self.particleMassComboBoxCurrentTextChanged)
        self.ui.customParticleMassLineEdit.setValidator(self.createSpatialFloatValidator())
        
        # SIMULATION WIDTH
        # ---
        self.ui.simulationWidthLineEdit.setValidator(self.createSpatialFloatValidator())
        
        # BASE POTENTIAL
        # ---
        self.ui.basePotentialLineEdit.setValidator(self.createSpatialFloatValidator())
        
        # Situace
        # =====================================================
        self.situation: Situation = self.init_situation()
        self.resimulate()
       
        
        # Status bar
        # ====================================================
        # Language change
        # --- (events)
        self.ui.czechRadioButton.clicked.connect(self.czechRadioButtonPressed)
        self.ui.englishRadioButton.clicked.connect(self.englishRadioButtonPressed)
        
        self.ui.englishRadioButton.click()
    
    def getParticleMass(self) -> float:
        weight_str = self.ui.particleMassComboBox.currentText()
        
        if weight_str == qtc.QCoreApplication.translate("Form", "Elektron (9.109e-31)", None):
            return float(9.109e-31)
        elif weight_str == qtc.QCoreApplication.translate("Form", "Proton (1.673e-27)", None):
            return float(1.673e-27)
        else:
            return self.getLineEditFloat(self.ui.customParticleMassLineEdit)
        
    def getLineEditFloat(self, lineEdit) -> float:
        return lineEdit.locale().toFloat(lineEdit.text())[0]
        
    def init_situation(self) -> Situation:
        situation = Situation()
        situation = self.getEnvironmentSettings(situation)
        
        return situation
        
    def getEnvironmentSettings(self, situation:Situation) -> Situation:
        situation.xAxisEnd = self.getLineEditFloat(self.ui.simulationWidthLineEdit)*nm
        situation.elementCount = self.ui.elementCountSlider.value()
        situation.alpha = (h_bar**2)/(2*self.getParticleMass())
        situation.basePotencial = self.getLineEditFloat(self.ui.basePotentialLineEdit)*eV
        
        return situation
        

    @qtc.Slot()
    def elementCountSliderValueChanged(self, x:int):
        self.ui.elementCountCurrentLabel.setText(str(x))
        
    @qtc.Slot()
    def particleMassComboBoxCurrentTextChanged(self, str):
        if(str==qtc.QCoreApplication.translate("Form", "Vlastní částice", None)):
            self.ui.customParticleMassLineEdit.setEnabled(True)
        else:
            self.ui.customParticleMassLineEdit.setEnabled(False)
            
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
        self.translateFloatLineEdit(self.ui.customParticleMassLineEdit)
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
        
        self.situation = self.getEnvironmentSettings(self.situation)
        self.figure.clear()
        
        self.situation.recalculatePresolve()
        E,psi, computation_time = self.situation.solveMatrix()
        
        plot_time_begin = time.time()
        self.drawSimulationGraph(self.situation)
        self.simulationCanvas.draw()
        plot_time_end = time.time()
        
        total_time: float = (plot_time_end-plot_time_begin) + computation_time
        
        simulationStatus.setSimulationTime(self, total_time)
        simulationStatus.setSimulationSize(self, E, psi, self.situation.mainDiagonal, self.situation.offDiagonal)
        simulationStatus.setCurrentStatus(self, simulationStatus.SimulationStatus.OK)
        
        
    
    @qtc.Slot()
    def resimulateButtonPressed(self):
        self.resimulate()
        
    def generateTestSituation(self) -> Situation:
        situation = Situation(xAxisEnd=100,
                          isPsiOnSameLevelAsE=True,
                          isResultNormalized=True,
                          energyLevelDrawCount=30,
                          xAxisStart=-10
                          )
        
        modifyPotencial1 = ModifyEnergy(situation, 10, 40, 0)
        modifyPotencial2 = CreateParabolicWell(situation, 40, 70, situation.basePotencial)
        
        situation.functionsModifyingPotential.append(modifyPotencial1)
        situation.functionsModifyingPotential.append(modifyPotencial2)
        
        situation.recalculatePresolve()
        situation.solveMatrix()
        
        return situation
    
    def drawSimulationGraph(self, situation: Situation) -> None:
        self.xAxis_nm = situation.xAxis/nm
        self.v0_ev = situation.v0/eV
        self.ax = self.figure.subplots()
        
        for i in range(0,situation.energyLevelDrawCount):
            matrix_i = situation.psi.T[i]
            matrix_i = situation.normalizePsi(matrix_i)
            
            if situation.isResultNormalized:
                matrix_i = matrix_i**2
            
            if situation.isPsiOnSameLavelAsE:
                matrix_i += situation.E[i]/eV

            if situation.isLevelColorbar:
                heatmap_body_y = np.full(situation.elementCount, situation.E[i]/eV)
                height = (situation.E[i+1] - situation.E[i])*situation.colorbarHeightCoeff
                self.ax.scatter(self.xAxis_nm,heatmap_body_y,c=matrix_i, cmap="plasma", s=height)
            else:
                self.ax.plot(self.xAxis_nm,matrix_i)

        if situation.isPotentialOnSecondaryAxis:
            self.ax2 = self.ax.twinx()
            self.ax2.plot(self.xAxis_nm, self.v0_ev, color="black")
            
            self.ax2.set_ylabel(qtc.QCoreApplication.translate("Form", "Potencial [eV]", None))
            self.ax.set_ylabel(qtc.QCoreApplication.translate("Form", "$Ψ^2$ [-]", None))
        else:
            self.ax.plot(self.xAxis_nm, self.v0_ev, color="black")
            self.ax.set_ylabel(f"{qtc.QCoreApplication.translate("Form", "$Ψ^2$ [-]", None)} / {qtc.QCoreApplication.translate("Form", "Potencial [eV]", None)}")

        self.ax.set_xlabel(qtc.QCoreApplication.translate("Form", "x [nm]", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
