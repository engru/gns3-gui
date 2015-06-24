# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Configuration page for QEMU VMs.
"""

import os
import sys
import re

from functools import partial
from collections import OrderedDict
from gns3.modules.qemu.dialogs.qemu_image_wizard import QemuImageWizard
from gns3.dialogs.symbol_selection_dialog import SymbolSelectionDialog
from gns3.node import Node
from gns3.qt import QtGui, QtCore, QtWidgets
from gns3.servers import Servers
from gns3.modules.module_error import ModuleError
from gns3.dialogs.node_properties_dialog import ConfigurationError
from gns3.image_manager import ImageManager

from ..ui.qemu_vm_configuration_page_ui import Ui_QemuVMConfigPageWidget
from .. import Qemu


class QemuVMConfigurationPage(QtWidgets.QWidget, Ui_QemuVMConfigPageWidget):

    """
    QWidget configuration page for QEMU VMs.
    """

    _default_images_dir = ""

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self._server = None

        self.uiHdaDiskImageToolButton.clicked.connect(self._hdaDiskImageBrowserSlot)
        self.uiHdbDiskImageToolButton.clicked.connect(self._hdbDiskImageBrowserSlot)
        self.uiHdcDiskImageToolButton.clicked.connect(self._hdcDiskImageBrowserSlot)
        self.uiHddDiskImageToolButton.clicked.connect(self._hddDiskImageBrowserSlot)

        self.uiHdaDiskImageCreateToolButton.clicked.connect(self._hdaDiskImageCreateSlot)
        self.uiHdbDiskImageCreateToolButton.clicked.connect(self._hdbDiskImageCreateSlot)
        self.uiHdcDiskImageCreateToolButton.clicked.connect(self._hdcDiskImageCreateSlot)
        self.uiHddDiskImageCreateToolButton.clicked.connect(self._hddDiskImageCreateSlot)

        self.uiSymbolToolButton.clicked.connect(self._symbolBrowserSlot)
        self.uiInitrdToolButton.clicked.connect(self._initrdBrowserSlot)
        self.uiKernelImageToolButton.clicked.connect(self._kernelImageBrowserSlot)
        self.uiActivateCPUThrottlingCheckBox.stateChanged.connect(self._cpuThrottlingChangedSlot)
        self.uiLegacyNetworkingCheckBox.stateChanged.connect(self._legacyNetworkingChangedSlot)

        # add the categories
        for name, category in Node.defaultCategories().items():
            self.uiCategoryComboBox.addItem(name, category)

        self._legacy_devices = ("e1000", "i82551", "i82557b", "i82559er", "ne2k_pci", "pcnet", "rtl8139", "virtio")
        self._qemu_network_devices = OrderedDict([("e1000", "Intel Gigabit Ethernet"),
                                                  ("i82550", "Intel i82550 Ethernet"),
                                                  ("i82551", "Intel i82551 Ethernet"),
                                                  ("i82557a", "Intel i82557A Ethernet"),
                                                  ("i82557b", "Intel i82557B Ethernet"),
                                                  ("i82557c", "Intel i82557C Ethernet"),
                                                  ("i82558a", "Intel i82558A Ethernet"),
                                                  ("i82558b", "Intel i82558B Ethernet"),
                                                  ("i82559a", "Intel i82559A Ethernet"),
                                                  ("i82559b", "Intel i82559B Ethernet"),
                                                  ("i82559c", "Intel i82559C Ethernet"),
                                                  ("i82559er", "Intel i82559ER Ethernet"),
                                                  ("i82562", "Intel i82562 Ethernet"),
                                                  ("i82801", "Intel i82801 Ethernet"),
                                                  ("ne2k_pci", "NE2000 Ethernet"),
                                                  ("pcnet", "AMD PCNet Ethernet"),
                                                  ("rtl8139", "Realtek 8139 Ethernet"),
                                                  ("virtio", "Legacy paravirtualized Network I/O"),
                                                  ("virtio-net-pci", "Paravirtualized Network I/O"),
                                                  ("vmxnet3", "VMWare Paravirtualized Ethernet v3")])

        self._refreshQemuNetworkDevices()

    def _symbolBrowserSlot(self):
        """
        Slot to open the symbol browser and select a new symbol.
        """

        symbol_path = self.uiSymbolLineEdit.text()
        dialog = SymbolSelectionDialog(self, symbol=symbol_path)
        dialog.show()
        if dialog.exec_():
            new_symbol_path = dialog.getSymbol()
            self.uiSymbolLineEdit.setText(new_symbol_path)
            self.uiSymbolLineEdit.setToolTip('<img src="{}"/>'.format(new_symbol_path))

    def _refreshQemuNetworkDevices(self, legacy_networking=False):
        """
        Refreshes the Qemu network device list.

        :param legacy_networking: True if legacy networking is enabled.
        """

        self.uiAdapterTypesComboBox.clear()
        for device_name, device_description in self._qemu_network_devices.items():
            if legacy_networking and device_name not in self._legacy_devices:
                continue
            self.uiAdapterTypesComboBox.addItem("{} ({})".format(device_description, device_name), device_name)

    def getServer(self):
        return Servers.instance().getServerFromString(self.getSettings()["server"])

    @staticmethod
    def getImageDirectory():
        return ImageManager.instance().getDirectoryForType("QEMU")

    @classmethod
    def getDiskImage(cls, parent, server):

        if not cls._default_images_dir:
            cls._default_images_dir = cls.getImageDirectory()

        path, _ = QtWidgets.QFileDialog.getOpenFileName(parent, "Select a QEMU disk image", cls._default_images_dir)
        if not path:
            return
        cls._default_images_dir = os.path.dirname(path)

        if not os.access(path, os.R_OK):
            QtWidgets.QMessageBox.critical(parent, "QEMU disk image", "Cannot read {}".format(path))
            return

        path = ImageManager.instance().askCopyUploadImage(parent, path, server, "QEMU")

        return path

    def _hdaDiskImageBrowserSlot(self):
        """
        Slot to open a file browser and select a QEMU hda disk image.
        """

        path = self.getDiskImage(self, self._server)
        if path:
            self.uiHdaDiskImageLineEdit.clear()
            self.uiHdaDiskImageLineEdit.setText(path)

    def _hdbDiskImageBrowserSlot(self):
        """
        Slot to open a file browser and select a QEMU hdb disk image.
        """

        path = self.getDiskImage(self, self._server)
        if path:
            self.uiHdbDiskImageLineEdit.clear()
            self.uiHdbDiskImageLineEdit.setText(path)

    def _hdcDiskImageBrowserSlot(self):
        """
        Slot to open a file browser and select a QEMU hdc disk image.
        """

        path = self.getDiskImage(self, self._server)
        if path:
            self.uiHdcDiskImageLineEdit.clear()
            self.uiHdcDiskImageLineEdit.setText(path)

    def _hddDiskImageBrowserSlot(self):
        """
        Slot to open a file browser and select a QEMU hdd disk image.
        """

        path = self.getDiskImage(self, self._server)
        if path:
            self.uiHddDiskImageLineEdit.clear()
            self.uiHddDiskImageLineEdit.setText(path)

    def _hdaDiskImageCreateSlot(self):
        create_dialog = QemuImageWizard(self, self.uiNameLineEdit.text() + '-hda')
        if QtWidgets.QDialog.Accepted == create_dialog.exec_():
            self.uiHdaDiskImageLineEdit.setText(create_dialog.uiLocationLineEdit.text())

    def _hdbDiskImageCreateSlot(self):
        create_dialog = QemuImageWizard(self, self.uiNameLineEdit.text() + '-hdb')
        if QtWidgets.QDialog.Accepted == create_dialog.exec_():
            self.uiHdbDiskImageLineEdit.setText(create_dialog.uiLocationLineEdit.text())

    def _hdcDiskImageCreateSlot(self):
        create_dialog = QemuImageWizard(self, self.uiNameLineEdit.text() + '-hdc')
        if QtWidgets.QDialog.Accepted == create_dialog.exec_():
            self.uiHdcDiskImageLineEdit.setText(create_dialog.uiLocationLineEdit.text())

    def _hddDiskImageCreateSlot(self):
        create_dialog = QemuImageWizard(self, self.uiNameLineEdit.text() + '-hdd')
        if QtWidgets.QDialog.Accepted == create_dialog.exec_():
            self.uiHddDiskImageLineEdit.setText(create_dialog.uiLocationLineEdit.text())

    def _initrdBrowserSlot(self):
        """
        Slot to open a file browser and select a QEMU initrd.
        """

        path = self.getDiskImage(self, self._server)
        if path:
            self.uiInitrdLineEdit.clear()
            self.uiInitrdLineEdit.setText(path)

    def _kernelImageBrowserSlot(self):
        """
        Slot to open a file browser and select a QEMU kernel image.
        """

        path = self.getDiskImage(self, self._server)
        if path:
            self.uiKernelImageLineEdit.clear()
            self.uiKernelImageLineEdit.setText(path)

    def _getQemuBinariesFromServerCallback(self, result, error=False, qemu_path=None, **kwargs):
        """
        Callback for getQemuBinariesFromServer.

        :param result: server response
        :param error: indicates an error (boolean)
        """

        if error:
            QtWidgets.QMessageBox.critical(self, "Qemu binaries", "Error: ".format(result["message"]))
        else:
            self.uiQemuListComboBox.clear()
            for qemu in result:
                if qemu["version"]:
                    self.uiQemuListComboBox.addItem("{path} (v{version})".format(path=qemu["path"], version=qemu["version"]), qemu["path"])
                else:
                    self.uiQemuListComboBox.addItem("{path}".format(path=qemu["path"]), qemu["path"])

        index = self.uiQemuListComboBox.findData("{path}".format(path=qemu_path))
        if index != -1:
            self.uiQemuListComboBox.setCurrentIndex(index)
        else:
            QtWidgets.QMessageBox.critical(self, "Qemu", "Could not find {} in the Qemu binaries list".format(qemu_path))
            self.uiQemuListComboBox.clear()

    def _cpuThrottlingChangedSlot(self, state):
        """
        Slot to enable or not CPU throttling.
        """

        if state:
            self.uiCPUThrottlingSpinBox.setEnabled(True)
        else:
            self.uiCPUThrottlingSpinBox.setEnabled(False)

    def _legacyNetworkingChangedSlot(self, state):
        """
        Slot to enable or not legacy networking.
        """

        if state:
            self._refreshQemuNetworkDevices(legacy_networking=True)
        else:
            self._refreshQemuNetworkDevices()

    def loadSettings(self, settings, node=None, group=False):
        """
        Loads the QEMU VM settings.

        :param settings: the settings (dictionary)
        :param node: Node instance
        :param group: indicates the settings apply to a group of VMs
        """

        if node:
            self._server = node.server()
        else:
            self._server = Servers.instance().getServerFromString(settings["server"])

        callback = partial(self._getQemuBinariesFromServerCallback, qemu_path=settings["qemu_path"])
        try:
            Qemu.instance().getQemuBinariesFromServer(self._server, callback)
        except ModuleError as e:
            QtWidgets.QMessageBox.critical(self, "Qemu binaries", "Error while getting the QEMU binaries: {}".format(e))
            self.uiQemuListComboBox.clear()

        if self._server.isLocal() and not sys.platform.startswith("linux"):
            self.uiKVMAccelerationCheckBox.hide()

        if not group:
            # set the device name
            self.uiNameLineEdit.setText(settings["name"])
            if "console" in settings:
                self.uiConsolePortSpinBox.setValue(settings["console"])
            else:
                self.uiConsolePortLabel.hide()
                self.uiConsolePortSpinBox.hide()
            self.uiHdaDiskImageLineEdit.setText(settings["hda_disk_image"])
            self.uiHdbDiskImageLineEdit.setText(settings["hdb_disk_image"])
            self.uiHdcDiskImageLineEdit.setText(settings["hdc_disk_image"])
            self.uiHddDiskImageLineEdit.setText(settings["hdd_disk_image"])
            self.uiInitrdLineEdit.setText(settings["initrd"])
            self.uiKernelImageLineEdit.setText(settings["kernel_image"])
        else:
            self.uiNameLabel.hide()
            self.uiNameLineEdit.hide()
            self.uiConsolePortLabel.hide()
            self.uiConsolePortSpinBox.hide()
            self.uiHdaDiskImageLabel.hide()
            self.uiHdaDiskImageLineEdit.hide()
            self.uiHdaDiskImageToolButton.hide()
            self.uiHdbDiskImageLabel.hide()
            self.uiHdbDiskImageLineEdit.hide()
            self.uiHdbDiskImageToolButton.hide()
            self.uiInitrdLabel.hide()
            self.uiInitrdLineEdit.hide()
            self.uiInitrdToolButton.hide()
            self.uiKernelImageLabel.hide()
            self.uiKernelImageLineEdit.hide()
            self.uiKernelImageToolButton.hide()

        if not node:
            # load the symbol
            self.uiSymbolLineEdit.setText(settings["symbol"])
            self.uiSymbolLineEdit.setToolTip('<img src="{}"/>'.format(settings["symbol"]))

            # load the category
            index = self.uiCategoryComboBox.findData(settings["category"])
            if index != -1:
                self.uiCategoryComboBox.setCurrentIndex(index)

            self.uiPortNameFormatLineEdit.setText(settings["port_name_format"])
            self.uiPortSegmentSizeSpinBox.setValue(settings["port_segment_size"])
        else:
            self.uiSymbolLabel.hide()
            self.uiSymbolLineEdit.hide()
            self.uiSymbolToolButton.hide()
            self.uiCategoryComboBox.hide()
            self.uiCategoryLabel.hide()
            self.uiCategoryComboBox.hide()
            self.uiPortNameFormatLabel.hide()
            self.uiPortNameFormatLineEdit.hide()
            self.uiPortSegmentSizeLabel.hide()
            self.uiPortSegmentSizeSpinBox.hide()

        self.uiKernelCommandLineEdit.setText(settings["kernel_command_line"])
        self.uiAdaptersSpinBox.setValue(settings["adapters"])

        self.uiLegacyNetworkingCheckBox.setChecked(settings["legacy_networking"])

        # load the MAC address setting
        self.uiMacAddrLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        if settings["mac_address"]:
            self.uiMacAddrLineEdit.setText(settings["mac_address"])
        else:
            self.uiMacAddrLineEdit.clear()

        self.uiACPIShutdownCheckBox.setChecked(settings["acpi_shutdown"])
        index = self.uiAdapterTypesComboBox.findData(settings["adapter_type"])
        if index != -1:
            self.uiAdapterTypesComboBox.setCurrentIndex(index)
        self.uiRamSpinBox.setValue(settings["ram"])

        self.uiKVMAccelerationCheckBox.setChecked(settings["kvm"])
        if settings["cpu_throttling"]:
            self.uiActivateCPUThrottlingCheckBox.setChecked(True)
            self.uiCPUThrottlingSpinBox.setValue(settings["cpu_throttling"])
        else:
            self.uiActivateCPUThrottlingCheckBox.setChecked(False)

        index = self.uiProcessPriorityComboBox.findText(settings["process_priority"], QtCore.Qt.MatchFixedString)
        if index != -1:
            self.uiProcessPriorityComboBox.setCurrentIndex(index)
        self.uiQemuOptionsLineEdit.setText(settings["options"])

    def saveSettings(self, settings, node=None, group=False):
        """
        Saves the QEMU VM settings.

        :param settings: the settings (dictionary)
        :param node: Node instance
        :param group: indicates the settings apply to a group of VMs
        """

        # these settings cannot be shared by nodes and updated
        # in the node properties dialog.
        if not group:

            name = self.uiNameLineEdit.text()
            if not name:
                QtWidgets.QMessageBox.critical(self, "Name", "The QEMU VM name cannot be empty!")
            else:
                settings["name"] = name

            if "console" in settings:
                settings["console"] = self.uiConsolePortSpinBox.value()
            settings["hda_disk_image"] = self.uiHdaDiskImageLineEdit.text().strip()
            settings["hdb_disk_image"] = self.uiHdbDiskImageLineEdit.text().strip()
            settings["hdc_disk_image"] = self.uiHdcDiskImageLineEdit.text().strip()
            settings["hdd_disk_image"] = self.uiHddDiskImageLineEdit.text().strip()
            settings["initrd"] = self.uiInitrdLineEdit.text().strip()
            settings["kernel_image"] = self.uiKernelImageLineEdit.text().strip()

            # check and save the MAC address
            mac = self.uiMacAddrLineEdit.text()
            if mac != ":::::":
                if not re.search(r"""^([0-9a-fA-F]{2}[:]){5}[0-9a-fA-F]{2}$""", mac):
                    QtWidgets.QMessageBox.critical(self, "MAC address", "Invalid MAC address (format required: hh:hh:hh:hh:hh:hh)")
                    if node:
                        raise ConfigurationError()
                else:
                    settings["mac_address"] = mac
            else:
                settings["mac_address"] = None

        else:
            del settings["name"]
            if "console" in settings:
                del settings["console"]
            del settings["hda_disk_image"]
            del settings["hdb_disk_image"]
            del settings["hdc_disk_image"]
            del settings["hdd_disk_image"]
            del settings["initrd"]
            del settings["kernel_image"]
            del settings["mac_address"]

        if not node:
            symbol_path = self.uiSymbolLineEdit.text()
            pixmap = QtGui.QPixmap(symbol_path)
            if pixmap.isNull():
                QtWidgets.QMessageBox.critical(self, "Symbol", "Invalid file or format not supported")
            else:
                settings["symbol"] = symbol_path

            settings["category"] = self.uiCategoryComboBox.itemData(self.uiCategoryComboBox.currentIndex())
            port_name_format = self.uiPortNameFormatLineEdit.text()
            if '{0}' not in port_name_format:
                QtWidgets.QMessageBox.critical(self, "Port name format", "The format must contain at least {0}")
            else:
                settings["port_name_format"] = self.uiPortNameFormatLineEdit.text()

            port_segment_size = self.uiPortSegmentSizeSpinBox.value()
            if port_segment_size and '{1}' not in port_name_format:
                QtWidgets.QMessageBox.critical(self, "Port name format", "The format must contain {1} if the segment size is not 0")
            else:
                settings["port_segment_size"] = port_segment_size

        if self.uiQemuListComboBox.count():
            qemu_path = self.uiQemuListComboBox.itemData(self.uiQemuListComboBox.currentIndex())
            settings["qemu_path"] = qemu_path

        settings["adapter_type"] = self.uiAdapterTypesComboBox.itemData(self.uiAdapterTypesComboBox.currentIndex())
        settings["kernel_command_line"] = self.uiKernelCommandLineEdit.text()

        adapters = self.uiAdaptersSpinBox.value()
        if node and settings["adapters"] != adapters:
            # check if the adapters settings have changed
            node_ports = node.ports()
            for node_port in node_ports:
                if not node_port.isFree():
                    QtWidgets.QMessageBox.critical(self, node.name(), "Changing the number of adapters while links are connected isn't supported yet! Please delete all the links first.")
                    raise ConfigurationError()

        settings["adapters"] = adapters
        settings["legacy_networking"] = self.uiLegacyNetworkingCheckBox.isChecked()
        settings["kvm"] = self.uiKVMAccelerationCheckBox.isChecked()
        settings["acpi_shutdown"] = self.uiACPIShutdownCheckBox.isChecked()
        settings["ram"] = self.uiRamSpinBox.value()
        if self.uiActivateCPUThrottlingCheckBox.isChecked():
            settings["cpu_throttling"] = self.uiCPUThrottlingSpinBox.value()
        else:
            settings["cpu_throttling"] = 0
        settings["process_priority"] = self.uiProcessPriorityComboBox.currentText().lower()
        settings["options"] = self.uiQemuOptionsLineEdit.text()
