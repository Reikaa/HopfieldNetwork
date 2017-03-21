#####################
# View\view.py #
#####################
from PyQt5 import QtGui, QtWidgets, QtCore


class MainView(QtWidgets.QMainWindow):

    #### properties for widget value ####
    @property
    def pushButton(self):
        return self.ui.pushButton.isChecked()
    @pushButton.setter
    def pushButton(self, value):
        self.ui.pushButton.setChecked(value)
    @property
    def pushButton_2(self):
        return self.ui.pushButton_2.isChecked()
    @pushButton_2.setter
    def pushButton_2(self, value):
        self.ui.pushButton_2.setChecked(value)
    @property
    def pushButton_3(self):
        return self.ui.pushButton_3.isChecked()
    @pushButton_3.setter
    def pushButton_3(self, value):
        self.ui.pushButton_3.setChecked(value)
    @property
    def pushButton_4(self):
        return self.ui.pushButton_4.isChecked()
    @pushButton_4.setter
    def pushButton_4(self, value):
        self.ui.pushButton_4.setChecked(value)
    @property
    def pushButton_5(self):
        return self.ui.pushButton_5.isChecked()
    @pushButton_5.setter
    def pushButton_4(self, value):
        self.ui.pushButton_5.setChecked(value)
    @property
    def checkBox(self):
        return self.ui.checkBox.isChecked()
    @checkBox.setter
    def checkBox(self, value):
        self.ui.checkBox.setChecked(value)
    @property
    def label(self):
        return self.ui.label.text()
    @label.setter
    def label(self, value):
        self.ui.label.setText(value)
    @property
    def label_2(self):
        return self.ui.label_2.text()
    @label_2.setter
    def label_2(self, value):
        self.ui.label_2.setText(value)
    @property
    def epochs(self):
        return self.ui.epochs.value()
    @epochs.setter
    def epochs(self, value):
        self.ui.epochs.setValue(value)
    @property
    def comboBox(self):
        return self.ui.comboBox.currentIndex()
    @comboBox.setter
    def comboBox(self, value):
        self.ui.comboBox.setCurrentIndex(value)
    @property
    def comboBox_2(self):
        return self.ui.comboBox_2.currentIndex()
    @comboBox.setter
    def comboBox_2(self, value):
        self.ui.comboBox_2.setCurrentIndex(value)

    #### properties for widget enabled state ####
    @property
    def pushButton_enabled(self):
        return self.ui.pushButton.isEnabled()
    @pushButton_enabled.setter
    def pushButton_enabled(self, value):
        self.ui.pushButton.setEnabled(value)
    @property
    def pushButton_2_enabled(self):
        return self.ui.pushButton_2.isEnabled()
    @pushButton_2_enabled.setter
    def pushButton_2_enabled(self, value):
        self.ui.pushButton_2.setEnabled(value)
    @property
    def pushButton_3_enabled(self):
        return self.ui.pushButton_3.isEnabled()
    @pushButton_3_enabled.setter
    def pushButton_3_enabled(self, value):
        self.ui.pushButton_3.setEnabled(value)
    @property
    def checkBox_enabled(self):
        return self.ui.checkBox.isEnabled()
    @checkBox_enabled.setter
    def checkBox_enabled(self, value):
        self.ui.checkBox.setEnabled(value)
    @property
    def label_enabled(self):
        return self.ui.label.isEnabled()
    @label_enabled.setter
    def label_enabled(self, value):
        self.ui.label.setEnabled(value)
    @property
    def label_2_enabled(self):
        return self.ui.label_label_2.isEnabled()
    @label_2_enabled.setter
    def label_2_enabled(self, value):
        self.ui.label_2.setEnabled(value)
    @property
    def epochs_enabled(self):
        return self.ui.epochs.isEnabled()
    @epochs_enabled.setter
    def epochs_enabled(self, value):
        self.ui.epochs.setEnabled(value)
    @property
    def comboBox_enabled(self):
        return self.ui.comboBox.isEnabled()
    @comboBox_enabled.setter
    def comboBox_enabled(self, value):
        self.ui.comboBox.setEnabled(value)
    @property
    def comboBox_2_enabled(self):
        return self.ui.comboBox_2.isEnabled()
    @comboBox_enabled.setter
    def comboBox_2_enabled(self, value):
        self.ui.comboBox_2.setEnabled(value)
    @property
    def comboBox_3_enabled(self):
        return self.ui.comboBox_3.isEnabled()
    @comboBox_enabled.setter
    def comboBox_3_enabled(self, value):
        self.ui.comboBox_3.setEnabled(value)
    
    def __init__(self, model, main_ctrl, Ui_MainView):
        self.model = model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.build_ui(Ui_MainView)
        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

    def build_ui(self, Ui_MainView):
        self.ui = Ui_MainView()
        self.ui.setupUi(self)
        
        #### set Qt model for compatible widget types ####
        # self.ui.comboBox.setModel(self.model.comboBox_model)

        #### connect widget signals to event functions ####
        self.ui.pushButton.clicked.connect(self.on_pushButton)
        self.ui.pushButton_2.clicked.connect(self.on_pushButton_2)
        self.ui.pushButton_3.clicked.connect(self.on_pushButton_3)
        self.ui.pushButton_4.clicked.connect(self.on_pushButton_4)
        self.ui.pushButton_5.clicked.connect(self.on_pushButton_5)
        self.ui.checkBox.stateChanged.connect(self.on_checkBox)
        self.ui.epochs.valueChanged.connect(self.on_epochs)
        self.ui.comboBox.currentIndexChanged.connect(self.on_comboBox)
        self.ui.comboBox_2.currentIndexChanged.connect(self.on_comboBox_2)
        self.ui.comboBox_3.currentIndexChanged.connect(self.on_comboBox_3)


    def update_ui_from_model(self):
        print('DEBUG: update_ui_from_model called')
        #### update widget values from model ####
        self.ui.gridLayout = self.model.gridLayout
        self.ui.gridLayoutWidget.setVisible(False)
        self.ui.gridLayoutWidget = self.model.gridLayoutWidget
        self.ui.gridLayoutWidget.setParent(self)
        self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(19, 79, 1040, 600))
        self.ui.gridLayoutWidget.update()
        self.ui.gridLayoutWidget.show()
        if self.model.gridLayoutWidget_2: self.show_learned_patterns()
        if self.model.nb_pattern_to_present: self.update_unlearn_comboBox()
    
    def update_unlearn_comboBox(self):
        self.ui.comboBox_3.clear()
        for itm in range(self.model.nb_pattern_to_present):
            self.ui.comboBox_3.addItem("")
            self.ui.comboBox_3.setItemText(itm, "Pattern " + str(itm))

    def show_learned_patterns(self):
        self.ui.gridLayoutWidget_2 = self.model.gridLayoutWidget_2
        self.ui.gridLayout_2 = self.model.gridLayout_2
        self.ui.gridLayoutWidget_2.setWindowTitle("Learned patterns")
        self.ui.gridLayoutWidget_2.show()

    #### widget signal event functions ####
    def on_pushButton(self): self.main_ctrl.change_pushButton(self.pushButton)
    def on_pushButton_2(self): self.main_ctrl.change_pushButton_2(self.pushButton_2)
    def on_pushButton_3(self): self.main_ctrl.change_pushButton_3(self.pushButton_3)
    def on_pushButton_4(self): self.main_ctrl.change_pushButton_4(self.pushButton_4)
    def on_pushButton_5(self): self.main_ctrl.change_pushButton_5(self.pushButton_5)
    def on_checkBox(self, state): self.main_ctrl.change_checkBox(state)
    def on_epochs(self, value): self.main_ctrl.change_epochs(value)
    def on_comboBox(self, index): self.main_ctrl.change_comboBox(index)
    def on_comboBox_2(self, index): self.main_ctrl.change_comboBox_2(index)
    def on_comboBox_3(self, index): self.main_ctrl.change_comboBox_3(index)
