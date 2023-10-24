# terminale pip install qrcode pillow  yazıp  yüklüyoruz.
import qrcode

# Daha sonra code adında bir değişken oluşturalım ve qrcode.make('') komutunu kullanalım. Burada isterseniz bir metin girişi yapabilirsiniz veya isterseniz bir url girişi yapabilirsiniz.
code =  qrcode.make('https://github.com/Akdrkzl')
code.save('qrcode.png')
# save metodu ile çıktımızı alıyoruz.Burada save içerisine hangi formatta çıktı almak istediğimizi ve çıktı alırken hangi isimde olması gerektiğini belirliyoruz.
# son olarak terminalde python qr.py çalıştırıp çıktımızı alıyoruz.
