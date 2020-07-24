import unreal
import sys
sys.path.append("C:\\Python27\\Lib\\site-packages")

from PySide import QtCore, QtGui, QtUiTools

editor_level_lib = unreal.EditorLevelLibrary()

class SimpleGUI(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SimpleGUI, self).__init__(parent)

        #load the created ui widget
        self.widget = QtUiTools.QUiLoader().load("H:\\EpicGames\\UE4PythonToolPack\\GUI\\form.ui")

        # attach the widget to the "self" GUI
        self.widget.setParent(self)

        # set the UI geometry (if UI is not centered/visible)
        self.widget.setGeometry(0, 0, self.widget.width(), self.widget.height())

        self.text_l = self.widget.findChild(QtGui.QLineEdit, "TextBox_L")
        self.text_r = self.widget.findChild(QtGui.QLineEdit, "TextBox_R")
        self.checkbox = self.widget.findChild(QtGui.QCheckBox, "CheckBox")

        #find and assign slider
        self.slider = self.widget.findChild(QtGui.QSlider, "horizontalSlider")
        self.slider.sliderMoved.connect(self.on_slide)

        # find buttons and set up handlers
        self.btn_ok = self.widget.findChild(QtGui.QPushButton, "okButton")
        self.btn_ok.clicked.connect(self.ok_clicked)
        self.btn_cancel = self.widget.findChild(QtGui.QPushButton, "cancelButton")
        self.btn_cancel.clicked.connect(self.cancel_clicked)

    # triggered on clicked of okButton
    def ok_clicked(self):
        text_l = self.text_l.text()
        text_r = self.text_r.text()
        is_checked = self.checkbox.isChecked()

        unreal.log("Text Left Value: {}".format(text_l))
        unreal.log("Text Right Value: {}".format(text_r))
        unreal.log("CheckBox Value: {}".format(is_checked))

    def cancel_clicked(self):
        unreal.log("Canceled")
        self.close()

    def on_slide(self):
        slider_value = self.slider.value()

        # move the selected actor according to the slider value
        selected_actors = editor_level_lib.get_selected_level_actors()

        if len(selected_actors) > 0:
            actor = selected_actors[0]

            #get old trensform, change y axis value and write back
            new_transform = actor.get_actor_transform()
            new_transform.translation.y = slider_value

            actor.set_actor_transform(new_transform, True, True)

# only created an instance of the GUI when it's not already running
app = None
if not QtGui.QApplication.instance():
    app = QtGui.QApplication(sys.argv)

# start the GUI
main_window = SimpleGUI()
main_window.show()