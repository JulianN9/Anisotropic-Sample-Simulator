# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FittingPopUp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FittingPopUp(object):
    def setupUi(self, FittingPopUp):
        if not FittingPopUp.objectName():
            FittingPopUp.setObjectName(u"FittingPopUp")
        FittingPopUp.resize(400, 111)
        self.verticalLayout = QVBoxLayout(FittingPopUp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titlelabel = QLabel(FittingPopUp)
        self.titlelabel.setObjectName(u"titlelabel")

        self.verticalLayout.addWidget(self.titlelabel)

        self.label = QLabel(FittingPopUp)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(FittingPopUp)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(FittingPopUp)
        self.buttonBox.accepted.connect(FittingPopUp.accept)
        self.buttonBox.rejected.connect(FittingPopUp.reject)

        QMetaObject.connectSlotsByName(FittingPopUp)
    # setupUi

    def retranslateUi(self, FittingPopUp):
        FittingPopUp.setWindowTitle(QCoreApplication.translate("FittingPopUp", u"Dialog", None))
        self.titlelabel.setText(QCoreApplication.translate("FittingPopUp", u"Fitting Now", None))
        self.label.setText(QCoreApplication.translate("FittingPopUp", u"Time Elapsed: 0", None))
    # retranslateUi

