# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedOptions.ui'
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
    QFormLayout, QGridLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_AdvancedOptions(object):
    def setupUi(self, AdvancedOptions):
        if not AdvancedOptions.objectName():
            AdvancedOptions.setObjectName(u"AdvancedOptions")
        AdvancedOptions.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AdvancedOptions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(AdvancedOptions)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.TRangeLayout = QGridLayout()
        self.TRangeLayout.setObjectName(u"TRangeLayout")
        self.TeBox = QSpinBox(AdvancedOptions)
        self.TeBox.setObjectName(u"TeBox")
        self.TeBox.setMinimum(1)
        self.TeBox.setMaximum(1000)
        self.TeBox.setValue(100)

        self.TRangeLayout.addWidget(self.TeBox, 1, 2, 1, 1)

        self.TeLabel = QLabel(AdvancedOptions)
        self.TeLabel.setObjectName(u"TeLabel")

        self.TRangeLayout.addWidget(self.TeLabel, 0, 2, 1, 1)

        self.TMBox = QSpinBox(AdvancedOptions)
        self.TMBox.setObjectName(u"TMBox")
        self.TMBox.setMinimum(100)
        self.TMBox.setMaximum(1000)
        self.TMBox.setValue(300)

        self.TRangeLayout.addWidget(self.TMBox, 1, 1, 1, 1)

        self.TmBox = QSpinBox(AdvancedOptions)
        self.TmBox.setObjectName(u"TmBox")
        self.TmBox.setMinimum(1)
        self.TmBox.setMaximum(100)
        self.TmBox.setValue(2)

        self.TRangeLayout.addWidget(self.TmBox, 1, 0, 1, 1)

        self.TmLabel = QLabel(AdvancedOptions)
        self.TmLabel.setObjectName(u"TmLabel")

        self.TRangeLayout.addWidget(self.TmLabel, 0, 0, 1, 1)

        self.TMLabel = QLabel(AdvancedOptions)
        self.TMLabel.setObjectName(u"TMLabel")

        self.TRangeLayout.addWidget(self.TMLabel, 0, 1, 1, 1)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.TRangeLayout)

        self.label_11 = QLabel(AdvancedOptions)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.INLayout = QGridLayout()
        self.INLayout.setObjectName(u"INLayout")
        self.INxLabel = QLabel(AdvancedOptions)
        self.INxLabel.setObjectName(u"INxLabel")

        self.INLayout.addWidget(self.INxLabel, 0, 0, 1, 1)

        self.INxBox = QSpinBox(AdvancedOptions)
        self.INxBox.setObjectName(u"INxBox")
        self.INxBox.setMinimum(1)
        self.INxBox.setMaximum(1)

        self.INLayout.addWidget(self.INxBox, 1, 0, 1, 1)

        self.INyLabel = QLabel(AdvancedOptions)
        self.INyLabel.setObjectName(u"INyLabel")

        self.INLayout.addWidget(self.INyLabel, 0, 1, 1, 1)

        self.INzLabel = QLabel(AdvancedOptions)
        self.INzLabel.setObjectName(u"INzLabel")

        self.INLayout.addWidget(self.INzLabel, 0, 2, 1, 1)

        self.INyBox = QSpinBox(AdvancedOptions)
        self.INyBox.setObjectName(u"INyBox")
        self.INyBox.setMinimum(1)
        self.INyBox.setMaximum(1)

        self.INLayout.addWidget(self.INyBox, 1, 1, 1, 1)

        self.INzBox = QSpinBox(AdvancedOptions)
        self.INzBox.setObjectName(u"INzBox")
        self.INzBox.setMinimum(1)
        self.INzBox.setMaximum(1)

        self.INLayout.addWidget(self.INzBox, 1, 2, 1, 1)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.INLayout)

        self.label_12 = QLabel(AdvancedOptions)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.ONLayout = QGridLayout()
        self.ONLayout.setObjectName(u"ONLayout")
        self.ONxBox = QSpinBox(AdvancedOptions)
        self.ONxBox.setObjectName(u"ONxBox")
        self.ONxBox.setMinimum(1)
        self.ONxBox.setMaximum(1)

        self.ONLayout.addWidget(self.ONxBox, 1, 0, 1, 1)

        self.ONyLabel = QLabel(AdvancedOptions)
        self.ONyLabel.setObjectName(u"ONyLabel")

        self.ONLayout.addWidget(self.ONyLabel, 0, 1, 1, 1)

        self.ONxLabel = QLabel(AdvancedOptions)
        self.ONxLabel.setObjectName(u"ONxLabel")

        self.ONLayout.addWidget(self.ONxLabel, 0, 0, 1, 1)

        self.ONzLabel = QLabel(AdvancedOptions)
        self.ONzLabel.setObjectName(u"ONzLabel")

        self.ONLayout.addWidget(self.ONzLabel, 0, 2, 1, 1)

        self.ONyBox = QSpinBox(AdvancedOptions)
        self.ONyBox.setObjectName(u"ONyBox")
        self.ONyBox.setMinimum(1)
        self.ONyBox.setMaximum(1)

        self.ONLayout.addWidget(self.ONyBox, 1, 1, 1, 1)

        self.ONzBox = QSpinBox(AdvancedOptions)
        self.ONzBox.setObjectName(u"ONzBox")
        self.ONzBox.setMinimum(1)
        self.ONzBox.setMaximum(1)

        self.ONLayout.addWidget(self.ONzBox, 1, 2, 1, 1)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.ONLayout)

        self.label_13 = QLabel(AdvancedOptions)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.ResistivityButton = QPushButton(AdvancedOptions)
        self.ResistivityButton.setObjectName(u"ResistivityButton")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.ResistivityButton)

        self.label = QLabel(AdvancedOptions)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label)

        self.label_3 = QLabel(AdvancedOptions)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.ResistivitySR = QSpinBox(AdvancedOptions)
        self.ResistivitySR.setObjectName(u"ResistivitySR")
        self.ResistivitySR.setMaximum(10000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.ResistivitySR)

        self.ResistivitySeperator = QPlainTextEdit(AdvancedOptions)
        self.ResistivitySeperator.setObjectName(u"ResistivitySeperator")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.ResistivitySeperator)

        self.ResistivityHeader = QPlainTextEdit(AdvancedOptions)
        self.ResistivityHeader.setObjectName(u"ResistivityHeader")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ResistivityHeader)

        self.ResistivityHeaderLabel = QLabel(AdvancedOptions)
        self.ResistivityHeaderLabel.setObjectName(u"ResistivityHeaderLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.ResistivityHeaderLabel)


        self.verticalLayout.addLayout(self.formLayout)

        self.AOButtonBox = QDialogButtonBox(AdvancedOptions)
        self.AOButtonBox.setObjectName(u"AOButtonBox")
        self.AOButtonBox.setOrientation(Qt.Horizontal)
        self.AOButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.AOButtonBox)


        self.retranslateUi(AdvancedOptions)
        self.AOButtonBox.accepted.connect(AdvancedOptions.accept)
        self.AOButtonBox.rejected.connect(AdvancedOptions.reject)

        QMetaObject.connectSlotsByName(AdvancedOptions)
    # setupUi

    def retranslateUi(self, AdvancedOptions):
        AdvancedOptions.setWindowTitle(QCoreApplication.translate("AdvancedOptions", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AdvancedOptions", u"Temperature Range", None))
        self.TeLabel.setText(QCoreApplication.translate("AdvancedOptions", u"Entries", None))
        self.TmLabel.setText(QCoreApplication.translate("AdvancedOptions", u"T min", None))
        self.TMLabel.setText(QCoreApplication.translate("AdvancedOptions", u"T max", None))
        self.label_11.setText(QCoreApplication.translate("AdvancedOptions", u"Input Connection Width", None))
        self.INxLabel.setText(QCoreApplication.translate("AdvancedOptions", u"X Width", None))
        self.INyLabel.setText(QCoreApplication.translate("AdvancedOptions", u"Y Width", None))
        self.INzLabel.setText(QCoreApplication.translate("AdvancedOptions", u"Z Width", None))
        self.label_12.setText(QCoreApplication.translate("AdvancedOptions", u"Output Connection Width", None))
        self.ONyLabel.setText(QCoreApplication.translate("AdvancedOptions", u"Y Width", None))
        self.ONxLabel.setText(QCoreApplication.translate("AdvancedOptions", u"X Width", None))
        self.ONzLabel.setText(QCoreApplication.translate("AdvancedOptions", u"Z Width", None))
        self.label_13.setText(QCoreApplication.translate("AdvancedOptions", u"Customize Resistivity", None))
        self.ResistivityButton.setText(QCoreApplication.translate("AdvancedOptions", u"Resisitivity Functions", None))
        self.label.setText(QCoreApplication.translate("AdvancedOptions", u"Seperator", None))
        self.label_3.setText(QCoreApplication.translate("AdvancedOptions", u"Skip Rows", None))
        self.ResistivitySeperator.setPlainText(QCoreApplication.translate("AdvancedOptions", u",", None))
        self.ResistivityHeader.setPlainText(QCoreApplication.translate("AdvancedOptions", u"Temperature, Resistivity", None))
        self.ResistivityHeaderLabel.setText(QCoreApplication.translate("AdvancedOptions", u"Header", None))
    # retranslateUi

