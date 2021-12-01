import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.core import TextNode

from direct.gui.DirectGui import DirectFrame

# Add some text
bk_text = "Kelompok 4"
textObject = OnscreenText(text=bk_text, pos=(0.0, 0.85), scale=0.07,
                          fg=(6, 6, 6, 6), align=TextNode.ACenter,
                          mayChange=1)

# Add some text
output = ""
textObject = OnscreenText(text=output, pos=(0.012, -0.40), scale=0.07,
                          fg=(6, 6, 6, 6), align=TextNode.ACenter,
                          mayChange=1)
# Callback function to set text
v = [0]

def itemSel(arg):
    if arg == "Pilih Profil Anggota":
        # Callback function to set  text
        # Add button
        # No need to add an element
        bk_text = "Kelas D"
        textObject.setText(text=bk_text),
        imageObject = OnscreenImage(
        image='home.jpg', pos=(-0.5, 0, 0.02), scale=0.3,)
        
    if arg == "Anggota 1":
        b = DirectButton(text=("OK", "Click!", "rolling over", "disabled"),
                        scale=.05, pos=(-0.50, 0, 0.50))
        # No need to add an element
        bk_text = "Agnar Briantama Ridhwanullah (V3920003)"
        textObject.setText(text=bk_text),
        imageObject = OnscreenImage(
            image='agnar.jpeg', pos=(-0.5, 0, 0.02), scale=0.3,)
            
    if arg == "Anggota 2":
        b = DirectButton(text=("OK", "Click!", "rolling over", "disabled"),
                        scale=.05, pos=(-0.50, 0, 0.50))
        # No need to add an element
        bk_text = "Bancar Anggono Farros Santosa (V3920013)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='bancar.png', pos=(-0.5, 0, 0.02), scale=0.3,)

    if arg == "Anggota 3":
        b = DirectButton(text=("OK", "Click!", "rolling over", "disabled"),
                        scale=.05, pos=(-0.50, 0, 0.50))
        # No need to add an element
        bk_text = "Catur Edi Prasetyo (V3920014)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='catur.jpg', pos=(-0.5, 0, 0.02), scale=0.3,)

    if arg == "Anggota 4":
        b = DirectButton(text=("OK", "Click!", "rolling over", "disabled"),
                        scale=.05, pos=(-0.50, 0, 0.50))
        # No need to add an element
        bk_text = "Dwi Ayuni Rohana (V3920019)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='ayuni.jpg', pos=(-0.5, 0, 0.02), scale=0.3,)

    if arg == "Anggota 5":
        b = DirectButton(text=("OK", "Click!", "rolling over", "disabled"),
                        scale=.05, pos=(-0.50, 0, 0.50))
        # No need to add an element
        bk_text = "Intan Naumi (V3920028)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='intan.jpg', pos=(-0.5, 0, 0.02), scale=0.3,)        

# Create a frame
menu = DirectOptionMenu(text="options", scale=0.1, initialitem=2,
                        items=["Pilih Profil Anggota", "Anggota 1",
                               "Anggota 2", "Anggota 3", "Anggota 4", "Anggota 5"],
                        highlightColor=(0.1, 0.1, 0.1, 1),
                        command=itemSel, textMayChange=1)


def showValue():
    return menu

mybar = DirectScrollBar(range=(0, 50), value=50, pageSize=5, orientation=DGG.HORIZONTAL)
mybar.setPos(-0.50, 0, -0.50)

# Procedurally select a item
menu.set(0)

# Run the program
base.run()