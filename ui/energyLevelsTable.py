import numpy as np

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from typing import TYPE_CHECKING

from graph.physics import eV

if TYPE_CHECKING:
    from mainwindow import MainWindow

def addEntryToTable(mw: 'MainWindow', n: int, psiMax: float, En: float) -> None:
    table: QTableWidget = mw.ui.tableWidget
    
    tableItem_n: QTableWidgetItem = QTableWidgetItem(str(n))
    tableItem_psiMax: QTableWidgetItem = QTableWidgetItem(str(psiMax))
    tableItem_En: QTableWidgetItem = QTableWidgetItem(str(En/eV))
    
    table.setItem(n-1, 0, tableItem_n)
    table.setItem(n-1, 1, tableItem_psiMax)
    table.setItem(n-1, 2, tableItem_En)

def getPsiMax(psi: np.ndarray) -> float:
    return np.max(psi)

def setSimulationResultToTable(mw: 'MainWindow', E_array: np.ndarray, psi_array: np.ndarray) -> None:
    setTableDimensions(mw, E_array.shape[0])
    
    n: int = 1
    for En in E_array:
        psiMax: float = getPsiMax(psi_array[n-1])
        addEntryToTable(mw, n, psiMax, En)
        n = n + 1

def setTableDimensions(mw: 'MainWindow', E_arraySize: int) -> None:
    table: QTableWidget = mw.ui.tableWidget
    
    table.setRowCount(E_arraySize)