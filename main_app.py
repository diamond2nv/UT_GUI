# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:32:15 2016

@author: Ralph
"""

from pi_init import startup, waitontarget
from pipython import GCSDevice


import sys
import time
import Queue
import threading
from PyQt4 import QtGui

import lift_gui
import ctrl_receiver
import ctrl_donor
import global_parameters

class MainApp(QtGui.QMainWindow, lift_gui.Ui_MainWindow):
    def __init__(self,q1,q2,q3):
        super(self.__class__, self).__init__()
        self.setupUi(self)  

        self.active=False
        self.receiver_q=Queue.Queue()
        self.receiver_q=q1
        self.status_q=Queue.Queue()
        self.status_q=q2
        self.donor_q=Queue.Queue()
        self.donor_q=q3
        self.status_t=threading.Thread(target=self.status_loop)
        self.update_options = {
                                'update_receiver_x' : self.update_receiver_x,
                                'update_receiver_y' : self.update_receiver_y,
                                'update_receiver_z' : self.update_receiver_z,
                                'update_donor_x' : self.update_donor_x,
                                }

#        self.actionClose.triggered.connect(self.close)
        self.pushButton_receiver_stepper_x_move_abs.clicked.connect(self.receiver_stepper_x_move_abs)
        self.lineEdit_receiver_stepper_x_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_x_move_abs.setText('0.000')  
        self.pushButton_receiver_stepper_x_move_rel.clicked.connect(self.receiver_stepper_x_move_rel)
        self.lineEdit_receiver_stepper_x_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_x_move_rel.setText('0.000')     
        self.pushButton_receiver_stepper_x_home.clicked.connect(self.receiver_stepper_x_home)
        
        self.pushButton_receiver_stepper_y_move_abs.clicked.connect(self.receiver_stepper_y_move_abs)
        self.lineEdit_receiver_stepper_y_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_y_move_abs.setText('0.000')  
        self.pushButton_receiver_stepper_y_move_rel.clicked.connect(self.receiver_stepper_y_move_rel)
        self.lineEdit_receiver_stepper_y_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_y_move_rel.setText('0.000')     
        self.pushButton_receiver_stepper_y_home.clicked.connect(self.receiver_stepper_y_home)
        
        self.pushButton_receiver_stepper_z_move_abs.clicked.connect(self.receiver_stepper_z_move_abs)
        self.lineEdit_receiver_stepper_z_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_z_move_abs.setText('0.000')  
        self.pushButton_receiver_stepper_z_move_rel.clicked.connect(self.receiver_stepper_z_move_rel)
        self.lineEdit_receiver_stepper_z_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_receiver_stepper_z_move_rel.setText('0.000')     
        self.pushButton_receiver_stepper_z_home.clicked.connect(self.receiver_stepper_z_home)
        
        self.pushButton_donor_x_move_abs.clicked.connect(self.donor_x_move_abs)
        self.lineEdit_donor_x_move_abs.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_donor_x_move_abs.setText('0.000')  
        self.pushButton_donor_x_move_rel.clicked.connect(self.donor_x_move_rel)
        self.lineEdit_donor_x_move_rel.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_donor_x_move_rel.setText('0.000')     
        self.pushButton_donor_x_home.clicked.connect(self.donor_x_home)
        
    def status_loop(self):
        while self.active==True:
#            print 'status active'
            time.sleep(0.1)

            if not self.status_q.empty():        
                item=self.status_q.get()
                self.update_options[item[0]](item[1])
                self.status_q.task_done()
        
    def run(self):
        self.active=True
        self.status_t.start()

    def stop(self):
        self.active=False
        self.status_t.join()

    def receiver_stepper_x_move_abs(self):
        print("Command sent")
        self.receiver_q.put(['move_abs_x',float(self.lineEdit_receiver_stepper_x_move_abs.text())],False)
        
    def receiver_stepper_x_move_rel(self):
        print("Command sent")
        self.receiver_q.put(['move_rel_x',float(self.lineEdit_receiver_stepper_x_move_rel.text())],False)
        
    def receiver_stepper_x_home(self):
        print("Command sent")
        self.receiver_q.put(['home_x',0],False)
        
    def receiver_stepper_y_move_abs(self):
        print("Command sent")
        self.receiver_q.put(['move_abs_y',float(self.lineEdit_receiver_stepper_y_move_abs.text())],False)
        
    def receiver_stepper_y_move_rel(self):
        print("Command sent")
        self.receiver_q.put(['move_rel_y',float(self.lineEdit_receiver_stepper_y_move_rel.text())],False)
        
    def receiver_stepper_y_home(self):
        print("Command sent")
        self.receiver_q.put(['home_y',0],False)
        
    def receiver_stepper_z_move_abs(self):
        print("Command sent")
        self.receiver_q.put(['move_abs_z',float(self.lineEdit_receiver_stepper_z_move_abs.text())],False)
        
    def receiver_stepper_z_move_rel(self):
        print("Command sent")
        self.receiver_q.put(['move_rel_z',float(self.lineEdit_receiver_stepper_z_move_rel.text())],False)
        
    def receiver_stepper_z_home(self):
        print("Command sent")
        self.receiver_q.put(['home_z',0],False)
        
    def donor_x_move_abs(self):
        print("Command sent")
        self.donor_q.put(['move_abs_x',float(self.lineEdit_donor_x_move_abs.text())],False)
        
    def donor_x_move_rel(self):
        print("Command sent")
        self.donor_q.put(['move_rel_x',float(self.lineEdit_donor_x_move_rel.text())],False)
        
    def donor_x_home(self):
        print("Command sent")
        self.donor_q.put(['home_x',0],False)
        
        
    def update_receiver_x(self,pos):
        self.lcdNumber_receiver_stepper_x.display(pos) 
        global gbl_receiver_x_pos
        gbl_receiver_x_pos=pos
               
    def update_receiver_y(self,pos):
        self.lcdNumber_receiver_stepper_y.display(pos) 
        global gbl_receiver_y_pos
        gbl_receiver_y_pos=pos
        
    def update_receiver_z(self,pos):
        self.lcdNumber_receiver_stepper_z.display(pos) 
        global gbl_receiver_z_pos
        gbl_receiver_z_pos=pos
        
    def update_donor_x(self,pos):
        self.lcdNumber_donor_x.display(pos) 
        global gbl_receiver_x_pos
        gbl_donor_x_pos=pos
        

def main():
    receiver_q = Queue.Queue()
    donor_q = Queue.Queue()
    status_q = Queue.Queue()
    ctl_receiver=ctrl_receiver.control_receiver(receiver_q,status_q)
    ctl_receiver.run()
    ctl_donor=ctrl_donor.control_donor(donor_q,status_q)
    ctl_donor.run()
    
    app = QtGui.QApplication(sys.argv)  
    form = MainApp(receiver_q,status_q,donor_q)
    form.run()
    form.show()                         
    app.exec_()
    form.stop()
    
    time.sleep(1)
    ctl_receiver.stop()
    ctl_donor.stop()


if __name__ == '__main__':              
    main()  
