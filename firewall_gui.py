import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton
import subprocess

class FirewallGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ubuntu Firewall GUI")
        self.layout = QVBoxLayout()

        self.label = QLabel("Select the rules to enable/disable:")
        self.layout.addWidget(self.label)

        self.rule1 = QCheckBox("Allow SSH (Port 22)")
        self.layout.addWidget(self.rule1)

        self.rule2 = QCheckBox("Allow HTTP (Port 80)")
        self.layout.addWidget(self.rule2)

        self.rule3 = QCheckBox("Allow HTTPS (Port 443)")
        self.layout.addWidget(self.rule3)

        self.submit_button = QPushButton("Apply Rules")
        self.submit_button.clicked.connect(self.apply_rules)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def apply_rules(self):
        rules = []
        if self.rule1.isChecked():
            rules.append("22")
        if self.rule2.isChecked():
            rules.append("80")
        if self.rule3.isChecked():
            rules.append("443")

        # Execute iptables commands
        for rule in rules:
            subprocess.run(["sudo", "ufw", "allow", rule])

        print("Firewall rules applied.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirewallGUI()
    window.show()
    sys.exit(app.exec_())

