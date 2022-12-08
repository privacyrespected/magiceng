import cv2
from matplotlib import pyplot as plt
import tkinter as tk
imageA = cv2.imread(r'characters\char_A.jpg')
imageB = cv2.imread(r'characters\char_B.jpg')
imageC = cv2.imread(r'characters\char_c.jpg')
imageD = cv2.imread(r'characters\char_D.jpg')
imageE = cv2.imread(r'characters\char_E.jpg')
imageF = cv2.imread(r'characters\char_F.jpg')
imageG = cv2.imread(r'characters\char_G.jpg')
imageH = cv2.imread(r'characters\char_H.jpg')
imageI = cv2.imread(r'characters\char_IJ.jpg')
imageJ= cv2.imread(r'characters\char_IJ.jpg')
imageK = cv2.imread(r'characters\char_K.jpg')
imageL = cv2.imread(r'characters\char_L.jpg')
imageM = cv2.imread(r'characters\char_M.jpg')
imageN = cv2.imread(r'characters\char_N.jpg')
imageO = cv2.imread(r'characters\char_O.jpg')
imageP = cv2.imread(r'characters\char_P.jpg')
imageQ = cv2.imread(r'characters\char_Q.jpg')
imageR = cv2.imread(r'characters\char_R.jpg')
imageS = cv2.imread(r'characters\char_S.jpg')
imageT = cv2.imread(r'characters\char_T.jpg')
imageU = cv2.imread(r'characters\char_UVW.jpg')
imageV = cv2.imread(r'characters\char_UVW.jpg')
imageW= cv2.imread(r'characters\char_UVW.jpg')
imageX = cv2.imread(r'characters\char_X.jpg')
imageY = cv2.imread(r'characters\char_Y.jpg')
imageZ = cv2.imread(r'characters\char_Z.jpg')
imageZEND = cv2.imread(r'characters\char_ZEND.jpg')
data={ 
    "a":imageA,
    "b":imageB,
    "c":imageC,
    "d":imageD,
    "e":imageE,
    "f":imageF,
    "g":imageG,
    "h":imageH,
    "i":imageI,
    "j":imageJ,
    "k":imageK,
    "l":imageL,
    "m":imageM,
    "n":imageN,
    "o":imageO,
    "p":imageP,
    "q":imageQ,
    "r":imageR,
    "s":imageS,
    "t":imageT,
    "u":imageU,
    "v":imageV,
    "w":imageW,
    "x":imageX,
    "y":imageY,
    "z":imageZ
}

root = tk.Tk()
root.title("Main")
root.geometry("600x400")
var1=tk.StringVar()
def submit():
    var=var1.get()
    ##
    var= var.replace(" ","")
    var =var=''.join([j for i,j in enumerate(var) if j not in var[:i]])
    var=list(var)
    list_length= len(var)
    rows=1
    columns=list_length+ 1
    position =1 
    fig = plt.figure(figsize=(10, 7))
    for i in var:
        if i in data:
            fig.add_subplot(rows, columns,position)
            plt.imshow(data[i])
            plt.axis('off')
            position = position +1
    position = position 
    fig.add_subplot(rows, columns,position)
    plt.imshow(imageZEND)
    plt.axis('off')
    plt.show()


    var1.set("")
label= tk.Label(root, text="Input: ", font =("calibre",10, 'bold'))
entry= tk.Entry(root, textvariable=var1,font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)
label2=tk.Label(root,text=var1,font =("calibre",10, 'bold'))
label.grid(row=0,column=0)
entry.grid(row=0,column=1)
sub_btn.grid(row=1,column=0)
root.mainloop()

