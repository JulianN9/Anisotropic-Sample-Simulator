import sys
import numpy as np
import pandas as pd
import pickle
import itertools as it
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QSlider, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout, QDialog, QFileDialog
from ui_MainWindow import Ui_MainWindow
from ui_AdvancedOptions import Ui_AdvancedOptions
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from Simulator3d import simulate
from ContourPlot import plotContour
from MatrixDiagram3d import plotMatrix, plotLeads
from ResistancePlot import ResistancePlot
from ResistivityFunctions import userfunction
from Fitting import fitR

# Iterating the inputlists over their widths.
def inputlist(list,listWidth):
    newlist=[]
    for i,j,k in it.product(*[range(listWidth[0]),range(listWidth[1]),range(listWidth[2])]):
            newlist.append([list[0]+i,list[1]+j,list[2]+k])
    return newlist

# Class to plot matplotlib
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100,check=False):
        fig = Figure(figsize=(width, height), dpi=dpi)
        if check==False:
            self.axes = fig.add_subplot(111)
        else:
            self.axes = fig.add_subplot(111,projection='3d')
        super(MplCanvas, self).__init__(fig)

# Advanced Options Dialog Class
class AdvancedOptions(QtWidgets.QDialog, Ui_AdvancedOptions):
    def __init__(self,Nlist,INlist,ONlist,SR,SEP,Header,TRange):
        super(AdvancedOptions, self).__init__()
        self.setupUi(self)
        Nx, Ny, Nz = Nlist
        self.INxBox.setMaximum(Nx); self.ONxBox.setMaximum(Nx)
        self.INyBox.setMaximum(Ny); self.ONyBox.setMaximum(Ny)
        self.INzBox.setMaximum(Nz); self.ONzBox.setMaximum(Nz)
        self.INxBox.setValue(INlist[0]); self.ONxBox.setValue(ONlist[0])
        self.INyBox.setValue(INlist[1]); self.ONyBox.setValue(ONlist[1])
        self.INzBox.setValue(INlist[2]); self.ONzBox.setValue(ONlist[2])
        self.TmBox.setValue(TRange[0]); self.TMBox.setValue(TRange[1]); self.TeBox.setValue(TRange[2])
        self.ResistivitySR.setValue(SR)
        self.ResistivitySeperator.setPlainText(SEP)
        self.ResistivityHeader.setPlainText(str(Header).replace('[', '').replace(']', '').replace("'", '').replace('"', ''))

        self.fileName = ""
        self.ResistivityButton.clicked.connect(self.GetFileName)

    def GetFileName(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Load Data", "", "Data File (*.txt *.csv *.lvm *.dat)")[0]

# Main Window Class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Basic Functionality:
        # Setting up the Dictionary
        self.VD = {}
        self.FD = {}
        self.VD['TRange'] = [2,300,100]
        self.VD['INlist'] = [1,1,1]
        self.VD['ONlist'] = [1,1,1]
        self.VD['DatafileName'] = ""
        self.VD['DataSR'] = 0
        self.VD['DataSep'] = ','
        self.VD['DataHeader'] = ['T','R']
        self.GrabMValues()
        self.TemperatureList = np.linspace(*self.VD['TRange'])
        self.CalcRxList()
        self.CalcRyList()
        self.CalcRzList()
        # Setting up buttons
        self.IntializeButton.clicked.connect(self.Initialize)
        self.MeasureButton.clicked.connect(self.Measure)
        self.toolButton.clicked.connect(self.OpenAO)
        self.RxButtonBox.accepted.connect(self.CalcRxList)
        self.RyButtonBox.accepted.connect(self.CalcRyList)
        self.RzButtonBox.accepted.connect(self.CalcRzList)
        self.RxButtonBox.accepted.connect(self.PlotResitivity)
        self.RyButtonBox.accepted.connect(self.PlotResitivity)
        self.RzButtonBox.accepted.connect(self.PlotResitivity)
        self.RxButtonBox.rejected.connect(self.SetRxValues)
        self.RyButtonBox.rejected.connect(self.SetRyValues)
        self.RzButtonBox.rejected.connect(self.SetRzValues)
        # Setting up changing ranges
        self.NxBox.valueChanged[int].connect(self.changeNxValue)
        self.NyBox.valueChanged[int].connect(self.changeNyValue)
        self.NzBox.valueChanged[int].connect(self.changeNzValue)
        self.IxBox.valueChanged[int].connect(self.changeIOValue)
        self.IyBox.valueChanged[int].connect(self.changeIOValue)
        self.IzBox.valueChanged[int].connect(self.changeIOValue)
        self.OxBox.valueChanged[int].connect(self.changeIOValue)
        self.OyBox.valueChanged[int].connect(self.changeIOValue)
        self.OzBox.valueChanged[int].connect(self.changeIOValue)
        self.IvBox.valueChanged.connect(self.changeVValue)
        self.OvBox.valueChanged.connect(self.changeVValue)
        # Selecting amount of polynomials:
        self.GrabPValues()
        # Connecting State Changes
        self.RxPoly2Check.stateChanged[int].connect(self.ChangePxState)
        self.RxPoly3Check.stateChanged[int].connect(self.ChangePxState)
        self.RxPoly4Check.stateChanged[int].connect(self.ChangePxState)
        self.RxPoly5Check.stateChanged[int].connect(self.ChangePxState)
        self.RyPoly2Check.stateChanged[int].connect(self.ChangePyState)
        self.RyPoly3Check.stateChanged[int].connect(self.ChangePyState)
        self.RyPoly4Check.stateChanged[int].connect(self.ChangePyState)
        self.RyPoly5Check.stateChanged[int].connect(self.ChangePyState)
        self.RzPoly2Check.stateChanged[int].connect(self.ChangePzState)
        self.RzPoly3Check.stateChanged[int].connect(self.ChangePzState)
        self.RzPoly4Check.stateChanged[int].connect(self.ChangePzState)
        self.RzPoly5Check.stateChanged[int].connect(self.ChangePzState)

        # Graphics Setup:
        # Matrix Presentation:
        self.MatrixCanvas = MplCanvas(self, width=8, height=6, dpi=100,check=True)
        self.MatrixLayout = QVBoxLayout()
        self.MatrixTab.setLayout(self.MatrixLayout)
        self.MatrixLayout.addWidget(self.MatrixCanvas)
        self.RedrawMesh()
        # Contour Presentation:
        self.ContourCanvas = MplCanvas(self, width=5, height=4, dpi=100)

        # self.ContourToolbar = NavigationToolbar(self.ContourCanvas, self)
        # self.ContourLayout.addWidget(self.ContourToolbar)

        self.TValue = 0
        self.ZValue = 1

        self.TemperatureSlider = QSlider(self.ContourTab)
        self.TemperatureSlider.valueChanged[int].connect(self.changeTValue)
        self.TemperatureSlider.setOrientation(QtCore.Qt.Horizontal)

        self.ZSlider = QSlider(self.ContourTab)
        self.ZSlider.setMinimum(1)
        self.ZSlider.setMaximum(1)
        self.ZSlider.valueChanged[int].connect(self.changeZValue)
        self.ZSlider.setOrientation(QtCore.Qt.Horizontal)


        self.TemperatureLabel = QLabel(self.ContourTab)
        self.TemperatureLabel.setText("Temperature: "+str(self.TemperatureList[0]))

        self.ContourLayout = QVBoxLayout()
        self.ContourTab.setLayout(self.ContourLayout)

        self.ContourLayout.addWidget(self.ContourCanvas)
        self.ContourLayout.addWidget(self.TemperatureSlider)
        self.ContourLayout.addWidget(self.TemperatureLabel)
        self.ContourLayout.addWidget(self.ZSlider)
        # Resistance Presentation:
        self.ResistanceCanvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.ResistanceToolbar = NavigationToolbar(self.ResistanceCanvas, self)
        self.ResistanceLayout = QVBoxLayout()
        self.ResistanceTab.setLayout(self.ResistanceLayout)
        self.ResistanceLayout.addWidget(self.ResistanceToolbar)

        self.ResistanceLayout.addWidget(self.ResistanceCanvas)
        # Resistivity Presentation:
        self.ResistivityCanvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.ResistivityToolbar = NavigationToolbar(self.ResistivityCanvas, self)
        self.ResistivityLayout = QVBoxLayout()
        self.ResistivityTab.setLayout(self.ResistivityLayout)
        self.ResistivityLayout.addWidget(self.ResistivityToolbar)

        self.ResistivityLayout.addWidget(self.ResistivityCanvas)

        self.PlotResitivity()

        # Fitting Presentation:
        self.FittingCanvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.FittingToolbar = NavigationToolbar(self.FittingCanvas, self)
        self.FittingLayout = QVBoxLayout()
        self.FittingTab.setLayout(self.FittingLayout)
        self.FittingLayout.addWidget(self.FittingToolbar)

        self.FittingLayout.addWidget(self.FittingCanvas)
        self.FittingLayoutButtons = QHBoxLayout()
        self.FittingLayout.addLayout(self.FittingLayoutButtons)
        self.FittingPins = QtWidgets.QPushButton("Fit Pins")
        self.FittingRx = QtWidgets.QPushButton("Fit Rx")
        self.FittingRy = QtWidgets.QPushButton("Fit Ry")
        self.FittingRz = QtWidgets.QPushButton("Fit Rz")
        self.FittingLayoutButtons.addWidget(self.FittingPins)
        self.FittingLayoutButtons.addWidget(self.FittingRx)
        self.FittingLayoutButtons.addWidget(self.FittingRy)
        self.FittingLayoutButtons.addWidget(self.FittingRz)

        # self.DataPD = pd.DataFrame()
        self.FittingPins.clicked.connect(self.FittingWrapperP)
        self.FittingRx.clicked.connect(self.FittingWrapperX)
        self.FittingRy.clicked.connect(self.FittingWrapperY)
        self.FittingRz.clicked.connect(self.FittingWrapperZ)


        # Setting Up Actions:
        # self.menubar.triggered()
        # self.actionSave.triggered.connect(self.SaveDict('saved_dictionary'))
        # self.actionOpen.triggered.connect(self.LoadDict('saved_dictionary'))
        self.actionSave.triggered.connect(self.SaveDict)
        self.actionOpen.triggered.connect(self.LoadDict)

    def GrabMValues(self):
        self.VD['Nlist'] = [self.NxBox.value(),self.NyBox.value(),self.NzBox.value()]
        self.VD['Vlist'] = [ self.IvBox.value(), self.OvBox.value() ]
        self.VD['Ilist'] = inputlist([self.IxBox.value(), self.IyBox.value(), self.IzBox.value()],self.VD['INlist'])
        self.VD['Olist'] = inputlist([self.OxBox.value(), self.OyBox.value(), self.OzBox.value()],self.VD['ONlist'])
        self.VD['IPlist'] = [[self.IPxBox.value(),self.IPyBox.value(),self.IPzBox.value()]]
        self.VD['OPlist'] = [[self.OPxBox.value(),self.OPyBox.value(),self.OPzBox.value()]]

    def GrabRxValues(self):
        #Rx Polynomials
        self.VD['RxP1'] = [self.RxP1A.value(), self.RxP1B.value(), self.RxP1C.value()]
        self.VD['RxP2'] = [self.RxP2A.value(), self.RxP2B.value(), self.RxP2C.value()]
        self.VD['RxP3'] = [self.RxP3A.value(), self.RxP3B.value(), self.RxP3C.value()]
        self.VD['RxP4'] = [self.RxP4A.value(), self.RxP4B.value(), self.RxP4C.value()]
        self.VD['RxP5'] = [self.RxP5A.value(), self.RxP5B.value(), self.RxP5C.value()]
        #Rx Fermi-Dirac Distributions
        self.VD['RxB1'] = [self.RxB1A.value(), self.RxB1B.value(), self.RxPoly2Check.isChecked()]
        self.VD['RxB2'] = [self.RxB2A.value(), self.RxB2B.value(), self.RxPoly3Check.isChecked()]
        self.VD['RxB3'] = [self.RxB3A.value(), self.RxB3B.value(), self.RxPoly4Check.isChecked()]
        self.VD['RxB4'] = [self.RxB4A.value(), self.RxB4B.value(), self.RxPoly5Check.isChecked()]
        return self.RxScaleNxCheck.isChecked()

    def GrabRyValues(self):
        #Ry Polynomials
        self.VD['RyP1'] = [self.RyP1A.value(), self.RyP1B.value(), self.RyP1C.value()]
        self.VD['RyP2'] = [self.RyP2A.value(), self.RyP2B.value(), self.RyP2C.value()]
        self.VD['RyP3'] = [self.RyP3A.value(), self.RyP3B.value(), self.RyP3C.value()]
        self.VD['RyP4'] = [self.RyP4A.value(), self.RyP4B.value(), self.RyP4C.value()]
        self.VD['RyP5'] = [self.RyP5A.value(), self.RyP5B.value(), self.RyP5C.value()]
        #Ry Fermi-Dirac Distributions
        self.VD['RyB1'] = [self.RyB1A.value(), self.RyB1B.value(), self.RyPoly2Check.isChecked()]
        self.VD['RyB2'] = [self.RyB2A.value(), self.RyB2B.value(), self.RyPoly3Check.isChecked()]
        self.VD['RyB3'] = [self.RyB3A.value(), self.RyB3B.value(), self.RyPoly4Check.isChecked()]
        self.VD['RyB4'] = [self.RyB4A.value(), self.RyB4B.value(), self.RyPoly5Check.isChecked()]
        return self.RyScaleNyCheck.isChecked()

    def GrabRzValues(self):
        #Rz Polynomials
        self.VD['RzP1'] = [self.RzP1A.value(), self.RzP1B.value(), self.RzP1C.value()]
        self.VD['RzP2'] = [self.RzP2A.value(), self.RzP2B.value(), self.RzP2C.value()]
        self.VD['RzP3'] = [self.RzP3A.value(), self.RzP3B.value(), self.RzP3C.value()]
        self.VD['RzP4'] = [self.RzP4A.value(), self.RzP4B.value(), self.RzP4C.value()]
        self.VD['RzP5'] = [self.RzP5A.value(), self.RzP5B.value(), self.RzP5C.value()]
        #Rz Fermi-Dirac Distributions
        self.VD['RzB1'] = [self.RzB1A.value(), self.RzB1B.value(), self.RzPoly2Check.isChecked()]
        self.VD['RzB2'] = [self.RzB2A.value(), self.RzB2B.value(), self.RzPoly3Check.isChecked()]
        self.VD['RzB3'] = [self.RzB3A.value(), self.RzB3B.value(), self.RzPoly4Check.isChecked()]
        self.VD['RzB4'] = [self.RzB4A.value(), self.RzB4B.value(), self.RzPoly5Check.isChecked()]
        return self.RzScaleNzCheck.isChecked()

    def SetMValues(self,dict):
        self.NxBox.setValue(dict['Nlist'][0]); self.NyBox.setValue(dict['Nlist'][1]); self.NzBox.setValue(dict['Nlist'][2])
        self.IvBox.setValue(dict['Vlist'][0]); self.OvBox.setValue(dict['Vlist'][1])
        self.IxBox.setValue(dict['Ilist'][0][0]); self.IyBox.setValue(dict['Ilist'][0][1]); self.IzBox.setValue(dict['Ilist'][0][2])
        self.OxBox.setValue(dict['Olist'][0][0]); self.OyBox.setValue(dict['Olist'][0][1]); self.OzBox.setValue(dict['Olist'][0][2])
        self.IPxBox.setValue(dict['IPlist'][0][0]); self.IPyBox.setValue(dict['IPlist'][0][1]); self.IPzBox.setValue(dict['IPlist'][0][2])
        self.OPxBox.setValue(dict['OPlist'][0][0]); self.OPyBox.setValue(dict['OPlist'][0][1]); self.OPzBox.setValue(dict['OPlist'][0][2])
        self.TemperatureList = np.linspace(*dict['TRange'])
        self.VD = dict

    def SetRxValues(self):
        #Rx Polynomials
        self.RxP1A.setValue(self.VD['RxP1'][0]); self.RxP1B.setValue(self.VD['RxP1'][1]); self.RxP1C.setValue(self.VD['RxP1'][2])
        self.RxP2A.setValue(self.VD['RxP2'][0]); self.RxP2B.setValue(self.VD['RxP2'][1]); self.RxP2C.setValue(self.VD['RxP2'][2])
        self.RxP3A.setValue(self.VD['RxP3'][0]); self.RxP3B.setValue(self.VD['RxP3'][1]); self.RxP3C.setValue(self.VD['RxP3'][2])
        self.RxP4A.setValue(self.VD['RxP4'][0]); self.RxP4B.setValue(self.VD['RxP4'][1]); self.RxP4C.setValue(self.VD['RxP4'][2])
        self.RxP5A.setValue(self.VD['RxP5'][0]); self.RxP5B.setValue(self.VD['RxP5'][1]); self.RxP5C.setValue(self.VD['RxP5'][2])
        #Rx Fermi-Dirac Distributions
        self.RxB1A.setValue(self.VD['RxB1'][0]); self.RxB1B.setValue(self.VD['RxB1'][1]); self.RxPoly2Check.setChecked(self.VD['RxB1'][2])
        self.RxB2A.setValue(self.VD['RxB2'][0]); self.RxB2B.setValue(self.VD['RxB2'][1]); self.RxPoly3Check.setChecked(self.VD['RxB2'][2])
        self.RxB3A.setValue(self.VD['RxB3'][0]); self.RxB3B.setValue(self.VD['RxB3'][1]); self.RxPoly4Check.setChecked(self.VD['RxB3'][2])
        self.RxB4A.setValue(self.VD['RxB4'][0]); self.RxB4B.setValue(self.VD['RxB4'][1]); self.RxPoly5Check.setChecked(self.VD['RxB4'][2])

    def SetRyValues(self):
        #Ry Polynomials
        self.RyP1A.setValue(self.VD['RyP1'][0]); self.RyP1B.setValue(self.VD['RyP1'][1]); self.RyP1C.setValue(self.VD['RyP1'][2])
        self.RyP2A.setValue(self.VD['RyP2'][0]); self.RyP2B.setValue(self.VD['RyP2'][1]); self.RyP2C.setValue(self.VD['RyP2'][2])
        self.RyP3A.setValue(self.VD['RyP3'][0]); self.RyP3B.setValue(self.VD['RyP3'][1]); self.RyP3C.setValue(self.VD['RyP3'][2])
        self.RyP4A.setValue(self.VD['RyP4'][0]); self.RyP4B.setValue(self.VD['RyP4'][1]); self.RyP4C.setValue(self.VD['RyP4'][2])
        self.RyP5A.setValue(self.VD['RyP5'][0]); self.RyP5B.setValue(self.VD['RyP5'][1]); self.RyP5C.setValue(self.VD['RyP5'][2])
        #Ry Fermi-Dirac Distributions
        self.RyB1A.setValue(self.VD['RyB1'][0]); self.RyB1B.setValue(self.VD['RyB1'][1]); self.RyPoly2Check.setChecked(self.VD['RyB1'][2])
        self.RyB2A.setValue(self.VD['RyB2'][0]); self.RyB2B.setValue(self.VD['RyB2'][1]); self.RyPoly3Check.setChecked(self.VD['RyB2'][2])
        self.RyB3A.setValue(self.VD['RyB3'][0]); self.RyB3B.setValue(self.VD['RyB3'][1]); self.RyPoly4Check.setChecked(self.VD['RyB3'][2])
        self.RyB4A.setValue(self.VD['RyB4'][0]); self.RyB4B.setValue(self.VD['RyB4'][1]); self.RyPoly5Check.setChecked(self.VD['RyB4'][2])

    def SetRzValues(self):
        #Rz Polynomials
        self.RzP1A.setValue(self.VD['RzP1'][0]); self.RzP1B.setValue(self.VD['RzP1'][1]); self.RzP1C.setValue(self.VD['RzP1'][2])
        self.RzP2A.setValue(self.VD['RzP2'][0]); self.RzP2B.setValue(self.VD['RzP2'][1]); self.RzP2C.setValue(self.VD['RzP2'][2])
        self.RzP3A.setValue(self.VD['RzP3'][0]); self.RzP3B.setValue(self.VD['RzP3'][1]); self.RzP3C.setValue(self.VD['RzP3'][2])
        self.RzP4A.setValue(self.VD['RzP4'][0]); self.RzP4B.setValue(self.VD['RzP4'][1]); self.RzP4C.setValue(self.VD['RzP4'][2])
        self.RzP5A.setValue(self.VD['RzP5'][0]); self.RzP5B.setValue(self.VD['RzP5'][1]); self.RzP5C.setValue(self.VD['RzP5'][2])
        #Rz Fermi-Dirac Distributions
        self.RzB1A.setValue(self.VD['RzB1'][0]); self.RzB1B.setValue(self.VD['RzB1'][1]); self.RzPoly2Check.setChecked(self.VD['RzB1'][2])
        self.RzB2A.setValue(self.VD['RzB2'][0]); self.RzB2B.setValue(self.VD['RzB2'][1]); self.RzPoly3Check.setChecked(self.VD['RzB2'][2])
        self.RzB3A.setValue(self.VD['RzB3'][0]); self.RzB3B.setValue(self.VD['RzB3'][1]); self.RzPoly4Check.setChecked(self.VD['RzB3'][2])
        self.RzB4A.setValue(self.VD['RzB4'][0]); self.RzB4B.setValue(self.VD['RzB4'][1]); self.RzPoly5Check.setChecked(self.VD['RzB4'][2])

    def CalcRxList(self):
        if self.GrabRxValues():
            Prefactor = self.RxScale.value()/max(self.VD['Nlist'][0]-1,1)
        else:
            Prefactor = self.RxScale.value()
        self.Rx = Prefactor*userfunction(self.TemperatureList,self.VD['RxP1'],self.VD['RxP2'],self.VD['RxP3'],self.VD['RxP4'],self.VD['RxP5'],self.VD['RxB1'],self.VD['RxB2'],self.VD['RxB3'],self.VD['RxB4'])
        
    def CalcRyList(self):
        if self.GrabRyValues():
            Prefactor = self.RyScale.value()/max(self.VD['Nlist'][1]-1,1)
        else:
            Prefactor = self.RyScale.value()
        self.Ry = Prefactor*userfunction(self.TemperatureList,self.VD['RyP1'],self.VD['RyP2'],self.VD['RyP3'],self.VD['RyP4'],self.VD['RyP5'],self.VD['RyB1'],self.VD['RyB2'],self.VD['RyB3'],self.VD['RyB4'])

    def CalcRzList(self):
        if self.GrabRzValues():
            Prefactor = self.RzScale.value()/max(self.VD['Nlist'][2]-1,1)
        else:
            Prefactor = self.RzScale.value()
        self.Rz = Prefactor*userfunction(self.TemperatureList,self.VD['RzP1'],self.VD['RzP2'],self.VD['RzP3'],self.VD['RzP4'],self.VD['RzP5'],self.VD['RzB1'],self.VD['RzB2'],self.VD['RzB3'],self.VD['RzB4'])
        
    def GrabPValues(self):
        self.PxValue = sum(i[2] for i in [self.VD['RxB1'],self.VD['RxB2'],self.VD['RxB3'],self.VD['RxB4']])+1
        self.PyValue = sum(i[2] for i in [self.VD['RyB1'],self.VD['RyB2'],self.VD['RyB3'],self.VD['RyB4']])+1
        self.PzValue = sum(i[2] for i in [self.VD['RzB1'],self.VD['RzB2'],self.VD['RzB3'],self.VD['RzB4']])+1

    def ChangePxState(self,check):
        if check>1:
            self.PxValue += 1
        elif check == 0:
            self.PxValue -= 1

        self.RxPoly5Check.setEnabled(False)
        self.RxPoly4Check.setEnabled(False)
        self.RxPoly3Check.setEnabled(False)
        self.RxPoly2Check.setEnabled(False)
        
        self.RxWidget4.setEnabled(True)
        self.RxWidget3.setEnabled(True)
        self.RxWidget2.setEnabled(True)
        self.RxWidget1.setEnabled(True)

        if self.PxValue == 5:
            self.RxPoly5Check.setEnabled(True)
        elif self.PxValue == 4:
            self.RxWidget4.setEnabled(False)
            self.RxPoly5Check.setEnabled(True)
            self.RxPoly4Check.setEnabled(True)
        elif self.PxValue == 3:
            self.RxWidget4.setEnabled(False)
            self.RxWidget3.setEnabled(False)
            self.RxPoly4Check.setEnabled(True)
            self.RxPoly3Check.setEnabled(True)
        if self.PxValue == 2:
            self.RxWidget4.setEnabled(False)
            self.RxWidget3.setEnabled(False)
            self.RxWidget2.setEnabled(False)
            self.RxPoly3Check.setEnabled(True)
            self.RxPoly2Check.setEnabled(True)
        if self.PxValue == 1:
            self.RxWidget4.setEnabled(False)
            self.RxWidget3.setEnabled(False)
            self.RxWidget2.setEnabled(False)
            self.RxWidget1.setEnabled(False)
            self.RxPoly2Check.setEnabled(True)

    def ChangePyState(self,check):
        if check>1:
            self.PyValue += 1
        elif check ==0:
            self.PyValue -= 1

        self.RyPoly5Check.setEnabled(False)
        self.RyPoly4Check.setEnabled(False)
        self.RyPoly3Check.setEnabled(False)
        self.RyPoly2Check.setEnabled(False)
        
        self.RyWidget4.setEnabled(True)
        self.RyWidget3.setEnabled(True)
        self.RyWidget2.setEnabled(True)
        self.RyWidget1.setEnabled(True)

        if self.PyValue == 5:
            self.RyPoly5Check.setEnabled(True)
        elif self.PyValue == 4:
            self.RyWidget4.setEnabled(False)
            self.RyPoly5Check.setEnabled(True)
            self.RyPoly4Check.setEnabled(True)
        elif self.PyValue == 3:
            self.RyWidget4.setEnabled(False)
            self.RyWidget3.setEnabled(False)
            self.RyPoly4Check.setEnabled(True)
            self.RyPoly3Check.setEnabled(True)
        if self.PyValue == 2:
            self.RyWidget4.setEnabled(False)
            self.RyWidget3.setEnabled(False)
            self.RyWidget2.setEnabled(False)
            self.RyPoly3Check.setEnabled(True)
            self.RyPoly2Check.setEnabled(True)
        if self.PyValue == 1:
            self.RyWidget4.setEnabled(False)
            self.RyWidget3.setEnabled(False)
            self.RyWidget2.setEnabled(False)
            self.RyWidget1.setEnabled(False)
            self.RyPoly2Check.setEnabled(True)

    def ChangePzState(self,check):
        if check>1:
            self.PzValue += 1
        elif check==0:
            self.PzValue -= 1
        
        self.RzPoly5Check.setEnabled(False)
        self.RzPoly4Check.setEnabled(False)
        self.RzPoly3Check.setEnabled(False)
        self.RzPoly2Check.setEnabled(False)
        
        self.RzWidget4.setEnabled(True)
        self.RzWidget3.setEnabled(True)
        self.RzWidget2.setEnabled(True)
        self.RzWidget1.setEnabled(True)

        if self.PzValue == 5:
            self.RzPoly5Check.setEnabled(True)
        elif self.PzValue == 4:
            self.RzWidget4.setEnabled(False)
            self.RzPoly5Check.setEnabled(True)
            self.RzPoly4Check.setEnabled(True)
        elif self.PzValue == 3:
            self.RzWidget4.setEnabled(False)
            self.RzWidget3.setEnabled(False)
            self.RzPoly4Check.setEnabled(True)
            self.RzPoly3Check.setEnabled(True)
        if self.PzValue == 2:
            self.RzWidget4.setEnabled(False)
            self.RzWidget3.setEnabled(False)
            self.RzWidget2.setEnabled(False)
            self.RzPoly3Check.setEnabled(True)
            self.RzPoly2Check.setEnabled(True)
        if self.PzValue == 1:
            self.RzWidget4.setEnabled(False)
            self.RzWidget3.setEnabled(False)
            self.RzWidget2.setEnabled(False)
            self.RzWidget1.setEnabled(False)
            self.RzPoly2Check.setEnabled(True)

    def PlotResitivity(self):
        self.ResistivityCanvas.axes.clear()
        if self.VD['Nlist'][0]>1:
            self.ResistivityCanvas.axes.plot(self.TemperatureList,self.Rx,label='Rx')
        if self.VD['Nlist'][1]>1:
            self.ResistivityCanvas.axes.plot(self.TemperatureList,self.Ry,label='Ry')
        if self.VD['Nlist'][2]>1:
            self.ResistivityCanvas.axes.plot(self.TemperatureList,self.Rz,label='Rz')
        self.ResistivityCanvas.axes.legend()
        self.ResistivityCanvas.draw()

    def RedrawMesh(self,check=False):
        self.MatrixCanvas.axes.clear()
        plotMatrix(self.MatrixCanvas.axes,self.VD['Nlist'])
        plotLeads(self.MatrixCanvas.axes,self.VD['Ilist'],self.VD['Olist'],'Red','v')
        if check:
            plotLeads(self.MatrixCanvas.axes,self.VD['IPlist'],self.VD['OPlist'],'Black','X')
        self.MatrixCanvas.draw()

    def SetBoxMaximums(self):
        self.IxBox.setMaximum(self.VD['Nlist'][0]-self.VD['INlist'][0]+1); self.OxBox.setMaximum(self.VD['Nlist'][0]-self.VD['ONlist'][0]+1)
        self.IyBox.setMaximum(self.VD['Nlist'][1]-self.VD['INlist'][1]+1); self.OyBox.setMaximum(self.VD['Nlist'][1]-self.VD['ONlist'][1]+1)
        self.IzBox.setMaximum(self.VD['Nlist'][2]-self.VD['INlist'][2]+1); self.OzBox.setMaximum(self.VD['Nlist'][2]-self.VD['ONlist'][2]+1)
        self.IPxBox.setMaximum(self.VD['Nlist'][0]); self.OPxBox.setMaximum(self.VD['Nlist'][0])
        self.IPyBox.setMaximum(self.VD['Nlist'][1]); self.OPyBox.setMaximum(self.VD['Nlist'][1])
        self.IPzBox.setMaximum(self.VD['Nlist'][2]); self.OPzBox.setMaximum(self.VD['Nlist'][2])

    def Initialize(self):
        # Defining size of matrix, current input and output locations and values:
        self.GrabMValues()
        # Simulating the voltage matrices across the temperature range
        self.df = simulate(self.VD['Nlist'],self.VD['Ilist'],self.VD['Olist'],self.VD['Vlist'],self.TemperatureList,[self.Rx,self.Ry,self.Rz])
        # Plotting the TMax, Z=1 contour on the contour tab:
        self.ContourCanvas.axes.clear()
        plotContour(self.ContourCanvas.axes,self.df,self.VD['Nlist'],1,0,self.VD['Vlist'])
        self.ContourCanvas.draw()
        # Setting the T and slider to the correct locations and maximum:
        self.TemperatureSlider.setValue(0)
        self.TemperatureSlider.setMaximum(len(self.TemperatureList)-1)
        self.ZSlider.setValue(1)
        self.ZSlider.setMaximum(self.VD['Nlist'][2])
        # Enabling the measure resistivity button:
        self.MeasurementWidget.setEnabled(True)
        self.MeasureButton.setEnabled(True)
        self.ContourTab.setEnabled(True)
        self.ResistanceTab.setEnabled(True)
        self.FittingTab.setEnabled(True)
        # Resetting the resistance canvas:
        self.ResistanceCanvas.axes.clear()
        self.ResistanceCanvas.draw()

    def Measure(self):
        # Grab Values and Draw Mesh:
        self.GrabMValues()
        self.RedrawMesh(True)
        # Plot the resistance across these points through the temperature range.
        ResistancePlot(self.ResistanceCanvas.axes,self.df,self.VD['IPlist'],self.VD['OPlist'],self.CheckX.isChecked(),self.CheckY.isChecked(),self.CheckZ.isChecked())
        self.ResistanceCanvas.draw()


    def OpenAO(self):
        self.GrabMValues()
        dlg = AdvancedOptions(self.VD['Nlist'],self.VD['INlist'],self.VD['ONlist'],self.VD['DataSR'],self.VD['DataSep'],self.VD['DataHeader'],self.VD['TRange'])
        dlg.setWindowTitle("Advanced Options")
        if dlg.exec():
            self.MeasurementWidget.setEnabled(False)
            self.TemperatureList = np.linspace(dlg.TmBox.value(),dlg.TMBox.value(),dlg.TeBox.value())
            self.VD['TRange'] = [dlg.TmBox.value(),dlg.TMBox.value(),dlg.TeBox.value()]
            self.VD['INlist'] = [dlg.INxBox.value(),dlg.INyBox.value(),dlg.INzBox.value()]
            self.VD['ONlist'] = [dlg.ONxBox.value(),dlg.ONyBox.value(),dlg.ONzBox.value()]
            self.GrabMValues()
            self.SetBoxMaximums()
            self.RedrawMesh()
            self.VD['DataSR'] = dlg.ResistivitySR.value()
            self.VD['DataSep'] = dlg.ResistivitySeperator.toPlainText()
            self.VD['DataHeader'] = dlg.ResistivityHeader.toPlainText().split(", ")
            if not(dlg.fileName == ""):
                self.VD['DatafileName'] = dlg.fileName
                self.loadMData()

    def loadMData(self):
        self.DataPD = pd.read_csv(self.VD['DatafileName'], skiprows=self.VD['DataSR'], sep=self.VD['DataSep'], names=self.VD['DataHeader'],engine='python')
        self.FittingCanvas.axes.clear()
        self.FittingCanvas.axes.plot(self.DataPD['T'],self.DataPD['R'])
        self.FittingCanvas.draw()
        self.FittingTab.setEnabled(True)

    def changeTValue(self, value):
        self.TValue = value
        plotContour(self.ContourCanvas.axes,self.df,self.VD['Nlist'],self.ZValue,value,self.VD['Vlist'])
        self.ContourCanvas.draw()
        self.TemperatureLabel.setText("Temperature: "+str(self.TemperatureList[value]))

    def changeZValue(self, value):
        self.ZValue = value
        plotContour(self.ContourCanvas.axes,self.df,self.VD['Nlist'],value,self.TValue,self.VD['Vlist'])
        self.ContourCanvas.draw()

    def changeNxValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.GrabMValues()
        self.SetBoxMaximums()
        self.RedrawMesh()

    def changeNyValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.GrabMValues()
        self.SetBoxMaximums()
        self.RedrawMesh()

    def changeNzValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-setting the Z Value on the slider:
        if self.ZValue > value:
            self.ZValue = value
        # Re-draw the matrix canvas
        self.GrabMValues()
        self.SetBoxMaximums()
        self.RedrawMesh()

    def changeIOValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.GrabMValues()
        self.SetBoxMaximums()
        self.RedrawMesh()

    def changeVValue(self, value):
        # Disabling the measurement widget
        self.IvBox.setMinimum(self.OvBox.value()+0.01)
        self.OvBox.setMaximum(self.IvBox.value()-0.01)
        self.MeasurementWidget.setEnabled(False)

    def FittingWrapperP(self):
        print('fitting')
        params, count = self.FittingFunction(0)

    def FittingWrapperX(self):
        print('fitting')
        params, count, Rfit = self.FittingFunction(1)

        self.FD['RxP1'] = params[0:3]
        self.FD['xScale'] = params[-1]
        for i in range(4):
            if i < count-1:
                inputP = 'RxP'+str(i+2)
                inputB = 'RxB'+str(count-1-i)
                self.FD[inputP] = params[3*(i+1):3*(i+2)]
                self.FD[inputB] = params[-(1+2*(i+1)):-(1+2*i)]+[True]
            else: 
                inputP = 'RxP'+str(i+2)
                inputB = 'RxB'+str(1+i)
                self.FD[inputP] = [1,1,0]
                self.FD[inputB] = [1,1,False]
        print(self.FD)

        newscale = max(self.DataPD['R'])/max(Rfit)
        self.FittingCanvas.axes.plot(self.TemperatureList,newscale*Rfit)
        self.FittingCanvas.draw()

    def FittingWrapperY(self):
        print('fitting')
        params, count, Rfit = self.FittingFunction(2)
        print(params)

        self.FD['RyP1'] = params[0:3]
        self.FD['yScale'] = params[-1]
        for i in range(4):
            if i < count-1:
                inputP = 'RyP'+str(i+2)
                inputB = 'RyB'+str(count-1-i)
                self.FD[inputP] = params[3*(i+1):3*(i+2)]
                self.FD[inputB] = params[-(1+2*(i+1)):-(1+2*i)]+[True]
            else: 
                inputP = 'RyP'+str(i+2)
                inputB = 'RyB'+str(1+i)
                self.FD[inputP] = [1,1,0]
                self.FD[inputB] = [1,1,False]
        print(self.FD)

        # if self.GrabRyValues():
        #     Prefactor = self.FD['yScale']/max(self.VD['Nlist'][1]-1,1)
        # else:
        #     Prefactor = self.FD['yScale']
        # self.FT = Prefactor*userfunction(self.TemperatureList,self.FD['RyP1'],self.FD['RyP2'],self.FD['RyP3'],self.FD['RyP4'],self.FD['RyP5'],self.FD['RyB1'],self.FD['RyB2'],self.FD['RyB3'],self.FD['RyB4'])
        newscale = max(self.DataPD['R'])/max(Rfit)
        self.FittingCanvas.axes.plot(self.TemperatureList,newscale*Rfit)
        self.FittingCanvas.draw()

    def FittingWrapperZ(self):
        print('fitting')
        params, count, Rfit = self.FittingFunction(3)

        self.FD['RzP1'] = params[0:3]
        for i in range(4):
            if i < count-1:
                inputP = 'RzP'+str(i+2)
                inputB = 'RzB'+str(count-1-i)
                self.FD[inputP] = params[3*(i+1):3*(i+2)]
                self.FD[inputB] = params[-(1+2*(i+1)):-(1+2*i)]+[True]
            else: 
                inputP = 'RzP'+str(i+2)
                inputB = 'RzB'+str(1+i)
                self.FD[inputP] = [1,1,0]
                self.FD[inputB] = [1,1,False]
        print(self.FD)

        newscale = max(self.DataPD['R'])/max(Rfit)
        self.FittingCanvas.axes.plot(self.TemperatureList,newscale*Rfit)
        self.FittingCanvas.draw()

    def FittingFunction(self,mode):
        if mode == 3:
            if self.GrabRzValues():
                Prefactor = self.RzScale.value()/max(self.VD['Nlist'][1]-1,1)
            else:
                Prefactor = self.RzScale.value()
            RP = [self.VD['RzP1'],self.VD['RzP2'],self.VD['RzP3'],self.VD['RzP4'],self.VD['RzP5']]
            RB = [self.VD['RzB1'],self.VD['RzB2'],self.VD['RzB3'],self.VD['RzB4']]
        elif mode == 2:
            if self.GrabRyValues():
                Prefactor = self.RyScale.value()/max(self.VD['Nlist'][1]-1,1)
            else:
                Prefactor = self.RyScale.value()
            RP = [self.VD['RyP1'],self.VD['RyP2'],self.VD['RyP3'],self.VD['RyP4'],self.VD['RyP5']]
            RB = [self.VD['RyB1'],self.VD['RyB2'],self.VD['RyB3'],self.VD['RyB4']]
        else:
            if self.GrabRyValues():
                Prefactor = self.RyScale.value()/max(self.VD['Nlist'][1]-1,1)
            else:
                Prefactor = self.RyScale.value()
            RP = [self.VD['RxP1'],self.VD['RxP2'],self.VD['RxP3'],self.VD['RxP4'],self.VD['RxP5']]
            RB = [self.VD['RxB1'],self.VD['RxB2'],self.VD['RxB3'],self.VD['RxB4']]
        params, count, Rfit = fitR(self.DataPD['R'],self.DataPD['T'],self.TemperatureList,self.VD['Nlist'],self.VD['Ilist'],self.VD['Olist'],self.VD['Vlist'],self.Rx,self.Ry,self.Rz,self.VD['IPlist'],self.VD['OPlist'],RP,RB,Prefactor,mode)
        return params, count, Rfit

    def SaveDict(self):
        self.GrabRxValues()
        self.GrabRyValues()
        self.GrabRzValues()
        self.GrabMValues()
        with open('saved_dictionary.pkl', 'wb') as f:
            pickle.dump(self.VD,f)
        print(self.VD)

    def LoadDict(self):
        with open('saved_dictionary.pkl', 'rb') as f:
            Dict = pickle.load(f)
        self.SetMValues(Dict)
        self.SetBoxMaximums()
        self.RedrawMesh()
        self.SetRxValues()
        self.SetRyValues()
        self.SetRzValues()
        self.CalcRxList()
        self.CalcRyList()
        self.CalcRzList()
        self.GrabPValues()
        self.ChangePxState(1)
        self.ChangePxState(1)
        self.ChangePxState(1)
        self.PlotResitivity()
        self.MeasurementWidget.setEnabled(False)
        if not(self.VD['DatafileName']==""):
            self.loadMData()
        #Redundancy
        self.VD = Dict

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())