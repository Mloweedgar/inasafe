# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minimum_needs_configuration.ui'
#
# Created: Fri Oct 31 07:57:22 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_minimumNeeds(object):
    def setupUi(self, minimumNeeds):
        minimumNeeds.setObjectName(_fromUtf8("minimumNeeds"))
        minimumNeeds.resize(742, 666)
        minimumNeeds.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridLayout_3 = QtGui.QGridLayout(minimumNeeds)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.profileLabel = QtGui.QLabel(minimumNeeds)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileLabel.sizePolicy().hasHeightForWidth())
        self.profileLabel.setSizePolicy(sizePolicy)
        self.profileLabel.setObjectName(_fromUtf8("profileLabel"))
        self.horizontalLayout_2.addWidget(self.profileLabel)
        self.profileComboBox = QtGui.QComboBox(minimumNeeds)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileComboBox.sizePolicy().hasHeightForWidth())
        self.profileComboBox.setSizePolicy(sizePolicy)
        self.profileComboBox.setObjectName(_fromUtf8("profileComboBox"))
        self.horizontalLayout_2.addWidget(self.profileComboBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveButton = QtGui.QPushButton(minimumNeeds)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.saveAsButton = QtGui.QPushButton(minimumNeeds)
        self.saveAsButton.setObjectName(_fromUtf8("saveAsButton"))
        self.horizontalLayout.addWidget(self.saveAsButton)
        self.newButton = QtGui.QPushButton(minimumNeeds)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.horizontalLayout.addWidget(self.newButton)
        self.importButton = QtGui.QPushButton(minimumNeeds)
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.horizontalLayout.addWidget(self.importButton)
        self.exportButton = QtGui.QPushButton(minimumNeeds)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout.addWidget(self.exportButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(minimumNeeds)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.stackedWidget = QtGui.QStackedWidget(minimumNeeds)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setFrameShape(QtGui.QFrame.Panel)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.addButton = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMaximumSize(QtCore.QSize(32, 32))
        self.addButton.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)
        self.addButton.setAutoFillBackground(False)
        self.addButton.setText(_fromUtf8("+"))
        self.addButton.setCheckable(False)
        self.addButton.setAutoDefault(True)
        self.addButton.setDefault(False)
        self.addButton.setFlat(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout_3.addWidget(self.addButton)
        self.removeButton = QtGui.QPushButton(self.page)
        self.removeButton.setMaximumSize(QtCore.QSize(32, 32))
        self.removeButton.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.removeButton.setFont(font)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.editButton = QtGui.QPushButton(self.page)
        self.editButton.setMaximumSize(QtCore.QSize(32, 32))
        self.editButton.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.editButton.setFont(font)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.horizontalLayout_3.addWidget(self.editButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.resourceListWidget = QtGui.QListWidget(self.page)
        self.resourceListWidget.setObjectName(_fromUtf8("resourceListWidget"))
        self.gridLayout.addWidget(self.resourceListWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.provenanceLable = QtGui.QLabel(self.page)
        self.provenanceLable.setObjectName(_fromUtf8("provenanceLable"))
        self.horizontalLayout_5.addWidget(self.provenanceLable)
        self.provenanceLineEdit = QtGui.QLineEdit(self.page)
        self.provenanceLineEdit.setObjectName(_fromUtf8("provenanceLineEdit"))
        self.horizontalLayout_5.addWidget(self.provenanceLineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.resourceGroupBox = QtGui.QGroupBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resourceGroupBox.sizePolicy().hasHeightForWidth())
        self.resourceGroupBox.setSizePolicy(sizePolicy)
        self.resourceGroupBox.setTitle(_fromUtf8(""))
        self.resourceGroupBox.setObjectName(_fromUtf8("resourceGroupBox"))
        self.verticalLayout.addWidget(self.resourceGroupBox)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.discardButton = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.discardButton.sizePolicy().hasHeightForWidth())
        self.discardButton.setSizePolicy(sizePolicy)
        self.discardButton.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.discardButton.setFont(font)
        self.discardButton.setObjectName(_fromUtf8("discardButton"))
        self.horizontalLayout_4.addWidget(self.discardButton)
        self.acceptButton = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.acceptButton.sizePolicy().hasHeightForWidth())
        self.acceptButton.setSizePolicy(sizePolicy)
        self.acceptButton.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.acceptButton.setFont(font)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.horizontalLayout_4.addWidget(self.acceptButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(minimumNeeds)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), minimumNeeds.close)
        QtCore.QMetaObject.connectSlotsByName(minimumNeeds)

    def retranslateUi(self, minimumNeeds):
        minimumNeeds.setWindowTitle(_translate("minimumNeeds", "Minimum Needs", None))
        self.profileLabel.setText(_translate("minimumNeeds", "Profile:", None))
        self.profileComboBox.setToolTip(_translate("minimumNeeds", "Select a profile", None))
        self.saveButton.setText(_translate("minimumNeeds", "Save", None))
        self.saveAsButton.setText(_translate("minimumNeeds", "Save As ...", None))
        self.newButton.setText(_translate("minimumNeeds", "New...", None))
        self.importButton.setText(_translate("minimumNeeds", "Import ...", None))
        self.exportButton.setText(_translate("minimumNeeds", "Export ...", None))
        self.closeButton.setText(_translate("minimumNeeds", "Close", None))
        self.addButton.setToolTip(_translate("minimumNeeds", "Add new resource", None))
        self.removeButton.setToolTip(_translate("minimumNeeds", "Remove selected resource", None))
        self.removeButton.setText(_translate("minimumNeeds", "-", None))
        self.editButton.setToolTip(_translate("minimumNeeds", "Edit selected resource", None))
        self.editButton.setText(_translate("minimumNeeds", "E", None))
        self.provenanceLable.setText(_translate("minimumNeeds", "Provenance", None))
        self.discardButton.setToolTip(_translate("minimumNeeds", "Discard and return", None))
        self.discardButton.setText(_translate("minimumNeeds", "X", None))
        self.acceptButton.setToolTip(_translate("minimumNeeds", "Accept and return", None))
        self.acceptButton.setText(_translate("minimumNeeds", "✓", None))

