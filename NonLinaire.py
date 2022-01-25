# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NonLineaire.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator_NonLineaire(object):
    def setupUi(self, Calculator_NonLineaire):
        Calculator_NonLineaire.setObjectName("Calculator_NonLineaire")
        Calculator_NonLineaire.resize(1155, 836)
        Calculator_NonLineaire.setStyleSheet("background-color: rgb(196, 200, 255);")
        self.titre = QtWidgets.QLabel(Calculator_NonLineaire)
        self.titre.setGeometry(QtCore.QRect(120, 0, 501, 71))
        self.titre.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 22pt \"Monotype Corsiva\";")
        self.titre.setObjectName("titre")
        self.methodes = QtWidgets.QComboBox(Calculator_NonLineaire)
        self.methodes.setGeometry(QtCore.QRect(310, 100, 161, 21))
        self.methodes.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 12pt \"Monotype Corsiva\";")
        self.methodes.setObjectName("methodes")
        self.methodes.addItem("")
        self.methodes.addItem("")
        self.methodes.addItem("")
        self.methodes.addItem("")
        self.label_2 = QtWidgets.QLabel(Calculator_NonLineaire)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 271, 41))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.label_2.setObjectName("label_2")
        self.nameFonctionObje = QtWidgets.QLabel(Calculator_NonLineaire)
        self.nameFonctionObje.setGeometry(QtCore.QRect(10, 140, 161, 41))
        self.nameFonctionObje.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.nameFonctionObje.setObjectName("nameFonctionObje")
        self.tableWidget = QtWidgets.QTableWidget(Calculator_NonLineaire)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 801, 71))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.a = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.a.setGeometry(QtCore.QRect(50, 230, 113, 22))
        self.a.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a.setObjectName("a")
        self.b = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.b.setGeometry(QtCore.QRect(180, 230, 113, 22))
        self.b.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.b.setObjectName("b")
        self.c = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.c.setGeometry(QtCore.QRect(300, 230, 113, 22))
        self.c.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c.setObjectName("c")
        self.f = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.f.setGeometry(QtCore.QRect(680, 230, 113, 22))
        self.f.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.f.setObjectName("f")
        self.e = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.e.setGeometry(QtCore.QRect(550, 230, 113, 22))
        self.e.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e.setObjectName("e")
        self.d = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.d.setGeometry(QtCore.QRect(430, 230, 113, 22))
        self.d.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.d.setObjectName("d")
        self.label_4 = QtWidgets.QLabel(Calculator_NonLineaire)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 511, 41))
        self.label_4.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.label_4.setObjectName("label_4")
        self.x0 = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.x0.setGeometry(QtCore.QRect(110, 340, 113, 22))
        self.x0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x0.setObjectName("x0")
        self.x1 = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.x1.setGeometry(QtCore.QRect(320, 340, 113, 22))
        self.x1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x1.setObjectName("x1")
        self.epsi = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.epsi.setGeometry(QtCore.QRect(560, 340, 113, 22))
        self.epsi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.epsi.setObjectName("epsi")
        self.pas = QtWidgets.QLineEdit(Calculator_NonLineaire)
        self.pas.setGeometry(QtCore.QRect(780, 340, 113, 22))
        self.pas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pas.setText("")
        self.pas.setObjectName("pas")
        self.namex0 = QtWidgets.QLabel(Calculator_NonLineaire)
        self.namex0.setGeometry(QtCore.QRect(70, 330, 31, 31))
        self.namex0.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.namex0.setObjectName("namex0")
        self.namepas = QtWidgets.QLabel(Calculator_NonLineaire)
        self.namepas.setGeometry(QtCore.QRect(730, 330, 41, 31))
        self.namepas.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.namepas.setObjectName("namepas")
        self.nameepsilon = QtWidgets.QLabel(Calculator_NonLineaire)
        self.nameepsilon.setGeometry(QtCore.QRect(480, 330, 71, 31))
        self.nameepsilon.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.nameepsilon.setObjectName("nameepsilon")
        self.namex1 = QtWidgets.QLabel(Calculator_NonLineaire)
        self.namex1.setGeometry(QtCore.QRect(280, 330, 31, 31))
        self.namex1.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.namex1.setObjectName("namex1")
        self.solve = QtWidgets.QPushButton(Calculator_NonLineaire)
        self.solve.setGeometry(QtCore.QRect(410, 400, 131, 31))
        self.solve.setStyleSheet("\n"
"font: italic 14pt \"Monotype Corsiva\";\n"
"background-color: rgb(196, 200, 255);")
        self.solve.setObjectName("solve")
        self.label_9 = QtWidgets.QLabel(Calculator_NonLineaire)
        self.label_9.setGeometry(QtCore.QRect(60, 420, 81, 41))
        self.label_9.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 14pt \"Monotype Corsiva\";")
        self.label_9.setObjectName("label_9")
        self.Resultat_Tableau = QtWidgets.QTextEdit(Calculator_NonLineaire)
        self.Resultat_Tableau.setGeometry(QtCore.QRect(63, 466, 891, 331))
        self.Resultat_Tableau.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Resultat_Tableau.setObjectName("Resultat_Tableau")
        self.label_10 = QtWidgets.QLabel(Calculator_NonLineaire)
        self.label_10.setGeometry(QtCore.QRect(970, 810, 191, 31))
        self.label_10.setStyleSheet("\n"
"background-color: rgb(244, 222, 255);\n"
"font: italic 10pt \"Monotype Corsiva\";")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Calculator_NonLineaire)
        QtCore.QMetaObject.connectSlotsByName(Calculator_NonLineaire)

    def retranslateUi(self, Calculator_NonLineaire):
        _translate = QtCore.QCoreApplication.translate
        Calculator_NonLineaire.setWindowTitle(_translate("Calculator_NonLineaire", "Dialog"))
        self.titre.setText(_translate("Calculator_NonLineaire", "      Méthodes d\'optimisations "))
        self.methodes.setItemText(0, _translate("Calculator_NonLineaire", "Newton Raphson"))
        self.methodes.setItemText(1, _translate("Calculator_NonLineaire", "Dichotomie"))
        self.methodes.setItemText(2, _translate("Calculator_NonLineaire", "Pas fixe"))
        self.methodes.setItemText(3, _translate("Calculator_NonLineaire", "Pas accéléré "))
        self.label_2.setText(_translate("Calculator_NonLineaire", "Choisissez la méthode de calcul :"))
        self.nameFonctionObje.setText(_translate("Calculator_NonLineaire", "Fonction objective"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Calculator_NonLineaire", "f(x)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Calculator_NonLineaire", "x^5"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Calculator_NonLineaire", "x^4"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Calculator_NonLineaire", "x^3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Calculator_NonLineaire", "x^2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Calculator_NonLineaire", "x"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Calculator_NonLineaire", "Constante"))
        self.label_4.setText(_translate("Calculator_NonLineaire", "Veuillez entrer les valeurs suivantes selon la méthode choisie :"))
        self.namex0.setText(_translate("Calculator_NonLineaire", "x0"))
        self.namepas.setText(_translate("Calculator_NonLineaire", "Pas"))
        self.nameepsilon.setText(_translate("Calculator_NonLineaire", "Epsilon"))
        self.namex1.setText(_translate("Calculator_NonLineaire", "x1"))
        self.solve.setText(_translate("Calculator_NonLineaire", "Résoudre"))
        self.label_9.setText(_translate("Calculator_NonLineaire", "Résultat"))
        self.label_10.setText(_translate("Calculator_NonLineaire", "Designed by Manal NEJMI"))
        
        self.solve.clicked.connect(self.solve_clicked)
        
    def solve_clicked(self):
        self.Resultat_Tableau.clear()
        if self.methodes.currentIndex()==0: #Newton Raphtson
        
            # eps= 0.01
            # xi=3
            eps= float(self.epsi.text())
            xi= float(self.x0.text())
                #calcul de la fonction objective
            def f(x,a,b,c,d,e,f):
                return a*(x**5)+b*(x**4)+c*(x**3)+d*(x**2)+e*x+f
                #calcul des dérivées première et seconde de cette fonction:
            def f1(x,a,b,c,d,e): #premère dérivé
                return 5*a*(x**4) + 4*b*(x**3)+ 3*c*(x**2)+ 2*d*x + e
            def f2(x,a,b,c,d):#dérivé f
                return 20*a*(x**3) + 12*b*(x**2)+ 6*c*x+ 2*d
                #On repète l'opération tant que espsilon est grand
                
            while True:
                xf=xi-f1(xi,float(self.a.text()),float(self.b.text()),float(self.c.text()),float(self.d.text()),float(self.e.text()))/f2(xi, float(self.a.text()),float(self.b.text()),float(self.c.text()),float(self.d.text()))
                if abs(f1(xf,float(self.a.text()),float(self.b.text()),float(self.c.text()),float(self.d.text()),float(self.e.text()))) <= eps:
                    break
                xi=xf
                    
            print (xf)
            self.Resultat_Tableau.setText("Le point optimum est: " +str(xf)) 
        elif self.methodes.currentIndex()==1: #Dichotomie // Bissection
            a=float(self.a.text())
            b=float(self.b.text())
            c=float(self.c.text())
            d=float(self.d.text())
            e=float(self.e.text())
            f=float(self.f.text())
            def fonction(x):
                return a*(x**5)+b*(x**4)+c*(x**3)+d*(x**2)+e*x+f
            
    
            def bissec(a,b,epsilon,optimum):
                x0=(a+b)/2
                x1=(a+x0)/2
                x2=(x0+b)/2
                f0 = fonction(x0)
                f1 = fonction(x1)
                f2 = fonction(x2)
                if optimum == 'mini':
                    if f2>f0 and f0>f1:
                        b=x0
                    elif f2<f0 and f0<f1:
                        a=x0
                    elif f1>f0 and f2>f0:
                        a=x1
                        b=x2
                elif optimum == 'maxi':
                    if f2>f0 and f0>f1:
                        a=x0
                    elif f2<f0 and f0<f1:
                        b=x0
                    elif f1>f0 and f2>f0:
                        if f1==max(f1,f2):
                            b=x1
                        else:
                            a=x2
                return(a,b)
            
            def biss(a,b,optimum,epsilon):
                while (b-a)>epsilon:
                    (a,b)=bissec(a,b,epsilon,optimum)
                return (a+b)/2
            
            eps= float(self.epsi.text())
            x0= float(self.x0.text())
            x1= float(self.x1.text())
            
            xfinal=biss(x0,x1,"mini",eps)
            
            self.Resultat_Tableau.setText("Le point optimum est: " +str(xfinal)) 
        
        #elif self.methode.currentIndex()==2: #Pas fixe
        #else:#Pas accéléré
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator_NonLineaire = QtWidgets.QDialog()
    ui = Ui_Calculator_NonLineaire()
    ui.setupUi(Calculator_NonLineaire)
    Calculator_NonLineaire.show()
    sys.exit(app.exec_())

