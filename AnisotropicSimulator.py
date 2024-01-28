import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QSlider, QLabel
from ui_MainWindow import Ui_MainWindow
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from Simulator import simulate
from ContourPlot import contourfit
from MatrixDiagram import plotMatrix
from ResistancePlot import ResistancePlot

# # Show the GUI
# loader = QUiLoader()
# app = QtWidgets.QApplication(sys.argv)
# window = loader.load("AnisotropicSimulator.ui", None)
# window.show()
# app.exec()

# # Code the GUI

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Basic Functionality:
        # self.pushButton.setCheckable(True)
        self.IntializeButton.clicked.connect(self.Initialize)
        self.MeasureButton.clicked.connect(self.Measure)

        # Setting Ranges on Positions:
        self.NxBox.valueChanged[int].connect(self.changeNxValue)
        self.NyBox.valueChanged[int].connect(self.changeNyValue)
        self.NzBox.valueChanged[int].connect(self.changeNzValue)

        # Matrix Presentation:
        self.MatrixCanvas = MplCanvas(self, width=6, height=4, dpi=100)
        self.MatrixLayout.addWidget(self.MatrixCanvas)
        plotMatrix(self.MatrixCanvas.axes,24,12,1,1,1,12)
        self.MatrixCanvas.draw()

        # Contour Presentation:
        self.ContourCanvas = MplCanvas(self, width=5, height=4, dpi=100)

        # self.ContourToolbar = NavigationToolbar(self.ContourCanvas, self)
        # self.ContourLayout.addWidget(self.ContourToolbar)

        self.TemperatureSlider = QSlider(self.ContourTab)
        self.TemperatureSlider.valueChanged[int].connect(self.changeTValue)
        self.TemperatureSlider.setDisabled(True)
        self.TemperatureSlider.setOrientation(QtCore.Qt.Horizontal)

        self.TemperatureLabel = QLabel(self.ContourTab)
        self.TemperatureLabel.setText("Temperature: "+str(300.0))

        self.ContourLayout.addWidget(self.ContourCanvas)
        self.ContourLayout.addWidget(self.TemperatureSlider)
        self.ContourLayout.addWidget(self.TemperatureLabel)

        # Resistance Presentation:
        self.ResistanceCanvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.ResistanceToolbar = NavigationToolbar(self.ResistanceCanvas, self)
        self.ResistanceLayout.addWidget(self.ResistanceToolbar)

        self.ResistanceLayout.addWidget(self.ResistanceCanvas)

    def Initialize(self):
        self.Nx = self.NxBox.value()
        self.Ny = self.NyBox.value()
        self.Ix = self.IxBox.value()
        self.Iy = self.IyBox.value()
        self.Ox = self.OxBox.value()
        self.Oy = self.OyBox.value()
        self.Vin = self.IvBox.value()
        self.Vout = self.OvBox.value()
        self.df = simulate(self.Nx,self.Ny,self.Ix,self.Iy,self.Ox,self.Oy,self.Vin,self.Vout)

        contourfit(self.ContourCanvas.axes,self.df,self.Nx,self.Ny,0)
        self.TemperatureSlider.setValue(0)
        self.ContourCanvas.draw()
        self.TemperatureSlider.setEnabled(True)
        self.MeasureButton.setEnabled(True)

        self.ResistanceCanvas.axes.clear()
        self.ResistanceCanvas.draw()

        print("Clicked")
        # print(df)

    def Measure(self):
        self.IPx = self.IPxBox.value()
        self.IPy = self.IPyBox.value()
        self.OPx = self.OPxBox.value()
        self.OPy = self.OPyBox.value()

        ResistancePlot(self.ResistanceCanvas.axes,self.df,self.IPx,self.IPy,self.OPx,self.OPy,self.CheckX.isChecked(),self.CheckY.isChecked())
        self.ResistanceCanvas.draw()

        print("Clicked Measure")
        # print(df)

    def changeTValue(self, value):
        contourfit(self.ContourCanvas.axes,self.df,self.Nx,self.Ny,value)
        self.ContourCanvas.draw()
        self.TemperatureLabel.setText("Temperature: "+str(300.0-value*(300.-2.)/(100-1)))
        # print(value)

    def changeNxValue(self, value):
        self.IxBox.setMaximum(value)
        self.OxBox.setMaximum(value)
        self.IPxBox.setMaximum(value)
        self.OPxBox.setMaximum(value)

    def changeNyValue(self, value):
        self.IyBox.setMaximum(value)
        self.OyBox.setMaximum(value)
        self.IPyBox.setMaximum(value)
        self.OPyBox.setMaximum(value)

    def changeNzValue(self, value):
        self.IzBox.setMaximum(value)
        self.OzBox.setMaximum(value)
        self.IPzBox.setMaximum(value)
        self.OPzBox.setMaximum(value)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()