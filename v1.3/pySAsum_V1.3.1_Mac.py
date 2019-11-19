from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy, h5py, os, sys

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# Interface
class Ui_MainWindow(QtGui.QMainWindow):

    def __create_element(self, object, geometry, object_name, text=None, font=None, placeholder=None, visible=None, stylesheet=None, checked=None, checkable=None, title=None, combo=None, enabled=None):
        object.setObjectName(object_name)

        if not geometry == [999, 999, 999, 999]:
            object.setGeometry(QtCore.QRect(geometry[0], geometry[1], geometry[2], geometry[3]))

        if not text == None: object.setText(text)
        if not title == None: object.setTitle(title)
        if not font == None: object.setFont(font)
        if not placeholder == None: object.setPlaceholderText(placeholder)
        if not visible == None: object.setVisible(visible)
        if not checked == None: object.setChecked(checked)
        if not checkable == None: object.setCheckable(checked)
        if not enabled == None: object.setEnabled(enabled)

        if not stylesheet == None: object.setStyleSheet(stylesheet)

        if not combo == None:
            for i in combo: object.addItem(str(i))


    def setupUi(self, MainWindow):
        # Fonts
        font_headline = QtGui.QFont()
        font_headline.setPointSize(13)
        font_headline.setBold(True)

        font_graphs = QtGui.QFont()
        font_graphs.setPixelSize(12)
        font_graphs.setBold(False)

        font_ee = QtGui.QFont()
        font_ee.setPointSize(11)
        font_ee.setBold(False)

        # Graphs background
        pg.setConfigOption('background', (255, 255, 255))
        pg.setConfigOption('foreground', 'k')

        # Main window
        MainWindow_size = [1100, 787]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(MainWindow_size[0], MainWindow_size[1])
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(MainWindow_size[0], MainWindow_size[1]))
        MainWindow.setMaximumSize(QtCore.QSize(MainWindow_size[0], MainWindow_size[1]))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle("pySAsum")
        MainWindow.setWindowIcon(QtGui.QIcon(self.current_dir + "\icon.png"))
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Block: scan A
        self.label_scan_A = QtWidgets.QLabel(self.centralwidget)
        self.__create_element(self.label_scan_A, [15, 0, 80, 20], "label_scan_A", text="Scan A", font=font_headline)
        self.groupBox_scan_A = QtWidgets.QGroupBox(self.centralwidget)
        self.__create_element(self.groupBox_scan_A, [5, 5, 300, 375], "groupBox_scan_A")
        self.lineEdit_scan_A_name = QtWidgets.QLineEdit(self.groupBox_scan_A)
        self.__create_element(self.lineEdit_scan_A_name, [5, 22, 260, 20], "lineEdit_scan_A_name", font=font_ee)
        self.toolButton_scan_A = QtWidgets.QToolButton(self.groupBox_scan_A)
        self.__create_element(self.toolButton_scan_A, [275, 22, 20, 20], "toolButton_scan_A", text="...", font=font_ee)
        self.label_scan_A_type = QtWidgets.QLabel(self.groupBox_scan_A)
        self.__create_element(self.label_scan_A_type, [5, 45, 40, 20], "label_scan_A_type", text="Type:", font=font_ee)
        self.comboBox_scan_A_type = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.__create_element(self.comboBox_scan_A_type, [45, 45, 150, 20], "comboBox_scan_A_type", combo=["Single point", "Integrated image", "2D map"], font=font_ee)
        self.graphicsView_scan_A = pg.ImageView(self.groupBox_scan_A)
        self.__create_element(self.graphicsView_scan_A, [3, 70, 295, 275], "graphicsView_scan_A")
        self.graphicsView_scan_A.ui.histogram.hide()
        self.graphicsView_scan_A.ui.menuBtn.hide()
        self.graphicsView_scan_A.ui.roiBtn.hide()
        self.label_scan_A_polarisation = QtWidgets.QLabel(self.groupBox_scan_A)
        self.__create_element(self.label_scan_A_polarisation, [5, 350, 75, 20], "label_scan_A_polarisation", text="Polarisation:", font=font_ee)
        self.comboBox_scan_A_polarisation = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.__create_element(self.comboBox_scan_A_polarisation, [75, 350, 55, 20], "comboBox_scan_A_polarisation", font=font_ee)
        self.label_scan_A_point_number = QtWidgets.QLabel(self.groupBox_scan_A)
        self.__create_element(self.label_scan_A_point_number, [158, 350, 80, 20], "label_scan_A_point_number", text="Point number:", font=font_ee)
        self.comboBox_scan_A_point_number = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.__create_element(self.comboBox_scan_A_point_number, [240, 350, 55, 20], "comboBox_scan_A_point_number", font=font_ee)

        # Block: scan B
        self.label_scan_B = QtWidgets.QLabel(self.centralwidget)
        self.__create_element(self.label_scan_B, [15, 385, 80, 20], "label_scan_B", text="Scan B", font=font_headline)
        self.groupBox_scan_B = QtWidgets.QGroupBox(self.centralwidget)
        self.__create_element(self.groupBox_scan_B, [5, 390, 300, 375], "groupBox_scan_B")
        self.lineEdit_scan_B_name = QtWidgets.QLineEdit(self.groupBox_scan_B)
        self.__create_element(self.lineEdit_scan_B_name, [5, 22, 260, 20], "lineEdit_scan_B_name", font=font_ee)
        self.toolButton_scan_B = QtWidgets.QToolButton(self.groupBox_scan_B)
        self.__create_element(self.toolButton_scan_B, [275, 22, 20, 20], "toolButton_scan_B", text="...", font=font_ee)
        self.label_scan_B_type = QtWidgets.QLabel(self.groupBox_scan_B)
        self.__create_element(self.label_scan_B_type, [5, 45, 40, 20], "label_scan_B_type", text="Type:", font=font_ee)
        self.comboBox_scan_B_type = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.__create_element(self.comboBox_scan_B_type, [45, 45, 150, 20], "comboBox_scan_B_type", combo=["Single point", "Integrated image", "2D map"], font=font_ee)
        self.graphicsView_scan_B = pg.ImageView(self.groupBox_scan_B)
        self.__create_element(self.graphicsView_scan_B, [3, 70, 295, 275], "graphicsView_scan_B")
        self.graphicsView_scan_B.ui.histogram.hide()
        self.graphicsView_scan_B.ui.menuBtn.hide()
        self.graphicsView_scan_B.ui.roiBtn.hide()
        self.label_scan_B_polarisation = QtWidgets.QLabel(self.groupBox_scan_B)
        self.__create_element(self.label_scan_B_polarisation, [5, 350, 75, 20], "label_scan_B_polarisation", text="Polarisation:", font=font_ee)
        self.comboBox_scan_B_polarisation = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.__create_element(self.comboBox_scan_B_polarisation, [75, 350, 55, 20], "comboBox_scan_B_polarisation", font=font_ee)
        self.label_scan_B_point_number = QtWidgets.QLabel(self.groupBox_scan_B)
        self.__create_element(self.label_scan_B_point_number, [158, 350, 80, 20], "label_scan_B_point_number", text="Point number:", font=font_ee)
        self.comboBox_scan_B_point_number = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.__create_element(self.comboBox_scan_B_point_number, [240, 350, 55, 20], "comboBox_scan_B_point_number", font=font_ee)

        # Block: Result
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.__create_element(self.label_result, [325, 0, 61, 20], "label_result", text="Result", font=font_headline)
        self.groupBox_result = QtWidgets.QGroupBox(self.centralwidget)
        self.__create_element(self.groupBox_result, [320, 5, 775, 760], "groupBox_result")
        # ROI part is hidden by default
        self.graphicsView_result_integrated_roi = pg.PlotWidget(self.groupBox_result)
        self.__create_element(self.graphicsView_result_integrated_roi, [3, 431, 770, 275], "graphicsView_result_integrated_roi")
        self.graphicsView_result_integrated_roi.getAxis("bottom").tickFont = font_graphs
        self.graphicsView_result_integrated_roi.getAxis("bottom").setStyle(tickTextOffset=10)
        self.graphicsView_result_integrated_roi.getAxis("left").tickFont = font_graphs
        self.graphicsView_result_integrated_roi.getAxis("left").setStyle(tickTextOffset=10)
        self.graphicsView_result_integrated_roi.showAxis("top")
        self.graphicsView_result_integrated_roi.getAxis("top").setStyle(showValues=False)
        self.graphicsView_result_integrated_roi.showAxis("right")
        self.graphicsView_result_integrated_roi.getAxis("right").setStyle(showValues=False)
        self.label_result_roi_coorddinates = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_roi_coorddinates, [10, 710, 400, 22], "label_result_roi_coorddinates", text="ROI coordinates: left                right                top                bottom", font=font_ee)
        self.lineEdit_result_roi_left = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_left, [127, 710, 40, 22], "lineEdit_result_roi_left", text="10", font=font_ee)
        self.lineEdit_result_roi_right = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_right, [217, 710, 40, 22], "lineEdit_result_roi_right", text="20", font=font_ee)
        self.lineEdit_result_roi_top = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_top, [297, 710, 40, 22], "lineEdit_result_roi_top", text="10", font=font_ee)
        self.lineEdit_result_roi_bottom = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_bottom, [407, 710, 40, 22], "lineEdit_result_roi_bottom", text="20", font=font_ee)
        self.pushButton_result_turn_roi = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_turn_roi, [535, 710, 80, 22], "pushButton_result_turn_roi", text="Turn ROI", font=font_headline)
        self.pushButton_result_export_integrated_roi = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_export_integrated_roi, [620, 710, 151, 22], "pushButton_result_export_integrated_roi", text="Export int. ROI", font=font_headline)

        # This part of Result block is visible
        self.checkBox_result_devide_by_monitor = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_devide_by_monitor, [5, 22, 241, 22], "checkBox_result_devide_by_monitor", text="Devide by monitors", font=font_ee)
        self.label_result_aspect_ratio = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_aspect_ratio, [170, 22, 75, 20], "label_result_aspect_ratio", text="Aspect ratio:", font=font_ee)
        self.horizontalSlider_result_aspect_ratio = QtWidgets.QSlider(self.groupBox_result)
        self.__create_element(self.horizontalSlider_result_aspect_ratio, [250, 22, 140, 22], "horizontalSlider_result_aspect_ratio")
        self.horizontalSlider_result_aspect_ratio.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_result_aspect_ratio.setMinimum(1)
        self.horizontalSlider_result_aspect_ratio.setMaximum(30)
        self.horizontalSlider_result_aspect_ratio.setValue(1)
        self.lineEdit_result_operation_sign = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_operation_sign, [450, 22, 20, 22], "lineEdit_result_operation_sign", text=" - ", font=font_ee)
        self.lineEdit_result_operation = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_operation, [475, 22, 200, 22], "lineEdit_result_operation", stylesheet="color:rgb(0,0,0)", enabled=False, font=font_ee)
        self.pushButton_result_swap_ab = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_swap_ab, [680, 22, 90, 22], "pushButton_result_swap_ab", text="(A<->B)", font=font_headline)
        self.graphicsView_result = pg.ImageView(self.groupBox_result)
        self.__create_element(self.graphicsView_result, [3, 48, 770, 684], "graphicsView_result")
        self.graphicsView_result.ui.menuBtn.hide()
        self.graphicsView_result.ui.roiBtn.hide()
        self.graphicsView_result.ui.histogram.clickAccepted
        colmap = pg.ColorMap(numpy.array([0.4, 0.5, 0.6]),
                             numpy.array([[0, 0, 255, 255], [0, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
        self.graphicsView_result.setColorMap(colmap)

        self.label_result_reduce_number_of_pixels = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_reduce_number_of_pixels, [10, 736, 250, 20], "label_result_reduce_number_of_pixels", text="Reduce number of pixels in each direction by:", font=font_ee)
        self.checkBox_result_reduce_number_of_pixels_by_2 = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_reduce_number_of_pixels_by_2, [270, 736, 241, 20], "checkBox_result_reduce_number_of_pixels_by_2", text="x2", font=font_ee)
        self.checkBox_result_reduce_number_of_pixels_by_4 = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_reduce_number_of_pixels_by_4, [315, 736, 241, 20], "checkBox_result_reduce_number_of_pixels_by_4", text="x4", font=font_ee)
        self.checkBox_result_reduce_number_of_pixels_by_8 = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_reduce_number_of_pixels_by_8, [360, 736, 241, 20], "checkBox_result_reduce_number_of_pixels_by_8", text="x8", font=font_ee)
        self.pushButton_result_export = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_export, [620, 735, 151, 22], "pushButton_result_export", text="Export result (2D)", font=font_headline)
        self.pushButton_result_ROI = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_ROI, [535, 735, 80, 22], "pushButton_result_ROI", text="ROI", font=font_headline)

        # Menu and statusbar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.__create_element(self.menubar, [0, 0, 717, 21], "menubar", font=font_ee)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.__create_element(self.menuHelp, [999, 999, 999, 999], "menuHelp", title="Help", font=font_ee)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.__create_element(self.actionVersion, [999, 999, 999, 999], "actionVersion", text="Version 1.3.1", font=font_ee)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuHelp.menuAction())

