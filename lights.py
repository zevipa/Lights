#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys


class Lights(QtGui.QWidget):

    def __init__(self):
        super(Lights, self).__init__()
        self.createBlocks()
        self.initUi()

    def createBlocks(self):
        """Create the 9 clickable boxes"""
        # Main colors of the boxes
        self.light = QtGui.QPixmap("light.png")
        self.dark = QtGui.QPixmap("dark.png")
        
        self.block1 = QtGui.QLabel()  # The "blocks" are labels with an image with click events 
        self.block1.mousePressEvent = lambda event:self.block1_click()  # Add a mouse press event 
        self.block1.setPixmap(self.dark)  # The block is dark by default
        # If blckxlight is 0, the block should be dark, if it is 1, it should be light
        self.blck1Light = 0 # A variable to track whether the block is light or dark

        self.block2 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block2.mousePressEvent = lambda event:self.block2_click()
        self.blck2Light = 0

        self.block3 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block3.mousePressEvent = lambda event:self.block3_click()
        self.blck3Light = 0

        self.block4 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block4.mousePressEvent = lambda event:self.block4_click()
        self.blck4Light = 0

        self.block5 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block5.mousePressEvent = lambda event:self.block5_click()
        self.blck5Light = 0

        self.block6 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block6.mousePressEvent = lambda event:self.block6_click()
        self.blck6Light = 0

        self.block7 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block7.mousePressEvent = lambda event:self.block7_click()
        self.blck7Light = 0

        self.block8 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block8.mousePressEvent = lambda event:self.block8_click()
        self.blck8Light = 0

        self.block9 = QtGui.QLabel(pixmap=self.dark)  # The block is dark by default
        self.block9.mousePressEvent = lambda event:self.block9_click()
        self.blck9Light = 0

    def initUi(self):

        self.grid = QtGui.QGridLayout()  # main grid for the boxes
        # Add all the squares to the grid
        self.grid.addWidget(self.block1, 0, 0)
        self.grid.addWidget(self.block2, 0, 1)
        self.grid.addWidget(self.block3, 0, 2)
        self.grid.addWidget(self.block4, 1, 0)
        self.grid.addWidget(self.block5, 1, 1)
        self.grid.addWidget(self.block6, 1, 2)
        self.grid.addWidget(self.block7, 2, 0)
        self.grid.addWidget(self.block8, 2, 1)
        self.grid.addWidget(self.block9, 2, 2)
        
        # A reset button to darken all the boxes 
        resetButton = QtGui.QPushButton('Reset')
        resetButton.clicked.connect(self.reset)
        # An about button that shows an about dialog
        helpButton = QtGui.QPushButton('Help')
        helpButton.clicked.connect(self.help)

        # Create an hbox for 3 buttons
        self.bttnBox = QtGui.QHBoxLayout()
        self.bttnBox.setSpacing(0)
        self.bttnBox.addWidget(resetButton)
        self.bttnBox.addWidget(helpButton)

        # Label that will display something once the user has won
        self.winLabel = QtGui.QLabel('Congrats! You have won!')
        self.winLabel.hide()

        self.vbox = QtGui.QVBoxLayout()  # main vbox for the grid and label 
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.bttnBox)
        self.vbox.addWidget(self.winLabel)
        
        self.setLayout(self.vbox)  # Make the grid the layout of the window
        
        self.setWindowTitle('Lights')
        self.setGeometry(300, 300, 0, 0)
        self.setFixedSize(0,0)  # So the window is at its minimum size, and can't be maximized
        self.show()

    def reset(self):
        """Make all the squares dark"""
        self.blck1Light = 0
        self.block1.setPixmap(self.dark)

        self.blck2Light = 0
        self.block2.setPixmap(self.dark)

        self.blck3Light = 0
        self.block3.setPixmap(self.dark)

        self.blck4Light = 0
        self.block4.setPixmap(self.dark)

        self.blck5Light = 0
        self.block5.setPixmap(self.dark)

        self.blck6Light = 0
        self.block6.setPixmap(self.dark)

        self.blck7Light = 0
        self.block7.setPixmap(self.dark)

        self.blck8Light = 0
        self.block8.setPixmap(self.dark)
        
        self.blck9Light = 0
        self.block9.setPixmap(self.dark)

        # Hide the winning! label
        self.winLabel.hide()      

    def help(self):
        """Open a help dialog"""
        helpMessage = """The object of the game Lights is to light up every square on the grid."""
        hlp = QtGui.QMessageBox()
        hlp.information(self, "hai", helpMessage)

    def block1_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck1Light == 0: # If it is dark
            # Make it light
            self.blck1Light = 1   
            self.block1.setPixmap(self.light)

        elif self.blck1Light == 1: # If it is lit 
            self.blck1Light = 0  # Make it dark 
            self.block1.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck2Light == 0:
            self.blck2Light = 1
            self.block2.setPixmap(self.light)
        elif self.blck2Light == 1:
            self.blck2Light = 0
            self.block2.setPixmap(self.dark)
            
        if self.blck4Light == 0:
            self.blck4Light = 1
            self.block4.setPixmap(self.light)
        elif self.blck4Light == 1:
            self.blck4Light = 0
            self.block4.setPixmap(self.dark)
        self.check()

    def block2_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck2Light == 0: # If it is dark
            # Make it light
            self.blck2Light = 1   
            self.block2.setPixmap(self.light)

        elif self.blck2Light == 1: # If it is lit 
            self.blck2Light = 0  # Make it dark 
            self.block2.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck1Light == 0:
            self.blck1Light = 1
            self.block1.setPixmap(self.light)
        elif self.blck1Light == 1:
            self.blck1Light = 0
            self.block1.setPixmap(self.dark)

        if self.blck3Light == 0:
            self.blck3Light = 1
            self.block3.setPixmap(self.light)
        elif self.blck3Light == 1:
            self.blck3Light = 0
            self.block3.setPixmap(self.dark)

        if self.blck5Light == 0:
            self.blck5Light = 1
            self.block5.setPixmap(self.light)
        elif self.blck5Light == 1:
            self.blck5Light = 0
            self.block5.setPixmap(self.dark)
        self.check()

    def block3_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck3Light == 0: # If it is dark
            # Make it light
            self.blck3Light = 1   
            self.block3.setPixmap(self.light)

        elif self.blck3Light == 1: # If it is lit 
            self.blck3Light = 0  # Make it dark 
            self.block3.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck2Light == 0:
            self.blck2Light = 1
            self.block2.setPixmap(self.light)
        elif self.blck2Light == 1:
            self.blck2Light = 0
            self.block2.setPixmap(self.dark)
            
        if self.blck6Light == 0:
            self.blck6Light = 1
            self.block6.setPixmap(self.light)
        elif self.blck6Light == 1:
            self.blck6Light = 0
            self.block6.setPixmap(self.dark)
        self.check()

    def block4_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck4Light == 0: # If it is dark
            # Make it light
            self.blck4Light = 1   
            self.block4.setPixmap(self.light)

        elif self.blck4Light == 1: # If it is lit 
            self.blck4Light = 0  # Make it dark 
            self.block4.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck1Light == 0:
            self.blck1Light = 1
            self.block1.setPixmap(self.light)
        elif self.blck1Light == 1:
            self.blck1Light = 0
            self.block1.setPixmap(self.dark)

        if self.blck5Light == 0:
            self.blck5Light = 1
            self.block5.setPixmap(self.light)
        elif self.blck5Light == 1:
            self.blck5Light = 0
            self.block5.setPixmap(self.dark)

        if self.blck7Light == 0:
            self.blck7Light = 1
            self.block7.setPixmap(self.light)
        elif self.blck7Light == 1:
            self.blck7Light = 0
            self.block7.setPixmap(self.dark)
        self.check()

    def block5_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck5Light == 0: # If it is dark
            # Make it light
            self.blck5Light = 1   
            self.block5.setPixmap(self.light)

        elif self.blck5Light == 1: # If it is lit 
            self.blck5Light = 0  # Make it dark 
            self.block5.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck2Light == 0:
            self.blck2Light = 1
            self.block2.setPixmap(self.light)
        elif self.blck2Light == 1:
            self.blck2Light = 0
            self.block2.setPixmap(self.dark)

        if self.blck4Light == 0:
            self.blck4Light = 1
            self.block4.setPixmap(self.light)
        elif self.blck4Light == 1:
            self.blck4Light = 0
            self.block4.setPixmap(self.dark)

        if self.blck6Light == 0:
            self.blck6Light = 1
            self.block6.setPixmap(self.light)
        elif self.blck6Light == 1:
            self.blck6Light = 0
            self.block6.setPixmap(self.dark)

        if self.blck8Light == 0:
            self.blck8Light = 1
            self.block8.setPixmap(self.light)
        elif self.blck8Light == 1:
            self.blck8Light = 0
            self.block8.setPixmap(self.dark)
        self.check()

    def block6_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck6Light == 0: # If it is dark
            # Make it light
            self.blck6Light = 1   
            self.block6.setPixmap(self.light)

        elif self.blck6Light == 1: # If it is lit 
            self.blck6Light = 0  # Make it dark 
            self.block6.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck3Light == 0:
            self.blck3Light = 1
            self.block3.setPixmap(self.light)
        elif self.blck3Light == 1:
            self.blck3Light = 0
            self.block3.setPixmap(self.dark)

        if self.blck5Light == 0:
            self.blck5Light = 1
            self.block5.setPixmap(self.light)
        elif self.blck5Light == 1:
            self.blck5Light = 0
            self.block5.setPixmap(self.dark)

        if self.blck9Light == 0:
            self.blck9Light = 1
            self.block9.setPixmap(self.light)
        elif self.blck9Light == 1:
            self.blck9Light = 0
            self.block9.setPixmap(self.dark)
        self.check()

    def block7_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck7Light == 0: # If it is dark
            # Make it light
            self.blck7Light = 1   
            self.block7.setPixmap(self.light)

        elif self.blck7Light == 1: # If it is lit 
            self.blck7Light = 0  # Make it dark 
            self.block7.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck4Light == 0:
            self.blck4Light = 1
            self.block4.setPixmap(self.light)
        elif self.blck4Light == 1:
            self.blck4Light = 0
            self.block4.setPixmap(self.dark)
            
        if self.blck8Light == 0:
            self.blck8Light = 1
            self.block8.setPixmap(self.light)
        elif self.blck8Light == 1:
            self.blck8Light = 0
            self.block8.setPixmap(self.dark)
        self.check()

    def block8_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck8Light == 0: # If it is dark
            # Make it light
            self.blck8Light = 1   
            self.block8.setPixmap(self.light)

        elif self.blck8Light == 1: # If it is lit 
            self.blck8Light = 0  # Make it dark 
            self.block8.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck5Light == 0:
            self.blck5Light = 1
            self.block5.setPixmap(self.light)
        elif self.blck5Light == 1:
            self.blck5Light = 0
            self.block5.setPixmap(self.dark)

        if self.blck7Light == 0:
            self.blck7Light = 1
            self.block7.setPixmap(self.light)
        elif self.blck7Light == 1:
            self.blck7Light = 0
            self.block7.setPixmap(self.dark)

        if self.blck9Light == 0:
            self.blck9Light = 1
            self.block9.setPixmap(self.light)
        elif self.blck9Light == 1:
            self.blck9Light = 0
            self.block9.setPixmap(self.dark)
        self.check()

    def block9_click(self):
        """ Light or darken the block and all adjacent blocks"""
        if self.blck9Light == 0: # If it is dark
            # Make it light
            self.blck9Light = 1   
            self.block9.setPixmap(self.light)

        elif self.blck9Light == 1: # If it is lit 
            self.blck9Light = 0  # Make it dark 
            self.block9.setPixmap(self.dark)

        # Check the adjacent blocks
        if self.blck6Light == 0:
            self.blck6Light = 1
            self.block6.setPixmap(self.light)
        elif self.blck6Light == 1:
            self.blck6Light = 0
            self.block6.setPixmap(self.dark)
            
        if self.blck8Light == 0:
            self.blck8Light = 1
            self.block8.setPixmap(self.light)
        elif self.blck8Light == 1:
            self.blck8Light = 0
            self.block8.setPixmap(self.dark)
        self.check()

    def check(self):
        """Check if the board is fully lit"""
        if self.blck1Light == 1 and self.blck2Light == 1 and self.blck3Light == 1 and self.blck4Light == 1 and self.blck5Light == 1 and self.blck6Light == 1 and self.blck7Light == 1 and self.blck8Light == 1 and self.blck9Light == 1:
            self.winLabel.show()
        else:
            # if all of the blocks aren't lit, or they aren't lit anymore
            self.winLabel.hide()


def main():
    app = QtGui.QApplication(sys.argv)
    lights = Lights()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
