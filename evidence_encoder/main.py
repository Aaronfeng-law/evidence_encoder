import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog,
    QComboBox, QLineEdit, QCheckBox, QMessageBox, QListWidget, QListWidgetItem, QGroupBox
)
from core import process_pdf, evidence_options
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("證據編號工具")
        self.resize(700, 400)
        main_layout = QHBoxLayout()
        # 左側：檔案清單
        self.file_list = QListWidget()
        self.file_list.currentRowChanged.connect(self.load_file_settings)
        main_layout.addWidget(self.file_list, 2)

        # 右側：設定區
        right_layout = QVBoxLayout()
        self.add_file_btn = QPushButton("選擇 PDF 檔案")
        self.add_file_btn.clicked.connect(self.choose_file)
        right_layout.addWidget(self.add_file_btn)

        # 設定表單
        right_layout.addWidget(QLabel("選擇證據類型："))
        self.combo = QComboBox()
        for k, v in evidence_options.items():
            self.combo.addItem(f"{v} ({k})", k)
        right_layout.addWidget(self.combo)

        right_layout.addWidget(QLabel("自訂文字（僅選擇自訂時填寫）："))
        self.custom_text = QLineEdit()
        right_layout.addWidget(self.custom_text)

        right_layout.addWidget(QLabel("證據編號："))
        self.number_edit = QLineEdit("1")
        right_layout.addWidget(self.number_edit)

        self.need_number = QCheckBox("加上「號」")
        self.need_number.setChecked(True)
        right_layout.addWidget(self.need_number)

        self.advanced_checkbox = QCheckBox("進階設定：自訂標籤插入位置")
        self.advanced_checkbox.setChecked(False)
        self.advanced_checkbox.stateChanged.connect(self.toggle_advanced)
        right_layout.addWidget(self.advanced_checkbox)

        self.advanced_group = QGroupBox()
        adv_layout = QVBoxLayout()
        adv_layout.addWidget(QLabel("X 座標（預設570）"))
        self.x_edit = QLineEdit("570")
        adv_layout.addWidget(self.x_edit)
        adv_layout.addWidget(QLabel("Y 座標（預設25）"))
        self.y_edit = QLineEdit("25")
        adv_layout.addWidget(self.y_edit)
        self.advanced_group.setLayout(adv_layout)
        self.advanced_group.setVisible(False)
        right_layout.addWidget(self.advanced_group)

        right_layout.addWidget(QLabel("字體大小（預設16）："))
        self.font_size_edit = QLineEdit("16")
        right_layout.addWidget(self.font_size_edit)

        self.save_btn = QPushButton("儲存本檔案設定")
        self.save_btn.clicked.connect(self.save_file_settings)
        right_layout.addWidget(self.save_btn)

        self.process_btn = QPushButton("批次處理所有檔案")
        self.process_btn.clicked.connect(self.process_all_files)
        right_layout.addWidget(self.process_btn)

        self.status_label = QLabel("")
        right_layout.addWidget(self.status_label)

        main_layout.addLayout(right_layout, 3)
        self.setLayout(main_layout)

        # 記錄每個檔案的設定
        self.file_settings = {}


        self.combo.currentIndexChanged.connect(self.mark_unsaved)
        self.custom_text.textChanged.connect(self.mark_unsaved)
        self.number_edit.textChanged.connect(self.mark_unsaved)
        self.need_number.stateChanged.connect(self.mark_unsaved)
        self.font_size_edit.textChanged.connect(self.mark_unsaved)
        self.x_edit.textChanged.connect(self.mark_unsaved)
        self.y_edit.textChanged.connect(self.mark_unsaved)
        self.advanced_checkbox.stateChanged.connect(self.mark_unsaved)

    def choose_file(self):
        files, _ = QFileDialog.getOpenFileNames(self, "選擇 PDF 檔案", "", "PDF Files (*.pdf)")
        for f in files:
            basename = os.path.basename(f)
            if basename not in self.file_settings:
                self.file_list.addItem(basename)
                self.file_settings[basename] = {
                    "path": f,  # 存完整路徑
                    "evidence_type": self.combo.currentData(),
                    "custom_text": "",
                    "evidence_number": "1",
                    "need_number": True,
                    "font_size": 16,
                    "x": 570,
                    "y": 25,
                }

    def load_file_settings(self, row):
        if row < 0:
            return
        basename = self.file_list.item(row).text().rstrip(" *")
        setting = self.file_settings[basename]
        idx = self.combo.findData(setting["evidence_type"])
        self.combo.setCurrentIndex(idx if idx >= 0 else 0)
        self.custom_text.setText(setting["custom_text"])
        self.number_edit.setText(setting["evidence_number"])
        self.need_number.setChecked(setting["need_number"])
        self.font_size_edit.setText(str(setting["font_size"]))
        self.x_edit.setText(str(setting["x"]))
        self.y_edit.setText(str(setting["y"]))
        self.advanced_checkbox.setChecked(setting["x"] != 570 or setting["y"] != 25)

    def save_file_settings(self):
        row = self.file_list.currentRow()
        if row < 0:
            return
        file = self.file_list.item(row).text().rstrip(" *")
        # 取得原本的 path
        old_path = self.file_settings[file].get("path", "")
        self.file_settings[file] = {
            "path": old_path,  # 保留完整路徑
            "evidence_type": self.combo.currentData(),
            "custom_text": self.custom_text.text(),
            "evidence_number": self.number_edit.text() or "1",
            "need_number": self.need_number.isChecked(),
            "font_size": int(self.font_size_edit.text() or "16"),
            "x": float(self.x_edit.text() or "570"),
            "y": float(self.y_edit.text() or "25"),
        }
        self.status_label.setText(f"已儲存設定：{os.path.basename(file)}")
        # 移除星號
        self.file_list.item(row).setText(file)

    def toggle_advanced(self, state):
        self.advanced_group.setVisible(state == 2)

    def process_all_files(self):
        from main import process_pdf
        results = []
        for i in range(self.file_list.count()):
            basename = self.file_list.item(i).text().rstrip(" *")
            setting = self.file_settings[basename]
            file_path = setting["path"]  # 用完整路徑
            try:
                output_pdf = process_pdf(
                    pdf_file=file_path,
                    evidence_type=setting["evidence_type"],
                    evidence_number=setting["evidence_number"],
                    need_number=setting["need_number"],
                    custom_text=setting["custom_text"],
                    font_size=setting["font_size"],
                    output_dir="output",
                    x=setting["x"],
                    y=setting["y"]
                )
                results.append(output_pdf)
            except Exception as e:
                QMessageBox.critical(self, "錯誤", f"{basename} 處理失敗：{e}")
        QMessageBox.information(self, "完成", f"已處理 {len(results)} 個檔案！\n輸出資料夾：output")

    def mark_unsaved(self):
        row = self.file_list.currentRow()
        if row < 0:
            return
        item = self.file_list.item(row)
        text = item.text()
        if not text.endswith(" *"):
            item.setText(text + " *")
        self.status_label.setText("尚未儲存設定：" + os.path.basename(self.file_list.item(row).text().rstrip(" *")))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())