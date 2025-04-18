#Tạo giao diện cho project
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit, QFileDialog
)
from PyQt6.QtCore import Qt, pyqtSignal
import core

# Thành phần GUI cho việc kéo và thả file
# Kế thừa từ QLabel để tạo vùng kéo và thả
class DropArea(QLabel):
    fileDropped = pyqtSignal(str)

# hàm khởi tạo của DropArea
# Đặt các thuộc tính cho vùng kéo và thả
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setText("Drag and drop memory dump file here")
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;
                border-radius: 10px;
                padding: 50px;
                color: #555;
            }
        """)

# hàm xử lý sự kiện kéo và thả file
# Nếu file được kéo vào là file hợp lệ thì chấp nhận sự kiện
# Nếu không thì từ chối sự kiện
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

# hàm xử lý sự kiện thả file
# Lấy đường dẫn file từ sự kiện và phát tín hiệu fileDropped với đường dẫn file
# Cập nhật văn bản hiển thị trong vùng kéo và thả với đường dẫn file đã thả
    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.setText(f"Loaded file:\n{file_path}")
        self.fileDropped.emit(file_path)

# Thành phần GUI chính của project
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.memory_dump = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Memory Analyzer')
        self.setGeometry(100, 100, 800, 600)

        self.drop_area = DropArea()
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        
        # tạo các nút bấm
        self.pslist_btn = QPushButton('Run pslist', clicked=self.run_pslist)
        self.pstree_btn = QPushButton('Run pstree', clicked=self.run_pstree)
        self.cmdline_btn = QPushButton('Run cmdline', clicked=self.run_cmdline)
        self.malfind_btn = QPushButton('Run malfind', clicked=self.run_malfind)
        self.export_btn = QPushButton('Export to CSV', clicked=self.export_csv)
        exit_btn = QPushButton('Exit', clicked=self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.drop_area)
        layout.addWidget(self.output_area)
        
        # tạo layout cho các nút bấm
        # Sử dụng QVBoxLayout để sắp xếp các nút bấm theo cột dọc
        btn_layout = QVBoxLayout()
        
        # tạo hàng đầu tiên với pslist và pstree
        top_row = QHBoxLayout()
        top_row.addWidget(self.pslist_btn)
        top_row.addWidget(self.pstree_btn)
        btn_layout.addLayout(top_row)
        
        # tạo hàng thứ hai với cmdline và malfind
        bottom_row = QHBoxLayout()
        bottom_row.addWidget(self.cmdline_btn)
        bottom_row.addWidget(self.malfind_btn)
        btn_layout.addLayout(bottom_row)
        
        # thêm nút export và exit vào hàng riêng
        export_exit_row = QHBoxLayout()
        export_exit_row.addWidget(self.export_btn)
        export_exit_row.addWidget(exit_btn)
        btn_layout.addLayout(export_exit_row)
        
        layout.addLayout(btn_layout)
        
        # thêm các nút bấm vào layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Kết nối tín hiệu từ vùng kéo và thả với hàm xử lý sự kiện
        # Khi file được thả vào vùng kéo và thả, hàm set_memory_dump sẽ được gọi
        self.drop_area.fileDropped.connect(self.set_memory_dump)

    # hàm xử lý sự kiện khi file được thả vào vùng kéo và thả
    # Lưu đường dẫn file vào biến memory_dump và xóa nội dung trong vùng hiển thị kết quả
    def set_memory_dump(self, path):
        self.memory_dump = path
        self.output_area.clear()

    # hàm xử lý sự kiện khi nút Run pslist được nhấn
    # Kiểm tra xem đã có file nào được thả vào vùng kéo và thả chưa
    def run_pslist(self):
        if not self.memory_dump:
            self.output_area.setText("Error: No memory dump loaded!")
            return

        output = core.run_pslist(self.memory_dump)
        self.output_area.setText(output)

    # xử lý sự kiện khi nút Run pstree được nhấn
    # Kiểm tra xem đã có file nào được thả vào vùng kéo và thả chưa
    def run_pstree(self):
        if not self.memory_dump:
            self.output_area.setText("Error: No memory dump loaded!")
            return

        output = core.run_pstree(self.memory_dump)
        self.output_area.setText(output)

    # hàm xử lý sự kiện khi nút Run cmdline được nhấn
    # Kiểm tra xem đã có file nào được thả vào vùng kéo và thả chưa
    def run_cmdline(self):
        if not self.memory_dump:
            self.output_area.setText("Error: No memory dump loaded!")
            return

        output = core.run_cmdline(self.memory_dump)
        self.output_area.setText(output)
    
    # hàm xử lý sự kiện khi nút Run malfind được nhấn
    # Kiểm tra xem đã có file nào được thả vào vùng kéo và thả chưa
    # Nếu có thì gọi hàm run_malfind từ core.py để thực hiện phân tích
    def run_malfind(self):
        if not self.memory_dump:
            self.output_area.setText("Error: No memory dump loaded!")
            return

        output = core.run_malfind(self.memory_dump)
        self.output_area.setText(output)

    # hàm xử lý sự kiện khi nút Export to CSV được nhấn
    # Kiểm tra xem có nội dung nào trong vùng hiển thị kết quả không
    def export_csv(self):
        output_text = self.output_area.toPlainText()
        if not output_text:
            return
            
        path, _ = QFileDialog.getSaveFileName(
            self, 
            "Save CSV", 
            "", 
            "CSV Files (*.csv)"
        )
        
        if path:
            error = core.export_csv(output_text, path)
            if error:
                self.output_area.append(f"\n\n{error}")
            else:
                self.output_area.append(f"\n\nCSV exported to: {path}")