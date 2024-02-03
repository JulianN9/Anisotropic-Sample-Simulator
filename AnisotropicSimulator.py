import sys
import numpy as np
import itertools as it
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QSlider, QLabel, QSizePolicy, QVBoxLayout, QDialog
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
    def __init__(self,Nlist,INlist,ONlist):
        super(AdvancedOptions, self).__init__()
        self.setupUi(self)
        Nx, Ny, Nz = Nlist
        self.INxBox.setMaximum(Nx); self.ONxBox.setMaximum(Nx)
        self.INyBox.setMaximum(Ny); self.ONyBox.setMaximum(Ny)
        self.INzBox.setMaximum(Nz); self.ONzBox.setMaximum(Nz)
        self.INxBox.setValue(INlist[0]); self.ONxBox.setValue(ONlist[0])
        self.INyBox.setValue(INlist[1]); self.ONyBox.setValue(ONlist[1])
        self.INzBox.setValue(INlist[2]); self.ONzBox.setValue(ONlist[2])
        
# Main Window Class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Basic Functionality:
        # Setting up buttons
        self.IntializeButton.clicked.connect(self.Initialize)
        self.MeasureButton.clicked.connect(self.Measure)
        self.toolButton.clicked.connect(self.OpenAO)
        self.RxButtonBox.accepted.connect(self.CalcRxList)
        self.RyButtonBox.accepted.connect(self.CalcRyList)
        self.RzButtonBox.accepted.connect(self.CalcRzList)
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
        # Some values that can be changed in advanced options:
        self.TemperatureList = np.linspace(2,300,100)
        self.INlist = [1,1,1]
        self.ONlist = [1,1,1]
        self.GrabMValues()
        self.CalcRxList()
        self.CalcRyList()
        self.CalcRzList()

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

    def GrabMValues(self):
        self.N = [self.NxBox.value(),self.NyBox.value(),self.NzBox.value()]
        self.Vlist = [ self.IvBox.value(), self.OvBox.value() ]
        self.Ilist = inputlist([self.IxBox.value(), self.IyBox.value(), self.IzBox.value()],self.INlist)
        self.Olist = inputlist([self.OxBox.value(), self.OyBox.value(), self.OzBox.value()],self.ONlist)
        self.IPlist = [[self.IPxBox.value(),self.IPyBox.value(),self.IPzBox.value()]]
        self.OPlist = [[self.OPxBox.value(),self.OPyBox.value(),self.OPzBox.value()]]

    def GrabRxValues(self):
        #Rx Polynomials
        self.RxP1 = [self.RxP1A.value(), self.RxP1B.value(), self.RxP1C.value()]
        self.RxP2 = [self.RxP2A.value(), self.RxP2B.value(), self.RxP2C.value()]
        self.RxP3 = [self.RxP3A.value(), self.RxP3B.value(), self.RxP3C.value()]
        self.RxP4 = [self.RxP4A.value(), self.RxP4B.value(), self.RxP4C.value()]
        self.RxP5 = [self.RxP5A.value(), self.RxP5B.value(), self.RxP5C.value()]
        #Rx Fermi-Dirac Distributions
        self.RxB1 = [self.RxB1A.value(), self.RxB1B.value(), self.RxPoly2Check.isChecked()]
        self.RxB2 = [self.RxB2A.value(), self.RxB2B.value(), self.RxPoly3Check.isChecked()]
        self.RxB3 = [self.RxB3A.value(), self.RxB3B.value(), self.RxPoly4Check.isChecked()]
        self.RxB4 = [self.RxB4A.value(), self.RxB4B.value(), self.RxPoly5Check.isChecked()]

    def GrabRyValues(self):
        #Ry Polynomials
        self.RyP1 = [self.RyP1A.value(), self.RyP1B.value(), self.RyP1C.value()]
        self.RyP2 = [self.RyP2A.value(), self.RyP2B.value(), self.RyP2C.value()]
        self.RyP3 = [self.RyP3A.value(), self.RyP3B.value(), self.RyP3C.value()]
        self.RyP4 = [self.RyP4A.value(), self.RyP4B.value(), self.RyP4C.value()]
        self.RyP5 = [self.RyP5A.value(), self.RyP5B.value(), self.RyP5C.value()]
        #Ry Fermi-Dirac Distributions
        self.RyB1 = [self.RyB1A.value(), self.RyB1B.value(), self.RyPoly2Check.isChecked()]
        self.RyB2 = [self.RyB2A.value(), self.RyB2B.value(), self.RyPoly3Check.isChecked()]
        self.RyB3 = [self.RyB3A.value(), self.RyB3B.value(), self.RyPoly4Check.isChecked()]
        self.RyB4 = [self.RyB4A.value(), self.RyB4B.value(), self.RyPoly5Check.isChecked()]

    def GrabRzValues(self):
        #Rz Polynomials
        self.RzP1 = [self.RzP1A.value(), self.RzP1B.value(), self.RzP1C.value()]
        self.RzP2 = [self.RzP2A.value(), self.RzP2B.value(), self.RzP2C.value()]
        self.RzP3 = [self.RzP3A.value(), self.RzP3B.value(), self.RzP3C.value()]
        self.RzP4 = [self.RzP4A.value(), self.RzP4B.value(), self.RzP4C.value()]
        self.RzP5 = [self.RzP5A.value(), self.RzP5B.value(), self.RzP5C.value()]
        #Rz Fermi-Dirac Distributions
        self.RzB1 = [self.RzB1A.value(), self.RzB1B.value(), self.RzPoly2Check.isChecked()]
        self.RzB2 = [self.RzB2A.value(), self.RzB2B.value(), self.RzPoly3Check.isChecked()]
        self.RzB3 = [self.RzB3A.value(), self.RzB3B.value(), self.RzPoly4Check.isChecked()]
        self.RzB4 = [self.RzB4A.value(), self.RzB4B.value(), self.RzPoly5Check.isChecked()]

    def SetRxValues(self):
        #Rx Polynomials
        self.RxP1A.setValue(self.RxP1[0]); self.RxP1B.setValue(self.RxP1[1]); self.RxP1C.setValue(self.RxP1[2])
        self.RxP2A.setValue(self.RxP2[0]); self.RxP2B.setValue(self.RxP2[1]); self.RxP2C.setValue(self.RxP2[2])
        self.RxP3A.setValue(self.RxP3[0]); self.RxP3B.setValue(self.RxP3[1]); self.RxP3C.setValue(self.RxP3[2])
        self.RxP4A.setValue(self.RxP4[0]); self.RxP4B.setValue(self.RxP4[1]); self.RxP4C.setValue(self.RxP4[2])
        self.RxP5A.setValue(self.RxP5[0]); self.RxP5B.setValue(self.RxP5[1]); self.RxP5C.setValue(self.RxP5[2])
        #Rx Fermi-Dirac Distributions
        self.RxB1A.setValue(self.RxB1[0]); self.RxB1B.setValue(self.RxB1[1]); self.RzPoly2Check.setChecked(self.RxB1[2])
        self.RxB2A.setValue(self.RxB2[0]); self.RxB2B.setValue(self.RxB2[1]); self.RzPoly2Check.setChecked(self.RxB2[2])
        self.RxB3A.setValue(self.RxB3[0]); self.RxB3B.setValue(self.RxB3[1]); self.RzPoly2Check.setChecked(self.RxB3[2])
        self.RxB4A.setValue(self.RxB4[0]); self.RxB4B.setValue(self.RxB4[1]); self.RzPoly2Check.setChecked(self.RxB4[2])

    def SetRyValues(self):
        #Ry Polynomials
        self.RyP1A.setValue(self.RyP1[0]); self.RyP1B.setValue(self.RyP1[1]); self.RyP1C.setValue(self.RyP1[2])
        self.RyP2A.setValue(self.RyP2[0]); self.RyP2B.setValue(self.RyP2[1]); self.RyP2C.setValue(self.RyP2[2])
        self.RyP3A.setValue(self.RyP3[0]); self.RyP3B.setValue(self.RyP3[1]); self.RyP3C.setValue(self.RyP3[2])
        self.RyP4A.setValue(self.RyP4[0]); self.RyP4B.setValue(self.RyP4[1]); self.RyP4C.setValue(self.RyP4[2])
        self.RyP5A.setValue(self.RyP5[0]); self.RyP5B.setValue(self.RyP5[1]); self.RyP5C.setValue(self.RyP5[2])
        #Ry Fermi-Dirac Distributions
        self.RyB1A.setValue(self.RyB1[0]); self.RyB1B.setValue(self.RyB1[1]); self.RzPoly2Check.setChecked(self.RyB1[2])
        self.RyB2A.setValue(self.RyB2[0]); self.RyB2B.setValue(self.RyB2[1]); self.RzPoly2Check.setChecked(self.RyB2[2])
        self.RyB3A.setValue(self.RyB3[0]); self.RyB3B.setValue(self.RyB3[1]); self.RzPoly2Check.setChecked(self.RyB3[2])
        self.RyB4A.setValue(self.RyB4[0]); self.RyB4B.setValue(self.RyB4[1]); self.RzPoly2Check.setChecked(self.RyB4[2])

    def SetRzValues(self):
        #Rz Polynomials
        self.RzP1A.setValue(self.RzP1[0]); self.RzP1B.setValue(self.RzP1[1]); self.RzP1C.setValue(self.RzP1[2])
        self.RzP2A.setValue(self.RzP2[0]); self.RzP2B.setValue(self.RzP2[1]); self.RzP2C.setValue(self.RzP2[2])
        self.RzP3A.setValue(self.RzP3[0]); self.RzP3B.setValue(self.RzP3[1]); self.RzP3C.setValue(self.RzP3[2])
        self.RzP4A.setValue(self.RzP4[0]); self.RzP4B.setValue(self.RzP4[1]); self.RzP4C.setValue(self.RzP4[2])
        self.RzP5A.setValue(self.RzP5[0]); self.RzP5B.setValue(self.RzP5[1]); self.RzP5C.setValue(self.RzP5[2])
        #Rz Fermi-Dirac Distributions
        self.RzB1A.setValue(self.RzB1[0]); self.RzB1B.setValue(self.RzB1[1]); self.RzPoly2Check.setChecked(self.RzB1[2])
        self.RzB2A.setValue(self.RzB2[0]); self.RzB2B.setValue(self.RzB2[1]); self.RzPoly2Check.setChecked(self.RzB2[2])
        self.RzB3A.setValue(self.RzB3[0]); self.RzB3B.setValue(self.RzB3[1]); self.RzPoly2Check.setChecked(self.RzB3[2])
        self.RzB4A.setValue(self.RzB4[0]); self.RzB4B.setValue(self.RzB4[1]); self.RzPoly2Check.setChecked(self.RzB4[2])

    # Move the sacle
    def CalcRxList(self):
        self.GrabRxValues()
        # Prefactor = self.RxScale.value()/max(self.N[0]-1,1)
        Prefactor = self.RxScale.value()
        self.Rx = Prefactor*userfunction(self.TemperatureList,*self.RxP1,*self.RxP2,*self.RxP3,*self.RxP4,*self.RxP5,*self.RxB1,*self.RxB2,*self.RxB3,*self.RxB4)
        
    def CalcRyList(self):
        self.GrabRyValues()
        # Prefactor = self.RyScale.value()/max(self.N[1]-1,1)
        Prefactor = self.RyScale.value()
        self.Ry = Prefactor*userfunction(self.TemperatureList,*self.RyP1,*self.RyP2,*self.RyP3,*self.RyP4,*self.RyP5,*self.RyB1,*self.RyB2,*self.RyB3,*self.RyB4)

    def CalcRzList(self):
        self.GrabRzValues()
        # Prefactor = self.RzScale.value()/max(self.N[2]-1,1)
        Prefactor = self.RzScale.value()
        self.Rz = Prefactor*userfunction(self.TemperatureList,*self.RzP1,*self.RzP2,*self.RzP3,*self.RzP4,*self.RzP5,*self.RzB1,*self.RzB2,*self.RzB3,*self.RzB4)
        
    def PlotResitivity(self):
        self.ResistivityCanvas.axes.clear()
        self.ResistivityCanvas.axes.plot(self.TemperatureList,self.Rx,label='Rx')
        self.ResistivityCanvas.axes.plot(self.TemperatureList,self.Ry,label='Ry')
        self.ResistivityCanvas.axes.plot(self.TemperatureList,self.Rz,label='Rz')
        self.ResistivityCanvas.axes.legend()
        self.ResistivityCanvas.draw()

    def RedrawMesh(self,check=False):
        self.MatrixCanvas.axes.clear()
        plotMatrix(self.MatrixCanvas.axes,self.N)
        plotLeads(self.MatrixCanvas.axes,self.Ilist,self.Olist,'Red','v')
        if check:
            plotLeads(self.MatrixCanvas.axes,self.IPlist,self.OPlist,'Black','X')
        self.MatrixCanvas.draw()

    def SetBoxMaximums(self):
        self.IxBox.setMaximum(self.N[0]-self.INlist[0]+1); self.OxBox.setMaximum(self.N[0]-self.ONlist[0]+1)
        self.IyBox.setMaximum(self.N[1]-self.INlist[1]+1); self.OyBox.setMaximum(self.N[1]-self.ONlist[1]+1)
        self.IzBox.setMaximum(self.N[2]-self.INlist[2]+1); self.OzBox.setMaximum(self.N[2]-self.ONlist[2]+1)
        self.IPxBox.setMaximum(self.N[0]); self.OPxBox.setMaximum(self.N[0])
        self.IPyBox.setMaximum(self.N[1]); self.OPyBox.setMaximum(self.N[1])
        self.IPzBox.setMaximum(self.N[2]); self.OPzBox.setMaximum(self.N[2])

    def Initialize(self):
        # Defining size of matrix, current input and output locations and values:
        self.GrabMValues()
        # Simulating the voltage matrices across the temperature range
        self.df = simulate(self.N,self.Ilist,self.Olist,self.Vlist,self.TemperatureList)
        # Plotting the TMax, Z=1 contour on the contour tab:
        self.ContourCanvas.axes.clear()
        plotContour(self.ContourCanvas.axes,self.df,self.N,1,0,self.Vlist)
        self.ContourCanvas.draw()
        # Setting the T and slider to the correct locations and maximum:
        self.TemperatureSlider.setValue(0)
        self.TemperatureSlider.setMaximum(len(self.TemperatureList)-1)
        self.ZSlider.setValue(1)
        self.ZSlider.setMaximum(self.N[2])
        # Enabling the measure resistivity button:
        self.MeasurementWidget.setEnabled(True)
        self.MeasureButton.setEnabled(True)
        self.ContourTab.setEnabled(True)
        self.ResistanceTab.setEnabled(True)
        # Resetting the resistance canvas:
        self.ResistanceCanvas.axes.clear()
        self.ResistanceCanvas.draw()

    def Measure(self):
        # Grab Values and Draw Mesh:
        self.GrabMValues()
        self.RedrawMesh(True)
        # Plot the resistance across these points through the temperature range.
        ResistancePlot(self.ResistanceCanvas.axes,self.df,self.IPlist,self.OPlist,self.CheckX.isChecked(),self.CheckY.isChecked(),self.CheckZ.isChecked())
        self.ResistanceCanvas.draw()


    def OpenAO(self):
        self.GrabMValues()
        dlg = AdvancedOptions(self.N,self.INlist,self.ONlist)
        dlg.setWindowTitle("HELLO!")
        if dlg.exec():
            self.MeasurementWidget.setEnabled(False)
            self.TemperatureList = np.linspace(dlg.TmBox.value(),dlg.TMBox.value(),dlg.TeBox.value())
            self.INlist = [dlg.INxBox.value(),dlg.INyBox.value(),dlg.INzBox.value()]
            self.ONlist = [dlg.ONxBox.value(),dlg.ONyBox.value(),dlg.ONzBox.value()]
            self.GrabMValues()
            self.SetBoxMaximums()
            self.RedrawMesh()


    def changeTValue(self, value):
        self.TValue = value
        plotContour(self.ContourCanvas.axes,self.df,self.N,self.ZValue,value,self.Vlist)
        self.ContourCanvas.draw()
        self.TemperatureLabel.setText("Temperature: "+str(self.TemperatureList[value]))

    def changeZValue(self, value):
        self.ZValue = value
        plotContour(self.ContourCanvas.axes,self.df,self.N,value,self.TValue,self.Vlist)
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

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())