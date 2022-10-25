import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QDialog, QMessageBox
import mainwindow
import att
# import att_ctrl
import qdarkstyle
from qt_material import apply_stylesheet

import rename


class MainWindow_ctrl(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, MainWindow):
        super(MainWindow_ctrl, self).__init__()
        super().setupUi(MainWindow)

        self.start_mum = 1
        self.img_dir = ''
        self.label_dir = ''
        self.save_dir = ''
        self.img_suffix = self.img_format_box.currentText()
        self.label_suffix = self.label_format_box.currentText()

        self.init_dir = 'D://'

        self.img_dir_input_botton.clicked.connect(lambda: self.choose_img_dir())
        self.label_dir_input_botton.clicked.connect(lambda: self.choose_label_dir())
        self.save_dir_input_botton.clicked.connect(lambda: self.choose_save_dir())

        self.do_botton.clicked.connect(lambda: self.start())

    def choose_img_dir(self):
        self.img_dir = QFileDialog.getExistingDirectory(self, "选择图片文件夹", self.init_dir)
        self.init_dir = self.img_dir
        self.img_dir_input_edit.setText(self.img_dir)

    def choose_label_dir(self):
        self.label_dir = QFileDialog.getExistingDirectory(self, "选择标签文件夹", self.init_dir)
        self.init_dir = self.label_dir
        self.label_dir_input_edit.setText(self.label_dir)

    def choose_save_dir(self):
        self.save_dir = QFileDialog.getExistingDirectory(self, "选择保存文件夹", self.init_dir)
        self.init_dir = self.save_dir
        self.save_dir_input_edit.setText(self.save_dir)

    def start(self):
        self.img_suffix = self.img_format_box.currentText()
        self.label_suffix = self.label_format_box.currentText()

        att_window = Att_ctrl(self.save_dir, self.img_dir, self.label_dir, self.img_suffix, self.label_suffix,
                              self.start_mum)
        # print(img_format)

        att_window.show()
        # att_window.get_data()
        # self.start_rename()
        # sys.exit(app.exec_())


class Att_ctrl(QWidget, att.Ui_Form):
    def __init__(self, save_dir, img_dir, label_dir, img_suffix, label_suffix, start_num):
        super(Att_ctrl, self).__init__()
        self.setupUi(self)

        self.save_dir = save_dir
        self.img_dir = img_dir
        self.label_dir = label_dir
        self.img_suffix = img_suffix
        self.label_suffix = label_suffix
        self.start_num = start_num

        self.img_dir_att.setText(f"图片文件夹: {img_dir}")
        self.label_dir_att.setText(f"标签文件夹: {label_dir}")
        self.save_dir_att.setText(f"保存文件夹: {save_dir}")

        self.confirm.clicked.connect(lambda: self.just_do())
        self.dont.clicked.connect(lambda: self.close())

    def just_do(self):
        self.close()
        # print(self.label_suffix)
        # print(self.img_suffix)
        # print("2")
        rename_return = rename.replace(self.img_dir, self.label_dir, self.save_dir, self.img_suffix, self.label_suffix,
                                       self.start_num)
        if rename_return == 1:
            QMessageBox.information(self, "成功", f"文件已保存至{self.save_dir}/the_new_")

    # def get_data():


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_window = QMainWindow()
    # apply_stylesheet(app, theme="dark_amber.xml")
    ui = MainWindow_ctrl(main_window)
    main_window.show()
    sys.exit(app.exec_())
