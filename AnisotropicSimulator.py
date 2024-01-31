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

# FINISH IMPLEMENTING THIS
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
        self.GrabValues()

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

    def GrabValues(self):
        self.N = [self.NxBox.value(),self.NyBox.value(),self.NzBox.value()]
        self.Vlist = [ self.IvBox.value(), self.OvBox.value() ]
        self.Ilist = inputlist([self.IxBox.value(), self.IyBox.value(), self.IzBox.value()],self.INlist)
        self.Olist = inputlist([self.OxBox.value(), self.OyBox.value(), self.OzBox.value()],self.ONlist)
        self.IPlist = [[self.IPxBox.value(),self.IPyBox.value(),self.IPzBox.value()]]
        self.OPlist = [[self.OPxBox.value(),self.OPyBox.value(),self.OPzBox.value()]]

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
        self.GrabValues()
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
        self.GrabValues()
        self.RedrawMesh(True)
        # Plot the resistance across these points through the temperature range.
        ResistancePlot(self.ResistanceCanvas.axes,self.df,self.IPlist,self.OPlist,self.CheckX.isChecked(),self.CheckY.isChecked(),self.CheckZ.isChecked())
        self.ResistanceCanvas.draw()


    def OpenAO(self):
        self.GrabValues()
        dlg = AdvancedOptions(self.N,self.INlist,self.ONlist)
        dlg.setWindowTitle("HELLO!")
        if dlg.exec():
            self.MeasurementWidget.setEnabled(False)
            self.TemperatureList = np.linspace(dlg.TmBox.value(),dlg.TMBox.value(),dlg.TeBox.value())
            self.INlist = [dlg.INxBox.value(),dlg.INyBox.value(),dlg.INzBox.value()]
            self.ONlist = [dlg.ONxBox.value(),dlg.ONyBox.value(),dlg.ONzBox.value()]
            self.GrabValues()
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
        self.GrabValues()
        self.SetBoxMaximums()
        self.RedrawMesh()

    def changeNyValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.GrabValues()
        self.SetBoxMaximums()
        self.RedrawMesh()

    def changeNzValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-setting the Z Value on the slider:
        if self.ZValue > value:
            self.ZValue = value
        # Re-draw the matrix canvas
        self.GrabValues()
        self.SetBoxMaximums()
        self.RedrawMesh()

    def changeIOValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.GrabValues()
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