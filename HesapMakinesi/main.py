import sys
from PyQt5.QtWidgets import QApplication
from HesapMakinesi.hesapMakinesi import Hm_arayuz

uygulama = QApplication(sys.argv)

hesap_makinesi = Hm_arayuz()
sys.exit(uygulama.exec_())