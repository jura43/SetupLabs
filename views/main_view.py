from PyQt6 import QtWidgets as qwt
from views.main_view_ui import Ui_Form
from views.main_view_functions import switchStackedWidget, openFileOpenWindow

class MainWindow(qwt.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.show()

        self.ui.contentStackedWidget.setCurrentWidget(self.ui.home) #Setting Home screen as default
        self.ui.setupPage.setCurrentWidget(self.ui.tyres) #Setting tyres page as default

        self.viewSetup = None

        # Assigning functions to menu buttons
        self.ui.menuHome.clicked.connect(lambda: switchStackedWidget(self.ui.contentStackedWidget, self.ui.home))
        self.ui.menuView.clicked.connect(self._switchViewSetup)

        # Assigning function to setup view buttons
        self.ui.closeSetupButton.clicked.connect(lambda: switchStackedWidget(self.ui.contentStackedWidget, self.ui.openViewSetup))
        self.ui.tyresButton.clicked.connect(lambda: switchStackedWidget(self.ui.setupPage, self.ui.tyres))
        self.ui.electronicsButton.clicked.connect(lambda: switchStackedWidget(self.ui.setupPage, self.ui.electronics))
        self.ui.fuelNstratButton.clicked.connect(lambda: switchStackedWidget(self.ui.setupPage, self.ui.fuelNstrat))
        self.ui.mechanicalGripButton.clicked.connect(lambda: switchStackedWidget(self.ui.setupPage, self.ui.mechanicalGrip))
        self.ui.dampersButton.clicked.connect(lambda: switchStackedWidget(self.ui.setupPage, self.ui.dampers))
        self.ui.aeroButton.clicked.connect(lambda: switchStackedWidget(self.ui.setupPage, self.ui.aero))

        # Assigning function to open setup file
        self.ui.openViewSetupButton.clicked.connect(self._viewSetup)
        
    # Statement for checking if setup file is selected
    def _switchViewSetup(self):
        if self.viewSetup == None:
            switchStackedWidget(self.ui.contentStackedWidget, self.ui.openViewSetup)
        else:
            switchStackedWidget(self.ui.contentStackedWidget, self.ui.viewSetup)

    def _viewSetup(self):
        self.viewSetup = openFileOpenWindow(self, self.ui.contentStackedWidget, self.ui.viewSetup)

        # Setting lables with values
        self.ui.carTitle.setText(self.viewSetup.carTitle)
        # Tyres FL
        self.ui.psiFLValue.setText(str(self.viewSetup.tyrePressure[0]) + " psi")
        self.ui.toeFLValue.setText(str(self.viewSetup.tyreToe[0]) + "°")
        self.ui.camberFLValue.setText(str(self.viewSetup.tyreCamber[0]) + "°")
        self.ui.casterFLValue.setText(str(self.viewSetup.tyreCaster[0]) + "°")
        # Tyres FR
        self.ui.psiFRValue.setText(str(self.viewSetup.tyrePressure[1]) + " psi")
        self.ui.toeFRValue.setText(str(self.viewSetup.tyreToe[1]) + "°")
        self.ui.camberFRValue.setText(str(self.viewSetup.tyreCamber[1]) + "°")
        self.ui.casterFRValue.setText(str(self.viewSetup.tyreCaster[1]) + "°")
        # Tyres RL
        self.ui.psiRLValue.setText(str(self.viewSetup.tyrePressure[2]) + " psi")
        self.ui.toeRLValue.setText(str(self.viewSetup.tyreToe[2]) + "°")
        self.ui.camberRLValue.setText(str(self.viewSetup.tyreCamber[2]) + "°")
        # Tyres RR
        self.ui.psiRRValue.setText(str(self.viewSetup.tyrePressure[3]) + " psi")
        self.ui.toeRRValue.setText(str(self.viewSetup.tyreToe[3]) + "°")
        self.ui.camberRRValue.setText(str(self.viewSetup.tyreCamber[3]) + "°")
        # Electronics
        self.ui.tc1Value.setText(str(self.viewSetup.tc1))
        self.ui.tc2Value.setText(str(self.viewSetup.tc2))
        self.ui.absValue.setText(str(self.viewSetup.abs))
        self.ui.ecuValue.setText(str(self.viewSetup.ecu))
        # Fuel and strategy
        self.ui.fuelValue.setText(str(self.viewSetup.fuel))
        self.ui.tyreSetValue.setText(str(self.viewSetup.tyreSet))
        self.ui.frontBrakePadsValue.setText(str(self.viewSetup.frontBrakePad))
        self.ui.rearBrakePadsValue.setText(str(self.viewSetup.rearBrakePad))
        # Mechanical grip
        # Front
        self.ui.frontARBValue.setText(str(self.viewSetup.frontARB))
        self.ui.brakePowerValue.setText(str(self.viewSetup.brakePower) + "%")
        self.ui.brakeBiasValue.setText(str(self.viewSetup.brakeBias) + "%")
        self.ui.steeringRatioValue.setText(str(self.viewSetup.steeringRatio))
        # Front left
        self.ui.frontLeftWheelRateValue.setText(str(self.viewSetup.wheelRate[0]) + " N/m")
        self.ui.frontLeftBumpstopRangeValue.setText(str(self.viewSetup.bumpStopRange[0]))
        self.ui.frontLeftBumpstopRateValue.setText(str(self.viewSetup.bumpStopRate[0]) + " N")
        # Front right
        self.ui.frontRightWheelRateValue.setText(str(self.viewSetup.wheelRate[1]) + " N/m")
        self.ui.frontRightBumpstopRangeValue.setText(str(self.viewSetup.bumpStopRange[1]))
        self.ui.frontRightBumpstopRateValue.setText(str(self.viewSetup.bumpStopRate[1]) + " N")
        # Rear left
        self.ui.rearLeftWheelRateValue.setText(str(self.viewSetup.wheelRate[2]) + " N/m")
        self.ui.rearLeftBumpstopRangeValue.setText(str(self.viewSetup.bumpStopRange[2]))
        self.ui.rearLeftBumpstopRateValue.setText(str(self.viewSetup.bumpStopRate[2]) + " N")
        # Rear right
        self.ui.rearRightWheelRateValue.setText(str(self.viewSetup.wheelRate[3]) + " N/m")
        self.ui.rearRightBumpstopRangeValue.setText(str(self.viewSetup.bumpStopRange[3]))
        self.ui.rearRightBumpstopRateValue.setText(str(self.viewSetup.bumpStopRate[3]) + " N")
        # Dampers
        # Front left
        self.ui.slowBumpFLValue.setText(str(self.viewSetup.bumpSlow[0]))
        self.ui.slowReboundFLValue.setText(str(self.viewSetup.reboundSlow[0]))
        self.ui.fastBumpFLValue.setText(str(self.viewSetup.bumpFast[0]))
        self.ui.fastReboundFLValue.setText(str(self.viewSetup.reboundFast[0]))
        # Front right
        self.ui.slowBumpFRValue.setText(str(self.viewSetup.bumpSlow[1]))
        self.ui.slowReboundFRValue.setText(str(self.viewSetup.reboundSlow[1]))
        self.ui.fastBumpFRValue.setText(str(self.viewSetup.bumpFast[1]))
        self.ui.fastReboundFRValue.setText(str(self.viewSetup.reboundFast[1]))
        # Rear left
        self.ui.slowBumpRLValue.setText(str(self.viewSetup.bumpSlow[2]))
        self.ui.slowReboundRLValue.setText(str(self.viewSetup.reboundSlow[2]))
        self.ui.fastBumpRLValue.setText(str(self.viewSetup.bumpFast[2]))
        self.ui.fastReboundRLValue.setText(str(self.viewSetup.reboundFast[2]))
        # Rear right
        self.ui.slowBumpRRValue.setText(str(self.viewSetup.bumpSlow[3]))
        self.ui.slowReboundRRValue.setText(str(self.viewSetup.reboundSlow[3]))
        self.ui.fastBumpRRValue.setText(str(self.viewSetup.bumpFast[3]))
        self.ui.fastReboundRRValue.setText(str(self.viewSetup.reboundFast[3]))
        # Aero
        # Rear
        self.ui.rearRideHeightValue.setText(str(self.viewSetup.rideHeight[1]) + " mm")
        self.ui.wingValue.setText(str(self.viewSetup.rearWing))
        self.ui.rearBrakeDuctValue.setText(str(self.viewSetup.brakeDucts[1]))
        # Front
        self.ui.frontRideHeightValue.setText(str(self.viewSetup.rideHeight[0]) + " mm")
        self.ui.splitterValue.setText(str(self.viewSetup.frontSpliter))
        self.ui.frontBrakeDuctValue.setText(str(self.viewSetup.brakeDucts[0]))