# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1042, 906)
        Form.setMinimumSize(QSize(0, 300))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.simulationGroupBox = QGroupBox(Form)
        self.simulationGroupBox.setObjectName(u"simulationGroupBox")
        self.simulationGroupBox.setMinimumSize(QSize(0, 300))
        self.verticalLayout_2 = QVBoxLayout(self.simulationGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.simulationLayout = QVBoxLayout()
        self.simulationLayout.setObjectName(u"simulationLayout")

        self.verticalLayout_2.addLayout(self.simulationLayout)


        self.verticalLayout.addWidget(self.simulationGroupBox)

        self.statusTopLine = QFrame(Form)
        self.statusTopLine.setObjectName(u"statusTopLine")
        self.statusTopLine.setFrameShape(QFrame.Shape.HLine)
        self.statusTopLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.statusTopLine)

        self.statusFrame = QFrame(Form)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setMaximumSize(QSize(16777215, 30))
        self.statusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.statusFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 2, -1, 2)
        self.statusLabelWidget = QWidget(self.statusFrame)
        self.statusLabelWidget.setObjectName(u"statusLabelWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.statusLabelWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.statusLabelTitle = QLabel(self.statusLabelWidget)
        self.statusLabelTitle.setObjectName(u"statusLabelTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabelTitle.sizePolicy().hasHeightForWidth())
        self.statusLabelTitle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.statusLabelTitle.setFont(font)

        self.horizontalLayout_2.addWidget(self.statusLabelTitle)

        self.statusLabelDisplay = QLabel(self.statusLabelWidget)
        self.statusLabelDisplay.setObjectName(u"statusLabelDisplay")
        self.statusLabelDisplay.setText(u"-")

        self.horizontalLayout_2.addWidget(self.statusLabelDisplay)


        self.horizontalLayout.addWidget(self.statusLabelWidget)

        self.simulationSizeLabelWidget = QWidget(self.statusFrame)
        self.simulationSizeLabelWidget.setObjectName(u"simulationSizeLabelWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.simulationSizeLabelWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.simulationSizeLabelTitle = QLabel(self.simulationSizeLabelWidget)
        self.simulationSizeLabelTitle.setObjectName(u"simulationSizeLabelTitle")
        sizePolicy.setHeightForWidth(self.simulationSizeLabelTitle.sizePolicy().hasHeightForWidth())
        self.simulationSizeLabelTitle.setSizePolicy(sizePolicy)
        self.simulationSizeLabelTitle.setFont(font)

        self.horizontalLayout_4.addWidget(self.simulationSizeLabelTitle)

        self.simulationSizeLabelDisplay = QLabel(self.simulationSizeLabelWidget)
        self.simulationSizeLabelDisplay.setObjectName(u"simulationSizeLabelDisplay")
        self.simulationSizeLabelDisplay.setText(u"0 B")

        self.horizontalLayout_4.addWidget(self.simulationSizeLabelDisplay)


        self.horizontalLayout.addWidget(self.simulationSizeLabelWidget)

        self.simulationTimeLabelWidget = QWidget(self.statusFrame)
        self.simulationTimeLabelWidget.setObjectName(u"simulationTimeLabelWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.simulationTimeLabelWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.simulationTimeLabelTitle = QLabel(self.simulationTimeLabelWidget)
        self.simulationTimeLabelTitle.setObjectName(u"simulationTimeLabelTitle")
        sizePolicy.setHeightForWidth(self.simulationTimeLabelTitle.sizePolicy().hasHeightForWidth())
        self.simulationTimeLabelTitle.setSizePolicy(sizePolicy)
        self.simulationTimeLabelTitle.setFont(font)

        self.horizontalLayout_7.addWidget(self.simulationTimeLabelTitle)

        self.simulationTimeLabelDisplay = QLabel(self.simulationTimeLabelWidget)
        self.simulationTimeLabelDisplay.setObjectName(u"simulationTimeLabelDisplay")
        self.simulationTimeLabelDisplay.setText(u"0.0 s")

        self.horizontalLayout_7.addWidget(self.simulationTimeLabelDisplay)


        self.horizontalLayout.addWidget(self.simulationTimeLabelWidget)

        self.clearSimulationButton = QPushButton(self.statusFrame)
        self.clearSimulationButton.setObjectName(u"clearSimulationButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clearSimulationButton.sizePolicy().hasHeightForWidth())
        self.clearSimulationButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.clearSimulationButton)

        self.resimulateButton = QPushButton(self.statusFrame)
        self.resimulateButton.setObjectName(u"resimulateButton")
        sizePolicy1.setHeightForWidth(self.resimulateButton.sizePolicy().hasHeightForWidth())
        self.resimulateButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.resimulateButton)


        self.verticalLayout.addWidget(self.statusFrame)

        self.statusBottomLine = QFrame(Form)
        self.statusBottomLine.setObjectName(u"statusBottomLine")
        self.statusBottomLine.setFrameShape(QFrame.Shape.HLine)
        self.statusBottomLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.statusBottomLine)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.environmentTab = QWidget()
        self.environmentTab.setObjectName(u"environmentTab")
        self.verticalLayout_4 = QVBoxLayout(self.environmentTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pocetPrvkuWidget = QWidget(self.environmentTab)
        self.pocetPrvkuWidget.setObjectName(u"pocetPrvkuWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pocetPrvkuWidget.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuWidget.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.pocetPrvkuWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pocetPrvkuMaximumLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuMaximumLabel.setObjectName(u"pocetPrvkuMaximumLabel")
        self.pocetPrvkuMaximumLabel.setText(u"2000")

        self.gridLayout.addWidget(self.pocetPrvkuMaximumLabel, 1, 3, 1, 1)

        self.pocetPrvkuLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuLabel.setObjectName(u"pocetPrvkuLabel")

        self.gridLayout.addWidget(self.pocetPrvkuLabel, 1, 0, 1, 1)

        self.pocetPrvkuSlider = QSlider(self.pocetPrvkuWidget)
        self.pocetPrvkuSlider.setObjectName(u"pocetPrvkuSlider")
        self.pocetPrvkuSlider.setMinimum(10)
        self.pocetPrvkuSlider.setMaximum(2000)
        self.pocetPrvkuSlider.setValue(500)
        self.pocetPrvkuSlider.setOrientation(Qt.Orientation.Horizontal)
        self.pocetPrvkuSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout.addWidget(self.pocetPrvkuSlider, 1, 2, 1, 1)

        self.pocetPrvkuMinimumLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuMinimumLabel.setObjectName(u"pocetPrvkuMinimumLabel")
        self.pocetPrvkuMinimumLabel.setText(u"10")

        self.gridLayout.addWidget(self.pocetPrvkuMinimumLabel, 1, 1, 1, 1)

        self.pocetPrvkuCurrentLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuCurrentLabel.setObjectName(u"pocetPrvkuCurrentLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pocetPrvkuCurrentLabel.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuCurrentLabel.setSizePolicy(sizePolicy3)
        self.pocetPrvkuCurrentLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pocetPrvkuCurrentLabel.setText(u"500")
        self.pocetPrvkuCurrentLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout.addWidget(self.pocetPrvkuCurrentLabel, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.pocetPrvkuWidget)

        self.simulationWidthWidget = QWidget(self.environmentTab)
        self.simulationWidthWidget.setObjectName(u"simulationWidthWidget")
        sizePolicy.setHeightForWidth(self.simulationWidthWidget.sizePolicy().hasHeightForWidth())
        self.simulationWidthWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.simulationWidthWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.simulationWidthLabel = QLabel(self.simulationWidthWidget)
        self.simulationWidthLabel.setObjectName(u"simulationWidthLabel")
        sizePolicy.setHeightForWidth(self.simulationWidthLabel.sizePolicy().hasHeightForWidth())
        self.simulationWidthLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.simulationWidthLabel)

        self.simulationWidthLineEdit = QLineEdit(self.simulationWidthWidget)
        self.simulationWidthLineEdit.setObjectName(u"simulationWidthLineEdit")
        self.simulationWidthLineEdit.setMaximumSize(QSize(200, 16777215))
        self.simulationWidthLineEdit.setText(u"100")
        self.simulationWidthLineEdit.setMaxLength(30)
        self.simulationWidthLineEdit.setPlaceholderText(u"")

        self.horizontalLayout_5.addWidget(self.simulationWidthLineEdit)


        self.verticalLayout_4.addWidget(self.simulationWidthWidget)

        self.basePotentialWidget = QWidget(self.environmentTab)
        self.basePotentialWidget.setObjectName(u"basePotentialWidget")
        sizePolicy.setHeightForWidth(self.basePotentialWidget.sizePolicy().hasHeightForWidth())
        self.basePotentialWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.basePotentialWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.basePotentialLabel = QLabel(self.basePotentialWidget)
        self.basePotentialLabel.setObjectName(u"basePotentialLabel")
        sizePolicy.setHeightForWidth(self.basePotentialLabel.sizePolicy().hasHeightForWidth())
        self.basePotentialLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.basePotentialLabel)

        self.basePotentialLineEdit = QLineEdit(self.basePotentialWidget)
        self.basePotentialLineEdit.setObjectName(u"basePotentialLineEdit")
        self.basePotentialLineEdit.setMaximumSize(QSize(200, 16777215))
        self.basePotentialLineEdit.setText(u"0.3")
        self.basePotentialLineEdit.setMaxLength(30)

        self.horizontalLayout_8.addWidget(self.basePotentialLineEdit)


        self.verticalLayout_4.addWidget(self.basePotentialWidget)

        self.particleWeightWidget = QWidget(self.environmentTab)
        self.particleWeightWidget.setObjectName(u"particleWeightWidget")
        sizePolicy.setHeightForWidth(self.particleWeightWidget.sizePolicy().hasHeightForWidth())
        self.particleWeightWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.particleWeightWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.particelWeightLabel = QLabel(self.particleWeightWidget)
        self.particelWeightLabel.setObjectName(u"particelWeightLabel")
        sizePolicy.setHeightForWidth(self.particelWeightLabel.sizePolicy().hasHeightForWidth())
        self.particelWeightLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.particelWeightLabel)

        self.particleWeightComboBox = QComboBox(self.particleWeightWidget)
        self.particleWeightComboBox.addItem("")
        self.particleWeightComboBox.addItem("")
        self.particleWeightComboBox.addItem("")
        self.particleWeightComboBox.setObjectName(u"particleWeightComboBox")
        self.particleWeightComboBox.setEnabled(True)
        self.particleWeightComboBox.setMinimumSize(QSize(200, 0))
        self.particleWeightComboBox.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.particleWeightComboBox)

        self.customParticleWeightLabel = QLabel(self.particleWeightWidget)
        self.customParticleWeightLabel.setObjectName(u"customParticleWeightLabel")
        sizePolicy.setHeightForWidth(self.customParticleWeightLabel.sizePolicy().hasHeightForWidth())
        self.customParticleWeightLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.customParticleWeightLabel)

        self.customParticleWeightLineEdit = QLineEdit(self.particleWeightWidget)
        self.customParticleWeightLineEdit.setObjectName(u"customParticleWeightLineEdit")
        self.customParticleWeightLineEdit.setEnabled(False)
        self.customParticleWeightLineEdit.setMaximumSize(QSize(200, 16777215))
        self.customParticleWeightLineEdit.setText(u"")
        self.customParticleWeightLineEdit.setMaxLength(30)

        self.horizontalLayout_6.addWidget(self.customParticleWeightLineEdit)


        self.verticalLayout_4.addWidget(self.particleWeightWidget)

        self.environmentTabVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.environmentTabVerticalSpacer)

        self.tabWidget.addTab(self.environmentTab, "")
        self.potencialTab = QWidget()
        self.potencialTab.setObjectName(u"potencialTab")
        self.horizontalLayout_9 = QHBoxLayout(self.potencialTab)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.addElementWidget = QWidget(self.potencialTab)
        self.addElementWidget.setObjectName(u"addElementWidget")
        self.addElementWidget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.addElementWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.addElementLabel = QLabel(self.addElementWidget)
        self.addElementLabel.setObjectName(u"addElementLabel")

        self.verticalLayout_5.addWidget(self.addElementLabel)

        self.addElementList = QListWidget(self.addElementWidget)
        QListWidgetItem(self.addElementList)
        QListWidgetItem(self.addElementList)
        self.addElementList.setObjectName(u"addElementList")

        self.verticalLayout_5.addWidget(self.addElementList)

        self.addElementButton = QPushButton(self.addElementWidget)
        self.addElementButton.setObjectName(u"addElementButton")

        self.verticalLayout_5.addWidget(self.addElementButton)


        self.horizontalLayout_9.addWidget(self.addElementWidget)

        self.elementListWidget = QWidget(self.potencialTab)
        self.elementListWidget.setObjectName(u"elementListWidget")
        self.elementListWidget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.elementListWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.elementListLabel = QLabel(self.elementListWidget)
        self.elementListLabel.setObjectName(u"elementListLabel")

        self.verticalLayout_6.addWidget(self.elementListLabel)

        self.elementListList = QListWidget(self.elementListWidget)
        QListWidgetItem(self.elementListList)
        QListWidgetItem(self.elementListList)
        self.elementListList.setObjectName(u"elementListList")

        self.verticalLayout_6.addWidget(self.elementListList)

        self.elementListButtonWidget = QWidget(self.elementListWidget)
        self.elementListButtonWidget.setObjectName(u"elementListButtonWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.elementListButtonWidget.sizePolicy().hasHeightForWidth())
        self.elementListButtonWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_11 = QHBoxLayout(self.elementListButtonWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.elementListRemoveButton = QPushButton(self.elementListButtonWidget)
        self.elementListRemoveButton.setObjectName(u"elementListRemoveButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(60)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.elementListRemoveButton.sizePolicy().hasHeightForWidth())
        self.elementListRemoveButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.elementListRemoveButton)

        self.elementListButtonDown = QPushButton(self.elementListButtonWidget)
        self.elementListButtonDown.setObjectName(u"elementListButtonDown")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(15)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.elementListButtonDown.sizePolicy().hasHeightForWidth())
        self.elementListButtonDown.setSizePolicy(sizePolicy6)

        self.horizontalLayout_11.addWidget(self.elementListButtonDown)

        self.elementListButtonUp = QPushButton(self.elementListButtonWidget)
        self.elementListButtonUp.setObjectName(u"elementListButtonUp")
        sizePolicy6.setHeightForWidth(self.elementListButtonUp.sizePolicy().hasHeightForWidth())
        self.elementListButtonUp.setSizePolicy(sizePolicy6)

        self.horizontalLayout_11.addWidget(self.elementListButtonUp)


        self.verticalLayout_6.addWidget(self.elementListButtonWidget)


        self.horizontalLayout_9.addWidget(self.elementListWidget)

        self.potentialDividerLine = QFrame(self.potencialTab)
        self.potentialDividerLine.setObjectName(u"potentialDividerLine")
        self.potentialDividerLine.setFrameShape(QFrame.Shape.VLine)
        self.potentialDividerLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.potentialDividerLine)

        self.editElementWidget = QWidget(self.potencialTab)
        self.editElementWidget.setObjectName(u"editElementWidget")
        self.verticalLayout_7 = QVBoxLayout(self.editElementWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.editElementTitleLabel = QLabel(self.editElementWidget)
        self.editElementTitleLabel.setObjectName(u"editElementTitleLabel")
        self.editElementTitleLabel.setFont(font)

        self.verticalLayout_7.addWidget(self.editElementTitleLabel)

        self.editElementStartWidget = QWidget(self.editElementWidget)
        self.editElementStartWidget.setObjectName(u"editElementStartWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.editElementStartWidget.sizePolicy().hasHeightForWidth())
        self.editElementStartWidget.setSizePolicy(sizePolicy7)
        self.gridLayout_2 = QGridLayout(self.editElementStartWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.editElementStartTitleLabel = QLabel(self.editElementStartWidget)
        self.editElementStartTitleLabel.setObjectName(u"editElementStartTitleLabel")

        self.gridLayout_2.addWidget(self.editElementStartTitleLabel, 1, 0, 1, 1)

        self.editElementStartSlider = QSlider(self.editElementStartWidget)
        self.editElementStartSlider.setObjectName(u"editElementStartSlider")
        self.editElementStartSlider.setValue(20)
        self.editElementStartSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.editElementStartSlider, 1, 1, 1, 1)

        self.editElementStartStatusLabel = QLabel(self.editElementStartWidget)
        self.editElementStartStatusLabel.setObjectName(u"editElementStartStatusLabel")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.editElementStartStatusLabel.sizePolicy().hasHeightForWidth())
        self.editElementStartStatusLabel.setSizePolicy(sizePolicy8)
        self.editElementStartStatusLabel.setText(u"20")
        self.editElementStartStatusLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.editElementStartStatusLabel, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.editElementStartWidget)

        self.editElementEndWidget = QWidget(self.editElementWidget)
        self.editElementEndWidget.setObjectName(u"editElementEndWidget")
        sizePolicy7.setHeightForWidth(self.editElementEndWidget.sizePolicy().hasHeightForWidth())
        self.editElementEndWidget.setSizePolicy(sizePolicy7)
        self.gridLayout_3 = QGridLayout(self.editElementEndWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.editElementEndTitleLabel = QLabel(self.editElementEndWidget)
        self.editElementEndTitleLabel.setObjectName(u"editElementEndTitleLabel")

        self.gridLayout_3.addWidget(self.editElementEndTitleLabel, 1, 0, 1, 1)

        self.editElementEndSlider = QSlider(self.editElementEndWidget)
        self.editElementEndSlider.setObjectName(u"editElementEndSlider")
        self.editElementEndSlider.setPageStep(10)
        self.editElementEndSlider.setValue(10)
        self.editElementEndSlider.setTracking(True)
        self.editElementEndSlider.setOrientation(Qt.Orientation.Horizontal)
        self.editElementEndSlider.setInvertedAppearance(True)
        self.editElementEndSlider.setInvertedControls(False)

        self.gridLayout_3.addWidget(self.editElementEndSlider, 1, 1, 1, 1)

        self.editElementEndStatusLabel = QLabel(self.editElementEndWidget)
        self.editElementEndStatusLabel.setObjectName(u"editElementEndStatusLabel")
        sizePolicy8.setHeightForWidth(self.editElementEndStatusLabel.sizePolicy().hasHeightForWidth())
        self.editElementEndStatusLabel.setSizePolicy(sizePolicy8)
        self.editElementEndStatusLabel.setText(u"50")
        self.editElementEndStatusLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_3.addWidget(self.editElementEndStatusLabel, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.editElementEndWidget)

        self.newPotentialWidget = QWidget(self.editElementWidget)
        self.newPotentialWidget.setObjectName(u"newPotentialWidget")
        sizePolicy.setHeightForWidth(self.newPotentialWidget.sizePolicy().hasHeightForWidth())
        self.newPotentialWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.newPotentialWidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.newPotentialLabel = QLabel(self.newPotentialWidget)
        self.newPotentialLabel.setObjectName(u"newPotentialLabel")
        sizePolicy.setHeightForWidth(self.newPotentialLabel.sizePolicy().hasHeightForWidth())
        self.newPotentialLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.newPotentialLabel)

        self.newPotentialLineEdit = QLineEdit(self.newPotentialWidget)
        self.newPotentialLineEdit.setObjectName(u"newPotentialLineEdit")
        self.newPotentialLineEdit.setMaximumSize(QSize(200, 16777215))
        self.newPotentialLineEdit.setMaxLength(5)

        self.horizontalLayout_10.addWidget(self.newPotentialLineEdit)


        self.verticalLayout_7.addWidget(self.newPotentialWidget)

        self.editElementVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.editElementVerticalSpacer)


        self.horizontalLayout_9.addWidget(self.editElementWidget)

        self.tabWidget.addTab(self.potencialTab, "")
        self.tunnelingTab = QWidget()
        self.tunnelingTab.setObjectName(u"tunnelingTab")
        self.horizontalLayout_18 = QHBoxLayout(self.tunnelingTab)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tunnelingGroupBox = QGroupBox(self.tunnelingTab)
        self.tunnelingGroupBox.setObjectName(u"tunnelingGroupBox")
        self.tunnelingGroupBox.setMinimumSize(QSize(600, 200))
        self.verticalLayout_3 = QVBoxLayout(self.tunnelingGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tunnelingFrame = QFrame(self.tunnelingGroupBox)
        self.tunnelingFrame.setObjectName(u"tunnelingFrame")
        self.tunnelingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tunnelingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.placeholderTunnelingLabel = QLabel(self.tunnelingFrame)
        self.placeholderTunnelingLabel.setObjectName(u"placeholderTunnelingLabel")
        self.placeholderTunnelingLabel.setGeometry(QRect(140, 180, 171, 16))

        self.verticalLayout_3.addWidget(self.tunnelingFrame)


        self.horizontalLayout_18.addWidget(self.tunnelingGroupBox)

        self.tunnelingScrollArea = QScrollArea(self.tunnelingTab)
        self.tunnelingScrollArea.setObjectName(u"tunnelingScrollArea")
        self.tunnelingScrollArea.setMaximumSize(QSize(400, 16777215))
        self.tunnelingScrollArea.setAutoFillBackground(False)
        self.tunnelingScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.tunnelingScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tunnelingScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tunnelingScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -240, 380, 686))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollAreaWidget = QWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setMaximumSize(QSize(370, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 9, -1)
        self.tunnelingHintLabel = QLabel(self.scrollAreaWidget)
        self.tunnelingHintLabel.setObjectName(u"tunnelingHintLabel")
        sizePolicy7.setHeightForWidth(self.tunnelingHintLabel.sizePolicy().hasHeightForWidth())
        self.tunnelingHintLabel.setSizePolicy(sizePolicy7)
        self.tunnelingHintLabel.setFont(font)
        self.tunnelingHintLabel.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.tunnelingHintLabel)

        self.tunnelingSectionAGroupBox = QGroupBox(self.scrollAreaWidget)
        self.tunnelingSectionAGroupBox.setObjectName(u"tunnelingSectionAGroupBox")
        self.verticalLayout_12 = QVBoxLayout(self.tunnelingSectionAGroupBox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tunnelingSectionAStartWidget = QWidget(self.tunnelingSectionAGroupBox)
        self.tunnelingSectionAStartWidget.setObjectName(u"tunnelingSectionAStartWidget")
        sizePolicy2.setHeightForWidth(self.tunnelingSectionAStartWidget.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionAStartWidget.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.tunnelingSectionAStartWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tunnelingSectionAStartStartLabel = QLabel(self.tunnelingSectionAStartWidget)
        self.tunnelingSectionAStartStartLabel.setObjectName(u"tunnelingSectionAStartStartLabel")
        self.tunnelingSectionAStartStartLabel.setText(u"10")

        self.gridLayout_4.addWidget(self.tunnelingSectionAStartStartLabel, 2, 1, 1, 1)

        self.tunnelingSectionAStartTitleLabel = QLabel(self.tunnelingSectionAStartWidget)
        self.tunnelingSectionAStartTitleLabel.setObjectName(u"tunnelingSectionAStartTitleLabel")

        self.gridLayout_4.addWidget(self.tunnelingSectionAStartTitleLabel, 2, 0, 1, 1)

        self.tunnelingSectionAStartEndRangeLabel = QLabel(self.tunnelingSectionAStartWidget)
        self.tunnelingSectionAStartEndRangeLabel.setObjectName(u"tunnelingSectionAStartEndRangeLabel")
        self.tunnelingSectionAStartEndRangeLabel.setText(u"2000")

        self.gridLayout_4.addWidget(self.tunnelingSectionAStartEndRangeLabel, 2, 3, 1, 1)

        self.tunnelingSectionAStartSlider = QSlider(self.tunnelingSectionAStartWidget)
        self.tunnelingSectionAStartSlider.setObjectName(u"tunnelingSectionAStartSlider")
        self.tunnelingSectionAStartSlider.setMinimum(10)
        self.tunnelingSectionAStartSlider.setMaximum(2000)
        self.tunnelingSectionAStartSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tunnelingSectionAStartSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_4.addWidget(self.tunnelingSectionAStartSlider, 2, 2, 1, 1)

        self.tunnelingSectionAStartDoubleSpinBox = QDoubleSpinBox(self.tunnelingSectionAStartWidget)
        self.tunnelingSectionAStartDoubleSpinBox.setObjectName(u"tunnelingSectionAStartDoubleSpinBox")
        sizePolicy1.setHeightForWidth(self.tunnelingSectionAStartDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionAStartDoubleSpinBox.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.tunnelingSectionAStartDoubleSpinBox, 1, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.tunnelingSectionAStartWidget)

        self.tunnelingSectionAEndWidget = QWidget(self.tunnelingSectionAGroupBox)
        self.tunnelingSectionAEndWidget.setObjectName(u"tunnelingSectionAEndWidget")
        sizePolicy2.setHeightForWidth(self.tunnelingSectionAEndWidget.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionAEndWidget.setSizePolicy(sizePolicy2)
        self.gridLayout_5 = QGridLayout(self.tunnelingSectionAEndWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tunnelingSectionAEndSlider = QSlider(self.tunnelingSectionAEndWidget)
        self.tunnelingSectionAEndSlider.setObjectName(u"tunnelingSectionAEndSlider")
        self.tunnelingSectionAEndSlider.setMinimum(10)
        self.tunnelingSectionAEndSlider.setMaximum(2000)
        self.tunnelingSectionAEndSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tunnelingSectionAEndSlider.setInvertedAppearance(True)
        self.tunnelingSectionAEndSlider.setInvertedControls(False)
        self.tunnelingSectionAEndSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_5.addWidget(self.tunnelingSectionAEndSlider, 2, 2, 1, 1)

        self.tunnelingSectionAEndTitleLabel = QLabel(self.tunnelingSectionAEndWidget)
        self.tunnelingSectionAEndTitleLabel.setObjectName(u"tunnelingSectionAEndTitleLabel")

        self.gridLayout_5.addWidget(self.tunnelingSectionAEndTitleLabel, 2, 0, 1, 1)

        self.tunnelingSectionAEndEndLabel = QLabel(self.tunnelingSectionAEndWidget)
        self.tunnelingSectionAEndEndLabel.setObjectName(u"tunnelingSectionAEndEndLabel")
        self.tunnelingSectionAEndEndLabel.setText(u"2000")

        self.gridLayout_5.addWidget(self.tunnelingSectionAEndEndLabel, 2, 3, 1, 1)

        self.tunnelingSectionAEndStartLabel = QLabel(self.tunnelingSectionAEndWidget)
        self.tunnelingSectionAEndStartLabel.setObjectName(u"tunnelingSectionAEndStartLabel")
        self.tunnelingSectionAEndStartLabel.setText(u"10")

        self.gridLayout_5.addWidget(self.tunnelingSectionAEndStartLabel, 2, 1, 1, 1)

        self.tunnelingSectionAEndDoubleSpinBox = QDoubleSpinBox(self.tunnelingSectionAEndWidget)
        self.tunnelingSectionAEndDoubleSpinBox.setObjectName(u"tunnelingSectionAEndDoubleSpinBox")
        sizePolicy1.setHeightForWidth(self.tunnelingSectionAEndDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionAEndDoubleSpinBox.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.tunnelingSectionAEndDoubleSpinBox, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.tunnelingSectionAEndWidget)


        self.verticalLayout_10.addWidget(self.tunnelingSectionAGroupBox)

        self.tunnelingSectionBGroupBox = QGroupBox(self.scrollAreaWidget)
        self.tunnelingSectionBGroupBox.setObjectName(u"tunnelingSectionBGroupBox")
        self.verticalLayout_13 = QVBoxLayout(self.tunnelingSectionBGroupBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tunnelingSectionBStartWidget = QWidget(self.tunnelingSectionBGroupBox)
        self.tunnelingSectionBStartWidget.setObjectName(u"tunnelingSectionBStartWidget")
        sizePolicy2.setHeightForWidth(self.tunnelingSectionBStartWidget.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionBStartWidget.setSizePolicy(sizePolicy2)
        self.gridLayout_6 = QGridLayout(self.tunnelingSectionBStartWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tunnelingSectionBStartSlider = QSlider(self.tunnelingSectionBStartWidget)
        self.tunnelingSectionBStartSlider.setObjectName(u"tunnelingSectionBStartSlider")
        self.tunnelingSectionBStartSlider.setMinimum(10)
        self.tunnelingSectionBStartSlider.setMaximum(2000)
        self.tunnelingSectionBStartSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tunnelingSectionBStartSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_6.addWidget(self.tunnelingSectionBStartSlider, 1, 2, 1, 1)

        self.tunnelingSectionBStartTitleLabel = QLabel(self.tunnelingSectionBStartWidget)
        self.tunnelingSectionBStartTitleLabel.setObjectName(u"tunnelingSectionBStartTitleLabel")

        self.gridLayout_6.addWidget(self.tunnelingSectionBStartTitleLabel, 1, 0, 1, 1)

        self.tunnelingSectionBStartEndLabel = QLabel(self.tunnelingSectionBStartWidget)
        self.tunnelingSectionBStartEndLabel.setObjectName(u"tunnelingSectionBStartEndLabel")
        self.tunnelingSectionBStartEndLabel.setText(u"2000")

        self.gridLayout_6.addWidget(self.tunnelingSectionBStartEndLabel, 1, 3, 1, 1)

        self.tunnelingSectionBStartStartLabel = QLabel(self.tunnelingSectionBStartWidget)
        self.tunnelingSectionBStartStartLabel.setObjectName(u"tunnelingSectionBStartStartLabel")
        self.tunnelingSectionBStartStartLabel.setText(u"10")

        self.gridLayout_6.addWidget(self.tunnelingSectionBStartStartLabel, 1, 1, 1, 1)

        self.tunnelingSectionBStartDoubleSpinBox = QDoubleSpinBox(self.tunnelingSectionBStartWidget)
        self.tunnelingSectionBStartDoubleSpinBox.setObjectName(u"tunnelingSectionBStartDoubleSpinBox")
        sizePolicy1.setHeightForWidth(self.tunnelingSectionBStartDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionBStartDoubleSpinBox.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.tunnelingSectionBStartDoubleSpinBox, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_13.addWidget(self.tunnelingSectionBStartWidget)

        self.tunnelingSectionBEndWidget = QWidget(self.tunnelingSectionBGroupBox)
        self.tunnelingSectionBEndWidget.setObjectName(u"tunnelingSectionBEndWidget")
        sizePolicy2.setHeightForWidth(self.tunnelingSectionBEndWidget.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionBEndWidget.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.tunnelingSectionBEndWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tunnelingSectionBEndSlider = QSlider(self.tunnelingSectionBEndWidget)
        self.tunnelingSectionBEndSlider.setObjectName(u"tunnelingSectionBEndSlider")
        self.tunnelingSectionBEndSlider.setMinimum(10)
        self.tunnelingSectionBEndSlider.setMaximum(2000)
        self.tunnelingSectionBEndSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tunnelingSectionBEndSlider.setInvertedAppearance(True)
        self.tunnelingSectionBEndSlider.setInvertedControls(False)
        self.tunnelingSectionBEndSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_7.addWidget(self.tunnelingSectionBEndSlider, 1, 2, 1, 1)

        self.tunnelingSectionBEndTitleLabel = QLabel(self.tunnelingSectionBEndWidget)
        self.tunnelingSectionBEndTitleLabel.setObjectName(u"tunnelingSectionBEndTitleLabel")

        self.gridLayout_7.addWidget(self.tunnelingSectionBEndTitleLabel, 1, 0, 1, 1)

        self.tunnelingSectionBEndEndLabel = QLabel(self.tunnelingSectionBEndWidget)
        self.tunnelingSectionBEndEndLabel.setObjectName(u"tunnelingSectionBEndEndLabel")
        self.tunnelingSectionBEndEndLabel.setText(u"2000")

        self.gridLayout_7.addWidget(self.tunnelingSectionBEndEndLabel, 1, 3, 1, 1)

        self.tunnelingSectionBEndStartLabel = QLabel(self.tunnelingSectionBEndWidget)
        self.tunnelingSectionBEndStartLabel.setObjectName(u"tunnelingSectionBEndStartLabel")
        self.tunnelingSectionBEndStartLabel.setText(u"10")

        self.gridLayout_7.addWidget(self.tunnelingSectionBEndStartLabel, 1, 1, 1, 1)

        self.tunnelingSectionBEndDoubleSpinBox = QDoubleSpinBox(self.tunnelingSectionBEndWidget)
        self.tunnelingSectionBEndDoubleSpinBox.setObjectName(u"tunnelingSectionBEndDoubleSpinBox")
        sizePolicy1.setHeightForWidth(self.tunnelingSectionBEndDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.tunnelingSectionBEndDoubleSpinBox.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.tunnelingSectionBEndDoubleSpinBox, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_13.addWidget(self.tunnelingSectionBEndWidget)


        self.verticalLayout_10.addWidget(self.tunnelingSectionBGroupBox)

        self.tunnelingContainLevelsAboveBarrierCheckBox = QCheckBox(self.scrollAreaWidget)
        self.tunnelingContainLevelsAboveBarrierCheckBox.setObjectName(u"tunnelingContainLevelsAboveBarrierCheckBox")

        self.verticalLayout_10.addWidget(self.tunnelingContainLevelsAboveBarrierCheckBox)

        self.tunnelingContainLevelsAboveBarrierWidget = QWidget(self.scrollAreaWidget)
        self.tunnelingContainLevelsAboveBarrierWidget.setObjectName(u"tunnelingContainLevelsAboveBarrierWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.tunnelingContainLevelsAboveBarrierWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tunnelingContainLevelsAboveBarrierSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.tunnelingContainLevelsAboveBarrierSpacer)

        self.tunnelingContainLevelsAboveBarrierSpinBox = QSpinBox(self.tunnelingContainLevelsAboveBarrierWidget)
        self.tunnelingContainLevelsAboveBarrierSpinBox.setObjectName(u"tunnelingContainLevelsAboveBarrierSpinBox")
        sizePolicy1.setHeightForWidth(self.tunnelingContainLevelsAboveBarrierSpinBox.sizePolicy().hasHeightForWidth())
        self.tunnelingContainLevelsAboveBarrierSpinBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.tunnelingContainLevelsAboveBarrierSpinBox)

        self.tunnelingContainLevelsAboveBarrierLabel = QLabel(self.tunnelingContainLevelsAboveBarrierWidget)
        self.tunnelingContainLevelsAboveBarrierLabel.setObjectName(u"tunnelingContainLevelsAboveBarrierLabel")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.tunnelingContainLevelsAboveBarrierLabel.sizePolicy().hasHeightForWidth())
        self.tunnelingContainLevelsAboveBarrierLabel.setSizePolicy(sizePolicy9)

        self.horizontalLayout_3.addWidget(self.tunnelingContainLevelsAboveBarrierLabel)


        self.verticalLayout_10.addWidget(self.tunnelingContainLevelsAboveBarrierWidget)

        self.tunnelingDirectionGroupBox = QGroupBox(self.scrollAreaWidget)
        self.tunnelingDirectionGroupBox.setObjectName(u"tunnelingDirectionGroupBox")
        self.verticalLayout_14 = QVBoxLayout(self.tunnelingDirectionGroupBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tunnelingDirectionAtoBRadioButton = QRadioButton(self.tunnelingDirectionGroupBox)
        self.tunnelingDirectionAtoBRadioButton.setObjectName(u"tunnelingDirectionAtoBRadioButton")

        self.verticalLayout_14.addWidget(self.tunnelingDirectionAtoBRadioButton)

        self.tunnelingDirectionBtoARadioButton = QRadioButton(self.tunnelingDirectionGroupBox)
        self.tunnelingDirectionBtoARadioButton.setObjectName(u"tunnelingDirectionBtoARadioButton")

        self.verticalLayout_14.addWidget(self.tunnelingDirectionBtoARadioButton)

        self.tunnelingDirectionTogetherRadioButton = QRadioButton(self.tunnelingDirectionGroupBox)
        self.tunnelingDirectionTogetherRadioButton.setObjectName(u"tunnelingDirectionTogetherRadioButton")

        self.verticalLayout_14.addWidget(self.tunnelingDirectionTogetherRadioButton)

        self.tunnelingDirectionSeparateRadioButton = QRadioButton(self.tunnelingDirectionGroupBox)
        self.tunnelingDirectionSeparateRadioButton.setObjectName(u"tunnelingDirectionSeparateRadioButton")

        self.verticalLayout_14.addWidget(self.tunnelingDirectionSeparateRadioButton)


        self.verticalLayout_10.addWidget(self.tunnelingDirectionGroupBox)


        self.verticalLayout_15.addWidget(self.scrollAreaWidget)

        self.tunnelingScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_18.addWidget(self.tunnelingScrollArea)

        self.tabWidget.addTab(self.tunnelingTab, "")
        self.resultTab = QWidget()
        self.resultTab.setObjectName(u"resultTab")
        self.verticalLayout_8 = QVBoxLayout(self.resultTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.resultWidget = QWidget(self.resultTab)
        self.resultWidget.setObjectName(u"resultWidget")
        self.horizontalLayout_13 = QHBoxLayout(self.resultWidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.resultEnergyLevelsGroupBox = QGroupBox(self.resultWidget)
        self.resultEnergyLevelsGroupBox.setObjectName(u"resultEnergyLevelsGroupBox")
        self.verticalLayout_11 = QVBoxLayout(self.resultEnergyLevelsGroupBox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.levelsSpecificRangeWidget = QWidget(self.resultEnergyLevelsGroupBox)
        self.levelsSpecificRangeWidget.setObjectName(u"levelsSpecificRangeWidget")
        self.horizontalLayout_14 = QHBoxLayout(self.levelsSpecificRangeWidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.levelsSpecificRangeRadioButton = QRadioButton(self.levelsSpecificRangeWidget)
        self.levelsSpecificRangeRadioButton.setObjectName(u"levelsSpecificRangeRadioButton")

        self.horizontalLayout_14.addWidget(self.levelsSpecificRangeRadioButton)

        self.levelsSpecificRangeFromLabel = QLabel(self.levelsSpecificRangeWidget)
        self.levelsSpecificRangeFromLabel.setObjectName(u"levelsSpecificRangeFromLabel")
        sizePolicy.setHeightForWidth(self.levelsSpecificRangeFromLabel.sizePolicy().hasHeightForWidth())
        self.levelsSpecificRangeFromLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.levelsSpecificRangeFromLabel)

        self.levelsSpecificRangeFromSpinBox = QSpinBox(self.levelsSpecificRangeWidget)
        self.levelsSpecificRangeFromSpinBox.setObjectName(u"levelsSpecificRangeFromSpinBox")
        self.levelsSpecificRangeFromSpinBox.setMinimum(1)
        self.levelsSpecificRangeFromSpinBox.setMaximum(1000)

        self.horizontalLayout_14.addWidget(self.levelsSpecificRangeFromSpinBox)

        self.levelsSpecificRangeToLabel = QLabel(self.levelsSpecificRangeWidget)
        self.levelsSpecificRangeToLabel.setObjectName(u"levelsSpecificRangeToLabel")
        sizePolicy.setHeightForWidth(self.levelsSpecificRangeToLabel.sizePolicy().hasHeightForWidth())
        self.levelsSpecificRangeToLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.levelsSpecificRangeToLabel)

        self.levelsSpecificRangeToSpinBox = QSpinBox(self.levelsSpecificRangeWidget)
        self.levelsSpecificRangeToSpinBox.setObjectName(u"levelsSpecificRangeToSpinBox")
        self.levelsSpecificRangeToSpinBox.setMinimum(1)
        self.levelsSpecificRangeToSpinBox.setMaximum(1000)
        self.levelsSpecificRangeToSpinBox.setValue(3)

        self.horizontalLayout_14.addWidget(self.levelsSpecificRangeToSpinBox)

        self.levelsSpecificRangeLevelLabel = QLabel(self.levelsSpecificRangeWidget)
        self.levelsSpecificRangeLevelLabel.setObjectName(u"levelsSpecificRangeLevelLabel")

        self.horizontalLayout_14.addWidget(self.levelsSpecificRangeLevelLabel)


        self.verticalLayout_11.addWidget(self.levelsSpecificRangeWidget)

        self.levelsHighestPotentialWidget = QWidget(self.resultEnergyLevelsGroupBox)
        self.levelsHighestPotentialWidget.setObjectName(u"levelsHighestPotentialWidget")
        self.horizontalLayout_15 = QHBoxLayout(self.levelsHighestPotentialWidget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.levelsHighestPotentialRadioButton = QRadioButton(self.levelsHighestPotentialWidget)
        self.levelsHighestPotentialRadioButton.setObjectName(u"levelsHighestPotentialRadioButton")

        self.horizontalLayout_15.addWidget(self.levelsHighestPotentialRadioButton)

        self.levelsHighestPotentialComboBox = QComboBox(self.levelsHighestPotentialWidget)
        self.levelsHighestPotentialComboBox.addItem("")
        self.levelsHighestPotentialComboBox.addItem("")
        self.levelsHighestPotentialComboBox.setObjectName(u"levelsHighestPotentialComboBox")

        self.horizontalLayout_15.addWidget(self.levelsHighestPotentialComboBox)

        self.levelsHighestPotentialSpinBox = QSpinBox(self.levelsHighestPotentialWidget)
        self.levelsHighestPotentialSpinBox.setObjectName(u"levelsHighestPotentialSpinBox")

        self.horizontalLayout_15.addWidget(self.levelsHighestPotentialSpinBox)


        self.verticalLayout_11.addWidget(self.levelsHighestPotentialWidget)

        self.levelsRangePotentialWidget = QWidget(self.resultEnergyLevelsGroupBox)
        self.levelsRangePotentialWidget.setObjectName(u"levelsRangePotentialWidget")
        self.horizontalLayout_16 = QHBoxLayout(self.levelsRangePotentialWidget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.levelsRangePotentialRadioButton = QRadioButton(self.levelsRangePotentialWidget)
        self.levelsRangePotentialRadioButton.setObjectName(u"levelsRangePotentialRadioButton")

        self.horizontalLayout_16.addWidget(self.levelsRangePotentialRadioButton)

        self.levelsRangePotentialFromLabel = QLabel(self.levelsRangePotentialWidget)
        self.levelsRangePotentialFromLabel.setObjectName(u"levelsRangePotentialFromLabel")
        sizePolicy.setHeightForWidth(self.levelsRangePotentialFromLabel.sizePolicy().hasHeightForWidth())
        self.levelsRangePotentialFromLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.levelsRangePotentialFromLabel)

        self.levelsRangePotentialFromSpinBox = QDoubleSpinBox(self.levelsRangePotentialWidget)
        self.levelsRangePotentialFromSpinBox.setObjectName(u"levelsRangePotentialFromSpinBox")

        self.horizontalLayout_16.addWidget(self.levelsRangePotentialFromSpinBox)

        self.levelsRangePotentialToLabel = QLabel(self.levelsRangePotentialWidget)
        self.levelsRangePotentialToLabel.setObjectName(u"levelsRangePotentialToLabel")
        sizePolicy.setHeightForWidth(self.levelsRangePotentialToLabel.sizePolicy().hasHeightForWidth())
        self.levelsRangePotentialToLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.levelsRangePotentialToLabel)

        self.levelsRangePotentialToSpinBox = QDoubleSpinBox(self.levelsRangePotentialWidget)
        self.levelsRangePotentialToSpinBox.setObjectName(u"levelsRangePotentialToSpinBox")

        self.horizontalLayout_16.addWidget(self.levelsRangePotentialToSpinBox)

        self.levelsRangePotentialUnitLabel = QLabel(self.levelsRangePotentialWidget)
        self.levelsRangePotentialUnitLabel.setObjectName(u"levelsRangePotentialUnitLabel")

        self.horizontalLayout_16.addWidget(self.levelsRangePotentialUnitLabel)


        self.verticalLayout_11.addWidget(self.levelsRangePotentialWidget)

        self.resultEnergyLevelsGroupBoxSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.resultEnergyLevelsGroupBoxSpacer)


        self.horizontalLayout_13.addWidget(self.resultEnergyLevelsGroupBox)

        self.resultCheckboxesWidhet = QWidget(self.resultWidget)
        self.resultCheckboxesWidhet.setObjectName(u"resultCheckboxesWidhet")
        self.verticalLayout_9 = QVBoxLayout(self.resultCheckboxesWidhet)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.secondaryAxisPotentialCheckBox = QCheckBox(self.resultCheckboxesWidhet)
        self.secondaryAxisPotentialCheckBox.setObjectName(u"secondaryAxisPotentialCheckBox")

        self.verticalLayout_9.addWidget(self.secondaryAxisPotentialCheckBox)

        self.psiAsECheckBox = QCheckBox(self.resultCheckboxesWidhet)
        self.psiAsECheckBox.setObjectName(u"psiAsECheckBox")

        self.verticalLayout_9.addWidget(self.psiAsECheckBox)

        self.squarePsiCheckBox = QCheckBox(self.resultCheckboxesWidhet)
        self.squarePsiCheckBox.setObjectName(u"squarePsiCheckBox")

        self.verticalLayout_9.addWidget(self.squarePsiCheckBox)

        self.psiAsColorBarCheckBox = QCheckBox(self.resultCheckboxesWidhet)
        self.psiAsColorBarCheckBox.setObjectName(u"psiAsColorBarCheckBox")

        self.verticalLayout_9.addWidget(self.psiAsColorBarCheckBox)

        self.colorBarHeightCoefficientWidget = QWidget(self.resultCheckboxesWidhet)
        self.colorBarHeightCoefficientWidget.setObjectName(u"colorBarHeightCoefficientWidget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.colorBarHeightCoefficientWidget.sizePolicy().hasHeightForWidth())
        self.colorBarHeightCoefficientWidget.setSizePolicy(sizePolicy10)
        self.colorBarHeightCoefficientWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_12 = QHBoxLayout(self.colorBarHeightCoefficientWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 200, -1)
        self.colorBarHeightCoefficientHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.colorBarHeightCoefficientHorizontalSpacer)

        self.colorBarHeightCoefficientLabel = QLabel(self.colorBarHeightCoefficientWidget)
        self.colorBarHeightCoefficientLabel.setObjectName(u"colorBarHeightCoefficientLabel")
        sizePolicy1.setHeightForWidth(self.colorBarHeightCoefficientLabel.sizePolicy().hasHeightForWidth())
        self.colorBarHeightCoefficientLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.colorBarHeightCoefficientLabel)

        self.colorBarHeightCoefficientLineEdit = QLineEdit(self.colorBarHeightCoefficientWidget)
        self.colorBarHeightCoefficientLineEdit.setObjectName(u"colorBarHeightCoefficientLineEdit")
        sizePolicy1.setHeightForWidth(self.colorBarHeightCoefficientLineEdit.sizePolicy().hasHeightForWidth())
        self.colorBarHeightCoefficientLineEdit.setSizePolicy(sizePolicy1)
        self.colorBarHeightCoefficientLineEdit.setMaximumSize(QSize(200, 16777215))
        self.colorBarHeightCoefficientLineEdit.setText(u"100")
        self.colorBarHeightCoefficientLineEdit.setMaxLength(5)
        self.colorBarHeightCoefficientLineEdit.setPlaceholderText(u"")

        self.horizontalLayout_12.addWidget(self.colorBarHeightCoefficientLineEdit)


        self.verticalLayout_9.addWidget(self.colorBarHeightCoefficientWidget)

        self.resultCheckboxesVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.resultCheckboxesVerticalSpacer)


        self.horizontalLayout_13.addWidget(self.resultCheckboxesWidhet)


        self.verticalLayout_8.addWidget(self.resultWidget)

        self.applyChangesButton = QPushButton(self.resultTab)
        self.applyChangesButton.setObjectName(u"applyChangesButton")
        sizePolicy1.setHeightForWidth(self.applyChangesButton.sizePolicy().hasHeightForWidth())
        self.applyChangesButton.setSizePolicy(sizePolicy1)
        self.applyChangesButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_8.addWidget(self.applyChangesButton, 0, Qt.AlignmentFlag.AlignRight)

        self.tabWidget.addTab(self.resultTab, "")
        self.energyLevelsTableTab = QWidget()
        self.energyLevelsTableTab.setObjectName(u"energyLevelsTableTab")
        self.verticalLayout_16 = QVBoxLayout(self.energyLevelsTableTab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.tableWidget = QTableWidget(self.energyLevelsTableTab)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setText(u"3");
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setText(u"1");
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setText(u"1");
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setText(u"18e3");
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setText(u"2");
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setText(u"4");
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setText(u"18e3");
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setText(u"3");
        self.tableWidget.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setText(u"9");
        self.tableWidget.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setText(u"18e3");
        self.tableWidget.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_16.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.energyLevelsTableTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.footerWidget = QWidget(Form)
        self.footerWidget.setObjectName(u"footerWidget")
        self.horizontalLayout_17 = QHBoxLayout(self.footerWidget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(9, 2, 9, 2)
        self.creditsLabel = QLabel(self.footerWidget)
        self.creditsLabel.setObjectName(u"creditsLabel")
        sizePolicy.setHeightForWidth(self.creditsLabel.sizePolicy().hasHeightForWidth())
        self.creditsLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.creditsLabel)

        self.githubLabel = QLabel(self.footerWidget)
        self.githubLabel.setObjectName(u"githubLabel")

        self.horizontalLayout_17.addWidget(self.githubLabel)

        self.languageWidget = QWidget(self.footerWidget)
        self.languageWidget.setObjectName(u"languageWidget")
        sizePolicy10.setHeightForWidth(self.languageWidget.sizePolicy().hasHeightForWidth())
        self.languageWidget.setSizePolicy(sizePolicy10)
        self.horizontalLayout_20 = QHBoxLayout(self.languageWidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.czechRadioButton = QRadioButton(self.languageWidget)
        self.czechRadioButton.setObjectName(u"czechRadioButton")
        sizePolicy1.setHeightForWidth(self.czechRadioButton.sizePolicy().hasHeightForWidth())
        self.czechRadioButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_20.addWidget(self.czechRadioButton)

        self.englishRadioButton = QRadioButton(self.languageWidget)
        self.englishRadioButton.setObjectName(u"englishRadioButton")
        sizePolicy1.setHeightForWidth(self.englishRadioButton.sizePolicy().hasHeightForWidth())
        self.englishRadioButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_20.addWidget(self.englishRadioButton)


        self.horizontalLayout_17.addWidget(self.languageWidget)

        self.licenseLabel = QLabel(self.footerWidget)
        self.licenseLabel.setObjectName(u"licenseLabel")
        sizePolicy.setHeightForWidth(self.licenseLabel.sizePolicy().hasHeightForWidth())
        self.licenseLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.licenseLabel)


        self.verticalLayout.addWidget(self.footerWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nanotechnologie - Schr\u00f6dingerov\u00e1 rovnice", None))
        self.simulationGroupBox.setTitle(QCoreApplication.translate("Form", u"Simulace", None))
        self.statusLabelTitle.setText(QCoreApplication.translate("Form", u"Stav simulace:", None))
        self.simulationSizeLabelTitle.setText(QCoreApplication.translate("Form", u"Velikost simulace:", None))
        self.simulationTimeLabelTitle.setText(QCoreApplication.translate("Form", u"Doba v\u00fdpo\u010dtu simulace:", None))
        self.clearSimulationButton.setText(QCoreApplication.translate("Form", u"Vy\u010distit simulaci", None))
        self.resimulateButton.setText(QCoreApplication.translate("Form", u"P\u0159epo\u010d\u00edtat simulaci", None))
        self.pocetPrvkuLabel.setText(QCoreApplication.translate("Form", u"Po\u010det simula\u010dn\u00edch prvk\u016f (v\u00edc prvk\u016f = vy\u0161\u0161\u00ed p\u0159esnost, vy\u0161\u0161\u00ed n\u00e1roky na v\u00fdpo\u010det a pam\u011b\u0165)", None))
        self.simulationWidthLabel.setText(QCoreApplication.translate("Form", u"\u0160\u00ed\u0159ka simulace (nm)", None))
        self.basePotentialLabel.setText(QCoreApplication.translate("Form", u"Z\u00e1kladn\u00ed hladina potenci\u00e1lu (eV)", None))
        self.basePotentialLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.3", None))
        self.particelWeightLabel.setText(QCoreApplication.translate("Form", u"Hmotnost \u010d\u00e1stice (kg)", None))
        self.particleWeightComboBox.setItemText(0, QCoreApplication.translate("Form", u"Elektron (9.109e-31)", None))
        self.particleWeightComboBox.setItemText(1, QCoreApplication.translate("Form", u"Proton (1.673e-27)", None))
        self.particleWeightComboBox.setItemText(2, QCoreApplication.translate("Form", u"Vlastn\u00ed \u010d\u00e1stice", None))

        self.customParticleWeightLabel.setText(QCoreApplication.translate("Form", u"nebo vlastn\u00ed hmotnost \u010d\u00e1stice (kg)", None))
        self.customParticleWeightLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"1.234e-56", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.environmentTab), QCoreApplication.translate("Form", u"Prost\u0159ed\u00ed", None))
        self.addElementLabel.setText(QCoreApplication.translate("Form", u"P\u0159idat prvek", None))

        __sortingEnabled = self.addElementList.isSortingEnabled()
        self.addElementList.setSortingEnabled(False)
        ___qlistwidgetitem = self.addElementList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Upravit energii", None));
        ___qlistwidgetitem1 = self.addElementList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"Potenci\u00e1lov\u00e1 j\u00e1ma", None));
        self.addElementList.setSortingEnabled(__sortingEnabled)

        self.addElementButton.setText(QCoreApplication.translate("Form", u"P\u0159idat prvek", None))
        self.elementListLabel.setText(QCoreApplication.translate("Form", u"Prvky v simulaci", None))

        __sortingEnabled1 = self.elementListList.isSortingEnabled()
        self.elementListList.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.elementListList.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"Upravit energii 1", None));
        ___qlistwidgetitem3 = self.elementListList.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"Potenci\u00e1lov\u00e1 j\u00e1ma 1", None));
        self.elementListList.setSortingEnabled(__sortingEnabled1)

        self.elementListRemoveButton.setText(QCoreApplication.translate("Form", u"Odebrat", None))
        self.elementListButtonDown.setText(QCoreApplication.translate("Form", u"\u2193", None))
        self.elementListButtonUp.setText(QCoreApplication.translate("Form", u" \u2191", None))
        self.editElementTitleLabel.setText(QCoreApplication.translate("Form", u"Upravit energii 1", None))
        self.editElementStartTitleLabel.setText(QCoreApplication.translate("Form", u"Po\u010d\u00e1tek \u00fapravy", None))
        self.editElementEndTitleLabel.setText(QCoreApplication.translate("Form", u"Konec \u00fapravy", None))
        self.newPotentialLabel.setText(QCoreApplication.translate("Form", u"Nov\u00fd potenci\u00e1l (eV)", None))
        self.newPotentialLineEdit.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.newPotentialLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.potencialTab), QCoreApplication.translate("Form", u"\u00dapr\u00e1va potenci\u00e1lu", None))
        self.tunnelingGroupBox.setTitle(QCoreApplication.translate("Form", u"Graf tunelov\u00e1n\u00ed", None))
        self.placeholderTunnelingLabel.setText(QCoreApplication.translate("Form", u"Zde bude T=f(E/E_B) graf", None))
        self.tunnelingHintLabel.setText(QCoreApplication.translate("Form", u"Vyberte dva \u00faseky (nap\u0159\u00edklad dv\u011b j\u00e1my) pro zm\u011b\u0159en\u00ed tunelov\u00e1n\u00ed", None))
        self.tunnelingSectionAGroupBox.setTitle(QCoreApplication.translate("Form", u"\u00dasek \u03a8a", None))
        self.tunnelingSectionAStartTitleLabel.setText(QCoreApplication.translate("Form", u"Po\u010d\u00e1tek \u00faseku", None))
        self.tunnelingSectionAEndTitleLabel.setText(QCoreApplication.translate("Form", u"Konec \u00faseku", None))
        self.tunnelingSectionBGroupBox.setTitle(QCoreApplication.translate("Form", u"\u00dasek \u03a8b", None))
        self.tunnelingSectionBStartTitleLabel.setText(QCoreApplication.translate("Form", u"Po\u010d\u00e1tek \u00faseku", None))
        self.tunnelingSectionBEndTitleLabel.setText(QCoreApplication.translate("Form", u"Konec \u00faseku", None))
        self.tunnelingContainLevelsAboveBarrierCheckBox.setText(QCoreApplication.translate("Form", u"Zahrnout hladiny nad bari\u00e9rou", None))
        self.tunnelingContainLevelsAboveBarrierLabel.setText(QCoreApplication.translate("Form", u"hladin nad bari\u00e9rou", None))
        self.tunnelingDirectionGroupBox.setTitle(QCoreApplication.translate("Form", u"Sm\u011br tunelov\u00e1n\u00ed", None))
        self.tunnelingDirectionAtoBRadioButton.setText(QCoreApplication.translate("Form", u"\u00dasek \u03a8a do \u00faseku \u03a8b", None))
        self.tunnelingDirectionBtoARadioButton.setText(QCoreApplication.translate("Form", u"\u00dasek \u03a8b do \u00faseku \u03a8a", None))
        self.tunnelingDirectionTogetherRadioButton.setText(QCoreApplication.translate("Form", u"Dohromady", None))
        self.tunnelingDirectionSeparateRadioButton.setText(QCoreApplication.translate("Form", u"Ka\u017ed\u00fd zvl\u00e1\u0161\u0165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tunnelingTab), QCoreApplication.translate("Form", u"Tunelov\u00e1n\u00ed", None))
        self.resultEnergyLevelsGroupBox.setTitle(QCoreApplication.translate("Form", u"Zobrazen\u00ed energetick\u00fdch hladin", None))
        self.levelsSpecificRangeRadioButton.setText(QCoreApplication.translate("Form", u"Ur\u010dit\u00fd po\u010det hladin (1-1000):", None))
        self.levelsSpecificRangeFromLabel.setText(QCoreApplication.translate("Form", u"od", None))
        self.levelsSpecificRangeToLabel.setText(QCoreApplication.translate("Form", u"do", None))
        self.levelsSpecificRangeLevelLabel.setText(QCoreApplication.translate("Form", u"hladiny", None))
        self.levelsHighestPotentialRadioButton.setText(QCoreApplication.translate("Form", u"(Po\u010det hladin) nad/pod nejvy\u0161\u0161\u00edm potenci\u00e1lem:", None))
        self.levelsHighestPotentialComboBox.setItemText(0, QCoreApplication.translate("Form", u"Nad", None))
        self.levelsHighestPotentialComboBox.setItemText(1, QCoreApplication.translate("Form", u"Pod", None))

        self.levelsRangePotentialRadioButton.setText(QCoreApplication.translate("Form", u"Hladiny o energi\u00ed:", None))
        self.levelsRangePotentialFromLabel.setText(QCoreApplication.translate("Form", u"od", None))
        self.levelsRangePotentialToLabel.setText(QCoreApplication.translate("Form", u"do", None))
        self.levelsRangePotentialUnitLabel.setText(QCoreApplication.translate("Form", u"eV", None))
        self.secondaryAxisPotentialCheckBox.setText(QCoreApplication.translate("Form", u"Zobrazit potenci\u00e1l na sekund\u00e1rn\u00ed ose", None))
        self.psiAsECheckBox.setText(QCoreApplication.translate("Form", u"Zvednout vlnovou funkci \u03c8 o danou energetickou hladinu ", None))
        self.squarePsiCheckBox.setText(QCoreApplication.translate("Form", u"P\u0159ev\u00e9st vlnovou funkci na hustotu pravd\u011bpodobnosti (\u03c8\u2192\u03c8\u03c8*)", None))
        self.psiAsColorBarCheckBox.setText(QCoreApplication.translate("Form", u"Zn\u00e1zornit vlnovou funkci jako barevn\u00fd pruh", None))
        self.colorBarHeightCoefficientLabel.setText(QCoreApplication.translate("Form", u"Koeficient v\u00fd\u0161ky barevn\u00e9ho pruhu", None))
        self.applyChangesButton.setText(QCoreApplication.translate("Form", u"Aplikovat zm\u011bny", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resultTab), QCoreApplication.translate("Form", u"Zobrazen\u00ed v\u00fdsledku", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"n", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"En [eV]", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u03a8max [-]", None));

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.energyLevelsTableTab), QCoreApplication.translate("Form", u"Tabulka energetick\u00fdch hladin", None))
        self.creditsLabel.setText(QCoreApplication.translate("Form", u"Vytvo\u0159il Tom\u00e1\u0161 Svoboda (256695@vutbr.cz)", None))
        self.githubLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a href=\"https://github.com/TomZMarsu/NanotechnologieSchrodinger\"><span style=\" text-decoration: underline; color:#007af4;\">Zdrojov\u00fd k\u00f3d (GitHub)</span></a></p></body></html>", None))
        self.czechRadioButton.setText(QCoreApplication.translate("Form", u"\u010cesky", None))
        self.englishRadioButton.setText(QCoreApplication.translate("Form", u"English", None))
        self.licenseLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a href=\"https://www.gnu.org/licenses/gpl-3.0.html\"><span style=\" text-decoration: underline; color:#007af4;\">GNU GPL v3.0</span></a></p></body></html>", None))
    # retranslateUi

