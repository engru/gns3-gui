# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'virtualbox_vm_configuration_page.ui'
#
# Created: Tue Jun 23 17:38:16 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets

class Ui_virtualBoxVMConfigPageWidget(object):
    def setupUi(self, virtualBoxVMConfigPageWidget):
        virtualBoxVMConfigPageWidget.setObjectName("virtualBoxVMConfigPageWidget")
        virtualBoxVMConfigPageWidget.resize(510, 463)
        self.verticalLayout = QtWidgets.QVBoxLayout(virtualBoxVMConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(virtualBoxVMConfigPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.tab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(self.tab)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.tab)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(self.tab)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout.addWidget(self.uiCategoryLabel, 2, 0, 1, 1)
        self.uiCategoryComboBox = QtWidgets.QComboBox(self.tab)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.gridLayout.addWidget(self.uiCategoryComboBox, 2, 1, 1, 1)
        self.uiVMListLabel = QtWidgets.QLabel(self.tab)
        self.uiVMListLabel.setObjectName("uiVMListLabel")
        self.gridLayout.addWidget(self.uiVMListLabel, 3, 0, 1, 1)
        self.uiVMListComboBox = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.gridLayout.addWidget(self.uiVMListComboBox, 3, 1, 1, 1)
        self.uiVMRamLabel = QtWidgets.QLabel(self.tab)
        self.uiVMRamLabel.setObjectName("uiVMRamLabel")
        self.gridLayout.addWidget(self.uiVMRamLabel, 4, 0, 1, 1)
        self.uiVMRamSpinBox = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMRamSpinBox.sizePolicy().hasHeightForWidth())
        self.uiVMRamSpinBox.setSizePolicy(sizePolicy)
        self.uiVMRamSpinBox.setMaximum(65535)
        self.uiVMRamSpinBox.setObjectName("uiVMRamSpinBox")
        self.gridLayout.addWidget(self.uiVMRamSpinBox, 4, 1, 1, 1)
        self.uiConsolePortLabel = QtWidgets.QLabel(self.tab)
        self.uiConsolePortLabel.setObjectName("uiConsolePortLabel")
        self.gridLayout.addWidget(self.uiConsolePortLabel, 5, 0, 1, 1)
        self.uiConsolePortSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiConsolePortSpinBox.setMaximum(65535)
        self.uiConsolePortSpinBox.setObjectName("uiConsolePortSpinBox")
        self.gridLayout.addWidget(self.uiConsolePortSpinBox, 5, 1, 1, 1)
        self.uiEnableConsoleCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiEnableConsoleCheckBox.setObjectName("uiEnableConsoleCheckBox")
        self.gridLayout.addWidget(self.uiEnableConsoleCheckBox, 6, 0, 1, 2)
        self.uiACPIShutdownCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiACPIShutdownCheckBox.setObjectName("uiACPIShutdownCheckBox")
        self.gridLayout.addWidget(self.uiACPIShutdownCheckBox, 7, 0, 1, 2)
        self.uiHeadlessModeCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiHeadlessModeCheckBox.setChecked(False)
        self.uiHeadlessModeCheckBox.setObjectName("uiHeadlessModeCheckBox")
        self.gridLayout.addWidget(self.uiHeadlessModeCheckBox, 8, 0, 1, 2)
        self.uiBaseVMCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiBaseVMCheckBox.setEnabled(True)
        self.uiBaseVMCheckBox.setObjectName("uiBaseVMCheckBox")
        self.gridLayout.addWidget(self.uiBaseVMCheckBox, 9, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 138, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 1, 1, 1)
        self.uiTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiAdaptersLabel = QtWidgets.QLabel(self.tab_2)
        self.uiAdaptersLabel.setObjectName("uiAdaptersLabel")
        self.gridLayout_2.addWidget(self.uiAdaptersLabel, 0, 0, 1, 1)
        self.uiAdaptersSpinBox = QtWidgets.QSpinBox(self.tab_2)
        self.uiAdaptersSpinBox.setMinimum(1)
        self.uiAdaptersSpinBox.setMaximum(36)
        self.uiAdaptersSpinBox.setObjectName("uiAdaptersSpinBox")
        self.gridLayout_2.addWidget(self.uiAdaptersSpinBox, 0, 1, 1, 1)
        self.uiPortNameFormatLabel = QtWidgets.QLabel(self.tab_2)
        self.uiPortNameFormatLabel.setObjectName("uiPortNameFormatLabel")
        self.gridLayout_2.addWidget(self.uiPortNameFormatLabel, 1, 0, 1, 1)
        self.uiPortNameFormatLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.uiPortNameFormatLineEdit.setText("")
        self.uiPortNameFormatLineEdit.setObjectName("uiPortNameFormatLineEdit")
        self.gridLayout_2.addWidget(self.uiPortNameFormatLineEdit, 1, 1, 1, 1)
        self.uiPortSegmentSizeLabel = QtWidgets.QLabel(self.tab_2)
        self.uiPortSegmentSizeLabel.setObjectName("uiPortSegmentSizeLabel")
        self.gridLayout_2.addWidget(self.uiPortSegmentSizeLabel, 2, 0, 1, 1)
        self.uiPortSegmentSizeSpinBox = QtWidgets.QSpinBox(self.tab_2)
        self.uiPortSegmentSizeSpinBox.setMaximum(128)
        self.uiPortSegmentSizeSpinBox.setSingleStep(4)
        self.uiPortSegmentSizeSpinBox.setObjectName("uiPortSegmentSizeSpinBox")
        self.gridLayout_2.addWidget(self.uiPortSegmentSizeSpinBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.uiAdapterTypesComboBox = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdapterTypesComboBox.sizePolicy().hasHeightForWidth())
        self.uiAdapterTypesComboBox.setSizePolicy(sizePolicy)
        self.uiAdapterTypesComboBox.setObjectName("uiAdapterTypesComboBox")
        self.gridLayout_2.addWidget(self.uiAdapterTypesComboBox, 3, 1, 1, 1)
        self.uiUseAnyAdapterCheckBox = QtWidgets.QCheckBox(self.tab_2)
        self.uiUseAnyAdapterCheckBox.setObjectName("uiUseAnyAdapterCheckBox")
        self.gridLayout_2.addWidget(self.uiUseAnyAdapterCheckBox, 4, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(248, 178, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 1, 1, 1)
        self.uiTabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.uiTabWidget)

        self.retranslateUi(virtualBoxVMConfigPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(virtualBoxVMConfigPageWidget)

    def retranslateUi(self, virtualBoxVMConfigPageWidget):
        _translate = gns3.qt.translate
        virtualBoxVMConfigPageWidget.setWindowTitle(_translate("virtualBoxVMConfigPageWidget", "VirtualBox VM configuration"))
        self.uiNameLabel.setText(_translate("virtualBoxVMConfigPageWidget", "Name:"))
        self.uiSymbolLabel.setText(_translate("virtualBoxVMConfigPageWidget", "Symbol:"))
        self.uiSymbolToolButton.setText(_translate("virtualBoxVMConfigPageWidget", "&Browse..."))
        self.uiCategoryLabel.setText(_translate("virtualBoxVMConfigPageWidget", "Category:"))
        self.uiVMListLabel.setText(_translate("virtualBoxVMConfigPageWidget", "VM name:"))
        self.uiVMRamLabel.setText(_translate("virtualBoxVMConfigPageWidget", "RAM:"))
        self.uiVMRamSpinBox.setSuffix(_translate("virtualBoxVMConfigPageWidget", " MB"))
        self.uiConsolePortLabel.setText(_translate("virtualBoxVMConfigPageWidget", "Console port:"))
        self.uiEnableConsoleCheckBox.setText(_translate("virtualBoxVMConfigPageWidget", "Enable remote console"))
        self.uiACPIShutdownCheckBox.setText(_translate("virtualBoxVMConfigPageWidget", "Enable ACPI shutdown"))
        self.uiHeadlessModeCheckBox.setText(_translate("virtualBoxVMConfigPageWidget", "Start VM in headless mode"))
        self.uiBaseVMCheckBox.setText(_translate("virtualBoxVMConfigPageWidget", "Use as a linked base VM (experimental)"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("virtualBoxVMConfigPageWidget", "General settings"))
        self.uiAdaptersLabel.setText(_translate("virtualBoxVMConfigPageWidget", "Adapters:"))
        self.uiPortNameFormatLabel.setText(_translate("virtualBoxVMConfigPageWidget", "Name format:"))
        self.uiPortSegmentSizeLabel.setText(_translate("virtualBoxVMConfigPageWidget", "Segment size:"))
        self.label.setText(_translate("virtualBoxVMConfigPageWidget", "Type:"))
        self.uiUseAnyAdapterCheckBox.setText(_translate("virtualBoxVMConfigPageWidget", "Allow GNS3 to use any configured VirtualBox adapter"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab_2), _translate("virtualBoxVMConfigPageWidget", "Network"))

