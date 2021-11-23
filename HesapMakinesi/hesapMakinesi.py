from PyQt5 import QtWidgets
from HesapMakinesi.hm_arayüz import Ui_MainWindow

class Hm_arayuz(QtWidgets.QMainWindow,Ui_MainWindow):

    ilksayi = None
    ikincisayi = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #Rakam Butonları...
        self.pb0.clicked.connect(self.rakamlar)
        self.pb1.clicked.connect(self.rakamlar)
        self.pb2.clicked.connect(self.rakamlar)
        self.pb3.clicked.connect(self.rakamlar)
        self.pb4.clicked.connect(self.rakamlar)
        self.pb5.clicked.connect(self.rakamlar)
        self.pb6.clicked.connect(self.rakamlar)
        self.pb7.clicked.connect(self.rakamlar)
        self.pb8.clicked.connect(self.rakamlar)
        self.pb9.clicked.connect(self.rakamlar)

        #Nokta Butonu...
        self.nokta.clicked.connect(self.noktaButon)

        #İşaret ve yüzde butonları...
        self.yuzdeAl.clicked.connect(self.yuzdeFonk)
        self.isaretDegistir.clicked.connect(self.yuzdeFonk)

        #Aritmetik işlemler(artı, cıkarma, carpma, bölme)
        self.arti.clicked.connect(self.aritmatik_islemler)
        self.carpma.clicked.connect(self.aritmatik_islemler)
        self.bolme.clicked.connect(self.aritmatik_islemler)
        self.Eksi.clicked.connect(self.aritmatik_islemler)


        self.arti.setCheckable(True)
        self.Eksi.setCheckable(True)
        self.bolme.setCheckable(True)
        self.carpma.setCheckable(True)

        #Eşitir butonu...
        self.esittir.clicked.connect(self.sonuc)
        self.esittir.setCheckable(True)

        #Clear butonu...
        self.silme.clicked.connect(self.sil)




    def rakamlar(self):
        #buton değişkenine self.sender() ile basıldıgını kontrol etmesini söyledik...
        buton = self.sender()

        #Tekrar bir aritmetik işlem yapıldıgında ilk sayının ve ikinci sayının durumunu kontrol ediyoruz...
        if ((self.ikincisayi) and (self.esittir.isChecked())):
            self.label.setText(format(float(buton.text()), '.15g'))
            self.ikincisayi = True
            self.esittir.setChecked(False)

        # Birinci sayı ve ikinci sayıyı kontrol etme durumları...
        elif((self.arti.isChecked() or self.Eksi.isChecked() or self.carpma.isChecked() or self.bolme.isChecked()) and (not self.ikincisayi)):
            # Sayılara basıldıgında rakamları ekrana yazma kodu - ve '.15g' ilede başındaki sıfırları yok eder...
            self.label.setText(format(float(buton.text()), '.15g'))
            self.ikincisayi = True

        else:
            if(("." in self.label.text()) and buton.text() == "0"):
                self.label.setText(format(float(self.label.text() + buton.text()), '.15'))
            else:
                self.label.setText(format(float(self.label.text() + buton.text()), '.15g'))




    def noktaButon(self):
        self.label.setText(self.label.text() + ".")
        #Koşullu durum iki tane nokta sorunu çözülecek...

    def yuzdeFonk(self):
        buton = self.sender()

        #Ekrandaki değerleri al ve deger değişkenine aktar...
        deger = float(self.label.text())

        if (buton.text() == "+/-"):
            deger = deger*(-1)

        elif (buton.text() == "%"):
            deger = deger*0.01

        self.label.setText(format(deger, '.15g'))


    def aritmatik_islemler(self):
        buton = self.sender()
        self.ilksayi = float(self.label.text())
        buton.setChecked(True)

    def sonuc(self):
        ikinciDeger = float(self.label.text())

        if(self.arti.isChecked()):
            yeniDeger = self.ilksayi + ikinciDeger
            self.label.setText(format(yeniDeger, '.15g'))
            self.arti.setChecked(False)

        elif (self.Eksi.isChecked()):
            yeniDeger = self.ilksayi - ikinciDeger
            self.label.setText(format(yeniDeger, '.15g'))
            self.Eksi.setChecked(False)

        elif(self.carpma.isChecked()):
            yeniDeger = self.ilksayi * ikinciDeger
            self.label.setText(format(yeniDeger, '.15g'))
            self.carpma.setChecked(False)

        elif (self.bolme.isChecked()):
            yeniDeger = self.ilksayi / ikinciDeger
            self.label.setText(format(yeniDeger, '.15g'))
            self.bolme.setChecked(False)

    def sil(self):
        self.ilksayi = 0
        self.ikincisayi = False
        self.label.setText("0")
        self.arti.setChecked(False)
        self.Eksi.setChecked(False)
        self.carpma.setChecked(False)
        self.bolme.setChecked(False)
        self.esittir.setChecked(False)