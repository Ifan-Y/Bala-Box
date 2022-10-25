import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
import att


class Att_ctrl(QWidget, att.Ui_Form):
    def __init__(self, Ui_Form):
        super(Att_ctrl, self).__init__()
        super().setupUi(Ui_Form)
        # self.show


if __name__ == "__main__":
# def do_att():
    app = QApplication(sys.argv)
    main_window = QWidget()
    ui = Att_ctrl(main_window)
    main_window.show()
    sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     qpp = QApplication(sys.argv)
#     ui = Att_ctrl(QMainWindow)
#     ui.show()
#     sys.exit(qpp.exec_())

