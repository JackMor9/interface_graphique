# Importer le fichier .ui  converti en .py
import interface_graphique

#Importer le module sys nécessaire à l'exécution
import sys
#Importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets

class MaFenetre(QtWidgets.QMainWindow, interface_graphique.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MaFenetre, self).__init__(parent)
        self.setupUi(self) # Préparer l'interface utilisateur

    #Gestionnaire d'événement
    def on_Button_Etudiant_clicked(self):
        self.label_affichage.setText("BlaBla....")


def main():
    mon_app = QtWidgets.QApplication(sys.argv)
    mon_formulaire1 = MaFenetre()
    #mon_formulaire2 = MaFenetre()
    mon_formulaire1.show()
    mon_app.exec()


if __name__=="__main__":
    main()
#bbaaba
