# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

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
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
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

        self.horizontalLayout_2.addWidget(self.statusLabelDisplay)


        self.horizontalLayout.addWidget(self.statusLabelWidget)

        self.statusLabelWidget_2 = QWidget(self.statusFrame)
        self.statusLabelWidget_2.setObjectName(u"statusLabelWidget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.statusLabelWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.statusLabelTitle_3 = QLabel(self.statusLabelWidget_2)
        self.statusLabelTitle_3.setObjectName(u"statusLabelTitle_3")
        sizePolicy.setHeightForWidth(self.statusLabelTitle_3.sizePolicy().hasHeightForWidth())
        self.statusLabelTitle_3.setSizePolicy(sizePolicy)
        self.statusLabelTitle_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.statusLabelTitle_3)

        self.statusLabelDisplay_3 = QLabel(self.statusLabelWidget_2)
        self.statusLabelDisplay_3.setObjectName(u"statusLabelDisplay_3")

        self.horizontalLayout_4.addWidget(self.statusLabelDisplay_3)


        self.horizontalLayout.addWidget(self.statusLabelWidget_2)

        self.statusLabelWidget_3 = QWidget(self.statusFrame)
        self.statusLabelWidget_3.setObjectName(u"statusLabelWidget_3")
        self.horizontalLayout_7 = QHBoxLayout(self.statusLabelWidget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.statusLabelTitle_4 = QLabel(self.statusLabelWidget_3)
        self.statusLabelTitle_4.setObjectName(u"statusLabelTitle_4")
        sizePolicy.setHeightForWidth(self.statusLabelTitle_4.sizePolicy().hasHeightForWidth())
        self.statusLabelTitle_4.setSizePolicy(sizePolicy)
        self.statusLabelTitle_4.setFont(font)

        self.horizontalLayout_7.addWidget(self.statusLabelTitle_4)

        self.statusLabelDisplay_4 = QLabel(self.statusLabelWidget_3)
        self.statusLabelDisplay_4.setObjectName(u"statusLabelDisplay_4")

        self.horizontalLayout_7.addWidget(self.statusLabelDisplay_4)


        self.horizontalLayout.addWidget(self.statusLabelWidget_3)

        self.pushButton_6 = QPushButton(self.statusFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.resimulateButton = QPushButton(self.statusFrame)
        self.resimulateButton.setObjectName(u"resimulateButton")
        sizePolicy1.setHeightForWidth(self.resimulateButton.sizePolicy().hasHeightForWidth())
        self.resimulateButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.resimulateButton)


        self.verticalLayout.addWidget(self.statusFrame)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.environmentTab = QWidget()
        self.environmentTab.setObjectName(u"environmentTab")
        self.verticalLayout_4 = QVBoxLayout(self.environmentTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pocetPrvkuWidget = QWidget(self.environmentTab)
        self.pocetPrvkuWidget.setObjectName(u"pocetPrvkuWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pocetPrvkuWidget.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuWidget.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.pocetPrvkuWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pocetPrvkuMaximumLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuMaximumLabel.setObjectName(u"pocetPrvkuMaximumLabel")

        self.gridLayout.addWidget(self.pocetPrvkuMaximumLabel, 1, 3, 1, 1)

        self.pocetPrvkuLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuLabel.setObjectName(u"pocetPrvkuLabel")

        self.gridLayout.addWidget(self.pocetPrvkuLabel, 1, 0, 1, 1)

        self.pocetPrvkuSlider = QSlider(self.pocetPrvkuWidget)
        self.pocetPrvkuSlider.setObjectName(u"pocetPrvkuSlider")
        self.pocetPrvkuSlider.setMinimum(10)
        self.pocetPrvkuSlider.setMaximum(2000)
        self.pocetPrvkuSlider.setOrientation(Qt.Orientation.Horizontal)
        self.pocetPrvkuSlider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout.addWidget(self.pocetPrvkuSlider, 1, 2, 1, 1)

        self.pocetPrvkuMinimumLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuMinimumLabel.setObjectName(u"pocetPrvkuMinimumLabel")

        self.gridLayout.addWidget(self.pocetPrvkuMinimumLabel, 1, 1, 1, 1)

        self.pocetPrvkuCurrentLabel = QLabel(self.pocetPrvkuWidget)
        self.pocetPrvkuCurrentLabel.setObjectName(u"pocetPrvkuCurrentLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pocetPrvkuCurrentLabel.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuCurrentLabel.setSizePolicy(sizePolicy3)
        self.pocetPrvkuCurrentLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pocetPrvkuCurrentLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout.addWidget(self.pocetPrvkuCurrentLabel, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.pocetPrvkuWidget)

        self.konecOsyWidget = QWidget(self.environmentTab)
        self.konecOsyWidget.setObjectName(u"konecOsyWidget")
        sizePolicy.setHeightForWidth(self.konecOsyWidget.sizePolicy().hasHeightForWidth())
        self.konecOsyWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.konecOsyWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.konecOsyLabel = QLabel(self.konecOsyWidget)
        self.konecOsyLabel.setObjectName(u"konecOsyLabel")
        sizePolicy.setHeightForWidth(self.konecOsyLabel.sizePolicy().hasHeightForWidth())
        self.konecOsyLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.konecOsyLabel)

        self.konecOsyLineEdit = QLineEdit(self.konecOsyWidget)
        self.konecOsyLineEdit.setObjectName(u"konecOsyLineEdit")
        self.konecOsyLineEdit.setMaximumSize(QSize(200, 16777215))
        self.konecOsyLineEdit.setMaxLength(5)

        self.horizontalLayout_5.addWidget(self.konecOsyLineEdit)


        self.verticalLayout_4.addWidget(self.konecOsyWidget)

        self.energieWidget = QWidget(self.environmentTab)
        self.energieWidget.setObjectName(u"energieWidget")
        sizePolicy.setHeightForWidth(self.energieWidget.sizePolicy().hasHeightForWidth())
        self.energieWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.energieWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.energieLabel = QLabel(self.energieWidget)
        self.energieLabel.setObjectName(u"energieLabel")
        sizePolicy.setHeightForWidth(self.energieLabel.sizePolicy().hasHeightForWidth())
        self.energieLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.energieLabel)

        self.energieLineEdit = QLineEdit(self.energieWidget)
        self.energieLineEdit.setObjectName(u"energieLineEdit")
        self.energieLineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_8.addWidget(self.energieLineEdit)


        self.verticalLayout_4.addWidget(self.energieWidget)

        self.hmotnostCasticeWidget = QWidget(self.environmentTab)
        self.hmotnostCasticeWidget.setObjectName(u"hmotnostCasticeWidget")
        sizePolicy.setHeightForWidth(self.hmotnostCasticeWidget.sizePolicy().hasHeightForWidth())
        self.hmotnostCasticeWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.hmotnostCasticeWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.hmotnostCasticeLabel = QLabel(self.hmotnostCasticeWidget)
        self.hmotnostCasticeLabel.setObjectName(u"hmotnostCasticeLabel")
        sizePolicy.setHeightForWidth(self.hmotnostCasticeLabel.sizePolicy().hasHeightForWidth())
        self.hmotnostCasticeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.hmotnostCasticeLabel)

        self.hmotnostCasticeComboBox = QComboBox(self.hmotnostCasticeWidget)
        self.hmotnostCasticeComboBox.setObjectName(u"hmotnostCasticeComboBox")
        self.hmotnostCasticeComboBox.setEnabled(True)
        self.hmotnostCasticeComboBox.setMinimumSize(QSize(200, 0))
        self.hmotnostCasticeComboBox.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.hmotnostCasticeComboBox)

        self.vlastniHmotnostCasticeLabel = QLabel(self.hmotnostCasticeWidget)
        self.vlastniHmotnostCasticeLabel.setObjectName(u"vlastniHmotnostCasticeLabel")
        sizePolicy.setHeightForWidth(self.vlastniHmotnostCasticeLabel.sizePolicy().hasHeightForWidth())
        self.vlastniHmotnostCasticeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.vlastniHmotnostCasticeLabel)

        self.vlastniHmotnostCasticeLineEdit = QLineEdit(self.hmotnostCasticeWidget)
        self.vlastniHmotnostCasticeLineEdit.setObjectName(u"vlastniHmotnostCasticeLineEdit")
        self.vlastniHmotnostCasticeLineEdit.setEnabled(False)
        self.vlastniHmotnostCasticeLineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.vlastniHmotnostCasticeLineEdit)


        self.verticalLayout_4.addWidget(self.hmotnostCasticeWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.environmentTab, "")
        self.potencialTab = QWidget()
        self.potencialTab.setObjectName(u"potencialTab")
        self.horizontalLayout_9 = QHBoxLayout(self.potencialTab)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget = QWidget(self.potencialTab)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.listWidget = QListWidget(self.widget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_5.addWidget(self.listWidget)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.horizontalLayout_9.addWidget(self.widget)

        self.widget_2 = QWidget(self.potencialTab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.listWidget_2 = QListWidget(self.widget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_6.addWidget(self.listWidget_2)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_4 = QPushButton(self.widget_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(60)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(15)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_11.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy6.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy6)

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.verticalLayout_6.addWidget(self.widget_6)


        self.horizontalLayout_9.addWidget(self.widget_2)

        self.line = QFrame(self.potencialTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line)

        self.widget_3 = QWidget(self.potencialTab)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy7)
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.horizontalSlider = QSlider(self.widget_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setValue(20)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy8)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy7.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy7)
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.widget_5)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setPageStep(10)
        self.horizontalSlider_2.setValue(10)
        self.horizontalSlider_2.setTracking(True)
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setInvertedAppearance(True)
        self.horizontalSlider_2.setInvertedControls(False)

        self.gridLayout_3.addWidget(self.horizontalSlider_2, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy8.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy8)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_5)

        self.konecOsyWidget_2 = QWidget(self.widget_3)
        self.konecOsyWidget_2.setObjectName(u"konecOsyWidget_2")
        sizePolicy.setHeightForWidth(self.konecOsyWidget_2.sizePolicy().hasHeightForWidth())
        self.konecOsyWidget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.konecOsyWidget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.konecOsyLabel_2 = QLabel(self.konecOsyWidget_2)
        self.konecOsyLabel_2.setObjectName(u"konecOsyLabel_2")
        sizePolicy.setHeightForWidth(self.konecOsyLabel_2.sizePolicy().hasHeightForWidth())
        self.konecOsyLabel_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.konecOsyLabel_2)

        self.konecOsyLineEdit_2 = QLineEdit(self.konecOsyWidget_2)
        self.konecOsyLineEdit_2.setObjectName(u"konecOsyLineEdit_2")
        self.konecOsyLineEdit_2.setMaximumSize(QSize(200, 16777215))
        self.konecOsyLineEdit_2.setMaxLength(5)

        self.horizontalLayout_10.addWidget(self.konecOsyLineEdit_2)


        self.verticalLayout_7.addWidget(self.konecOsyWidget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_9.addWidget(self.widget_3)

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
        self.label_17 = QLabel(self.tunnelingFrame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(140, 180, 171, 16))

        self.verticalLayout_3.addWidget(self.tunnelingFrame)


        self.horizontalLayout_18.addWidget(self.tunnelingGroupBox)

        self.scrollArea = QScrollArea(self.tunnelingTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(400, 16777215))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 686))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_13 = QWidget(self.scrollAreaWidgetContents)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(370, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widget_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 9, -1)
        self.label_18 = QLabel(self.widget_13)
        self.label_18.setObjectName(u"label_18")
        sizePolicy7.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy7)
        self.label_18.setFont(font)
        self.label_18.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_18)

        self.groupBox_2 = QGroupBox(self.widget_13)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pocetPrvkuWidget_2 = QWidget(self.groupBox_2)
        self.pocetPrvkuWidget_2.setObjectName(u"pocetPrvkuWidget_2")
        sizePolicy2.setHeightForWidth(self.pocetPrvkuWidget_2.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuWidget_2.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.pocetPrvkuWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pocetPrvkuSlider_2 = QSlider(self.pocetPrvkuWidget_2)
        self.pocetPrvkuSlider_2.setObjectName(u"pocetPrvkuSlider_2")
        self.pocetPrvkuSlider_2.setMinimum(10)
        self.pocetPrvkuSlider_2.setMaximum(2000)
        self.pocetPrvkuSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.pocetPrvkuSlider_2.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_4.addWidget(self.pocetPrvkuSlider_2, 1, 2, 1, 1)

        self.pocetPrvkuLabel_2 = QLabel(self.pocetPrvkuWidget_2)
        self.pocetPrvkuLabel_2.setObjectName(u"pocetPrvkuLabel_2")

        self.gridLayout_4.addWidget(self.pocetPrvkuLabel_2, 1, 0, 1, 1)

        self.pocetPrvkuMaximumLabel_2 = QLabel(self.pocetPrvkuWidget_2)
        self.pocetPrvkuMaximumLabel_2.setObjectName(u"pocetPrvkuMaximumLabel_2")

        self.gridLayout_4.addWidget(self.pocetPrvkuMaximumLabel_2, 1, 3, 1, 1)

        self.pocetPrvkuMinimumLabel_2 = QLabel(self.pocetPrvkuWidget_2)
        self.pocetPrvkuMinimumLabel_2.setObjectName(u"pocetPrvkuMinimumLabel_2")

        self.gridLayout_4.addWidget(self.pocetPrvkuMinimumLabel_2, 1, 1, 1, 1)

        self.spinBox_4 = QSpinBox(self.pocetPrvkuWidget_2)
        self.spinBox_4.setObjectName(u"spinBox_4")
        sizePolicy1.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy1)
        self.spinBox_4.setValue(20)

        self.gridLayout_4.addWidget(self.spinBox_4, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.pocetPrvkuWidget_2)

        self.pocetPrvkuWidget_3 = QWidget(self.groupBox_2)
        self.pocetPrvkuWidget_3.setObjectName(u"pocetPrvkuWidget_3")
        sizePolicy2.setHeightForWidth(self.pocetPrvkuWidget_3.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuWidget_3.setSizePolicy(sizePolicy2)
        self.gridLayout_5 = QGridLayout(self.pocetPrvkuWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pocetPrvkuSlider_3 = QSlider(self.pocetPrvkuWidget_3)
        self.pocetPrvkuSlider_3.setObjectName(u"pocetPrvkuSlider_3")
        self.pocetPrvkuSlider_3.setMinimum(10)
        self.pocetPrvkuSlider_3.setMaximum(2000)
        self.pocetPrvkuSlider_3.setOrientation(Qt.Orientation.Horizontal)
        self.pocetPrvkuSlider_3.setInvertedAppearance(True)
        self.pocetPrvkuSlider_3.setInvertedControls(False)
        self.pocetPrvkuSlider_3.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_5.addWidget(self.pocetPrvkuSlider_3, 1, 2, 1, 1)

        self.pocetPrvkuLabel_3 = QLabel(self.pocetPrvkuWidget_3)
        self.pocetPrvkuLabel_3.setObjectName(u"pocetPrvkuLabel_3")

        self.gridLayout_5.addWidget(self.pocetPrvkuLabel_3, 1, 0, 1, 1)

        self.pocetPrvkuMaximumLabel_3 = QLabel(self.pocetPrvkuWidget_3)
        self.pocetPrvkuMaximumLabel_3.setObjectName(u"pocetPrvkuMaximumLabel_3")

        self.gridLayout_5.addWidget(self.pocetPrvkuMaximumLabel_3, 1, 3, 1, 1)

        self.pocetPrvkuMinimumLabel_3 = QLabel(self.pocetPrvkuWidget_3)
        self.pocetPrvkuMinimumLabel_3.setObjectName(u"pocetPrvkuMinimumLabel_3")

        self.gridLayout_5.addWidget(self.pocetPrvkuMinimumLabel_3, 1, 1, 1, 1)

        self.spinBox_5 = QSpinBox(self.pocetPrvkuWidget_3)
        self.spinBox_5.setObjectName(u"spinBox_5")
        sizePolicy1.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy1)
        self.spinBox_5.setValue(20)

        self.gridLayout_5.addWidget(self.spinBox_5, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.pocetPrvkuWidget_3)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_13)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pocetPrvkuWidget_4 = QWidget(self.groupBox_3)
        self.pocetPrvkuWidget_4.setObjectName(u"pocetPrvkuWidget_4")
        sizePolicy2.setHeightForWidth(self.pocetPrvkuWidget_4.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuWidget_4.setSizePolicy(sizePolicy2)
        self.gridLayout_6 = QGridLayout(self.pocetPrvkuWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pocetPrvkuSlider_4 = QSlider(self.pocetPrvkuWidget_4)
        self.pocetPrvkuSlider_4.setObjectName(u"pocetPrvkuSlider_4")
        self.pocetPrvkuSlider_4.setMinimum(10)
        self.pocetPrvkuSlider_4.setMaximum(2000)
        self.pocetPrvkuSlider_4.setOrientation(Qt.Orientation.Horizontal)
        self.pocetPrvkuSlider_4.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_6.addWidget(self.pocetPrvkuSlider_4, 1, 2, 1, 1)

        self.pocetPrvkuLabel_4 = QLabel(self.pocetPrvkuWidget_4)
        self.pocetPrvkuLabel_4.setObjectName(u"pocetPrvkuLabel_4")

        self.gridLayout_6.addWidget(self.pocetPrvkuLabel_4, 1, 0, 1, 1)

        self.pocetPrvkuMaximumLabel_4 = QLabel(self.pocetPrvkuWidget_4)
        self.pocetPrvkuMaximumLabel_4.setObjectName(u"pocetPrvkuMaximumLabel_4")

        self.gridLayout_6.addWidget(self.pocetPrvkuMaximumLabel_4, 1, 3, 1, 1)

        self.pocetPrvkuMinimumLabel_4 = QLabel(self.pocetPrvkuWidget_4)
        self.pocetPrvkuMinimumLabel_4.setObjectName(u"pocetPrvkuMinimumLabel_4")

        self.gridLayout_6.addWidget(self.pocetPrvkuMinimumLabel_4, 1, 1, 1, 1)

        self.spinBox_6 = QSpinBox(self.pocetPrvkuWidget_4)
        self.spinBox_6.setObjectName(u"spinBox_6")
        sizePolicy1.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy1)
        self.spinBox_6.setValue(20)

        self.gridLayout_6.addWidget(self.spinBox_6, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_13.addWidget(self.pocetPrvkuWidget_4)

        self.pocetPrvkuWidget_5 = QWidget(self.groupBox_3)
        self.pocetPrvkuWidget_5.setObjectName(u"pocetPrvkuWidget_5")
        sizePolicy2.setHeightForWidth(self.pocetPrvkuWidget_5.sizePolicy().hasHeightForWidth())
        self.pocetPrvkuWidget_5.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.pocetPrvkuWidget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pocetPrvkuSlider_5 = QSlider(self.pocetPrvkuWidget_5)
        self.pocetPrvkuSlider_5.setObjectName(u"pocetPrvkuSlider_5")
        self.pocetPrvkuSlider_5.setMinimum(10)
        self.pocetPrvkuSlider_5.setMaximum(2000)
        self.pocetPrvkuSlider_5.setOrientation(Qt.Orientation.Horizontal)
        self.pocetPrvkuSlider_5.setInvertedAppearance(True)
        self.pocetPrvkuSlider_5.setInvertedControls(False)
        self.pocetPrvkuSlider_5.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_7.addWidget(self.pocetPrvkuSlider_5, 1, 2, 1, 1)

        self.pocetPrvkuLabel_5 = QLabel(self.pocetPrvkuWidget_5)
        self.pocetPrvkuLabel_5.setObjectName(u"pocetPrvkuLabel_5")

        self.gridLayout_7.addWidget(self.pocetPrvkuLabel_5, 1, 0, 1, 1)

        self.pocetPrvkuMaximumLabel_5 = QLabel(self.pocetPrvkuWidget_5)
        self.pocetPrvkuMaximumLabel_5.setObjectName(u"pocetPrvkuMaximumLabel_5")

        self.gridLayout_7.addWidget(self.pocetPrvkuMaximumLabel_5, 1, 3, 1, 1)

        self.pocetPrvkuMinimumLabel_5 = QLabel(self.pocetPrvkuWidget_5)
        self.pocetPrvkuMinimumLabel_5.setObjectName(u"pocetPrvkuMinimumLabel_5")

        self.gridLayout_7.addWidget(self.pocetPrvkuMinimumLabel_5, 1, 1, 1, 1)

        self.spinBox_7 = QSpinBox(self.pocetPrvkuWidget_5)
        self.spinBox_7.setObjectName(u"spinBox_7")
        sizePolicy1.setHeightForWidth(self.spinBox_7.sizePolicy().hasHeightForWidth())
        self.spinBox_7.setSizePolicy(sizePolicy1)
        self.spinBox_7.setValue(20)

        self.gridLayout_7.addWidget(self.spinBox_7, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_13.addWidget(self.pocetPrvkuWidget_5)


        self.verticalLayout_10.addWidget(self.groupBox_3)

        self.checkBox_5 = QCheckBox(self.widget_13)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_10.addWidget(self.checkBox_5)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.spinBox_8 = QSpinBox(self.widget_14)
        self.spinBox_8.setObjectName(u"spinBox_8")
        sizePolicy1.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.spinBox_8)

        self.label_19 = QLabel(self.widget_14)
        self.label_19.setObjectName(u"label_19")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy9)

        self.horizontalLayout_3.addWidget(self.label_19)


        self.verticalLayout_10.addWidget(self.widget_14)

        self.groupBox_4 = QGroupBox(self.widget_13)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_4 = QRadioButton(self.groupBox_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_14.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox_4)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_14.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox_4)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout_14.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.groupBox_4)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.verticalLayout_14.addWidget(self.radioButton_7)


        self.verticalLayout_10.addWidget(self.groupBox_4)


        self.verticalLayout_15.addWidget(self.widget_13)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_18.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tunnelingTab, "")
        self.resultTab = QWidget()
        self.resultTab.setObjectName(u"resultTab")
        self.verticalLayout_8 = QVBoxLayout(self.resultTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_7 = QWidget(self.resultTab)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox = QGroupBox(self.widget_7)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_9 = QWidget(self.groupBox)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.radioButton = QRadioButton(self.widget_9)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_14.addWidget(self.radioButton)

        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_9)

        self.spinBox_2 = QSpinBox(self.widget_9)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(1000)

        self.horizontalLayout_14.addWidget(self.spinBox_2)

        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_8)

        self.spinBox = QSpinBox(self.widget_9)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setValue(3)

        self.horizontalLayout_14.addWidget(self.spinBox)

        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_14.addWidget(self.label_10)


        self.verticalLayout_11.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.groupBox)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.radioButton_2 = QRadioButton(self.widget_10)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_15.addWidget(self.radioButton_2)

        self.comboBox = QComboBox(self.widget_10)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_15.addWidget(self.comboBox)

        self.spinBox_3 = QSpinBox(self.widget_10)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_15.addWidget(self.spinBox_3)


        self.verticalLayout_11.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.groupBox)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.radioButton_3 = QRadioButton(self.widget_11)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_16.addWidget(self.radioButton_3)

        self.label_11 = QLabel(self.widget_11)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.label_11)

        self.doubleSpinBox = QDoubleSpinBox(self.widget_11)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_16.addWidget(self.doubleSpinBox)

        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.label_12)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.widget_11)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_2)

        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)


        self.verticalLayout_11.addWidget(self.widget_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)


        self.horizontalLayout_13.addWidget(self.groupBox)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_9 = QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_9.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.widget_8)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_9.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.widget_8)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_9.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.widget_8)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_9.addWidget(self.checkBox_4)

        self.konecOsyWidget_3 = QWidget(self.widget_8)
        self.konecOsyWidget_3.setObjectName(u"konecOsyWidget_3")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.konecOsyWidget_3.sizePolicy().hasHeightForWidth())
        self.konecOsyWidget_3.setSizePolicy(sizePolicy10)
        self.konecOsyWidget_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_12 = QHBoxLayout(self.konecOsyWidget_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 200, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.konecOsyLabel_3 = QLabel(self.konecOsyWidget_3)
        self.konecOsyLabel_3.setObjectName(u"konecOsyLabel_3")
        sizePolicy1.setHeightForWidth(self.konecOsyLabel_3.sizePolicy().hasHeightForWidth())
        self.konecOsyLabel_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.konecOsyLabel_3)

        self.konecOsyLineEdit_3 = QLineEdit(self.konecOsyWidget_3)
        self.konecOsyLineEdit_3.setObjectName(u"konecOsyLineEdit_3")
        sizePolicy1.setHeightForWidth(self.konecOsyLineEdit_3.sizePolicy().hasHeightForWidth())
        self.konecOsyLineEdit_3.setSizePolicy(sizePolicy1)
        self.konecOsyLineEdit_3.setMaximumSize(QSize(200, 16777215))
        self.konecOsyLineEdit_3.setMaxLength(5)

        self.horizontalLayout_12.addWidget(self.konecOsyLineEdit_3)


        self.verticalLayout_9.addWidget(self.konecOsyWidget_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout_13.addWidget(self.widget_8)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.pushButton_5 = QPushButton(self.resultTab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_8.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignRight)

        self.tabWidget.addTab(self.resultTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_16 = QVBoxLayout(self.tab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.tableWidget = QTableWidget(self.tab)
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
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_16.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.widget_12 = QWidget(Form)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(9, 2, 9, 2)
        self.label_14 = QLabel(self.widget_12)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_14)

        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_17.addWidget(self.label_15)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy10.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy10)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.radioButton_8 = QRadioButton(self.widget_15)
        self.radioButton_8.setObjectName(u"radioButton_8")
        sizePolicy1.setHeightForWidth(self.radioButton_8.sizePolicy().hasHeightForWidth())
        self.radioButton_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_20.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.widget_15)
        self.radioButton_9.setObjectName(u"radioButton_9")
        sizePolicy1.setHeightForWidth(self.radioButton_9.sizePolicy().hasHeightForWidth())
        self.radioButton_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_20.addWidget(self.radioButton_9)


        self.horizontalLayout_17.addWidget(self.widget_15)

        self.label_16 = QLabel(self.widget_12)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_16)


        self.verticalLayout.addWidget(self.widget_12)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nanotechnologie - Schr\u00f6dingerov\u00e1 rovnice", None))
        self.simulationGroupBox.setTitle(QCoreApplication.translate("Form", u"Simulace", None))
        self.statusLabelTitle.setText(QCoreApplication.translate("Form", u"Stav simulace:", None))
        self.statusLabelDisplay.setText(QCoreApplication.translate("Form", u"OK", None))
        self.statusLabelTitle_3.setText(QCoreApplication.translate("Form", u"Velikost simulace:", None))
        self.statusLabelDisplay_3.setText(QCoreApplication.translate("Form", u"10kB", None))
        self.statusLabelTitle_4.setText(QCoreApplication.translate("Form", u"Doba v\u00fdpo\u010dtu simulace:", None))
        self.statusLabelDisplay_4.setText(QCoreApplication.translate("Form", u"0.7 s", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Vy\u010distit simulaci", None))
        self.resimulateButton.setText(QCoreApplication.translate("Form", u"P\u0159epo\u010d\u00edtat simulaci", None))
        self.pocetPrvkuMaximumLabel.setText(QCoreApplication.translate("Form", u"2000", None))
        self.pocetPrvkuLabel.setText(QCoreApplication.translate("Form", u"Po\u010det simula\u010dn\u00edch prvk\u016f (v\u00edc prvk\u016f = vy\u0161\u0161\u00ed p\u0159esnost, vy\u0161\u0161\u00ed n\u00e1roky na v\u00fdpo\u010det a pam\u011b\u0165)", None))
        self.pocetPrvkuMinimumLabel.setText(QCoreApplication.translate("Form", u"10", None))
        self.pocetPrvkuCurrentLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>20</p></body></html>", None))
        self.konecOsyLabel.setText(QCoreApplication.translate("Form", u"\u0160\u00ed\u0159ka simulace (nm)", None))
        self.konecOsyLineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.konecOsyLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.energieLabel.setText(QCoreApplication.translate("Form", u"Z\u00e1kladn\u00ed hladina potenci\u00e1lu (eV)", None))
        self.energieLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.3", None))
        self.hmotnostCasticeLabel.setText(QCoreApplication.translate("Form", u"Hmotnost \u010d\u00e1stice (kg)", None))
        self.vlastniHmotnostCasticeLabel.setText(QCoreApplication.translate("Form", u"nebo vlastn\u00ed hmotnost \u010d\u00e1stice (kg)", None))
        self.vlastniHmotnostCasticeLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"1.234e-56", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.environmentTab), QCoreApplication.translate("Form", u"Prost\u0159ed\u00ed", None))
        self.label.setText(QCoreApplication.translate("Form", u"P\u0159idat prvek", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Upravit energii", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"Potenci\u00e1lov\u00e1 j\u00e1ma", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Form", u"P\u0159idat prvek", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Prvky v simulaci", None))

        __sortingEnabled1 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_2.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"Upravit energii 1", None));
        ___qlistwidgetitem3 = self.listWidget_2.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"Potenci\u00e1lov\u00e1 j\u00e1ma 1", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled1)

        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Odebrat", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u2193", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u" \u2191", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Upravit energii 1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Po\u010d\u00e1tek \u00fapravy", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"20", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Konec \u00fapravy", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"50", None))
        self.konecOsyLabel_2.setText(QCoreApplication.translate("Form", u"Nov\u00fd potenci\u00e1l (eV)", None))
        self.konecOsyLineEdit_2.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.konecOsyLineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.potencialTab), QCoreApplication.translate("Form", u"\u00dapr\u00e1va potenci\u00e1lu", None))
        self.tunnelingGroupBox.setTitle(QCoreApplication.translate("Form", u"Graf tunelov\u00e1n\u00ed", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Zde bude T=f(E/E_B) graf", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Vyberte dva \u00faseky (nap\u0159\u00edklad dv\u011b j\u00e1my) pro zm\u011b\u0159en\u00ed tunelov\u00e1n\u00ed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u00dasek \u03a8a", None))
        self.pocetPrvkuLabel_2.setText(QCoreApplication.translate("Form", u"Po\u010d\u00e1tek \u00faseku", None))
        self.pocetPrvkuMaximumLabel_2.setText(QCoreApplication.translate("Form", u"2000", None))
        self.pocetPrvkuMinimumLabel_2.setText(QCoreApplication.translate("Form", u"10", None))
        self.pocetPrvkuLabel_3.setText(QCoreApplication.translate("Form", u"Konec \u00faseku", None))
        self.pocetPrvkuMaximumLabel_3.setText(QCoreApplication.translate("Form", u"2000", None))
        self.pocetPrvkuMinimumLabel_3.setText(QCoreApplication.translate("Form", u"10", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u00dasek \u03a8b", None))
        self.pocetPrvkuLabel_4.setText(QCoreApplication.translate("Form", u"Po\u010d\u00e1tek \u00faseku", None))
        self.pocetPrvkuMaximumLabel_4.setText(QCoreApplication.translate("Form", u"2000", None))
        self.pocetPrvkuMinimumLabel_4.setText(QCoreApplication.translate("Form", u"10", None))
        self.pocetPrvkuLabel_5.setText(QCoreApplication.translate("Form", u"Konec \u00faseku", None))
        self.pocetPrvkuMaximumLabel_5.setText(QCoreApplication.translate("Form", u"2000", None))
        self.pocetPrvkuMinimumLabel_5.setText(QCoreApplication.translate("Form", u"10", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"Zahrnout hladiny nad bari\u00e9rou", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"hladin nad bari\u00e9rou", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Sm\u011br tunelov\u00e1n\u00ed", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u00dasek \u03a8a do \u00faseku \u03a8b", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u00dasek \u03a8b do \u00faseku \u03a8a", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"Dohromady", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"Ka\u017ed\u00fd zvl\u00e1\u0161\u0165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tunnelingTab), QCoreApplication.translate("Form", u"Tunelov\u00e1n\u00ed", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Zobrazen\u00ed energetick\u00fdch hladin", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Ur\u010dit\u00fd po\u010det hladin (1-1000):", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"od", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"do", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"hladiny", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"(Po\u010det hladin) nad/pod nejvy\u0161\u0161\u00edm potenci\u00e1lem:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Nad", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Pod", None))

        self.radioButton_3.setText(QCoreApplication.translate("Form", u"Hladiny o energi\u00ed:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"od", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"do", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"eV", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Zobrazit potenci\u00e1l na sekund\u00e1rn\u00ed ose", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Zvednout vlnovou funkci \u03c8 o danou energetickou hladinu ", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"P\u0159ev\u00e9st vlnovou funkci na hustotu pravd\u011bpodobnosti (\u03c8\u2192\u03c8\u03c8*)", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"Zn\u00e1zornit vlnovou funkci jako barevn\u00fd pruh", None))
        self.konecOsyLabel_3.setText(QCoreApplication.translate("Form", u"Koeficient v\u00fd\u0161ky barevn\u00e9ho pruhu", None))
        self.konecOsyLineEdit_3.setText(QCoreApplication.translate("Form", u"100", None))
        self.konecOsyLineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"100", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Aplikovat zm\u011bny", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resultTab), QCoreApplication.translate("Form", u"Zobrazen\u00ed v\u00fdsledku", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"n", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"En [eV]", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u03a8max [-]", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"3", None));

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"18e3", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"18e3", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"9", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"18e3", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tabulka energetick\u00fdch hladin", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Vytvo\u0159il Tom\u00e1\u0161 Svoboda (256695@vutbr.cz)", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Odkaz na github projektu (nen\u00ed je\u0161t\u011b vytvo\u0159en)", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"\u010cesky", None))
        self.radioButton_9.setText(QCoreApplication.translate("Form", u"English", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a href=\"https://www.gnu.org/licenses/gpl-3.0.html\"><span style=\" text-decoration: underline; color:#007af4;\">GNU GPL v3.0</span></a></p></body></html>", None))
    # retranslateUi

