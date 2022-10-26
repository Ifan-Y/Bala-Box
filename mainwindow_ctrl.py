import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QDialog, QMessageBox
import mainwindow
import att
# import att_ctrl
import qdarkstyle
from qt_material import apply_stylesheet
import os
import shutil


# import rename


class MainWindow_ctrl(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, MainWindow):
        super(MainWindow_ctrl, self).__init__()
        super().setupUi(MainWindow)

        self.start_num = 1
        self.img_dir = ''
        self.label_dir = ''
        self.save_dir = ''
        self.img_suffix = self.img_format_box.currentText()
        self.label_suffix = self.label_format_box.currentText()
        self.start_name = ''
        self.rename_progress_bar.reset()

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
        if self.save_dir == '':
            QMessageBox.information(self, "错误", "未选择保存文件夹")
            return
        elif self.img_dir == '':
            QMessageBox.information(self, "错误", "未选择图片文件夹")
            return
        elif self.label_dir == '':
            QMessageBox.information(self, "错误", "未选择标签文件夹")
            return

        self.img_suffix = self.img_format_box.currentText()
        self.label_suffix = self.label_format_box.currentText()
        self.start_num = self.start_num_box.value()
        self.start_name = self.start_name_edit.text()

        result = QMessageBox.information(self, "提示",
                                         f"保存文件夹: {self.save_dir}\n\n图片文件夹: {self.img_dir}\n\n标签文件夹: {self.label_dir}\n"
                                         f"\n图片格式： {self.img_suffix}\t标签格式： {self.label_suffix}"
                                         f"\n\n确定执行？？？",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            self.replace()

    def replace(self):
        save_dir_name = 'the_new'
        img_names = []
        # 拓展名不同的文件
        label_names = []
        other_img_names = []
        other_label_names = []
        for img_file in os.listdir(self.img_dir):
            img_file_path = os.path.join(self.img_dir, img_file)
            if not os.path.isdir(img_file_path):
                if os.path.splitext(img_file_path)[1] == self.img_suffix:
                    img_names.append(os.path.splitext(img_file)[0])
                else:
                    other_img_names.append(img_file)

        for file in os.listdir(self.label_dir):
            label_file_dir = os.path.join(self.label_dir, file)
            if not os.path.isdir(label_file_dir):
                if os.path.splitext(file)[1] == self.label_suffix:
                    label_names.append(os.path.splitext(file)[0])
                else:
                    other_label_names.append(file)

        # 取出共同元素
        img_names_set = set(img_names)
        label_names_set = set(label_names)
        same_names_set = img_names_set & label_names_set
        same_names = list(same_names_set)
        other_labels = list(label_names_set - same_names_set)
        other_imgs = list(img_names_set - same_names_set)

        same_names_num = len(same_names)
        self.rename_progress_bar.setRange(0, same_names_num + 1)

        while os.path.exists(f"{self.save_dir}\\{save_dir_name}"):
            save_dir_name += '1'
        os.mkdir(f"{self.save_dir}\\{save_dir_name}")
        os.mkdir(f"{self.save_dir}\\{save_dir_name}\\imgs")
        os.mkdir(f"{self.save_dir}\\{save_dir_name}\\labels")

        rename_file_num = 0

        for name in same_names:
            img_act_path = f"{self.img_dir}\\{name}{self.img_suffix}"
            label_act_path = f"{self.label_dir}\\{name}{self.label_suffix}"
            img_final_path = f"{self.save_dir}\\{save_dir_name}\\imgs\\{self.start_name}{self.start_num}{self.img_suffix}"
            label_final_path = f"{self.save_dir}\\{save_dir_name}\\labels\\{self.start_name}{self.start_num}{self.label_suffix}"

            shutil.copyfile(img_act_path, img_final_path)
            shutil.copyfile(label_act_path, label_final_path)

            self.start_num += 1
            rename_file_num += 1
            self.rename_progress_bar.setValue(rename_file_num)

        other_dir_name = f'{save_dir_name}\\Error'
        # while os.path.exists(f"{self.save_dir}\\{other_dir_name}"):
        #     other_dir_name += '1'
        os.mkdir(f"{self.save_dir}\\{other_dir_name}")
        if other_imgs:
            os.mkdir(f"{self.save_dir}\\{other_dir_name}\\img_single_error")
            for other_img in other_imgs:
                img_act_path = f"{self.img_dir}\\{other_img}{self.img_suffix}"
                img_final_path = f"{self.save_dir}\\{other_dir_name}\\img_single_error\\{other_img}{self.img_suffix}"
                shutil.copyfile(img_act_path, img_final_path)
        if other_labels:
            os.mkdir(f"{self.save_dir}\\{other_dir_name}\\label_single_error")
            for other_label in other_labels:
                label_act_path = f"{self.label_dir}\\{other_label}{self.label_suffix}"
                label_final_path = f"{self.save_dir}\\{other_dir_name}\\label_single_error\\{other_label}" \
                                   f"{self.label_suffix} "
                shutil.copyfile(label_act_path, label_final_path)
        if other_img_names:
            os.mkdir(f"{self.save_dir}\\{other_dir_name}\\img_suffix_error")
            for other_img in other_img_names:
                img_act_path = f"{self.img_dir}\\{other_img}"
                img_final_path = f"{self.save_dir}\\{other_dir_name}\\img_suffix_error\\{other_img}"
                shutil.copyfile(img_act_path, img_final_path)
        if other_label_names:
            os.mkdir(f"{self.save_dir}\\{other_dir_name}\\label_suffix_error")
            for other_label in other_label_names:
                img_act_path = f"{self.label_dir}\\{other_label}"
                img_final_path = f"{self.save_dir}\\{other_dir_name}\\label_suffix_error\\{other_label}"
                shutil.copyfile(img_act_path, img_final_path)

        self.rename_progress_bar.setValue(same_names_num+1)

        QMessageBox.information(self, "成功",
                                f"文件已保存至{self.save_dir}/{save_dir_name}\n\n已成功重命名{rename_file_num}个文件")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_window = QMainWindow()
    # apply_stylesheet(app, theme="dark_amber.xml")
    ui = MainWindow_ctrl(main_window)
    main_window.show()
    sys.exit(app.exec_())
