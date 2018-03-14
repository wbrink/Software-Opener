from PyQt5.QtWidgets import QApplication, QWidget
import sys
from design import Ui_Form
import threading
import subprocess
from software_dict import software_dict


class Opener(QWidget, Ui_Form):
    def __init__(self):
        super(Opener, self).__init__()

        # set up the user interface from designer
        self.setupUi(self)

        #connect the buttons
        self.open_button.clicked.connect(self.open_click)
        self.search_button.clicked.connect(self.search_click)
        self.upc_line_edit.returnPressed.connect(self.search_button.click)

    #implementing the buttons
    def search_click(self):
        upc = self.upc_line_edit.text()
        if upc in software_dict.keys():
            self.software_label.setText(list(software_dict[upc].keys())[0])
        else:
            self.software_label.setText("(No software with this code)")

    def open_click(self):
        def callback():
            upc = self.upc_line_edit.text()
            if upc in software_dict.keys():
                process = subprocess.run(list(software_dict[upc].values())[0])
            else:
                self.software_label.setText("(Please Enter Valid Code)")
        t = threading.Thread(target=callback)
        t.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Opener()
    form.show()
    sys.exit(app.exec_())
