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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 568)
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
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SetupWidget = QWidget(self.centralwidget)
        self.SetupWidget.setObjectName(u"SetupWidget")
        self.formLayout = QFormLayout(self.SetupWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.SetupWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.SetupWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.label_16 = QLabel(self.SetupWidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_8.addWidget(self.label_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.NxBox = QSpinBox(self.SetupWidget)
        self.NxBox.setObjectName(u"NxBox")
        self.NxBox.setMinimum(1)
        self.NxBox.setValue(24)

        self.horizontalLayout_9.addWidget(self.NxBox)

        self.NyBox = QSpinBox(self.SetupWidget)
        self.NyBox.setObjectName(u"NyBox")
        self.NyBox.setMinimum(1)
        self.NyBox.setValue(12)

        self.horizontalLayout_9.addWidget(self.NyBox)

        self.NzBox = QSpinBox(self.SetupWidget)
        self.NzBox.setObjectName(u"NzBox")
        self.NzBox.setMinimum(1)

        self.horizontalLayout_9.addWidget(self.NzBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.verticalLayout_4)

        self.MeshSizeLabel = QLabel(self.SetupWidget)
        self.MeshSizeLabel.setObjectName(u"MeshSizeLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.MeshSizeLabel)

        self.label_2 = QLabel(self.SetupWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.InputLocationLabel = QLabel(self.SetupWidget)
        self.InputLocationLabel.setObjectName(u"InputLocationLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.InputLocationLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.SetupWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_7 = QLabel(self.SetupWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(self.SetupWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.IxBox = QSpinBox(self.SetupWidget)
        self.IxBox.setObjectName(u"IxBox")
        self.IxBox.setMinimum(1)
        self.IxBox.setMaximum(24)
        self.IxBox.setValue(3)

        self.horizontalLayout_2.addWidget(self.IxBox)

        self.IyBox = QSpinBox(self.SetupWidget)
        self.IyBox.setObjectName(u"IyBox")
        self.IyBox.setMinimum(1)
        self.IyBox.setMaximum(12)

        self.horizontalLayout_2.addWidget(self.IyBox)

        self.IzBox = QSpinBox(self.SetupWidget)
        self.IzBox.setObjectName(u"IzBox")
        self.IzBox.setMinimum(1)
        self.IzBox.setMaximum(1)

        self.horizontalLayout_2.addWidget(self.IzBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.verticalLayout)

        self.OutputLocationLabel = QLabel(self.SetupWidget)
        self.OutputLocationLabel.setObjectName(u"OutputLocationLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.OutputLocationLabel)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.SetupWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.SetupWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.SetupWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.OxBox = QSpinBox(self.SetupWidget)
        self.OxBox.setObjectName(u"OxBox")
        self.OxBox.setMinimum(1)
        self.OxBox.setMaximum(24)
        self.OxBox.setValue(3)

        self.horizontalLayout_7.addWidget(self.OxBox)

        self.OyBox = QSpinBox(self.SetupWidget)
        self.OyBox.setObjectName(u"OyBox")
        self.OyBox.setMinimum(1)
        self.OyBox.setMaximum(12)
        self.OyBox.setValue(12)

        self.horizontalLayout_7.addWidget(self.OyBox)

        self.OzBox = QSpinBox(self.SetupWidget)
        self.OzBox.setObjectName(u"OzBox")
        self.OzBox.setMinimum(1)
        self.OzBox.setMaximum(1)

        self.horizontalLayout_7.addWidget(self.OzBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.verticalLayout_3)

        self.FixedVLabel = QLabel(self.SetupWidget)
        self.FixedVLabel.setObjectName(u"FixedVLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.FixedVLabel)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.InputVLabel = QLabel(self.SetupWidget)
        self.InputVLabel.setObjectName(u"InputVLabel")

        self.horizontalLayout_10.addWidget(self.InputVLabel)

        self.OutputVLabel = QLabel(self.SetupWidget)
        self.OutputVLabel.setObjectName(u"OutputVLabel")

        self.horizontalLayout_10.addWidget(self.OutputVLabel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.IvBox = QDoubleSpinBox(self.SetupWidget)
        self.IvBox.setObjectName(u"IvBox")
        self.IvBox.setMinimum(-100.000000000000000)
        self.IvBox.setMaximum(100.000000000000000)
        self.IvBox.setValue(5.000000000000000)

        self.horizontalLayout_11.addWidget(self.IvBox)

        self.OvBox = QDoubleSpinBox(self.SetupWidget)
        self.OvBox.setObjectName(u"OvBox")
        self.OvBox.setMinimum(-100.000000000000000)
        self.OvBox.setMaximum(100.000000000000000)
        self.OvBox.setValue(-5.000000000000000)

        self.horizontalLayout_11.addWidget(self.OvBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.verticalLayout_5)

        self.IntializeButton = QPushButton(self.SetupWidget)
        self.IntializeButton.setObjectName(u"IntializeButton")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.IntializeButton)


        self.verticalLayout_6.addWidget(self.SetupWidget)

        self.MeasurementWidget = QWidget(self.centralwidget)
        self.MeasurementWidget.setObjectName(u"MeasurementWidget")
        self.MeasurementWidget.setEnabled(False)
        self.formLayout_2 = QFormLayout(self.MeasurementWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.InputProbeLabel = QLabel(self.MeasurementWidget)
        self.InputProbeLabel.setObjectName(u"InputProbeLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.InputProbeLabel)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.MeasurementWidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.label_18 = QLabel(self.MeasurementWidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.label_19 = QLabel(self.MeasurementWidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.IPxBox = QSpinBox(self.MeasurementWidget)
        self.IPxBox.setObjectName(u"IPxBox")
        self.IPxBox.setMinimum(1)
        self.IPxBox.setMaximum(24)
        self.IPxBox.setValue(21)

        self.horizontalLayout_13.addWidget(self.IPxBox)

        self.IPyBox = QSpinBox(self.MeasurementWidget)
        self.IPyBox.setObjectName(u"IPyBox")
        self.IPyBox.setMinimum(1)
        self.IPyBox.setMaximum(12)

        self.horizontalLayout_13.addWidget(self.IPyBox)

        self.IPzBox = QSpinBox(self.MeasurementWidget)
        self.IPzBox.setObjectName(u"IPzBox")
        self.IPzBox.setMinimum(1)
        self.IPzBox.setMaximum(1)

        self.horizontalLayout_13.addWidget(self.IPzBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.verticalLayout_9)

        self.label_3 = QLabel(self.MeasurementWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.OutputProbeLabel = QLabel(self.MeasurementWidget)
        self.OutputProbeLabel.setObjectName(u"OutputProbeLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.OutputProbeLabel)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(self.MeasurementWidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_14.addWidget(self.label_20)

        self.label_21 = QLabel(self.MeasurementWidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)

        self.label_22 = QLabel(self.MeasurementWidget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_14.addWidget(self.label_22)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.OPxBox = QSpinBox(self.MeasurementWidget)
        self.OPxBox.setObjectName(u"OPxBox")
        self.OPxBox.setMinimum(1)
        self.OPxBox.setMaximum(24)
        self.OPxBox.setValue(21)

        self.horizontalLayout_15.addWidget(self.OPxBox)

        self.OPyBox = QSpinBox(self.MeasurementWidget)
        self.OPyBox.setObjectName(u"OPyBox")
        self.OPyBox.setMinimum(1)
        self.OPyBox.setMaximum(12)
        self.OPyBox.setValue(12)

        self.horizontalLayout_15.addWidget(self.OPyBox)

        self.OPzBox = QSpinBox(self.MeasurementWidget)
        self.OPzBox.setObjectName(u"OPzBox")
        self.OPzBox.setMinimum(1)
        self.OPzBox.setMaximum(1)

        self.horizontalLayout_15.addWidget(self.OPzBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.verticalLayout_10)

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


        self.verticalLayout_6.addWidget(self.MeasurementWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.TabWidget = QTabWidget(self.centralwidget)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setEnabled(True)
        self.TabWidget.setMinimumSize(QSize(600, 300))
        self.MatrixTab = QWidget()
        self.MatrixTab.setObjectName(u"MatrixTab")
        self.TabWidget.addTab(self.MatrixTab, "")
        self.ContourTab = QWidget()
        self.ContourTab.setObjectName(u"ContourTab")
        self.ContourTab.setEnabled(False)
        self.TabWidget.addTab(self.ContourTab, "")
        self.ResistanceTab = QWidget()
        self.ResistanceTab.setObjectName(u"ResistanceTab")
        self.ResistanceTab.setEnabled(False)
        self.TabWidget.addTab(self.ResistanceTab, "")
        self.FittingTab = QWidget()
        self.FittingTab.setObjectName(u"FittingTab")
        self.FittingTab.setEnabled(False)
        self.TabWidget.addTab(self.FittingTab, "")

        self.horizontalLayout.addWidget(self.TabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 911, 26))
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

        self.TabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"X Size", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Y Size", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Z Size", None))
        self.MeshSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Mesh Size", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input Variables", None))
        self.InputLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Input Location", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.OutputLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Output Location", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.FixedVLabel.setText(QCoreApplication.translate("MainWindow", u"Fixed Voltages", None))
        self.InputVLabel.setText(QCoreApplication.translate("MainWindow", u"Input Voltage", None))
        self.OutputVLabel.setText(QCoreApplication.translate("MainWindow", u"Output Voltage", None))
        self.IntializeButton.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.InputProbeLabel.setText(QCoreApplication.translate("MainWindow", u"Input Probe", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Measurement Variables", None))
        self.OutputProbeLabel.setText(QCoreApplication.translate("MainWindow", u"Output Probe", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"X position", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Y position", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Z position", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Show Intrinsic", None))
        self.CheckX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.CheckY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.CheckZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.MeasureButton.setText(QCoreApplication.translate("MainWindow", u"Measure", None))
#if QT_CONFIG(tooltip)
        self.TabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Matrix</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.MatrixTab), QCoreApplication.translate("MainWindow", u"Matrix", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.ContourTab), QCoreApplication.translate("MainWindow", u"Contour", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.ResistanceTab), QCoreApplication.translate("MainWindow", u"Resistance", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.FittingTab), QCoreApplication.translate("MainWindow", u"Fitting", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

