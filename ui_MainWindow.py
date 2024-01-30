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
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(933, 597)
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


        self.verticalLayout_6.addWidget(self.SetupWidget)

        self.MeasurementWidget = QWidget(self.centralwidget)
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


        self.verticalLayout_6.addWidget(self.MeasurementWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.TabWidget = QTabWidget(self.centralwidget)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabWidget.sizePolicy().hasHeightForWidth())
        self.TabWidget.setSizePolicy(sizePolicy)
        self.TabWidget.setMinimumSize(QSize(600, 300))
        self.TabWidget.setSizeIncrement(QSize(0, 0))
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
        self.menubar.setGeometry(QRect(0, 0, 933, 26))
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
#if QT_CONFIG(tooltip)
        self.TabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Matrix</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.MatrixTab), QCoreApplication.translate("MainWindow", u"Matrix", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.ContourTab), QCoreApplication.translate("MainWindow", u"Contour", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.ResistanceTab), QCoreApplication.translate("MainWindow", u"Resistance", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.FittingTab), QCoreApplication.translate("MainWindow", u"Fitting", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