# EE (Actions, drawing, math)
class GUI(Ui_MainWindow):

    current_dir = ""
    for i in sys.argv[0].split("/")[:-4]: current_dir += i + "/"

    def __init__(self):

        super(GUI, self).__init__()
        self.setupUi(self)

        # Actions on clicks
        self.toolButton_scan_A.clicked.connect(self.button_import_scan)
        self.toolButton_scan_B.clicked.connect(self.button_import_scan)
        self.comboBox_scan_A_point_number.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_A_polarisation.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_A_type.currentIndexChanged.connect(self.change_interface)
        self.comboBox_scan_B_point_number.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_B_polarisation.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_B_type.currentIndexChanged.connect(self.change_interface)
        self.pushButton_result_export.clicked.connect(self.button_export_result)

        self.checkBox_result_reduce_number_of_pixels_by_2.stateChanged.connect(self.reduce_number_of_pixels)
        self.checkBox_result_reduce_number_of_pixels_by_4.stateChanged.connect(self.reduce_number_of_pixels)
        self.checkBox_result_reduce_number_of_pixels_by_8.stateChanged.connect(self.reduce_number_of_pixels)

        self.pushButton_result_swap_ab.clicked.connect(self.diff_line)
        self.checkBox_result_devide_by_monitor.stateChanged.connect(self.draw_res)
        self.horizontalSlider_result_aspect_ratio.valueChanged.connect(self.draw_res)
        self.pushButton_result_ROI.clicked.connect(self.button_roi_calculate_show_turn_square)
        self.pushButton_result_turn_roi.clicked.connect(self.button_roi_calculate_show_turn_square)
        self.pushButton_result_export_integrated_roi.clicked.connect(self.button_export_roi)
        self.lineEdit_result_roi_left.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_roi_right.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_roi_top.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_roi_bottom.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_operation_sign.editingFinished.connect(self.diff_line)
        self.actionVersion.triggered.connect(self.menu_info)

        # use arrays to keep old "lines" and redraw only if they are different from new ones
        self.line_A, self.line_B = ["", ""], ["", ""]
        self.show_roi = 0
        self.turn_roi = 0
        self.draw_roi_result = []

        self.detector_image_A, self.detector_image_B = [], []
        self.res = []
        # I will use self.interface_A and self.interface_B to track what was
        # changed on the form and do changes without creating too many functions
        self.last_type_A, self.last_type_B = [], []

        self.initial_roi = []

    def button_import_scan(self):
        if self.sender().objectName() == "toolButton_scan_A":

            self.lineEdit_scan_A_name.setText("")

            data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", self.current_dir, ".h5 (*.h5)")
            if data_file[0] == "": return
            # Next "Import scans" will open last dir instead of the app location
            self.current_dir = data_file[0][0][:data_file[0][0].rfind("/")]

            self.lineEdit_scan_A_name.setText(data_file[0])
            if self.lineEdit_scan_A_name.text() == "": return

            self.comboBox_scan_A_point_number.clear()
            self.comboBox_scan_A_polarisation.clear()
            self.graphicsView_scan_A.clear()

            with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
                self.original_roi_A = numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('roi').get("roi"))
                self.lineEdit_result_roi_left.setText(str(self.original_roi_A[2])[:-2])
                self.lineEdit_result_roi_right.setText(str(self.original_roi_A[3])[:-2])
                self.lineEdit_result_roi_bottom.setText(str(self.original_roi_A[1])[:-2])
                self.lineEdit_result_roi_top.setText(str(self.original_roi_A[0])[:-2])

                for index, th in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('motors').get('th').get("value")):
                    self.comboBox_scan_A_point_number.addItem(str(index))

                for polarisation in FILE[list(FILE.keys())[0]].get("instrument").get('detectors'):

                    if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                        self.comboBox_scan_A_polarisation.addItem(str(polarisation)[-2:])
                    elif polarisation in ("psd"):
                        self.comboBox_scan_A_polarisation.addItem("np")

            self.comboBox_scan_A_point_number.setCurrentIndex(0)
            self.comboBox_scan_A_polarisation.setCurrentIndex(0)

            self.last_type_A = self.comboBox_scan_A_type.currentText()

        elif self.sender().objectName() == "toolButton_scan_B":
            self.lineEdit_scan_B_name.setText("")

            data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", self.current_dir, ".h5 (*.h5)")
            if data_file[0] == "": return
            # Next "Import scans" will open last dir
            self.current_dir = data_file[0][0][:data_file[0][0].rfind("/")]

            self.lineEdit_scan_B_name.setText(data_file[0])
            if self.lineEdit_scan_B_name.text() == "": return

            self.comboBox_scan_B_point_number.clear()
            self.comboBox_scan_B_polarisation.clear()
            self.graphicsView_scan_B.clear()

            with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:

                for index, th in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('motors').get('th').get("value")):
                    self.comboBox_scan_B_point_number.addItem(str(index))

                for polarisation in FILE[list(FILE.keys())[0]].get("instrument").get('detectors'):

                    if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                        self.comboBox_scan_B_polarisation.addItem(str(polarisation)[-2:])
                    elif polarisation in ("psd"):
                        self.comboBox_scan_B_polarisation.addItem("np")

            self.comboBox_scan_B_point_number.setCurrentIndex(0)
            self.comboBox_scan_B_polarisation.setCurrentIndex(0)

            self.last_type_B = self.comboBox_scan_B_type.currentText()

        self.diff_line()

    def button_export_result(self):
        # Export resulting picture as CSV
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", self.current_dir)
        if dir == "": return

        with open(dir + "/2D_map (" + self.lineEdit_result_operation.text() + ").dat", "w") as new_file_2d_map:
            for line in self.res:
                for row in line:
                    new_file_2d_map.write(str(int(row)) + " ")
                new_file_2d_map.write("\n")

    def change_interface(self):

        if  not self.last_type_A == self.comboBox_scan_A_type.currentText():
            # if we have "Single point" as a mode and we just changet to it -> change "Point number" to the first one
            if self.comboBox_scan_A_type.currentText() == "Single point": self.comboBox_scan_A_point_number.setCurrentIndex(0)
            # if we have "2D map" as a mode and we just changet to it -> change Scan B Type to "2D map" also
            elif self.comboBox_scan_A_type.currentText() == "2D map": self.comboBox_scan_B_type.setCurrentIndex(2)
            # if we changed from "2D map" -> change B also
            if self.last_type_A == "2D map":
                if self.comboBox_scan_A_type.currentText() == "Single point": self.comboBox_scan_B_type.setCurrentIndex(0)
                elif self.comboBox_scan_A_type.currentText() == "Integrated image": self.comboBox_scan_B_type.setCurrentIndex(1)

        # same for B
        if not self.last_type_B == self.comboBox_scan_B_type.currentText():
            if self.comboBox_scan_B_type.currentText() == "Single point": self.comboBox_scan_B_point_number.setCurrentIndex(0)
            elif self.comboBox_scan_B_type.currentText() == "2D map": self.comboBox_scan_A_type.setCurrentIndex(2)
            if self.last_type_B == "2D map":
                if self.comboBox_scan_B_type.currentText() == "Single point": self.comboBox_scan_A_type.setCurrentIndex(0)
                elif self.comboBox_scan_B_type.currentText() == "Integrated image": self.comboBox_scan_A_type.setCurrentIndex(1)

        # show/hide some elements depends on the mode
        if self.comboBox_scan_A_type.currentText() == "2D map" or self.comboBox_scan_B_type.currentText() == "2D map":
            self.checkBox_result_reduce_number_of_pixels_by_2.setDisabled(True)
            self.checkBox_result_reduce_number_of_pixels_by_4.setDisabled(True)
            self.checkBox_result_reduce_number_of_pixels_by_8.setDisabled(True)
        else:
            self.checkBox_result_reduce_number_of_pixels_by_2.setDisabled(False)
            self.checkBox_result_reduce_number_of_pixels_by_4.setDisabled(False)
            self.checkBox_result_reduce_number_of_pixels_by_8.setDisabled(False)

        if self.comboBox_scan_A_type.currentText() in ["2D map", "Integrated image"]:
            self.comboBox_scan_A_point_number.setDisabled(True)
        else:
            self.comboBox_scan_A_point_number.setDisabled(False)

        if self.comboBox_scan_B_type.currentText() in ["2D map", "Integrated image"]:
            self.comboBox_scan_B_point_number.setDisabled(True)
        else:
            self.comboBox_scan_B_point_number.setDisabled(False)

        self.last_type_A = self.comboBox_scan_A_type.currentText()
        self.last_type_B = self.comboBox_scan_B_type.currentText()

        self.diff_line()

    # diff line
    def diff_line(self):

        if not self.sender().objectName() == "pushButton_result_swap_ab":
            line = ""

            if self.lineEdit_result_operation_sign.text() not in ["-", " -", "- ", "+", " +", "+ "]:
                self.lineEdit_result_operation_sign.setText(" - ")
            if self.comboBox_scan_A_type.currentText() == "Single point" and not self.comboBox_scan_A_point_number.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(" + str(self.comboBox_scan_A_point_number.currentText()) + ")"
            elif self.comboBox_scan_A_type.currentText() == "Integrated image" and not self.comboBox_scan_A_polarisation.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(All)"
            elif self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_A_polarisation.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(2D map)"

            if self.comboBox_scan_B_type.currentText() == "Single point" and not self.comboBox_scan_B_point_number.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(" + str(self.comboBox_scan_B_point_number.currentText()) + ")"
            elif self.comboBox_scan_B_type.currentText() == "Integrated image" and not self.comboBox_scan_B_polarisation.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(All)"
            elif self.comboBox_scan_B_type.currentText() == "2D map" and not self.comboBox_scan_B_polarisation.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(2D map)"

            # fill one of the scans if it is the only one is imported
            if not self.line_A[0] == "" and self.line_B[0] == "": line = self.line_A[0]
            elif self.line_A[0] == "" and not self.line_B[0] == "": line = self.line_B[0]
            # otherwice check if a line is already presented and what is the first. Keep the same order
            else:
                if self.lineEdit_result_operation.text().find("A(") == 0:
                    line = self.line_A[0] + self.lineEdit_result_operation_sign.text() + self.line_B[0]
                else: line = self.line_B[0] + self.lineEdit_result_operation_sign.text() + self.line_A[0]

            self.lineEdit_result_operation.setText(line)

            if not self.line_A[0] == self.line_A[1]: self.draw_det_A_frame()
            self.line_A[1] = self.line_A[0]

            if not self.line_B[0] == self.line_B[1]: self.draw_det_B_frame()
            self.line_B[1] = self.line_B[0]

        else:

            if self.lineEdit_result_operation.text() == "": return

            if not self.lineEdit_result_operation.text().find(self.lineEdit_result_operation_sign.text()) > 0: return

            if self.lineEdit_result_operation.text().find(self.line_A[0]) == 0: # then A scan is first
                line = self.line_B[0] + self.lineEdit_result_operation_sign.text() + self.line_A[0]
            else: line = self.line_A[0] + self.lineEdit_result_operation_sign.text() + self.line_B[0]

            self.lineEdit_result_operation.setText(line)

        self.draw_res()

        if self.show_roi == 1: self.button_roi_calculate_show_turn_square()

    # draw graphs
    def draw_det_A_frame(self):

        self.graphicsView_scan_A.clear()

        if self.lineEdit_scan_A_name.text() == "" or self.comboBox_scan_A_point_number.currentText() == "" or self.comboBox_scan_A_polarisation.currentText() == "": return

        # define "detector name" by polarisation
        if self.comboBox_scan_A_polarisation.currentText() == "np": SCAN_PSD_A = "psd"
        else: SCAN_PSD_A = "psd_" + self.comboBox_scan_A_polarisation.currentText()

        with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
            # sum all detector images
            if self.comboBox_scan_A_type.currentText() == "Integrated image":
                for i in range(0, self.comboBox_scan_A_point_number.count() - 1):
                    if i == 0: self.detector_image_A = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[i]
                    else: self.detector_image_A = numpy.add(self.detector_image_A, FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[i])
            # sum each frame in Y axis
            elif self.comboBox_scan_A_type.currentText() == "2D map":
                self.detector_image_A = FILE[list(FILE.keys())[0]].get("instrument").get("detectors").get(SCAN_PSD_A).get('data')[:, :, :].sum(axis=1)
                self.detector_image_A = numpy.flip(self.detector_image_A, axis=0)
            # show specific frame
            else:
                self.detector_image_A = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[int(self.comboBox_scan_A_point_number.currentText())]

            # seems to be a numpy bag - I cant draw out an array until I subtract zero array of the same size of it
            self.detector_image_A = numpy.around(self.detector_image_A, decimals=0).astype(int)
            self.detector_image_A = numpy.subtract(self.detector_image_A, numpy.zeros((self.detector_image_A.shape[0], self.detector_image_A.shape[1])))

            self.graphicsView_scan_A.setImage(self.detector_image_A, axes={'x':1, 'y':0}, levels=(0,0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_A.setColorMap(colmap)

    def draw_det_B_frame(self):
        # see comments in draw_det_A_frame
        self.graphicsView_scan_B.clear()

        if self.lineEdit_scan_B_name.text() == "" or self.comboBox_scan_B_point_number.currentText() == "" or self.comboBox_scan_B_polarisation.currentText() == "": return

        if self.comboBox_scan_B_polarisation.currentText() == "np": SCAN_PSD_B = "psd"
        else: SCAN_PSD_B = "psd_" + self.comboBox_scan_B_polarisation.currentText()

        with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:

            if self.comboBox_scan_B_type.currentText() == "Integrated image":
                for i in range(0, self.comboBox_scan_B_point_number.count() - 1):
                    if i == 0: self.detector_image_B = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[i]
                    else: self.detector_image_B = numpy.add(self.detector_image_B, FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[i])
            elif self.comboBox_scan_B_type.currentText() == "2D map":
                self.detector_image_B = FILE[list(FILE.keys())[0]].get("instrument").get("detectors").get(SCAN_PSD_B).get('data')[:, :, :].sum(axis=1)
                self.detector_image_B = numpy.flip(self.detector_image_B, axis=0)
            else:
                self.detector_image_B = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[int(self.comboBox_scan_B_point_number.currentText())]

            self.detector_image_B = numpy.around(self.detector_image_B, decimals=0).astype(int)
            self.detector_image_B = numpy.subtract(self.detector_image_B, numpy.zeros((self.detector_image_B.shape[0], self.detector_image_B.shape[1])))

            self.graphicsView_scan_B.setImage(self.detector_image_B, axes={'x': 1, 'y': 0}, levels=(0, 0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_B.setColorMap(colmap)

    def draw_res(self):

        # Subtract 2D map only from other 2D map
        if (self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_B_type.currentText() == "2D map") or (self.comboBox_scan_B_type.currentText() == "2D map" and not self.comboBox_scan_A_type.currentText() == "2D map"): return

        if self.lineEdit_result_operation.text().find("()") > -1 or self.lineEdit_result_operation.text() in ["", self.lineEdit_result_operation_sign.text()] : return
        if not self.lineEdit_scan_A_name.text() == "" and (self.comboBox_scan_A_point_number.currentText() == "" or self.comboBox_scan_A_polarisation.currentText() == ""): return
        if not self.lineEdit_scan_B_name.text() == "" and (self.comboBox_scan_B_point_number.currentText() == "" or self.comboBox_scan_B_polarisation.currentText() == ""): return

        # Get requested in the line A frame
        if not self.line_A[0] == "":

            if self.comboBox_scan_A_polarisation.currentText() == "np": SCAN_PSD_A = "psd"
            else: SCAN_PSD_A = "psd_" + self.comboBox_scan_A_polarisation.currentText()

            with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
                # seems to be a bug in numpy arrays imported from hdf5 files. Need to redefine array type to int.
                self.detector_image_A = numpy.around(self.detector_image_A, decimals=0).astype(int)
                self.detector_image_A = numpy.subtract(self.detector_image_A, numpy.zeros((self.detector_image_A.shape[0], self.detector_image_A.shape[1])))

                for index, scaler in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if SCAN_PSD_A == "psd": monitor_A_identifier = "b'mon0'"
                    elif SCAN_PSD_A == "psd_uu": monitor_A_identifier = "b'm1'"
                    elif SCAN_PSD_A == "psd_dd": monitor_A_identifier = "b'm2'"
                    elif SCAN_PSD_A == "psd_du": monitor_A_identifier = "b'm3'"
                    elif SCAN_PSD_A == "psd_ud": monitor_A_identifier = "b'm4'"

                    if monitor_A_identifier in str(scaler):
                        if self.comboBox_scan_A_point_number.currentText() in ["All", "2D map"]:
                            monitor_A = numpy.sum(numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index])
                        else:
                            monitor_A = numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_scan_A_point_number.currentText())]

        # Get requested in the line B frame
        if not self.line_B[0] == "":

            if self.comboBox_scan_B_polarisation.currentText() == "np": SCAN_PSD_B = "psd"
            else: SCAN_PSD_B = "psd_" + self.comboBox_scan_B_polarisation.currentText()

            with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:
                # seems to be a bug in numpy arrays imported from hdf5 files. Need to redefine array type to int.
                self.detector_image_B = numpy.around(self.detector_image_B, decimals=0).astype(int)
                self.detector_image_B = numpy.subtract(self.detector_image_B, numpy.zeros((self.detector_image_B.shape[0], self.detector_image_B.shape[1])))

                for index, scaler in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if SCAN_PSD_B == "psd": monitor_B_identifier = "b'mon0'"
                    elif SCAN_PSD_B == "psd_uu": monitor_B_identifier = "b'm1'"
                    elif SCAN_PSD_B == "psd_dd": monitor_B_identifier = "b'm2'"
                    elif SCAN_PSD_B == "psd_du": monitor_B_identifier = "b'm3'"
                    elif SCAN_PSD_B == "psd_ud": monitor_B_identifier = "b'm4'"

                    if monitor_B_identifier in str(scaler):
                        if self.comboBox_scan_B_point_number.currentText() in ["All", "2D map"]:
                            monitor_B = numpy.sum(numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index])
                        else:
                            monitor_B = numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_scan_B_point_number.currentText())]

        # Do the subtraction
        if self.line_A[0] == "" and not self.line_B[0] == "": RES = self.detector_image_B
        elif not self.line_A[0] == "" and self.line_B[0] == "": RES = self.detector_image_A
        else:
            if not self.lineEdit_result_operation.text().find(self.line_A[0]) == 0:
                main = self.detector_image_B
                main_mon = monitor_B
                min = self.detector_image_A
                min_mon = monitor_A
            else:
                main = self.detector_image_A
                main_mon = monitor_A
                min = self.detector_image_B
                min_mon = monitor_B

            if self.checkBox_result_devide_by_monitor.isChecked():
                main = numpy.divide(main, main_mon/min_mon)

        scale_low = 0
        scale_high = 1

        if self.lineEdit_result_operation.text().find("+") > 0:
            RES = numpy.add(main, min)
        elif self.lineEdit_result_operation.text().find("-") > 0:
            RES = numpy.subtract(main, min)
            scale_low = -10
            scale_high = 10

            if self.checkBox_result_reduce_number_of_pixels_by_2.isChecked() or self.checkBox_result_reduce_number_of_pixels_by_4.isChecked() or self.checkBox_result_reduce_number_of_pixels_by_8.isChecked():
                scale_low = -20
                scale_high = 20

        if self.checkBox_result_reduce_number_of_pixels_by_2.isChecked(): RES = RES.reshape(int(RES.shape[0]/2), 2, int(RES.shape[1]/2), 2).sum(axis=1).sum(axis=2)
        elif self.checkBox_result_reduce_number_of_pixels_by_4.isChecked(): RES = RES.reshape(int(RES.shape[0]/4), 4, int(RES.shape[1]/4), 4).sum(axis=1).sum(axis=2)
        elif self.checkBox_result_reduce_number_of_pixels_by_8.isChecked(): RES = RES.reshape(int(RES.shape[0]/8), 8, int(RES.shape[0]/8), 8).sum(axis=1).sum(axis=2)

        RES = numpy.swapaxes(RES, 0,1)

        self.res = RES

        self.graphicsView_result.setImage(RES, scale=(1, self.horizontalSlider_result_aspect_ratio.value()))
        if not self.detector_image_A == []:
            self.graphicsView_scan_A.setImage(self.detector_image_A, axes={'x': 1, 'y': 0}, levels=(0, 0.1), scale=(1, self.horizontalSlider_result_aspect_ratio.value()))
        if not self.detector_image_B == []:
            self.graphicsView_scan_B.setImage(self.detector_image_B, axes={'x': 1, 'y': 0}, levels=(0, 0.1), scale=(1, self.horizontalSlider_result_aspect_ratio.value()))

        self.graphicsView_result.ui.histogram.setHistogramRange(scale_low, scale_high)
        self.graphicsView_result.ui.histogram.setLevels(scale_low, scale_high)

        self.statusbar.showMessage('Action "' + self.lineEdit_result_operation.text() + '" is performed.')

        self.button_roi_calculate_show_turn_square()

    # Reduce number of pixels
    def reduce_number_of_pixels(self):

        self.lineEdit_result_roi_left.setText(self.initial_roi[0])
        self.lineEdit_result_roi_right.setText(self.initial_roi[1])
        self.lineEdit_result_roi_bottom.setText(self.initial_roi[2])
        self.lineEdit_result_roi_top.setText(self.initial_roi[3])

        if self.sender().objectName() == "checkBox_result_reduce_number_of_pixels_by_2":
            if self.checkBox_result_reduce_number_of_pixels_by_2.isChecked():
                self.checkBox_result_reduce_number_of_pixels_by_4.setChecked(False)
                self.checkBox_result_reduce_number_of_pixels_by_8.setChecked(False)
                self.lineEdit_result_roi_left.setText(str(int(round(int(self.initial_roi[0])/2))))
                self.lineEdit_result_roi_right.setText(str(int(round(int(self.initial_roi[1])/2))))
                self.lineEdit_result_roi_bottom.setText(str(int(round(int(self.initial_roi[2])/2))))
                self.lineEdit_result_roi_top.setText(str(int(round(int(self.initial_roi[3])/2))))
            else:
                self.checkBox_result_reduce_number_of_pixels_by_2.setChecked(False)

        elif self.sender().objectName() == "checkBox_result_reduce_number_of_pixels_by_4":
            if self.checkBox_result_reduce_number_of_pixels_by_4.isChecked():
                self.checkBox_result_reduce_number_of_pixels_by_2.setChecked(False)
                self.checkBox_result_reduce_number_of_pixels_by_8.setChecked(False)
                self.lineEdit_result_roi_left.setText(str(int(round(int(self.initial_roi[0])/4))))
                self.lineEdit_result_roi_right.setText(str(int(round(int(self.initial_roi[1])/4))))
                self.lineEdit_result_roi_bottom.setText(str(int(round(int(self.initial_roi[2])/4))))
                self.lineEdit_result_roi_top.setText(str(int(round(int(self.initial_roi[3])/4))))
            else:
                self.checkBox_result_reduce_number_of_pixels_by_4.setChecked(False)
        elif self.sender().objectName() == "checkBox_result_reduce_number_of_pixels_by_8":
            if self.checkBox_result_reduce_number_of_pixels_by_8.isChecked():
                self.checkBox_result_reduce_number_of_pixels_by_2.setChecked(False)
                self.checkBox_result_reduce_number_of_pixels_by_4.setChecked(False)
                self.lineEdit_result_roi_left.setText(str(int(round(int(self.initial_roi[0])/8))))
                self.lineEdit_result_roi_right.setText(str(int(round(int(self.initial_roi[1])/8))))
                self.lineEdit_result_roi_bottom.setText(str(int(round(int(self.initial_roi[2])/8))))
                self.lineEdit_result_roi_top.setText(str(int(round(int(self.initial_roi[3])/8))))
            else:
                self.checkBox_result_reduce_number_of_pixels_by_8.setChecked(False)

        self.button_roi_calculate_show_turn_square()
        self.draw_res()

    def menu_info(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/") + "\icon.png"))
        msgBox.setText("PySAsum. " + self.actionVersion.text() + "\n\n"
                                                                                            "Alexey.Klechikov@gmail.com\n\n"
                                                                                            "Check new version at https://github.com/Alexey-Klechikov/pySAsum/releases")
        msgBox.exec_()

    # ROI
    def button_roi_calculate_show_turn_square(self):

        ####### turn roi
        if self.sender().objectName() == "pushButton_result_turn_roi":
            self.turn_roi = [1 if self.turn_roi == 0 else 0][0]

        ####### show roi
        if self.sender().objectName() == "pushButton_result_ROI":
            # resize Result 2D map to show what is hidden
            if self.show_roi == 0:
                self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 383))
                self.show_roi = 1
            else:
                self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 684))
                self.show_roi = 0

        ####### calculate
        plot_x = []
        plot_y = []

        self.graphicsView_result_integrated_roi.getPlotItem().clear()

        # for some reason I cant just plot an array (might be the problem with export of 2d arrays from hdf5), I do it in lame way instead
        if self.turn_roi == 0:
            for index, i in enumerate(self.res):
                if index < int(self.lineEdit_result_roi_left.text()) or index > int(self.lineEdit_result_roi_right.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_result_roi_top.text()) : int(self.lineEdit_result_roi_bottom.text())].sum())
        else:
            for index, i in enumerate(numpy.swapaxes(self.res, 0, 1)):
                if index < int(self.lineEdit_result_roi_top.text()) or index > int(self.lineEdit_result_roi_bottom.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_result_roi_left.text()) : int(self.lineEdit_result_roi_right.text())].sum())

        self.roi_plot_export = [plot_x, plot_y]

        s1 = pg.PlotCurveItem(x=plot_x, y=plot_y, pen=pg.mkPen(0, 0, 0))
        self.graphicsView_result_integrated_roi.addItem(s1)

        ####### square
        if self.sender().objectName() in ["comboBox_scan_A_type", "comboBox_scan_B_type"]:
            if self.comboBox_scan_A_type.currentText() == "2D map" or self.comboBox_scan_B_type.currentText() == "2D map":
                self.lineEdit_result_roi_bottom.setText(str(self.res.shape[1]))
                self.lineEdit_result_roi_top.setText("0")
            elif not self.initial_roi == []:
                self.lineEdit_result_roi_bottom.setText(self.initial_roi[2])
                self.lineEdit_result_roi_top.setText(self.initial_roi[3])

        if not self.checkBox_result_reduce_number_of_pixels_by_2.isChecked() and not self.checkBox_result_reduce_number_of_pixels_by_4.isChecked() and not self.checkBox_result_reduce_number_of_pixels_by_8.isChecked() and not self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_B_type.currentText() == "2D map":
            self.initial_roi = [self.lineEdit_result_roi_left.text(), self.lineEdit_result_roi_right.text(), self.lineEdit_result_roi_bottom.text(), self.lineEdit_result_roi_top.text()]

        if self.draw_roi_result:
            self.graphicsView_result.removeItem(self.draw_roi_result)

        spots = {'x': (int(self.lineEdit_result_roi_left.text()),
                                    int(self.lineEdit_result_roi_right.text()),
                                    int(self.lineEdit_result_roi_right.text()),
                                    int(self.lineEdit_result_roi_left.text()),
                                    int(self.lineEdit_result_roi_left.text())),
                              'y': (int(self.lineEdit_result_roi_top.text()) * self.horizontalSlider_result_aspect_ratio.value(),
                                    int(self.lineEdit_result_roi_top.text()) * self.horizontalSlider_result_aspect_ratio.value(),
                                    int(self.lineEdit_result_roi_bottom.text()) * self.horizontalSlider_result_aspect_ratio.value(),
                                    int(self.lineEdit_result_roi_bottom.text()) * self.horizontalSlider_result_aspect_ratio.value(),
                                    int(self.lineEdit_result_roi_top.text()) * self.horizontalSlider_result_aspect_ratio.value())}

        self.draw_roi_result = pg.PlotDataItem(spots, pen=pg.mkPen(255, 255, 255), connect="all")

        if self.show_roi == 1:
            self.graphicsView_result.addItem(self.draw_roi_result)

    def button_export_roi(self):
        # Export ROI as simple 2 column dat
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", self.current_dir)
        if dir == "": return

        with open(dir + "/ROI (" + self.lineEdit_result_operation.text() + ").dat", "w") as new_file_roi:
            for i in range(0, len(self.roi_plot_export[0])):
                new_file_roi.write(str(self.roi_plot_export[0][i]) + " " + str(int(round(self.roi_plot_export[1][i]))) )
                new_file_roi.write("\n")

if __name__ == "__main__":
    QtWidgets.QApplication.setStyle("Fusion")
    app = QtWidgets.QApplication(sys.argv)
    prog = GUI()
    prog.show()
    sys.exit(app.exec_())