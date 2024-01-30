import sys
import numpy as np
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
from ContourPlot import contourfit
from MatrixDiagram3d import plotMatrix, plotLeads
from ResistancePlot import ResistancePlot

# FINISH IMPLEMENTING THIS
def inputlist(list,Xwidth,Ywidth,Zwidth):
    newlist=[]
    for i in range(Xwidth):
        for j in range(Ywidth):
            for k in range(Zwidth):
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
    def __init__(self,Nx,Ny,Nz,Ilist,Olist):
        super(AdvancedOptions, self).__init__()
        self.setupUi(self)
        self.INxBox.setMaximum(Nx-Ilist[0]+1)
        self.INyBox.setMaximum(Ny-Ilist[1]+1)
        self.INzBox.setMaximum(Nz-Ilist[2]+1)
        self.ONxBox.setMaximum(Nx-Olist[0]+1)
        self.ONyBox.setMaximum(Ny-Olist[1]+1)
        self.ONzBox.setMaximum(Nz-Olist[2]+1)

# Main Window Class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Basic Functionality:
        # self.pushButton.setCheckable(True)
        self.IntializeButton.clicked.connect(self.Initialize)
        self.MeasureButton.clicked.connect(self.Measure)
        self.toolButton.clicked.connect(self.OpenAO)
        self.TemperatureList = np.linspace(2,300,100)

        # Setting Ranges on Positions:
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

        # Matrix Presentation:
        self.MatrixCanvas = MplCanvas(self, width=8, height=6, dpi=100,check=True)
        self.MatrixLayout = QVBoxLayout()
        self.MatrixTab.setLayout(self.MatrixLayout)
        self.MatrixLayout.addWidget(self.MatrixCanvas)
        plotMatrix(self.MatrixCanvas.axes,24,12,1)
        plotLeads(self.MatrixCanvas.axes,3,1,1,3,12,1,'Red','v')
        self.MatrixCanvas.draw()

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

    def Initialize(self):
        # Defining size of matrix, current input and output locations and values:
        self.Nx = self.NxBox.value(); self.Ny = self.NyBox.value(); self.Nz = self.NzBox.value()
        self.Ilist = [self.IxBox.value(), self.IyBox.value(), self.IzBox.value()]
        self.Olist = [ self.OxBox.value(), self.OyBox.value(), self.OzBox.value()]
        self.Vin = self.IvBox.value(); self.Vout = self.OvBox.value()
        # Simulating the voltage matrices across the temperature range
        self.df = simulate(self.Nx,self.Ny,self.Nz,[self.Ilist],[self.Olist],self.Vin,self.Vout,self.TemperatureList)
        # Plotting the TMax, Z=1 contour on the contour tab:
        self.ContourCanvas.axes.clear()
        contourfit(self.ContourCanvas.axes,self.df,self.Nx,self.Ny,1,0,self.Vin,self.Vout)
        self.ContourCanvas.draw()
        # Setting the T and slider to the correct locations and maximum:
        self.TemperatureSlider.setValue(0)
        self.TemperatureSlider.setMaximum(len(self.TemperatureList)-1)
        self.ZSlider.setValue(1)
        self.ZSlider.setMaximum(self.NzBox.value())
        # Enabling the measure resistivity button:
        self.MeasurementWidget.setEnabled(True)
        self.MeasureButton.setEnabled(True)
        self.ContourTab.setEnabled(True)
        self.ResistanceTab.setEnabled(True)
        # Resetting the resistance canvas:
        self.ResistanceCanvas.axes.clear()
        self.ResistanceCanvas.draw()

    def Measure(self):
        # Define location of the two probes on the sample
        self.IPx = self.IPxBox.value(); self.IPy = self.IPyBox.value(); self.IPz = self.IPzBox.value()
        self.OPx = self.OPxBox.value(); self.OPy = self.OPyBox.value(); self.OPz = self.OPzBox.value()
        # Plot the resistance across these points through the temperature range.
        ResistancePlot(self.ResistanceCanvas.axes,self.df,self.IPx,self.IPy,self.IPz,self.OPx,self.OPy,self.OPz,self.CheckX.isChecked(),self.CheckY.isChecked(),self.CheckZ.isChecked())
        self.ResistanceCanvas.draw()
        # Re-draw the matrix canvas
        self.MatrixCanvas.axes.clear()
        plotMatrix(self.MatrixCanvas.axes,self.NxBox.value(),self.NyBox.value(),self.NzBox.value())
        plotLeads(self.MatrixCanvas.axes,self.IxBox.value(),self.IyBox.value(),self.IzBox.value(),self.OxBox.value(),self.OyBox.value(),self.OzBox.value(),'Red','v')
        plotLeads(self.MatrixCanvas.axes,self.IPx,self.IPy,self.IPz,self.OPx,self.OPy,self.OPz,'Black','X')
        self.MatrixCanvas.draw()

    def OpenAO(self):
        dlg = AdvancedOptions(self.NxBox.value(),self.NyBox.value(),self.NzBox.value(),[self.IxBox.value(),self.IyBox.value(),self.IzBox.value()],[self.OxBox.value(),self.OyBox.value(),self.OzBox.value()])
        dlg.setWindowTitle("HELLO!")
        if dlg.exec():
            self.MeasurementWidget.setEnabled(False)
            self.TemperatureList = np.linspace(dlg.TmBox.value(),dlg.TMBox.value(),dlg.TeBox.value())


    def changeTValue(self, value):
        self.TValue = value
        contourfit(self.ContourCanvas.axes,self.df,self.Nx,self.Ny,self.ZValue,value,self.Vin,self.Vout)
        self.ContourCanvas.draw()
        self.TemperatureLabel.setText("Temperature: "+str(self.TemperatureList[value]))

    def changeZValue(self, value):
        self.ZValue = value
        contourfit(self.ContourCanvas.axes,self.df,self.Nx,self.Ny,value,self.TValue,self.Vin,self.Vout)
        self.ContourCanvas.draw()

    def changeNxValue(self, value):
        self.IxBox.setMaximum(value)
        self.OxBox.setMaximum(value)
        self.IPxBox.setMaximum(value)
        self.OPxBox.setMaximum(value)
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.MatrixCanvas.axes.clear()
        plotMatrix(self.MatrixCanvas.axes,self.NxBox.value(),self.NyBox.value(),self.NzBox.value())
        plotLeads(self.MatrixCanvas.axes,self.IxBox.value(),self.IyBox.value(),self.IzBox.value(),self.OxBox.value(),self.OyBox.value(),self.OzBox.value(),'Red','v')
        self.MatrixCanvas.draw()

    def changeNyValue(self, value):
        self.IyBox.setMaximum(value)
        self.OyBox.setMaximum(value)
        self.IPyBox.setMaximum(value)
        self.OPyBox.setMaximum(value)
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.MatrixCanvas.axes.clear()
        plotMatrix(self.MatrixCanvas.axes,self.NxBox.value(),self.NyBox.value(),self.NzBox.value())
        plotLeads(self.MatrixCanvas.axes,self.IxBox.value(),self.IyBox.value(),self.IzBox.value(),self.OxBox.value(),self.OyBox.value(),self.OzBox.value(),'Red','v')
        self.MatrixCanvas.draw()

    def changeNzValue(self, value):
        self.IzBox.setMaximum(value)
        self.OzBox.setMaximum(value)
        self.IPzBox.setMaximum(value)
        self.OPzBox.setMaximum(value)
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-setting the Z Value on the slider:
        if self.ZValue > value:
            self.ZValue = value
        # Re-draw the matrix canvas
        self.MatrixCanvas.axes.clear()
        plotMatrix(self.MatrixCanvas.axes,self.NxBox.value(),self.NyBox.value(),self.NzBox.value())
        plotLeads(self.MatrixCanvas.axes,self.IxBox.value(),self.IyBox.value(),self.IzBox.value(),self.OxBox.value(),self.OyBox.value(),self.OzBox.value(),'Red','v')
        self.MatrixCanvas.draw()

    def changeIOValue(self, value):
        # Disabling the measurement widget
        self.MeasurementWidget.setEnabled(False)
        # Re-draw the matrix canvas
        self.MatrixCanvas.axes.clear()
        plotMatrix(self.MatrixCanvas.axes,self.NxBox.value(),self.NyBox.value(),self.NzBox.value())
        plotLeads(self.MatrixCanvas.axes,self.IxBox.value(),self.IyBox.value(),self.IzBox.value(),self.OxBox.value(),self.OyBox.value(),self.OzBox.value(),'Red','v')
        self.MatrixCanvas.draw()

    def changeVValue(self, value):
        # Disabling the measurement widget
        self.IvBox.setMinimum(self.OvBox.value()+0.01)
        self.OvBox.setMaximum(self.IvBox.value()-0.01)
        self.MeasurementWidget.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())