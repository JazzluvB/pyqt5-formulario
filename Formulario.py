# Autor: Carlos Palacios
# Python 3.9.7
# Qt: 5
# Librerias
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys
import re # Verificar correo electronico y un domini valido

# Variables CCS Globales
estilo_etiquetas = """
QLabel{
background: none;
color:#FFFFFF;
font-weight:600;
border:none;
border-radius: 6px;                                    
    }
"""

# Estilo Cajas
estilo_cajas = """
QLineEdit{
background: none;
color:#FFFFFF;
font-weight:600;
border:none;
border-radius: 10px;                                    
    }
"""

# ---- CLASE PARA LABEL CON EFECTOS ----

# ---- Clase ----
class Formulario(QMainWindow):
    # Constructor
    def __init__(self):
        # Constructor de la clase heredada
        super().__init__()
        # Mandar llamar la interfaz
        self.interfaz()
        
    def interfaz(self):
        # Ventana
        self.setFixedSize(400, 420)
        self.setWindowTitle("Formulario")
        self.setWindowIcon(QIcon("C:/Users/soporte/Desktop/Python769/7035146.png"))
        self.setStyleSheet("Background-color:#1C1C1E; color: #776F6F")
        
        # Titulo
        self.lbtitulo = QLabel(self)
        self.lbtitulo.setText("Formulario De Registro")
        self.lbtitulo.setGeometry(50, 15, 300, 40)
        self.lbtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitulo.setFont(QFont("Helvetica Neue", 16))
        self.lbtitulo.setStyleSheet(estilo_etiquetas)
        


        # Nombre
        self.lbNombre = QLabel(self)
        self.lbNombre.setText("Nombre:")
        self.lbNombre.setGeometry(20, 70, 100, 30)
        self.lbNombre.setAlignment(QtCore.Qt.AlignLeft)
        self.lbNombre.setFont(QFont("Helvetica Neue", 12))
        self.lbNombre.setStyleSheet(estilo_etiquetas)
        
        # Paterno
        self.lbPaterno = QLabel(self)
        self.lbPaterno.setText("Paterno:")
        self.lbPaterno.setGeometry(20, 120, 100, 30)
        self.lbPaterno.setAlignment(QtCore.Qt.AlignLeft)
        self.lbPaterno.setFont(QFont("Helvetica Neue", 13))
        self.lbPaterno.setStyleSheet(estilo_etiquetas)
        
        # Materno
        self.lbMaterno = QLabel(self)
        self.lbMaterno.setText("Materno:")
        self.lbMaterno.setGeometry(20, 170, 100, 30)
        self.lbMaterno.setAlignment(QtCore.Qt.AlignLeft)
        self.lbMaterno.setFont(QFont("Helvetica Neue", 13))
        self.lbMaterno.setStyleSheet(estilo_etiquetas)
        
        # Correo
        self.lbCorreo = QLabel(self)
        self.lbCorreo.setText("Correo:")
        self.lbCorreo.setGeometry(20, 220, 150, 300)
        self.lbCorreo.setAlignment(QtCore.Qt.AlignLeft)
        self.lbCorreo.setFont(QFont("Helvetica Neue", 13))
        self.lbCorreo.setStyleSheet(estilo_etiquetas)
        
        # Celular
        self.lbCelular = QLabel(self)
        self.lbCelular.setText("Celular:")
        self.lbCelular.setGeometry(20, 270, 150, 30)
        self.lbCelular.setAlignment(QtCore.Qt.AlignLeft)
        self.lbCelular.setFont(QFont("Helvetica Neue", 13))
        self.lbCelular.setStyleSheet(estilo_etiquetas)
        
        # Caja Paterno
        self.txtPaterno = QLineEdit(self)
        self.txtPaterno.setGeometry(170, 120, 200, 30)
        self.txtPaterno.setAlignment(QtCore.Qt.AlignLeft)
        self.txtPaterno.setFont(QFont("Helvetica Neue", 13))
        self.txtPaterno.setStyleSheet(estilo_cajas)
        
        # Caja Materno
        self.txtMaterno = QLineEdit(self)
        self.txtMaterno.setGeometry(170, 170, 200, 30)
        self.txtMaterno.setAlignment(QtCore.Qt.AlignLeft)
        self.txtMaterno.setFont(QFont("Helvetica Neue", 13))
        self.txtMaterno.setStyleSheet(estilo_cajas)
        
        
        # Caja Nombre
        self.txtNombre = QLineEdit(self)
        self.txtNombre.setGeometry(170, 70, 200, 30)
        self.txtNombre.setAlignment(QtCore.Qt.AlignLeft)
        self.txtNombre.setFont(QFont("Helvetica Neue", 13))
        self.txtNombre.setStyleSheet(estilo_cajas)
        

        # Caja Correo
        self.txtCorreo = QLineEdit(self)
        self.txtCorreo.setGeometry(170, 220, 200, 30)
        self.txtCorreo.setAlignment(QtCore.Qt.AlignLeft)
        self.txtCorreo.setFont(QFont("Helvetica Neue", 13))
        self.txtCorreo.setStyleSheet(estilo_cajas)

        # Caja Celular 
        self.txtCelular = QLineEdit(self)
        self.txtCelular.setGeometry(170, 270, 200, 30)
        self.txtCelular.setAlignment(QtCore.Qt.AlignLeft)
        self.txtCelular.setFont(QFont("Helvetica Neue", 13))
        self.txtCelular.setStyleSheet(estilo_cajas)
        # Permitir maximo 10 digitos
        self.txtCelular.setMaxLength(10)
        # Solo permitir numeros al escribir
        self.txtCelular.setValidator(QIntValidator())


        # Cancelar
        self.btnCancelar = QPushButton(self)
        self.btnCancelar.setText("Cancelar")
        self.btnCancelar.setGeometry(270, 370, 120, 35)
        self.btnCancelar.setFont(QFont("San Francisco(SF)", 18))
        self.btnCancelar.setStyleSheet("""
                                        QPushButton{
                                            background-color:#2C2C2E;
                                            color:#FFFFFF;
                                            font-weight:250;
                                            border:2px solid #AA9E9E;
                                            border-radius: 10px; 
                                       }
                                        QPushButton:hover{
                                            background-color:#5A5555;
                                            color:#FFFFFF;
                                       }
                                        QPushButton:pressed{
                                            background-color:#4D4747;
                                            color:#FFFFFF;
                                       }
                                       """)
        
        # Cancelar
        self.btnRegistrar = QPushButton(self)
        self.btnRegistrar.setText("Registrar")
        self.btnRegistrar.setGeometry(140, 370, 120, 35)
        self.btnRegistrar.setFont(QFont("San Francisco(SF)", 18))
        self.btnRegistrar.setStyleSheet("""
                                        QPushButton{
                                            background-color:#2C2C2E;
                                            color:#FFFFFF;
                                            font-weight:250;
                                            border:2px solid #AA9E9E;
                                            border-radius: 10px; 
                                       }
                                        QPushButton:hover{
                                            background-color:#5A5555;
                                            color:#FFFFFF;
                                       }
                                        QPushButton:pressed{
                                            background-color:#4D4747;
                                            color:#FFFFFF;
                                       }
                                       """)


        # Vincular los metodos a los botones 
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnCancelar.clicked.connect(self.cancelar)



    def registrar(self):
      # Variables que reciben los resultados de las verificaciones
      VerificarNombreCompleto = self.validar_nombre()
      verificarCorreo = self.validar_correo()
      # Comprobar el Booleano
      if VerificarNombreCompleto == False:
          QMessageBox.warning(self, "Error", "Capturó un simbolo o digito erroneamente")
          return # Salir 
      

      if verificarCorreo == False:
          QMessageBox.warning(self, "Error", "Capturó un correo sin formato valido")
          return # Salir
    

    def cancelar(self):
        # Limpiar los componentes
        self.txtNombre.setText("")
        self.txtPaterno.setText("")
        self.txtMaterno.setText("")
        self.txtCorreo.setText("")
        self.txtCelular.setText("")
        # Avisar que se cancelo la operacion        
        QMessageBox.warning(self,"Atención", "Se canceló la operacion")

    
    def validar_nombre(self):
        texto = self.txtNombre.text() + self.txtPaterno.text() + self.txtMaterno.text()

        # Expresión regular que permite solo letras, tildes y espacios
        if re.match("^[A-Za-záéíóúÁÉÍÓÚüÜñÑ ]*$", texto):
            return True
        else:
            return False

    def validar_correo(self):
            # Obtener el texto del QLineEdit
            correo = self.txtCorreo.text()

            # Expresión regular para validar un correo electrónico
            patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            
            # Validar correo con el patrón
            if re.match(patron, correo):
                return True
            else:
                return False

    


# Estructura de arranque
if __name__== "__main__":
    # Instancia para iniciar la app
    app = QApplication(sys.argv)
    # Instancia de la clase principal
    formulario = Formulario()
    # Mostrar el FrontEnd
    formulario.show()
    # Ejecutar el BackEnd
    app.exec()