import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout, 
                             QTabWidget, QStackedWidget, QLineEdit, 
                             QComboBox, QTextEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import QIcon

# Импортиране на модулите за различните функционалности
import network_scanner
import vulnerability_scanner
import exploitation
import cryptography
import forensics
import wireless
import system_security
import system_administration
import utils

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("whoadaz")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))  # Заменете с икона на програмата

        # Създаване на централен widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Създаване на layout
        main_layout = QHBoxLayout(central_widget)

        # Създаване на лента с раздели
        self.tabs = QTabWidget(self)
        self.tabs.addTab(self.create_home_tab(), "Начало")
        self.tabs.addTab(self.create_network_scanner_tab(), "Сканиране на мрежата")
        self.tabs.addTab(self.create_vulnerability_scanner_tab(), "Анализ на уязвимости")
        self.tabs.addTab(self.create_exploitation_tab(), "Експлоатация")
        self.tabs.addTab(self.create_cryptography_tab(), "Криптография")
        self.tabs.addTab(self.create_forensics_tab(), "Форензика")
        self.tabs.addTab(self.create_wireless_tab(), "Безжични мрежи")
        self.tabs.addTab(self.create_system_security_tab(), "Системна сигурност")
        self.tabs.addTab(self.create_system_administration_tab(), "Системна администрация")
        main_layout.addWidget(self.tabs)

    def create_home_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Добре дошли в whoadaz!", self)
        layout.addWidget(label)
        tab.setLayout(layout)
        return tab

    def create_network_scanner_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Nmap сканиране
        nmap_label = QLabel("Nmap сканиране:")
        layout.addWidget(nmap_label)

        nmap_target_label = QLabel("Цел:")
        layout.addWidget(nmap_target_label)
        self.nmap_target_input = QLineEdit(self)
        layout.addWidget(self.nmap_target_input)

        nmap_ports_label = QLabel("Портове:")
        layout.addWidget(nmap_ports_label)
        self.nmap_ports_input = QLineEdit(self)
        layout.addWidget(self.nmap_ports_input)

        nmap_arguments_label = QLabel("Аргументи:")
        layout.addWidget(nmap_arguments_label)
        self.nmap_arguments_input = QLineEdit(self)
        layout.addWidget(self.nmap_arguments_input)

        nmap_button = QPushButton("Сканиране", self)
        nmap_button.clicked.connect(self.run_nmap_scan)
        layout.addWidget(nmap_button)

        self.nmap_output = QTextEdit(self)
        self.nmap_output.setReadOnly(True)
        layout.addWidget(self.nmap_output)

        # Angry IP Scanner
        # ... (добавяне на елементи за Angry IP Scanner)

        # Ping sweep
        # ... (добавяне на елементи за ping sweep)

        tab.setLayout(layout)
        return tab

    def run_nmap_scan(self):
        target = self.nmap_target_input.text()
        ports = self.nmap_ports_input.text()
        arguments = self.nmap_arguments_input.text()
        result = network_scanner.nmap_scan(target, ports, arguments)
        self.nmap_output.setText(result)

    def create_vulnerability_scanner_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Добавяне на основни елементи
        label = QLabel("Анализ на уязвимости", self)
        layout.addWidget(label)
        
        # Настройване на layout
        tab.setLayout(layout)
        return tab

    def create_exploitation_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Добавяне на основни елементи
        label = QLabel("Експлоатация", self)
        layout.addWidget(label)
        
        # Настройване на layout
        tab.setLayout(layout)
        return tab

    def create_cryptography_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Добавяне на основни елементи
        label = QLabel("Криптография", self)
        layout.addWidget(label)
        
        # Настройване на layout
        tab.setLayout(layout)
        return tab

    def create_forensics_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Добавяне на основни елементи
        label = QLabel("Форензика", self)
        layout.addWidget(label)
        
        # Настройване на layout
        tab.setLayout(layout)
        return tab

    def create_wireless_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Добавяне на основни елементи
        label = QLabel("Безжични мрежи", self)
        layout.addWidget(label)
        
        # Настройване на layout
        tab.setLayout(layout)
        return tab

    def create_system_security_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Добавяне на основни елементи
        label = QLabel("Системна сигурност", self)
        layout.addWidget(label)
        
        # Настройване на layout
        tab.setLayout(layout)
        return tab

    def create_system_administration_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Добавяне на основни елементи
        label = QLabel("Системна администрация", self)
        layout.addWidget(label)
        
        # Настройване на layout
        tab.setLayout(layout)
        return tab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())