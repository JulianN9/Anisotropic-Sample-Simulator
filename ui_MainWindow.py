# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnisotropicSimulator2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QDoubleSpinBox, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 849)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.OptionsTabWidget = QTabWidget(self.centralwidget)
        self.OptionsTabWidget.setObjectName(u"OptionsTabWidget")
        self.InputValuesTab = QWidget()
        self.InputValuesTab.setObjectName(u"InputValuesTab")
        self.verticalLayout = QVBoxLayout(self.InputValuesTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SetupWidget = QWidget(self.InputValuesTab)
        self.SetupWidget.setObjectName(u"SetupWidget")
        self.formLayout = QFormLayout(self.SetupWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.SetupWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.MeshSizeLabel = QLabel(self.SetupWidget)
        self.MeshSizeLabel.setObjectName(u"MeshSizeLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.MeshSizeLabel)

        self.InputLocationLabel = QLabel(self.SetupWidget)
        self.InputLocationLabel.setObjectName(u"InputLocationLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.InputLocationLabel)

        self.OutputLocationLabel = QLabel(self.SetupWidget)
        self.OutputLocationLabel.setObjectName(u"OutputLocationLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.OutputLocationLabel)

        self.FixedVLabel = QLabel(self.SetupWidget)
        self.FixedVLabel.setObjectName(u"FixedVLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.FixedVLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.IntializeButton = QPushButton(self.SetupWidget)
        self.IntializeButton.setObjectName(u"IntializeButton")

        self.horizontalLayout_4.addWidget(self.IntializeButton)

        self.toolButton = QToolButton(self.SetupWidget)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_4.addWidget(self.toolButton)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.NxBox = QSpinBox(self.SetupWidget)
        self.NxBox.setObjectName(u"NxBox")
        self.NxBox.setMinimum(1)
        self.NxBox.setValue(24)

        self.gridLayout.addWidget(self.NxBox, 1, 0, 1, 1)

        self.label_15 = QLabel(self.SetupWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 0, 1, 1, 1)

        self.label_14 = QLabel(self.SetupWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_16 = QLabel(self.SetupWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 0, 2, 1, 1)

        self.NyBox = QSpinBox(self.SetupWidget)
        self.NyBox.setObjectName(u"NyBox")
        self.NyBox.setMinimum(1)
        self.NyBox.setValue(12)

        self.gridLayout.addWidget(self.NyBox, 1, 1, 1, 1)

        self.NzBox = QSpinBox(self.SetupWidget)
        self.NzBox.setObjectName(u"NzBox")
        self.NzBox.setMinimum(1)

        self.gridLayout.addWidget(self.NzBox, 1, 2, 1, 1)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.SetupWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.SetupWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.IxBox = QSpinBox(self.SetupWidget)
        self.IxBox.setObjectName(u"IxBox")
        self.IxBox.setMinimum(1)
        self.IxBox.setMaximum(24)
        self.IxBox.setValue(3)

        self.gridLayout_2.addWidget(self.IxBox, 1, 0, 1, 1)

        self.label_6 = QLabel(self.SetupWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.IyBox = QSpinBox(self.SetupWidget)
        self.IyBox.setObjectName(u"IyBox")
        self.IyBox.setMinimum(1)
        self.IyBox.setMaximum(12)

        self.gridLayout_2.addWidget(self.IyBox, 1, 1, 1, 1)

        self.IzBox = QSpinBox(self.SetupWidget)
        self.IzBox.setObjectName(u"IzBox")
        self.IzBox.setMinimum(1)
        self.IzBox.setMaximum(1)

        self.gridLayout_2.addWidget(self.IzBox, 1, 2, 1, 1)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.SetupWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_12 = QLabel(self.SetupWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_11 = QLabel(self.SetupWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.OxBox = QSpinBox(self.SetupWidget)
        self.OxBox.setObjectName(u"OxBox")
        self.OxBox.setMinimum(1)
        self.OxBox.setMaximum(24)
        self.OxBox.setValue(3)

        self.gridLayout_3.addWidget(self.OxBox, 1, 0, 1, 1)

        self.OyBox = QSpinBox(self.SetupWidget)
        self.OyBox.setObjectName(u"OyBox")
        self.OyBox.setMinimum(1)
        self.OyBox.setMaximum(12)
        self.OyBox.setValue(12)

        self.gridLayout_3.addWidget(self.OyBox, 1, 1, 1, 1)

        self.OzBox = QSpinBox(self.SetupWidget)
        self.OzBox.setObjectName(u"OzBox")
        self.OzBox.setMinimum(1)
        self.OzBox.setMaximum(1)

        self.gridLayout_3.addWidget(self.OzBox, 1, 2, 1, 1)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.OutputVLabel = QLabel(self.SetupWidget)
        self.OutputVLabel.setObjectName(u"OutputVLabel")

        self.gridLayout_4.addWidget(self.OutputVLabel, 0, 1, 1, 1)

        self.InputVLabel = QLabel(self.SetupWidget)
        self.InputVLabel.setObjectName(u"InputVLabel")

        self.gridLayout_4.addWidget(self.InputVLabel, 0, 0, 1, 1)

        self.IvBox = QDoubleSpinBox(self.SetupWidget)
        self.IvBox.setObjectName(u"IvBox")
        self.IvBox.setMinimum(0.000000000000000)
        self.IvBox.setMaximum(100.000000000000000)
        self.IvBox.setValue(5.000000000000000)

        self.gridLayout_4.addWidget(self.IvBox, 1, 0, 1, 1)

        self.OvBox = QDoubleSpinBox(self.SetupWidget)
        self.OvBox.setObjectName(u"OvBox")
        self.OvBox.setMinimum(-100.000000000000000)
        self.OvBox.setMaximum(0.000000000000000)
        self.OvBox.setValue(-5.000000000000000)

        self.gridLayout_4.addWidget(self.OvBox, 1, 1, 1, 1)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.gridLayout_4)


        self.verticalLayout.addWidget(self.SetupWidget)

        self.MeasurementWidget = QWidget(self.InputValuesTab)
        self.MeasurementWidget.setObjectName(u"MeasurementWidget")
        self.MeasurementWidget.setEnabled(False)
        self.formLayout_2 = QFormLayout(self.MeasurementWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.InputProbeLabel = QLabel(self.MeasurementWidget)
        self.InputProbeLabel.setObjectName(u"InputProbeLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.InputProbeLabel)

        self.label_3 = QLabel(self.MeasurementWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.OutputProbeLabel = QLabel(self.MeasurementWidget)
        self.OutputProbeLabel.setObjectName(u"OutputProbeLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.OutputProbeLabel)

        self.label = QLabel(self.MeasurementWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.CheckX = QCheckBox(self.MeasurementWidget)
        self.CheckX.setObjectName(u"CheckX")
        self.CheckX.setChecked(True)

        self.horizontalLayout_16.addWidget(self.CheckX)

        self.CheckY = QCheckBox(self.MeasurementWidget)
        self.CheckY.setObjectName(u"CheckY")
        self.CheckY.setChecked(True)

        self.horizontalLayout_16.addWidget(self.CheckY)

        self.CheckZ = QCheckBox(self.MeasurementWidget)
        self.CheckZ.setObjectName(u"CheckZ")
        self.CheckZ.setChecked(False)

        self.horizontalLayout_16.addWidget(self.CheckZ)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_16)

        self.MeasureButton = QPushButton(self.MeasurementWidget)
        self.MeasureButton.setObjectName(u"MeasureButton")
        self.MeasureButton.setEnabled(False)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.MeasureButton)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_19 = QLabel(self.MeasurementWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 0, 2, 1, 1)

        self.label_18 = QLabel(self.MeasurementWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 0, 1, 1, 1)

        self.IPxBox = QSpinBox(self.MeasurementWidget)
        self.IPxBox.setObjectName(u"IPxBox")
        self.IPxBox.setMinimum(1)
        self.IPxBox.setMaximum(24)
        self.IPxBox.setValue(21)

        self.gridLayout_5.addWidget(self.IPxBox, 1, 0, 1, 1)

        self.IPzBox = QSpinBox(self.MeasurementWidget)
        self.IPzBox.setObjectName(u"IPzBox")
        self.IPzBox.setMinimum(1)
        self.IPzBox.setMaximum(1)

        self.gridLayout_5.addWidget(self.IPzBox, 1, 2, 1, 1)

        self.IPyBox = QSpinBox(self.MeasurementWidget)
        self.IPyBox.setObjectName(u"IPyBox")
        self.IPyBox.setMinimum(1)
        self.IPyBox.setMaximum(12)

        self.gridLayout_5.addWidget(self.IPyBox, 1, 1, 1, 1)

        self.label_17 = QLabel(self.MeasurementWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.gridLayout_5)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_21 = QLabel(self.MeasurementWidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_20 = QLabel(self.MeasurementWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_22 = QLabel(self.MeasurementWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 0, 2, 1, 1)

        self.OPxBox = QSpinBox(self.MeasurementWidget)
        self.OPxBox.setObjectName(u"OPxBox")
        self.OPxBox.setMinimum(1)
        self.OPxBox.setMaximum(24)
        self.OPxBox.setValue(21)

        self.gridLayout_6.addWidget(self.OPxBox, 1, 0, 1, 1)

        self.OPyBox = QSpinBox(self.MeasurementWidget)
        self.OPyBox.setObjectName(u"OPyBox")
        self.OPyBox.setMinimum(1)
        self.OPyBox.setMaximum(12)
        self.OPyBox.setValue(12)

        self.gridLayout_6.addWidget(self.OPyBox, 1, 1, 1, 1)

        self.OPzBox = QSpinBox(self.MeasurementWidget)
        self.OPzBox.setObjectName(u"OPzBox")
        self.OPzBox.setMinimum(1)
        self.OPzBox.setMaximum(1)

        self.gridLayout_6.addWidget(self.OPzBox, 1, 2, 1, 1)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.gridLayout_6)


        self.verticalLayout.addWidget(self.MeasurementWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.OptionsTabWidget.addTab(self.InputValuesTab, "")
        self.RxTab = QWidget()
        self.RxTab.setObjectName(u"RxTab")
        self.verticalLayout_5 = QVBoxLayout(self.RxTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.RxFormLayout = QFormLayout()
        self.RxFormLayout.setObjectName(u"RxFormLayout")
        self.label_4 = QLabel(self.RxTab)
        self.label_4.setObjectName(u"label_4")

        self.RxFormLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_10 = QLabel(self.RxTab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_9 = QLabel(self.RxTab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_8 = QLabel(self.RxTab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.RxP1C = QDoubleSpinBox(self.RxTab)
        self.RxP1C.setObjectName(u"RxP1C")
        self.RxP1C.setDecimals(3)
        self.RxP1C.setMinimum(-50.000000000000000)
        self.RxP1C.setMaximum(50.000000000000000)
        self.RxP1C.setValue(1.700000000000000)

        self.gridLayout_7.addWidget(self.RxP1C, 1, 2, 1, 1)

        self.RxP1B = QDoubleSpinBox(self.RxTab)
        self.RxP1B.setObjectName(u"RxP1B")
        self.RxP1B.setMaximum(5.000000000000000)
        self.RxP1B.setValue(2.000000000000000)

        self.gridLayout_7.addWidget(self.RxP1B, 1, 1, 1, 1)

        self.RxP1A = QDoubleSpinBox(self.RxTab)
        self.RxP1A.setObjectName(u"RxP1A")
        self.RxP1A.setDecimals(4)
        self.RxP1A.setMinimum(0.000100000000000)
        self.RxP1A.setMaximum(1.000000000000000)
        self.RxP1A.setSingleStep(0.000100000000000)
        self.RxP1A.setValue(0.030000000000000)

        self.gridLayout_7.addWidget(self.RxP1A, 1, 0, 1, 1)


        self.RxFormLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout_7)

        self.label_115 = QLabel(self.RxTab)
        self.label_115.setObjectName(u"label_115")

        self.RxFormLayout.setWidget(1, QFormLayout.LabelRole, self.label_115)

        self.RxScaleNxCheck = QCheckBox(self.RxTab)
        self.RxScaleNxCheck.setObjectName(u"RxScaleNxCheck")
        self.RxScaleNxCheck.setChecked(True)

        self.RxFormLayout.setWidget(2, QFormLayout.FieldRole, self.RxScaleNxCheck)

        self.RxScale = QDoubleSpinBox(self.RxTab)
        self.RxScale.setObjectName(u"RxScale")
        self.RxScale.setDecimals(5)
        self.RxScale.setMinimum(0.000010000000000)
        self.RxScale.setMaximum(1000000000.000000000000000)
        self.RxScale.setValue(15.000000000000000)

        self.RxFormLayout.setWidget(1, QFormLayout.FieldRole, self.RxScale)


        self.verticalLayout_5.addLayout(self.RxFormLayout)

        self.RxTickLayout = QHBoxLayout()
        self.RxTickLayout.setObjectName(u"RxTickLayout")
        self.RxPoly2Check = QCheckBox(self.RxTab)
        self.RxPoly2Check.setObjectName(u"RxPoly2Check")
        self.RxPoly2Check.setChecked(True)

        self.RxTickLayout.addWidget(self.RxPoly2Check)

        self.RxPoly3Check = QCheckBox(self.RxTab)
        self.RxPoly3Check.setObjectName(u"RxPoly3Check")

        self.RxTickLayout.addWidget(self.RxPoly3Check)

        self.RxPoly4Check = QCheckBox(self.RxTab)
        self.RxPoly4Check.setObjectName(u"RxPoly4Check")

        self.RxTickLayout.addWidget(self.RxPoly4Check)

        self.RxPoly5Check = QCheckBox(self.RxTab)
        self.RxPoly5Check.setObjectName(u"RxPoly5Check")

        self.RxTickLayout.addWidget(self.RxPoly5Check)


        self.verticalLayout_5.addLayout(self.RxTickLayout)

        self.RxWidget1 = QWidget(self.RxTab)
        self.RxWidget1.setObjectName(u"RxWidget1")
        self.formLayout_7 = QFormLayout(self.RxWidget1)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_37 = QLabel(self.RxWidget1)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_39 = QLabel(self.RxWidget1)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_13.addWidget(self.label_39, 0, 1, 1, 1)

        self.label_38 = QLabel(self.RxWidget1)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_13.addWidget(self.label_38, 0, 0, 1, 1)

        self.RxB1A = QDoubleSpinBox(self.RxWidget1)
        self.RxB1A.setObjectName(u"RxB1A")
        self.RxB1A.setMinimum(2.000000000000000)
        self.RxB1A.setMaximum(300.000000000000000)
        self.RxB1A.setValue(20.000000000000000)

        self.gridLayout_13.addWidget(self.RxB1A, 1, 0, 1, 1)

        self.RxB1B = QDoubleSpinBox(self.RxWidget1)
        self.RxB1B.setObjectName(u"RxB1B")
        self.RxB1B.setMinimum(0.010000000000000)
        self.RxB1B.setMaximum(100.000000000000000)
        self.RxB1B.setValue(10.000000000000000)

        self.gridLayout_13.addWidget(self.RxB1B, 1, 1, 1, 1)


        self.formLayout_7.setLayout(0, QFormLayout.FieldRole, self.gridLayout_13)

        self.label_40 = QLabel(self.RxWidget1)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_40)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_42 = QLabel(self.RxWidget1)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_14.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_41 = QLabel(self.RxWidget1)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_14.addWidget(self.label_41, 0, 1, 1, 1)

        self.label_43 = QLabel(self.RxWidget1)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_14.addWidget(self.label_43, 0, 2, 1, 1)

        self.RxP2A = QDoubleSpinBox(self.RxWidget1)
        self.RxP2A.setObjectName(u"RxP2A")
        self.RxP2A.setDecimals(4)
        self.RxP2A.setMinimum(0.000100000000000)
        self.RxP2A.setMaximum(1.000000000000000)
        self.RxP2A.setSingleStep(0.000100000000000)
        self.RxP2A.setValue(0.680000000000000)

        self.gridLayout_14.addWidget(self.RxP2A, 1, 0, 1, 1)

        self.RxP2B = QDoubleSpinBox(self.RxWidget1)
        self.RxP2B.setObjectName(u"RxP2B")
        self.RxP2B.setMaximum(5.000000000000000)
        self.RxP2B.setValue(1.000000000000000)

        self.gridLayout_14.addWidget(self.RxP2B, 1, 1, 1, 1)

        self.RxP2C = QDoubleSpinBox(self.RxWidget1)
        self.RxP2C.setObjectName(u"RxP2C")
        self.RxP2C.setDecimals(3)
        self.RxP2C.setMinimum(-50.000000000000000)
        self.RxP2C.setMaximum(50.000000000000000)

        self.gridLayout_14.addWidget(self.RxP2C, 1, 2, 1, 1)


        self.formLayout_7.setLayout(1, QFormLayout.FieldRole, self.gridLayout_14)


        self.verticalLayout_5.addWidget(self.RxWidget1)

        self.RxWidget2 = QWidget(self.RxTab)
        self.RxWidget2.setObjectName(u"RxWidget2")
        self.RxWidget2.setEnabled(False)
        self.formLayout_6 = QFormLayout(self.RxWidget2)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_30 = QLabel(self.RxWidget2)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_30)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_32 = QLabel(self.RxWidget2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_11.addWidget(self.label_32, 0, 1, 1, 1)

        self.label_31 = QLabel(self.RxWidget2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_11.addWidget(self.label_31, 0, 0, 1, 1)

        self.RxB2B = QDoubleSpinBox(self.RxWidget2)
        self.RxB2B.setObjectName(u"RxB2B")
        self.RxB2B.setMinimum(0.010000000000000)
        self.RxB2B.setMaximum(100.000000000000000)
        self.RxB2B.setValue(1.000000000000000)

        self.gridLayout_11.addWidget(self.RxB2B, 1, 1, 1, 1)

        self.RxB2A = QDoubleSpinBox(self.RxWidget2)
        self.RxB2A.setObjectName(u"RxB2A")
        self.RxB2A.setMinimum(2.000000000000000)
        self.RxB2A.setMaximum(300.000000000000000)
        self.RxB2A.setValue(50.000000000000000)

        self.gridLayout_11.addWidget(self.RxB2A, 1, 0, 1, 1)


        self.formLayout_6.setLayout(0, QFormLayout.FieldRole, self.gridLayout_11)

        self.label_33 = QLabel(self.RxWidget2)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_33)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_34 = QLabel(self.RxWidget2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_12.addWidget(self.label_34, 0, 1, 1, 1)

        self.label_36 = QLabel(self.RxWidget2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_12.addWidget(self.label_36, 0, 2, 1, 1)

        self.label_35 = QLabel(self.RxWidget2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_12.addWidget(self.label_35, 0, 0, 1, 1)

        self.RxP3A = QDoubleSpinBox(self.RxWidget2)
        self.RxP3A.setObjectName(u"RxP3A")
        self.RxP3A.setDecimals(4)
        self.RxP3A.setMinimum(0.000100000000000)
        self.RxP3A.setMaximum(1.000000000000000)
        self.RxP3A.setSingleStep(0.000100000000000)
        self.RxP3A.setValue(1.000000000000000)

        self.gridLayout_12.addWidget(self.RxP3A, 1, 0, 1, 1)

        self.RxP3B = QDoubleSpinBox(self.RxWidget2)
        self.RxP3B.setObjectName(u"RxP3B")
        self.RxP3B.setMaximum(5.000000000000000)
        self.RxP3B.setValue(1.000000000000000)

        self.gridLayout_12.addWidget(self.RxP3B, 1, 1, 1, 1)

        self.RxP3C = QDoubleSpinBox(self.RxWidget2)
        self.RxP3C.setObjectName(u"RxP3C")
        self.RxP3C.setDecimals(3)
        self.RxP3C.setMinimum(-50.000000000000000)
        self.RxP3C.setMaximum(50.000000000000000)

        self.gridLayout_12.addWidget(self.RxP3C, 1, 2, 1, 1)


        self.formLayout_6.setLayout(2, QFormLayout.FieldRole, self.gridLayout_12)


        self.verticalLayout_5.addWidget(self.RxWidget2)

        self.RxWidget3 = QWidget(self.RxTab)
        self.RxWidget3.setObjectName(u"RxWidget3")
        self.RxWidget3.setEnabled(False)
        self.formLayout_8 = QFormLayout(self.RxWidget3)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_44 = QLabel(self.RxWidget3)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_44)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_45 = QLabel(self.RxWidget3)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_15.addWidget(self.label_45, 0, 0, 1, 1)

        self.label_46 = QLabel(self.RxWidget3)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_15.addWidget(self.label_46, 0, 1, 1, 1)

        self.RxB3A = QDoubleSpinBox(self.RxWidget3)
        self.RxB3A.setObjectName(u"RxB3A")
        self.RxB3A.setMinimum(2.000000000000000)
        self.RxB3A.setMaximum(300.000000000000000)
        self.RxB3A.setValue(50.000000000000000)

        self.gridLayout_15.addWidget(self.RxB3A, 1, 0, 1, 1)

        self.RxB3B = QDoubleSpinBox(self.RxWidget3)
        self.RxB3B.setObjectName(u"RxB3B")
        self.RxB3B.setMinimum(0.010000000000000)
        self.RxB3B.setMaximum(100.000000000000000)
        self.RxB3B.setValue(1.000000000000000)

        self.gridLayout_15.addWidget(self.RxB3B, 1, 1, 1, 1)


        self.formLayout_8.setLayout(0, QFormLayout.FieldRole, self.gridLayout_15)

        self.label_47 = QLabel(self.RxWidget3)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_47)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_49 = QLabel(self.RxWidget3)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_16.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_48 = QLabel(self.RxWidget3)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_16.addWidget(self.label_48, 0, 1, 1, 1)

        self.label_50 = QLabel(self.RxWidget3)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_16.addWidget(self.label_50, 0, 2, 1, 1)

        self.RxP4A = QDoubleSpinBox(self.RxWidget3)
        self.RxP4A.setObjectName(u"RxP4A")
        self.RxP4A.setDecimals(4)
        self.RxP4A.setMinimum(0.000100000000000)
        self.RxP4A.setMaximum(1.000000000000000)
        self.RxP4A.setSingleStep(0.000100000000000)
        self.RxP4A.setValue(1.000000000000000)

        self.gridLayout_16.addWidget(self.RxP4A, 1, 0, 1, 1)

        self.RxP4B = QDoubleSpinBox(self.RxWidget3)
        self.RxP4B.setObjectName(u"RxP4B")
        self.RxP4B.setMaximum(5.000000000000000)
        self.RxP4B.setSingleStep(1.000000000000000)
        self.RxP4B.setValue(1.000000000000000)

        self.gridLayout_16.addWidget(self.RxP4B, 1, 1, 1, 1)

        self.RxP4C = QDoubleSpinBox(self.RxWidget3)
        self.RxP4C.setObjectName(u"RxP4C")
        self.RxP4C.setDecimals(3)
        self.RxP4C.setMinimum(-50.000000000000000)
        self.RxP4C.setMaximum(50.000000000000000)

        self.gridLayout_16.addWidget(self.RxP4C, 1, 2, 1, 1)


        self.formLayout_8.setLayout(1, QFormLayout.FieldRole, self.gridLayout_16)


        self.verticalLayout_5.addWidget(self.RxWidget3)

        self.RxWidget4 = QWidget(self.RxTab)
        self.RxWidget4.setObjectName(u"RxWidget4")
        self.RxWidget4.setEnabled(False)
        self.formLayout_5 = QFormLayout(self.RxWidget4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_23 = QLabel(self.RxWidget4)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_24 = QLabel(self.RxWidget4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_9.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.RxWidget4)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_9.addWidget(self.label_25, 0, 1, 1, 1)

        self.RxB4A = QDoubleSpinBox(self.RxWidget4)
        self.RxB4A.setObjectName(u"RxB4A")
        self.RxB4A.setMinimum(2.000000000000000)
        self.RxB4A.setMaximum(300.000000000000000)
        self.RxB4A.setSingleStep(1.000000000000000)
        self.RxB4A.setValue(50.000000000000000)

        self.gridLayout_9.addWidget(self.RxB4A, 1, 0, 1, 1)

        self.RxB4B = QDoubleSpinBox(self.RxWidget4)
        self.RxB4B.setObjectName(u"RxB4B")
        self.RxB4B.setMinimum(0.010000000000000)
        self.RxB4B.setMaximum(100.000000000000000)
        self.RxB4B.setValue(1.000000000000000)

        self.gridLayout_9.addWidget(self.RxB4B, 1, 1, 1, 1)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.gridLayout_9)

        self.label_26 = QLabel(self.RxWidget4)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_26)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_28 = QLabel(self.RxWidget4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_10.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_27 = QLabel(self.RxWidget4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_10.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_29 = QLabel(self.RxWidget4)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_10.addWidget(self.label_29, 0, 2, 1, 1)

        self.RxP5A = QDoubleSpinBox(self.RxWidget4)
        self.RxP5A.setObjectName(u"RxP5A")
        self.RxP5A.setDecimals(4)
        self.RxP5A.setMinimum(0.000100000000000)
        self.RxP5A.setMaximum(1.000000000000000)
        self.RxP5A.setSingleStep(0.000100000000000)
        self.RxP5A.setValue(1.000000000000000)

        self.gridLayout_10.addWidget(self.RxP5A, 1, 0, 1, 1)

        self.RxP5B = QDoubleSpinBox(self.RxWidget4)
        self.RxP5B.setObjectName(u"RxP5B")
        self.RxP5B.setMaximum(5.000000000000000)
        self.RxP5B.setValue(1.000000000000000)

        self.gridLayout_10.addWidget(self.RxP5B, 1, 1, 1, 1)

        self.RxP5C = QDoubleSpinBox(self.RxWidget4)
        self.RxP5C.setObjectName(u"RxP5C")
        self.RxP5C.setDecimals(3)
        self.RxP5C.setMinimum(-50.000000000000000)
        self.RxP5C.setMaximum(50.000000000000000)
        self.RxP5C.setValue(0.000000000000000)

        self.gridLayout_10.addWidget(self.RxP5C, 1, 2, 1, 1)


        self.formLayout_5.setLayout(1, QFormLayout.FieldRole, self.gridLayout_10)


        self.verticalLayout_5.addWidget(self.RxWidget4)

        self.RxButtonBox = QDialogButtonBox(self.RxTab)
        self.RxButtonBox.setObjectName(u"RxButtonBox")
        self.RxButtonBox.setLayoutDirection(Qt.LeftToRight)
        self.RxButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.RxButtonBox.setCenterButtons(True)

        self.verticalLayout_5.addWidget(self.RxButtonBox)

        self.OptionsTabWidget.addTab(self.RxTab, "")
        self.RyTab = QWidget()
        self.RyTab.setObjectName(u"RyTab")
        self.verticalLayout_4 = QVBoxLayout(self.RyTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.RyFormLayout = QFormLayout()
        self.RyFormLayout.setObjectName(u"RyFormLayout")
        self.label_79 = QLabel(self.RyTab)
        self.label_79.setObjectName(u"label_79")

        self.RyFormLayout.setWidget(0, QFormLayout.LabelRole, self.label_79)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_80 = QLabel(self.RyTab)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_26.addWidget(self.label_80, 0, 2, 1, 1)

        self.label_81 = QLabel(self.RyTab)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_26.addWidget(self.label_81, 0, 1, 1, 1)

        self.label_82 = QLabel(self.RyTab)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_26.addWidget(self.label_82, 0, 0, 1, 1)

        self.RyP1C = QDoubleSpinBox(self.RyTab)
        self.RyP1C.setObjectName(u"RyP1C")
        self.RyP1C.setDecimals(3)
        self.RyP1C.setMinimum(-50.000000000000000)
        self.RyP1C.setMaximum(50.000000000000000)
        self.RyP1C.setValue(0.000000000000000)

        self.gridLayout_26.addWidget(self.RyP1C, 1, 2, 1, 1)

        self.RyP1B = QDoubleSpinBox(self.RyTab)
        self.RyP1B.setObjectName(u"RyP1B")
        self.RyP1B.setMaximum(5.000000000000000)
        self.RyP1B.setValue(2.260000000000000)

        self.gridLayout_26.addWidget(self.RyP1B, 1, 1, 1, 1)

        self.RyP1A = QDoubleSpinBox(self.RyTab)
        self.RyP1A.setObjectName(u"RyP1A")
        self.RyP1A.setDecimals(4)
        self.RyP1A.setMinimum(0.000100000000000)
        self.RyP1A.setMaximum(1.000000000000000)
        self.RyP1A.setSingleStep(0.000100000000000)
        self.RyP1A.setValue(0.037600000000000)

        self.gridLayout_26.addWidget(self.RyP1A, 1, 0, 1, 1)


        self.RyFormLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout_26)

        self.label_116 = QLabel(self.RyTab)
        self.label_116.setObjectName(u"label_116")

        self.RyFormLayout.setWidget(1, QFormLayout.LabelRole, self.label_116)

        self.RyScaleNyCheck = QCheckBox(self.RyTab)
        self.RyScaleNyCheck.setObjectName(u"RyScaleNyCheck")
        self.RyScaleNyCheck.setChecked(True)

        self.RyFormLayout.setWidget(2, QFormLayout.FieldRole, self.RyScaleNyCheck)

        self.RyScale = QDoubleSpinBox(self.RyTab)
        self.RyScale.setObjectName(u"RyScale")
        self.RyScale.setDecimals(5)
        self.RyScale.setMinimum(0.000010000000000)
        self.RyScale.setMaximum(1000000000.000000000000000)
        self.RyScale.setValue(1000.000000000000000)

        self.RyFormLayout.setWidget(1, QFormLayout.FieldRole, self.RyScale)


        self.verticalLayout_4.addLayout(self.RyFormLayout)

        self.RyTickLayout = QHBoxLayout()
        self.RyTickLayout.setObjectName(u"RyTickLayout")
        self.RyPoly2Check = QCheckBox(self.RyTab)
        self.RyPoly2Check.setObjectName(u"RyPoly2Check")
        self.RyPoly2Check.setChecked(True)

        self.RyTickLayout.addWidget(self.RyPoly2Check)

        self.RyPoly3Check = QCheckBox(self.RyTab)
        self.RyPoly3Check.setObjectName(u"RyPoly3Check")
        self.RyPoly3Check.setChecked(True)

        self.RyTickLayout.addWidget(self.RyPoly3Check)

        self.RyPoly4Check = QCheckBox(self.RyTab)
        self.RyPoly4Check.setObjectName(u"RyPoly4Check")

        self.RyTickLayout.addWidget(self.RyPoly4Check)

        self.RyPoly5Check = QCheckBox(self.RyTab)
        self.RyPoly5Check.setObjectName(u"RyPoly5Check")

        self.RyTickLayout.addWidget(self.RyPoly5Check)


        self.verticalLayout_4.addLayout(self.RyTickLayout)

        self.RyWidget1 = QWidget(self.RyTab)
        self.RyWidget1.setObjectName(u"RyWidget1")
        self.formLayout_11 = QFormLayout(self.RyWidget1)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.label_65 = QLabel(self.RyWidget1)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_65)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_66 = QLabel(self.RyWidget1)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_22.addWidget(self.label_66, 0, 1, 1, 1)

        self.label_67 = QLabel(self.RyWidget1)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_22.addWidget(self.label_67, 0, 0, 1, 1)

        self.RyB1A = QDoubleSpinBox(self.RyWidget1)
        self.RyB1A.setObjectName(u"RyB1A")
        self.RyB1A.setMinimum(1.000000000000000)
        self.RyB1A.setMaximum(300.000000000000000)
        self.RyB1A.setValue(1.000000000000000)

        self.gridLayout_22.addWidget(self.RyB1A, 1, 0, 1, 1)

        self.RyB1B = QDoubleSpinBox(self.RyWidget1)
        self.RyB1B.setObjectName(u"RyB1B")
        self.RyB1B.setMinimum(0.010000000000000)
        self.RyB1B.setMaximum(100.000000000000000)
        self.RyB1B.setValue(7.720000000000000)

        self.gridLayout_22.addWidget(self.RyB1B, 1, 1, 1, 1)


        self.formLayout_11.setLayout(0, QFormLayout.FieldRole, self.gridLayout_22)

        self.label_68 = QLabel(self.RyWidget1)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.label_68)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_69 = QLabel(self.RyWidget1)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_23.addWidget(self.label_69, 0, 0, 1, 1)

        self.label_70 = QLabel(self.RyWidget1)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_23.addWidget(self.label_70, 0, 1, 1, 1)

        self.label_71 = QLabel(self.RyWidget1)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_23.addWidget(self.label_71, 0, 2, 1, 1)

        self.RyP2A = QDoubleSpinBox(self.RyWidget1)
        self.RyP2A.setObjectName(u"RyP2A")
        self.RyP2A.setDecimals(4)
        self.RyP2A.setMinimum(0.000100000000000)
        self.RyP2A.setMaximum(1.000000000000000)
        self.RyP2A.setSingleStep(0.000100000000000)
        self.RyP2A.setValue(0.175900000000000)

        self.gridLayout_23.addWidget(self.RyP2A, 1, 0, 1, 1)

        self.RyP2B = QDoubleSpinBox(self.RyWidget1)
        self.RyP2B.setObjectName(u"RyP2B")
        self.RyP2B.setMaximum(5.000000000000000)
        self.RyP2B.setValue(0.860000000000000)

        self.gridLayout_23.addWidget(self.RyP2B, 1, 1, 1, 1)

        self.RyP2C = QDoubleSpinBox(self.RyWidget1)
        self.RyP2C.setObjectName(u"RyP2C")
        self.RyP2C.setDecimals(3)
        self.RyP2C.setMinimum(-50.000000000000000)
        self.RyP2C.setMaximum(50.000000000000000)

        self.gridLayout_23.addWidget(self.RyP2C, 1, 2, 1, 1)


        self.formLayout_11.setLayout(1, QFormLayout.FieldRole, self.gridLayout_23)


        self.verticalLayout_4.addWidget(self.RyWidget1)

        self.RyWidget2 = QWidget(self.RyTab)
        self.RyWidget2.setObjectName(u"RyWidget2")
        self.RyWidget2.setEnabled(True)
        self.formLayout_9 = QFormLayout(self.RyWidget2)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_51 = QLabel(self.RyWidget2)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_51)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_53 = QLabel(self.RyWidget2)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_18.addWidget(self.label_53, 0, 0, 1, 1)

        self.label_52 = QLabel(self.RyWidget2)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_18.addWidget(self.label_52, 0, 1, 1, 1)

        self.RyB2A = QDoubleSpinBox(self.RyWidget2)
        self.RyB2A.setObjectName(u"RyB2A")
        self.RyB2A.setMinimum(2.000000000000000)
        self.RyB2A.setMaximum(300.000000000000000)
        self.RyB2A.setValue(35.000000000000000)

        self.gridLayout_18.addWidget(self.RyB2A, 1, 0, 1, 1)

        self.RyB2B = QDoubleSpinBox(self.RyWidget2)
        self.RyB2B.setObjectName(u"RyB2B")
        self.RyB2B.setMinimum(0.010000000000000)
        self.RyB2B.setMaximum(100.000000000000000)
        self.RyB2B.setValue(11.550000000000001)

        self.gridLayout_18.addWidget(self.RyB2B, 1, 1, 1, 1)


        self.formLayout_9.setLayout(0, QFormLayout.FieldRole, self.gridLayout_18)

        self.label_54 = QLabel(self.RyWidget2)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_54)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_55 = QLabel(self.RyWidget2)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_19.addWidget(self.label_55, 0, 1, 1, 1)

        self.label_56 = QLabel(self.RyWidget2)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_19.addWidget(self.label_56, 0, 2, 1, 1)

        self.label_57 = QLabel(self.RyWidget2)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_19.addWidget(self.label_57, 0, 0, 1, 1)

        self.RyP3A = QDoubleSpinBox(self.RyWidget2)
        self.RyP3A.setObjectName(u"RyP3A")
        self.RyP3A.setDecimals(4)
        self.RyP3A.setMinimum(0.000100000000000)
        self.RyP3A.setMaximum(1.000000000000000)
        self.RyP3A.setSingleStep(0.000100000000000)
        self.RyP3A.setValue(0.066500000000000)

        self.gridLayout_19.addWidget(self.RyP3A, 1, 0, 1, 1)

        self.RyP3B = QDoubleSpinBox(self.RyWidget2)
        self.RyP3B.setObjectName(u"RyP3B")
        self.RyP3B.setMaximum(5.000000000000000)
        self.RyP3B.setValue(0.760000000000000)

        self.gridLayout_19.addWidget(self.RyP3B, 1, 1, 1, 1)

        self.RyP3C = QDoubleSpinBox(self.RyWidget2)
        self.RyP3C.setObjectName(u"RyP3C")
        self.RyP3C.setDecimals(3)
        self.RyP3C.setMinimum(-50.000000000000000)
        self.RyP3C.setMaximum(50.000000000000000)
        self.RyP3C.setValue(6.733000000000000)

        self.gridLayout_19.addWidget(self.RyP3C, 1, 2, 1, 1)


        self.formLayout_9.setLayout(2, QFormLayout.FieldRole, self.gridLayout_19)


        self.verticalLayout_4.addWidget(self.RyWidget2)

        self.RyWidget3 = QWidget(self.RyTab)
        self.RyWidget3.setObjectName(u"RyWidget3")
        self.RyWidget3.setEnabled(False)
        self.formLayout_12 = QFormLayout(self.RyWidget3)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.label_72 = QLabel(self.RyWidget3)
        self.label_72.setObjectName(u"label_72")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_72)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_73 = QLabel(self.RyWidget3)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_24.addWidget(self.label_73, 0, 0, 1, 1)

        self.label_74 = QLabel(self.RyWidget3)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_24.addWidget(self.label_74, 0, 1, 1, 1)

        self.RyB3A = QDoubleSpinBox(self.RyWidget3)
        self.RyB3A.setObjectName(u"RyB3A")
        self.RyB3A.setMinimum(2.000000000000000)
        self.RyB3A.setMaximum(300.000000000000000)
        self.RyB3A.setValue(50.000000000000000)

        self.gridLayout_24.addWidget(self.RyB3A, 1, 0, 1, 1)

        self.RyB3B = QDoubleSpinBox(self.RyWidget3)
        self.RyB3B.setObjectName(u"RyB3B")
        self.RyB3B.setMinimum(0.010000000000000)
        self.RyB3B.setMaximum(100.000000000000000)
        self.RyB3B.setValue(1.000000000000000)

        self.gridLayout_24.addWidget(self.RyB3B, 1, 1, 1, 1)


        self.formLayout_12.setLayout(0, QFormLayout.FieldRole, self.gridLayout_24)

        self.label_75 = QLabel(self.RyWidget3)
        self.label_75.setObjectName(u"label_75")

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.label_75)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_76 = QLabel(self.RyWidget3)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_25.addWidget(self.label_76, 0, 0, 1, 1)

        self.label_77 = QLabel(self.RyWidget3)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_25.addWidget(self.label_77, 0, 1, 1, 1)

        self.label_78 = QLabel(self.RyWidget3)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_25.addWidget(self.label_78, 0, 2, 1, 1)

        self.RyP4A = QDoubleSpinBox(self.RyWidget3)
        self.RyP4A.setObjectName(u"RyP4A")
        self.RyP4A.setDecimals(4)
        self.RyP4A.setMinimum(0.000100000000000)
        self.RyP4A.setMaximum(1.000000000000000)
        self.RyP4A.setSingleStep(0.000100000000000)
        self.RyP4A.setValue(1.000000000000000)

        self.gridLayout_25.addWidget(self.RyP4A, 1, 0, 1, 1)

        self.RyP4B = QDoubleSpinBox(self.RyWidget3)
        self.RyP4B.setObjectName(u"RyP4B")
        self.RyP4B.setMaximum(5.000000000000000)
        self.RyP4B.setSingleStep(1.000000000000000)
        self.RyP4B.setValue(1.000000000000000)

        self.gridLayout_25.addWidget(self.RyP4B, 1, 1, 1, 1)

        self.RyP4C = QDoubleSpinBox(self.RyWidget3)
        self.RyP4C.setObjectName(u"RyP4C")
        self.RyP4C.setDecimals(3)
        self.RyP4C.setMinimum(-50.000000000000000)
        self.RyP4C.setMaximum(50.000000000000000)

        self.gridLayout_25.addWidget(self.RyP4C, 1, 2, 1, 1)


        self.formLayout_12.setLayout(1, QFormLayout.FieldRole, self.gridLayout_25)


        self.verticalLayout_4.addWidget(self.RyWidget3)

        self.RyWidget4 = QWidget(self.RyTab)
        self.RyWidget4.setObjectName(u"RyWidget4")
        self.RyWidget4.setEnabled(False)
        self.formLayout_10 = QFormLayout(self.RyWidget4)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.label_58 = QLabel(self.RyWidget4)
        self.label_58.setObjectName(u"label_58")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_58)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_59 = QLabel(self.RyWidget4)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_20.addWidget(self.label_59, 0, 0, 1, 1)

        self.label_60 = QLabel(self.RyWidget4)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_20.addWidget(self.label_60, 0, 1, 1, 1)

        self.RyB4A = QDoubleSpinBox(self.RyWidget4)
        self.RyB4A.setObjectName(u"RyB4A")
        self.RyB4A.setMinimum(2.000000000000000)
        self.RyB4A.setMaximum(300.000000000000000)
        self.RyB4A.setSingleStep(1.000000000000000)
        self.RyB4A.setValue(50.000000000000000)

        self.gridLayout_20.addWidget(self.RyB4A, 1, 0, 1, 1)

        self.RyB4B = QDoubleSpinBox(self.RyWidget4)
        self.RyB4B.setObjectName(u"RyB4B")
        self.RyB4B.setMinimum(0.010000000000000)
        self.RyB4B.setMaximum(100.000000000000000)
        self.RyB4B.setValue(1.000000000000000)

        self.gridLayout_20.addWidget(self.RyB4B, 1, 1, 1, 1)


        self.formLayout_10.setLayout(0, QFormLayout.FieldRole, self.gridLayout_20)

        self.label_61 = QLabel(self.RyWidget4)
        self.label_61.setObjectName(u"label_61")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_61)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_62 = QLabel(self.RyWidget4)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_21.addWidget(self.label_62, 0, 1, 1, 1)

        self.label_63 = QLabel(self.RyWidget4)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_21.addWidget(self.label_63, 0, 0, 1, 1)

        self.label_64 = QLabel(self.RyWidget4)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_21.addWidget(self.label_64, 0, 2, 1, 1)

        self.RyP5A = QDoubleSpinBox(self.RyWidget4)
        self.RyP5A.setObjectName(u"RyP5A")
        self.RyP5A.setDecimals(4)
        self.RyP5A.setMinimum(0.000100000000000)
        self.RyP5A.setMaximum(1.000000000000000)
        self.RyP5A.setSingleStep(0.000100000000000)
        self.RyP5A.setValue(1.000000000000000)

        self.gridLayout_21.addWidget(self.RyP5A, 1, 0, 1, 1)

        self.RyP5B = QDoubleSpinBox(self.RyWidget4)
        self.RyP5B.setObjectName(u"RyP5B")
        self.RyP5B.setMaximum(5.000000000000000)
        self.RyP5B.setValue(1.000000000000000)

        self.gridLayout_21.addWidget(self.RyP5B, 1, 1, 1, 1)

        self.RyP5C = QDoubleSpinBox(self.RyWidget4)
        self.RyP5C.setObjectName(u"RyP5C")
        self.RyP5C.setDecimals(3)
        self.RyP5C.setMinimum(-50.000000000000000)
        self.RyP5C.setMaximum(50.000000000000000)
        self.RyP5C.setValue(0.000000000000000)

        self.gridLayout_21.addWidget(self.RyP5C, 1, 2, 1, 1)


        self.formLayout_10.setLayout(1, QFormLayout.FieldRole, self.gridLayout_21)


        self.verticalLayout_4.addWidget(self.RyWidget4)

        self.RyButtonBox = QDialogButtonBox(self.RyTab)
        self.RyButtonBox.setObjectName(u"RyButtonBox")
        self.RyButtonBox.setLayoutDirection(Qt.LeftToRight)
        self.RyButtonBox.setOrientation(Qt.Horizontal)
        self.RyButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.RyButtonBox.setCenterButtons(True)

        self.verticalLayout_4.addWidget(self.RyButtonBox)

        self.OptionsTabWidget.addTab(self.RyTab, "")
        self.RzTab = QWidget()
        self.RzTab.setObjectName(u"RzTab")
        self.verticalLayout_3 = QVBoxLayout(self.RzTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.RzFormLayout = QFormLayout()
        self.RzFormLayout.setObjectName(u"RzFormLayout")
        self.label_111 = QLabel(self.RzTab)
        self.label_111.setObjectName(u"label_111")

        self.RzFormLayout.setWidget(0, QFormLayout.LabelRole, self.label_111)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_112 = QLabel(self.RzTab)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_35.addWidget(self.label_112, 0, 2, 1, 1)

        self.label_113 = QLabel(self.RzTab)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_35.addWidget(self.label_113, 0, 1, 1, 1)

        self.label_114 = QLabel(self.RzTab)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_35.addWidget(self.label_114, 0, 0, 1, 1)

        self.RzP1C = QDoubleSpinBox(self.RzTab)
        self.RzP1C.setObjectName(u"RzP1C")
        self.RzP1C.setDecimals(3)
        self.RzP1C.setMinimum(-50.000000000000000)
        self.RzP1C.setMaximum(50.000000000000000)
        self.RzP1C.setValue(1.700000000000000)

        self.gridLayout_35.addWidget(self.RzP1C, 1, 2, 1, 1)

        self.RzP1B = QDoubleSpinBox(self.RzTab)
        self.RzP1B.setObjectName(u"RzP1B")
        self.RzP1B.setMaximum(5.000000000000000)
        self.RzP1B.setValue(2.000000000000000)

        self.gridLayout_35.addWidget(self.RzP1B, 1, 1, 1, 1)

        self.RzP1A = QDoubleSpinBox(self.RzTab)
        self.RzP1A.setObjectName(u"RzP1A")
        self.RzP1A.setDecimals(4)
        self.RzP1A.setMinimum(0.000100000000000)
        self.RzP1A.setMaximum(1.000000000000000)
        self.RzP1A.setSingleStep(0.000100000000000)
        self.RzP1A.setValue(0.030000000000000)

        self.gridLayout_35.addWidget(self.RzP1A, 1, 0, 1, 1)


        self.RzFormLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout_35)

        self.label_117 = QLabel(self.RzTab)
        self.label_117.setObjectName(u"label_117")

        self.RzFormLayout.setWidget(1, QFormLayout.LabelRole, self.label_117)

        self.RzScaleNzCheck = QCheckBox(self.RzTab)
        self.RzScaleNzCheck.setObjectName(u"RzScaleNzCheck")
        self.RzScaleNzCheck.setChecked(True)

        self.RzFormLayout.setWidget(2, QFormLayout.FieldRole, self.RzScaleNzCheck)

        self.RzScale = QDoubleSpinBox(self.RzTab)
        self.RzScale.setObjectName(u"RzScale")
        self.RzScale.setDecimals(5)
        self.RzScale.setMinimum(0.000010000000000)
        self.RzScale.setMaximum(1000000000.000000000000000)
        self.RzScale.setValue(15.000000000000000)

        self.RzFormLayout.setWidget(1, QFormLayout.FieldRole, self.RzScale)


        self.verticalLayout_3.addLayout(self.RzFormLayout)

        self.RzTickLayout = QHBoxLayout()
        self.RzTickLayout.setObjectName(u"RzTickLayout")
        self.RzPoly2Check = QCheckBox(self.RzTab)
        self.RzPoly2Check.setObjectName(u"RzPoly2Check")
        self.RzPoly2Check.setChecked(True)

        self.RzTickLayout.addWidget(self.RzPoly2Check)

        self.RzPoly3Check = QCheckBox(self.RzTab)
        self.RzPoly3Check.setObjectName(u"RzPoly3Check")

        self.RzTickLayout.addWidget(self.RzPoly3Check)

        self.RzPoly4Check = QCheckBox(self.RzTab)
        self.RzPoly4Check.setObjectName(u"RzPoly4Check")

        self.RzTickLayout.addWidget(self.RzPoly4Check)

        self.RzPoly5Check = QCheckBox(self.RzTab)
        self.RzPoly5Check.setObjectName(u"RzPoly5Check")

        self.RzTickLayout.addWidget(self.RzPoly5Check)


        self.verticalLayout_3.addLayout(self.RzTickLayout)

        self.RzWidget1 = QWidget(self.RzTab)
        self.RzWidget1.setObjectName(u"RzWidget1")
        self.formLayout_16 = QFormLayout(self.RzWidget1)
        self.formLayout_16.setObjectName(u"formLayout_16")
        self.label_97 = QLabel(self.RzWidget1)
        self.label_97.setObjectName(u"label_97")

        self.formLayout_16.setWidget(0, QFormLayout.LabelRole, self.label_97)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_98 = QLabel(self.RzWidget1)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_31.addWidget(self.label_98, 0, 1, 1, 1)

        self.label_99 = QLabel(self.RzWidget1)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_31.addWidget(self.label_99, 0, 0, 1, 1)

        self.RzB1A = QDoubleSpinBox(self.RzWidget1)
        self.RzB1A.setObjectName(u"RzB1A")
        self.RzB1A.setMinimum(2.000000000000000)
        self.RzB1A.setMaximum(300.000000000000000)
        self.RzB1A.setValue(20.000000000000000)

        self.gridLayout_31.addWidget(self.RzB1A, 1, 0, 1, 1)

        self.RzB1B = QDoubleSpinBox(self.RzWidget1)
        self.RzB1B.setObjectName(u"RzB1B")
        self.RzB1B.setMinimum(0.010000000000000)
        self.RzB1B.setMaximum(100.000000000000000)
        self.RzB1B.setValue(10.000000000000000)

        self.gridLayout_31.addWidget(self.RzB1B, 1, 1, 1, 1)


        self.formLayout_16.setLayout(0, QFormLayout.FieldRole, self.gridLayout_31)

        self.label_100 = QLabel(self.RzWidget1)
        self.label_100.setObjectName(u"label_100")

        self.formLayout_16.setWidget(1, QFormLayout.LabelRole, self.label_100)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_101 = QLabel(self.RzWidget1)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_32.addWidget(self.label_101, 0, 0, 1, 1)

        self.label_102 = QLabel(self.RzWidget1)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_32.addWidget(self.label_102, 0, 1, 1, 1)

        self.label_103 = QLabel(self.RzWidget1)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_32.addWidget(self.label_103, 0, 2, 1, 1)

        self.RzP2A = QDoubleSpinBox(self.RzWidget1)
        self.RzP2A.setObjectName(u"RzP2A")
        self.RzP2A.setDecimals(4)
        self.RzP2A.setMinimum(0.000100000000000)
        self.RzP2A.setMaximum(1.000000000000000)
        self.RzP2A.setSingleStep(0.000100000000000)
        self.RzP2A.setValue(0.680000000000000)

        self.gridLayout_32.addWidget(self.RzP2A, 1, 0, 1, 1)

        self.RzP2B = QDoubleSpinBox(self.RzWidget1)
        self.RzP2B.setObjectName(u"RzP2B")
        self.RzP2B.setMaximum(5.000000000000000)
        self.RzP2B.setValue(1.000000000000000)

        self.gridLayout_32.addWidget(self.RzP2B, 1, 1, 1, 1)

        self.RzP2C = QDoubleSpinBox(self.RzWidget1)
        self.RzP2C.setObjectName(u"RzP2C")
        self.RzP2C.setDecimals(3)
        self.RzP2C.setMinimum(-50.000000000000000)
        self.RzP2C.setMaximum(50.000000000000000)

        self.gridLayout_32.addWidget(self.RzP2C, 1, 2, 1, 1)


        self.formLayout_16.setLayout(1, QFormLayout.FieldRole, self.gridLayout_32)


        self.verticalLayout_3.addWidget(self.RzWidget1)

        self.RzWidget2 = QWidget(self.RzTab)
        self.RzWidget2.setObjectName(u"RzWidget2")
        self.RzWidget2.setEnabled(False)
        self.formLayout_14 = QFormLayout(self.RzWidget2)
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.label_83 = QLabel(self.RzWidget2)
        self.label_83.setObjectName(u"label_83")

        self.formLayout_14.setWidget(0, QFormLayout.LabelRole, self.label_83)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_84 = QLabel(self.RzWidget2)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_27.addWidget(self.label_84, 0, 1, 1, 1)

        self.label_85 = QLabel(self.RzWidget2)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_27.addWidget(self.label_85, 0, 0, 1, 1)

        self.RzB2B = QDoubleSpinBox(self.RzWidget2)
        self.RzB2B.setObjectName(u"RzB2B")
        self.RzB2B.setMinimum(0.010000000000000)
        self.RzB2B.setMaximum(100.000000000000000)
        self.RzB2B.setValue(1.000000000000000)

        self.gridLayout_27.addWidget(self.RzB2B, 1, 1, 1, 1)

        self.RzB2A = QDoubleSpinBox(self.RzWidget2)
        self.RzB2A.setObjectName(u"RzB2A")
        self.RzB2A.setMinimum(2.000000000000000)
        self.RzB2A.setMaximum(300.000000000000000)
        self.RzB2A.setValue(50.000000000000000)

        self.gridLayout_27.addWidget(self.RzB2A, 1, 0, 1, 1)


        self.formLayout_14.setLayout(0, QFormLayout.FieldRole, self.gridLayout_27)

        self.label_86 = QLabel(self.RzWidget2)
        self.label_86.setObjectName(u"label_86")

        self.formLayout_14.setWidget(2, QFormLayout.LabelRole, self.label_86)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_87 = QLabel(self.RzWidget2)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_28.addWidget(self.label_87, 0, 1, 1, 1)

        self.label_88 = QLabel(self.RzWidget2)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_28.addWidget(self.label_88, 0, 2, 1, 1)

        self.label_89 = QLabel(self.RzWidget2)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_28.addWidget(self.label_89, 0, 0, 1, 1)

        self.RzP3A = QDoubleSpinBox(self.RzWidget2)
        self.RzP3A.setObjectName(u"RzP3A")
        self.RzP3A.setDecimals(4)
        self.RzP3A.setMinimum(0.000100000000000)
        self.RzP3A.setMaximum(1.000000000000000)
        self.RzP3A.setSingleStep(0.000100000000000)
        self.RzP3A.setValue(1.000000000000000)

        self.gridLayout_28.addWidget(self.RzP3A, 1, 0, 1, 1)

        self.RzP3B = QDoubleSpinBox(self.RzWidget2)
        self.RzP3B.setObjectName(u"RzP3B")
        self.RzP3B.setMaximum(5.000000000000000)
        self.RzP3B.setValue(1.000000000000000)

        self.gridLayout_28.addWidget(self.RzP3B, 1, 1, 1, 1)

        self.RzP3C = QDoubleSpinBox(self.RzWidget2)
        self.RzP3C.setObjectName(u"RzP3C")
        self.RzP3C.setDecimals(3)
        self.RzP3C.setMinimum(-50.000000000000000)
        self.RzP3C.setMaximum(50.000000000000000)

        self.gridLayout_28.addWidget(self.RzP3C, 1, 2, 1, 1)


        self.formLayout_14.setLayout(2, QFormLayout.FieldRole, self.gridLayout_28)


        self.verticalLayout_3.addWidget(self.RzWidget2)

        self.RzWidget3 = QWidget(self.RzTab)
        self.RzWidget3.setObjectName(u"RzWidget3")
        self.RzWidget3.setEnabled(False)
        self.formLayout_17 = QFormLayout(self.RzWidget3)
        self.formLayout_17.setObjectName(u"formLayout_17")
        self.label_104 = QLabel(self.RzWidget3)
        self.label_104.setObjectName(u"label_104")

        self.formLayout_17.setWidget(0, QFormLayout.LabelRole, self.label_104)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_105 = QLabel(self.RzWidget3)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_33.addWidget(self.label_105, 0, 0, 1, 1)

        self.label_106 = QLabel(self.RzWidget3)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_33.addWidget(self.label_106, 0, 1, 1, 1)

        self.RzB3A = QDoubleSpinBox(self.RzWidget3)
        self.RzB3A.setObjectName(u"RzB3A")
        self.RzB3A.setMinimum(2.000000000000000)
        self.RzB3A.setMaximum(300.000000000000000)
        self.RzB3A.setValue(50.000000000000000)

        self.gridLayout_33.addWidget(self.RzB3A, 1, 0, 1, 1)

        self.RzB3B = QDoubleSpinBox(self.RzWidget3)
        self.RzB3B.setObjectName(u"RzB3B")
        self.RzB3B.setMinimum(0.010000000000000)
        self.RzB3B.setMaximum(100.000000000000000)
        self.RzB3B.setValue(1.000000000000000)

        self.gridLayout_33.addWidget(self.RzB3B, 1, 1, 1, 1)


        self.formLayout_17.setLayout(0, QFormLayout.FieldRole, self.gridLayout_33)

        self.label_107 = QLabel(self.RzWidget3)
        self.label_107.setObjectName(u"label_107")

        self.formLayout_17.setWidget(1, QFormLayout.LabelRole, self.label_107)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_108 = QLabel(self.RzWidget3)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_34.addWidget(self.label_108, 0, 0, 1, 1)

        self.label_109 = QLabel(self.RzWidget3)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_34.addWidget(self.label_109, 0, 1, 1, 1)

        self.label_110 = QLabel(self.RzWidget3)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_34.addWidget(self.label_110, 0, 2, 1, 1)

        self.RzP4A = QDoubleSpinBox(self.RzWidget3)
        self.RzP4A.setObjectName(u"RzP4A")
        self.RzP4A.setDecimals(4)
        self.RzP4A.setMinimum(0.000100000000000)
        self.RzP4A.setMaximum(1.000000000000000)
        self.RzP4A.setSingleStep(0.000100000000000)
        self.RzP4A.setValue(1.000000000000000)

        self.gridLayout_34.addWidget(self.RzP4A, 1, 0, 1, 1)

        self.RzP4B = QDoubleSpinBox(self.RzWidget3)
        self.RzP4B.setObjectName(u"RzP4B")
        self.RzP4B.setMaximum(5.000000000000000)
        self.RzP4B.setSingleStep(1.000000000000000)
        self.RzP4B.setValue(1.000000000000000)

        self.gridLayout_34.addWidget(self.RzP4B, 1, 1, 1, 1)

        self.RzP4C = QDoubleSpinBox(self.RzWidget3)
        self.RzP4C.setObjectName(u"RzP4C")
        self.RzP4C.setDecimals(3)
        self.RzP4C.setMinimum(-50.000000000000000)
        self.RzP4C.setMaximum(50.000000000000000)

        self.gridLayout_34.addWidget(self.RzP4C, 1, 2, 1, 1)


        self.formLayout_17.setLayout(1, QFormLayout.FieldRole, self.gridLayout_34)


        self.verticalLayout_3.addWidget(self.RzWidget3)

        self.RzWidget4 = QWidget(self.RzTab)
        self.RzWidget4.setObjectName(u"RzWidget4")
        self.RzWidget4.setEnabled(False)
        self.formLayout_15 = QFormLayout(self.RzWidget4)
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.label_90 = QLabel(self.RzWidget4)
        self.label_90.setObjectName(u"label_90")

        self.formLayout_15.setWidget(0, QFormLayout.LabelRole, self.label_90)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_91 = QLabel(self.RzWidget4)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_29.addWidget(self.label_91, 0, 0, 1, 1)

        self.label_92 = QLabel(self.RzWidget4)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_29.addWidget(self.label_92, 0, 1, 1, 1)

        self.RzB4A = QDoubleSpinBox(self.RzWidget4)
        self.RzB4A.setObjectName(u"RzB4A")
        self.RzB4A.setMinimum(2.000000000000000)
        self.RzB4A.setMaximum(300.000000000000000)
        self.RzB4A.setSingleStep(1.000000000000000)
        self.RzB4A.setValue(50.000000000000000)

        self.gridLayout_29.addWidget(self.RzB4A, 1, 0, 1, 1)

        self.RzB4B = QDoubleSpinBox(self.RzWidget4)
        self.RzB4B.setObjectName(u"RzB4B")
        self.RzB4B.setMinimum(0.010000000000000)
        self.RzB4B.setMaximum(100.000000000000000)
        self.RzB4B.setValue(1.000000000000000)

        self.gridLayout_29.addWidget(self.RzB4B, 1, 1, 1, 1)


        self.formLayout_15.setLayout(0, QFormLayout.FieldRole, self.gridLayout_29)

        self.label_93 = QLabel(self.RzWidget4)
        self.label_93.setObjectName(u"label_93")

        self.formLayout_15.setWidget(1, QFormLayout.LabelRole, self.label_93)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_94 = QLabel(self.RzWidget4)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_30.addWidget(self.label_94, 0, 1, 1, 1)

        self.label_95 = QLabel(self.RzWidget4)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_30.addWidget(self.label_95, 0, 0, 1, 1)

        self.label_96 = QLabel(self.RzWidget4)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_30.addWidget(self.label_96, 0, 2, 1, 1)

        self.RzP5A = QDoubleSpinBox(self.RzWidget4)
        self.RzP5A.setObjectName(u"RzP5A")
        self.RzP5A.setDecimals(4)
        self.RzP5A.setMinimum(0.000100000000000)
        self.RzP5A.setMaximum(1.000000000000000)
        self.RzP5A.setSingleStep(0.000100000000000)
        self.RzP5A.setValue(1.000000000000000)

        self.gridLayout_30.addWidget(self.RzP5A, 1, 0, 1, 1)

        self.RzP5B = QDoubleSpinBox(self.RzWidget4)
        self.RzP5B.setObjectName(u"RzP5B")
        self.RzP5B.setMaximum(5.000000000000000)
        self.RzP5B.setValue(1.000000000000000)

        self.gridLayout_30.addWidget(self.RzP5B, 1, 1, 1, 1)

        self.RzP5C = QDoubleSpinBox(self.RzWidget4)
        self.RzP5C.setObjectName(u"RzP5C")
        self.RzP5C.setDecimals(3)
        self.RzP5C.setMinimum(-50.000000000000000)
        self.RzP5C.setMaximum(50.000000000000000)
        self.RzP5C.setValue(0.000000000000000)

        self.gridLayout_30.addWidget(self.RzP5C, 1, 2, 1, 1)


        self.formLayout_15.setLayout(1, QFormLayout.FieldRole, self.gridLayout_30)


        self.verticalLayout_3.addWidget(self.RzWidget4)

        self.RzButtonBox = QDialogButtonBox(self.RzTab)
        self.RzButtonBox.setObjectName(u"RzButtonBox")
        self.RzButtonBox.setLayoutDirection(Qt.LeftToRight)
        self.RzButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.RzButtonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.RzButtonBox)

        self.OptionsTabWidget.addTab(self.RzTab, "")

        self.horizontalLayout.addWidget(self.OptionsTabWidget)

        self.DisplayTabWidget = QTabWidget(self.centralwidget)
        self.DisplayTabWidget.setObjectName(u"DisplayTabWidget")
        self.DisplayTabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DisplayTabWidget.sizePolicy().hasHeightForWidth())
        self.DisplayTabWidget.setSizePolicy(sizePolicy)
        self.DisplayTabWidget.setMinimumSize(QSize(600, 300))
        self.DisplayTabWidget.setSizeIncrement(QSize(0, 0))
        self.MatrixTab = QWidget()
        self.MatrixTab.setObjectName(u"MatrixTab")
        self.DisplayTabWidget.addTab(self.MatrixTab, "")
        self.ResistivityTab = QWidget()
        self.ResistivityTab.setObjectName(u"ResistivityTab")
        self.DisplayTabWidget.addTab(self.ResistivityTab, "")
        self.ContourTab = QWidget()
        self.ContourTab.setObjectName(u"ContourTab")
        self.ContourTab.setEnabled(False)
        self.DisplayTabWidget.addTab(self.ContourTab, "")
        self.ResistanceTab = QWidget()
        self.ResistanceTab.setObjectName(u"ResistanceTab")
        self.ResistanceTab.setEnabled(False)
        self.DisplayTabWidget.addTab(self.ResistanceTab, "")
        self.FittingTab = QWidget()
        self.FittingTab.setObjectName(u"FittingTab")
        self.FittingTab.setEnabled(False)
        self.DisplayTabWidget.addTab(self.FittingTab, "")

        self.horizontalLayout.addWidget(self.DisplayTabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 957, 26))
        self.menuSetup = QMenu(self.menubar)
        self.menuSetup.setObjectName(u"menuSetup")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSetup.menuAction())
        self.menuSetup.addAction(self.actionNew)
        self.menuSetup.addAction(self.actionOpen)
        self.menuSetup.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        self.OptionsTabWidget.setCurrentIndex(0)
        self.DisplayTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input Variables", None))
        self.MeshSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Mesh Size", None))
        self.InputLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Input Location", None))
        self.OutputLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Output Location", None))
        self.FixedVLabel.setText(QCoreApplication.translate("MainWindow", u"Fixed Voltages", None))
        self.IntializeButton.setText(QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Y Size", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"X Size", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Z Size", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.OutputVLabel.setText(QCoreApplication.translate("MainWindow", u"Output Voltage", None))
        self.InputVLabel.setText(QCoreApplication.translate("MainWindow", u"Input Voltage", None))
        self.InputProbeLabel.setText(QCoreApplication.translate("MainWindow", u"Input Probe", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Measurement Variables", None))
        self.OutputProbeLabel.setText(QCoreApplication.translate("MainWindow", u"Output Probe", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Show Intrinsic", None))
        self.CheckX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.CheckY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.CheckZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.MeasureButton.setText(QCoreApplication.translate("MainWindow", u"Measure", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.OptionsTabWidget.setTabText(self.OptionsTabWidget.indexOf(self.InputValuesTab), QCoreApplication.translate("MainWindow", u"Geometry Inputs", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Poly 1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"RxScale", None))
        self.RxScaleNxCheck.setText(QCoreApplication.translate("MainWindow", u"Scale by Size of Mesh", None))
        self.RxPoly2Check.setText(QCoreApplication.translate("MainWindow", u"Poly 2", None))
        self.RxPoly3Check.setText(QCoreApplication.translate("MainWindow", u"Poly 3", None))
        self.RxPoly4Check.setText(QCoreApplication.translate("MainWindow", u"Poly 4", None))
        self.RxPoly5Check.setText(QCoreApplication.translate("MainWindow", u"Poly 5", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"F-D 1", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Poly 2", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"F-D 2", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Poly 3", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"F-D 3", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Poly 4", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"F-D 4", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Poly 5", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.OptionsTabWidget.setTabText(self.OptionsTabWidget.indexOf(self.RxTab), QCoreApplication.translate("MainWindow", u"Rx", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Poly 1", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"RyScale", None))
        self.RyScaleNyCheck.setText(QCoreApplication.translate("MainWindow", u"Scale by Size of Mesh", None))
        self.RyPoly2Check.setText(QCoreApplication.translate("MainWindow", u"Poly 2", None))
        self.RyPoly3Check.setText(QCoreApplication.translate("MainWindow", u"Poly 3", None))
        self.RyPoly4Check.setText(QCoreApplication.translate("MainWindow", u"Poly 4", None))
        self.RyPoly5Check.setText(QCoreApplication.translate("MainWindow", u"Poly 5", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"F-D 1", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Poly 2", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"F-D 2", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Poly 3", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"F-D 3", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Poly 4", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"F-D 4", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Poly 5", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.OptionsTabWidget.setTabText(self.OptionsTabWidget.indexOf(self.RyTab), QCoreApplication.translate("MainWindow", u"Ry", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Poly 1", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"RxScale", None))
        self.RzScaleNzCheck.setText(QCoreApplication.translate("MainWindow", u"Scale by Size of Mesh", None))
        self.RzPoly2Check.setText(QCoreApplication.translate("MainWindow", u"Poly 2", None))
        self.RzPoly3Check.setText(QCoreApplication.translate("MainWindow", u"Poly 3", None))
        self.RzPoly4Check.setText(QCoreApplication.translate("MainWindow", u"Poly 4", None))
        self.RzPoly5Check.setText(QCoreApplication.translate("MainWindow", u"Poly 5", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"F-D 1", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Poly 2", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"F-D 2", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Poly 3", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"F-D 3", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Poly 4", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"F-D 4", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Cutoff", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Poly 5", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Exponent", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.OptionsTabWidget.setTabText(self.OptionsTabWidget.indexOf(self.RzTab), QCoreApplication.translate("MainWindow", u"Rz", None))
#if QT_CONFIG(tooltip)
        self.DisplayTabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Matrix</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.DisplayTabWidget.setTabText(self.DisplayTabWidget.indexOf(self.MatrixTab), QCoreApplication.translate("MainWindow", u"Matrix", None))
        self.DisplayTabWidget.setTabText(self.DisplayTabWidget.indexOf(self.ResistivityTab), QCoreApplication.translate("MainWindow", u"Resistivity", None))
        self.DisplayTabWidget.setTabText(self.DisplayTabWidget.indexOf(self.ContourTab), QCoreApplication.translate("MainWindow", u"Contour", None))
        self.DisplayTabWidget.setTabText(self.DisplayTabWidget.indexOf(self.ResistanceTab), QCoreApplication.translate("MainWindow", u"Simulated Resistance", None))
        self.DisplayTabWidget.setTabText(self.DisplayTabWidget.indexOf(self.FittingTab), QCoreApplication.translate("MainWindow", u"Fitting", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

