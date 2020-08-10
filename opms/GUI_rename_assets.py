import unreal
import sys
sys.path.append("C:\Python27\Lib\site-packages")

from PySide import QtCore, QtGui, QtUiTools


def rename_assets(search_pattern, replace_pattern, use_case):
    # instances of unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    # get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log("Selected {} assets".format(num_assets))

    # loop over each asset and rename
    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)
        unreal.log(asset_name)

        # check if the asset name contains the to be replaced text
        if string_lib.contains(asset_name, search_pattern, use_case = use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            replaced_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case = search_case)
            editor_util.rename_asset(asset, replaced_name)

            replaced += 1
            unreal.log("Replaced {} with {}".format(asset_name, replaced_name))

        else:
            unreal.log("{} did not match the search pattern, was skipped".format(asset_name))

    unreal.log("Replaced {} of {} assets".format(replaced, num_assets))

class RenameGUI(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RenameGUI, self).__init__(parent)

        # load the created GUI
        self.widget = QtUiTools.QUiLoader().load("H:\\EpicGames\\UE4PythonToolPack\\GUI\\AssetRenamer.ui")
        self.widget.setParent(self)

        # set the size of widget
        self.widget.setGeometry(0, 0, self.widget.width(), self.widget.height())

        # find the interaction elements
        self.search = self.widget.findChild(QtGui.QLineEdit, "searchPattern")
        self.replace = self.widget.findChild(QtGui.QLineEdit, "replacePattern")

        self.use_case = self.widget.findChild(QtGui.QCheckBox, "checkBox")

        # find and assign trigger to pushButton
        self.rename_button = self.widget.findChild(QtGui.QPushButton, "pushButton")
        self.rename_button.clicked.connect(self.rename_handler)

    def rename_handler(self):
        search_pattern = self.search.text()
        replace_pattern = self.replace.text()
        use_case = self.use_case.isChecked()
        
        rename_assets(search_pattern, replace_pattern, use_case)

# only create an instance when it is not already running
app = None
if not QtGui.QApplication.instance():
    app = QtGui.QApplication(sys.argv)

# start the GUI
window = RenameGUI()
window.show()
