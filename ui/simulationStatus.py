import sys
import numpy as np

from PySide6.QtWidgets import QLabel
from mainwindow import MainWindow


def setSimulationTime(mw: MainWindow, time: float):
        timeLabel = mw.ui.simulationTimeLabelDisplay
        time_number: str = mw.locale().toString(time, format="f", precision=4)
        timeLabel.setText(f"{time_number} s")
        
def setSimulationSize(mw: MainWindow, E: np.ndarray, psi: np.ndarray, mainDiagonal: np.ndarray, offDiagonal: np.ndarray):
    size = sys.getsizeof(E) + sys.getsizeof(psi) + sys.getsizeof(mainDiagonal) + sys.getsizeof(offDiagonal)
    size_suffix: str = "B"
    
    if size/1e9 >= 1.0:
        size_suffix = "gB"
        size = size/1e9
    if size/1e6 >= 1.0:
        size_suffix = "mB"
        size = size/1e6
    if size/1e3 >= 1.0:
        size_suffix = "kB"
        size = size/1e3
    
    size_number: float = mw.ui.simulationSizeLabelDisplay.locale().toString(float(size), format="f", precision=3)
    mw.ui.simulationSizeLabelDisplay.setText(f"{size_number} {size_suffix}")
        
def translateSimulationTime(mw: MainWindow):
    label: QLabel = mw.ui.simulationTimeLabelDisplay
    splittedTimeStr: str = label.text().split(" ")
    timeSuffix: str = splittedTimeStr[1] 
    timeNumber: float = label.locale().toFloat(splittedTimeStr[0])[0]
    label.setLocale(mw.locale())
    timeNumberStr: str = label.locale().toString(timeNumber, format="f", precision=4)
    label.setText(f"{timeNumberStr} {timeSuffix}")
    
def translateSimulationSize(mw: MainWindow):
    label: QLabel = mw.ui.simulationSizeLabelDisplay
    splittedSizeStr: str = label.text().split(" ")
    sizeSuffix: str = splittedSizeStr[1] 
    sizeNumber: float = label.locale().toFloat(splittedSizeStr[0])[0]
    label.setLocale(mw.locale())
    sizeNumberStr: str = label.locale().toString(sizeNumber, format="f", precision=3)
    label.setText(f"{sizeNumberStr} {sizeSuffix}")
    
    