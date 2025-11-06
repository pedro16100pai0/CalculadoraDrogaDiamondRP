from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QSpinBox, QTextEdit, QGroupBox, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys

class CalculadoraDroga(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Droga e Lavagem")
        self.setGeometry(100, 100, 900, 540)
        self.setStyleSheet("background-color:#0f1720; color: #E6EEF3;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(14)

        # Header
        header = QLabel("💸 Calculadora de Droga e Lavagem")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_font = QFont("Segoe UI", 18, QFont.Weight.Bold)
        header.setFont(header_font)
        header.setStyleSheet("""
            color: white;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #227dbd, stop:1 #34ca97);
            padding: 12px;
            border-radius: 12px;
        """)
        layout.addWidget(header)

        # Inputs area (left: gramas/drogas; right: bonecos/dinheiro/percentagem)
        central_layout = QHBoxLayout()
        central_layout.setSpacing(12)

        # Drogas
        group_drogas = QGroupBox("Quantidades de Drogas (gramas)")
        group_drogas.setStyleSheet("""
            QGroupBox { font-weight:700; color:#E6EEF3; border: 1px solid #29509c; border-radius:8px; padding:8px; }
        """)
        grid_drogas = QGridLayout()
        grid_drogas.setHorizontalSpacing(10)
        grid_drogas.setVerticalSpacing(8)
        self.spin_meta = QSpinBox(); self.spin_meta.setRange(0, 100000)
        self.spin_meta.setSpecialValueText("")
        self.spin_meta.setStyleSheet("QSpinBox { background: #152940; color: #E6EEF3; border-radius:6px; }")
        self.spin_coca = QSpinBox(); self.spin_coca.setRange(0, 100000)
        self.spin_coca.setSpecialValueText("")
        self.spin_coca.setStyleSheet("QSpinBox { background: #152940; color: #E6EEF3; border-radius:6px; }")
        self.spin_erva = QSpinBox(); self.spin_erva.setRange(0, 100000)
        self.spin_erva.setSpecialValueText("")
        self.spin_erva.setStyleSheet("QSpinBox { background: #152940; color: #E6EEF3; border-radius:6px; }")
        grid_drogas.addWidget(QLabel("Metanfetamina:"), 0, 0)
        grid_drogas.addWidget(self.spin_meta, 0, 1)
        grid_drogas.addWidget(QLabel("Cocaína:"), 1, 0)
        grid_drogas.addWidget(self.spin_coca, 1, 1)
        grid_drogas.addWidget(QLabel("Erva:"), 2, 0)
        grid_drogas.addWidget(self.spin_erva, 2, 1)
        group_drogas.setLayout(grid_drogas)
        central_layout.addWidget(group_drogas, stretch=1)

        # Right area: bonecos, dinheiro sujo, percentagem
        group_info = QGroupBox("Opções Adicionais")
        group_info.setStyleSheet("""
            QGroupBox { font-weight:700; color:#E6EEF3; border: 1px solid #29509c; border-radius:8px; padding:8px; }
        """)
        info_layout = QGridLayout()
        info_layout.setHorizontalSpacing(10)
        info_layout.setVerticalSpacing(8)
        self.spin_bonecos = QSpinBox()
        self.spin_bonecos.setRange(0, 10000)
        self.spin_bonecos.setSpecialValueText("")
        self.spin_bonecos.setStyleSheet("QSpinBox { background: #173646; color: #E6EEF3; border-radius:6px; }")
        self.spin_dinheiro = QSpinBox()
        self.spin_dinheiro.setRange(0, 2000000000)
        self.spin_dinheiro.setSpecialValueText("")
        self.spin_dinheiro.setStyleSheet("QSpinBox { background: #173646; color: #E6EEF3; border-radius:6px; }")
        self.spin_percent = QSpinBox()
        self.spin_percent.setRange(0, 100)
        self.spin_percent.setValue(20)
        self.spin_percent.setStyleSheet("QSpinBox { background: #173646; color: #E6EEF3; border-radius:6px; }")
        info_layout.addWidget(QLabel("Bonecos (extra):"), 0, 0)
        info_layout.addWidget(self.spin_bonecos, 0, 1)
        info_layout.addWidget(QLabel("Dinheiro Sujo (manual):"), 1, 0)
        info_layout.addWidget(self.spin_dinheiro, 1, 1)
        info_layout.addWidget(QLabel("Taxa de lavagem (% retirada):"), 2, 0)
        info_layout.addWidget(self.spin_percent, 2, 1)
        group_info.setLayout(info_layout)
        central_layout.addWidget(group_info, stretch=1)

        layout.addLayout(central_layout)

        # Divider
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet("color: #29509c;")
        layout.addWidget(divider)

        # Botão calcular
        botao_calc = QPushButton("Calcular")
        botao_calc.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #1e5c7a, stop:1 #24a37b);
                color: white; font-weight:700; padding:10px 18px; border-radius:10px; font-size:16px;
            }
        """)
        botao_calc.clicked.connect(self.calcular)
        layout.addWidget(botao_calc)

        # Resultado (QTextEdit, scrollável)
        self.result_txt = QTextEdit()
        self.result_txt.setReadOnly(True)
        self.result_txt.setMinimumHeight(160)
        self.result_txt.setStyleSheet("""
            QTextEdit { background: #122025; color: #E6EEF3; border: 1px solid #29509c; border-radius:10px;
                       font-family: 'Segoe UI', sans-serif; font-size:15px; padding:14px; }
        """)
        layout.addWidget(self.result_txt)

        self.setLayout(layout)

    def calcular(self):
        meta = self.spin_meta.value()
        coca = self.spin_coca.value()
        erva = self.spin_erva.value()
        bonecos = self.spin_bonecos.value()
        dinheiro_manual = self.spin_dinheiro.value()
        percentagem = self.spin_percent.value()

        bonecos_droga = (meta // 100) + (coca // 100) + (erva // 100)
        bonecos_total = bonecos + bonecos_droga
        dinheiro_sujo = bonecos_total * 32000
        dinheiro_sujo_final = dinheiro_manual if dinheiro_manual > 0 else dinheiro_sujo
        dinheiro_limpo = dinheiro_sujo_final * ((100 - percentagem) / 100)

        linhas = []
        linhas.append(f"<b>Bonecos por drogas:</b> <span style='color:#41bbee'>{bonecos_droga}</span>")
        linhas.append(f"<b>Bonecos manuais:</b> <span style='color:#41bbee'>{bonecos}</span>")
        linhas.append(f"<b>Total de bonecos:</b> <span style='color:#cfd724'>{bonecos_total}</span>")
        linhas.append("<hr>")
        if dinheiro_manual > 0:
            linhas.append(f"<b>Dinheiro sujo (manual):</b> <span style='color:#ed9448'>€ {dinheiro_manual:,.0f}</span>")
        else:
            linhas.append(f"<b>Dinheiro sujo:</b> <span style='color:#ed9448'>€ {dinheiro_sujo:,.0f}</span>")
        linhas.append(f"<b>Taxa de lavagem retirada:</b> <span style='color:#bb3a39'>{percentagem}%</span>")
        linhas.append("<b>Dinheiro limpo após lavagem:</b>")
        linhas.append(f"<span style='color:#43c87a; font-size:20px; font-weight:700'>€ {dinheiro_limpo:,.2f}</span>")

        self.result_txt.setHtml("<br>".join(linhas))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraDroga()
    window.show()
    sys.exit(app.exec())