from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
#from SimpleCV import *
import time
from time import sleep
from PIL import Image as img, ImageTk

class MY_ARCAM():
    varPicture = ''
    varPosition = ''

    def __init__(self, initWindowName):
        self.initWinName = initWindowName
        self.username = StringVar()
        self.password = StringVar()

    def createForm(self):
        self.initWinName.title("AR Feast")
        self.initWinName.geometry('400x200')
        self.accounLabel = Label(self.initWinName, text = 'Username: ').place(x=80, y=15)
        self.accountEntry = Entry(self.initWinName, textvariable=self.username, show=None).place(x=155, y=15)
        self.pswLacel = Label(self.initWinName, text = 'Password: ').place(x=80, y=50)
        self.pswEntry = Entry(self.initWinName, textvariable=self.password, show='*').place(x=155, y=50)
        self.lgoinBtn = Button(self.initWinName, text='Login', command=self.loginCheck).place(x=170, y=85)
        self.registerBtn = Button(self.initWinName, text='Create an account', command=self.register).place(x=135, y=140)
        
    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name=='wangliang' and secret=='123456':
            for widget in self.initWinName.winfo_children():
                widget.destroy()
            self.setInitWindow()
            # MainPage()
        else:
            showinfo(title='错误', message='账号或密码错误！')

    def register(self):
        for widget in self.initWinName.winfo_children():
            widget.destroy()
        self.accounLabel = Label(self.initWinName, text = 'Username: ').place(x=80, y=15)
        self.accountEntry = Entry(self.initWinName, textvariable=self.username, show=None).place(x=155, y=15)
        self.pswLacel = Label(self.initWinName, text = 'Password: ').place(x=80, y=50)
        self.pswEntry = Entry(self.initWinName, textvariable=self.password, show='*').place(x=155, y=50)
        self.pswLacel = Label(self.initWinName, text = 'confirm password: ').place(x=32, y=85)
        self.pswEntry = Entry(self.initWinName, textvariable=self.password, show='*').place(x=155, y=85)
        self.confirmBtn = Button(self.initWinName, text='Register', command=self.checkRegister).place(x=170, y=120)

    def checkRegister(self):
        '''
        Determine whether the password entered the first time is the same as the password entered the second time
        '''
        #if the same
        showinfo(title='消息', message='注册成功')
        for widget in self.initWinName.winfo_children():
            widget.destroy()
        self.createForm()

    def setInitWindow(self):
        varPos = StringVar()
        varPic = StringVar()
        
        self.initWinName.title("AR Feast")
        self.initWinName.geometry('1080x680+10+10')

        self.logoLabel = Label(self.initWinName, text="Welcome To AR Feast", fg='green', font=('Arial',30))
        self.logoLabel.place(x=320, y=5)

        self.selPicLabel = Label(self.initWinName, text="Please select the stickers")
        self.selPicLabel.place(x=80, y=100)

        self.starRdoBtn = Radiobutton(self.initWinName, text='Star', command=self.selStar, variable=varPic, value='star')
        self.starRdoBtn.place(x=80, y=120)
        
        self.leafRdoBtn = Radiobutton(self.initWinName, text="Leaf", command=self.selLeaf, variable=varPic, value='leaf')
        self.leafRdoBtn.place(x=80, y=140)

        self.selPosLabel = Label(self.initWinName, text="Please select the part you want to post")
        self.selPosLabel.place(x=80, y=180)

        self.eyeRdoBtn = Radiobutton(self.initWinName, text='Eye', command=self.selEye, variable=varPos, value='eye')
        self.eyeRdoBtn.place(x=80, y=200)
        
        self.noseRdoBtn = Radiobutton(self.initWinName, text="Nose", command=self.selNose, variable=varPos, value='nose')
        self.noseRdoBtn.place(x=80, y=220)

        self.mouthRdoBtn = Radiobutton(self.initWinName, text="Mouth", command=self.selMouth, variable=varPos, value='mouth')
        self.mouthRdoBtn.place(x=80, y=240)

        self.takePic = Button(self.initWinName, text=("Star Take Photo"), font=('Arial', 15), bg='lightgreen', width=15, height=3, command=self.takePictures)
        self.takePic.place(x=80, y=280)

        self.viewPic = Button(self.initWinName, text=("View photos"), font=('Arial', 15), bg='lightgreen', width=15, height=3, command=self.viewPictures)
        self.viewPic.place(x=80, y=405)

    def selStar(self):
        MY_ARCAM.varPicture = 'star'

    def selLeaf(self):
        MY_ARCAM.varPicture = 'leaf'

    def selEye(self):
        MY_ARCAM.varPosition = 'eye'

    def selNose(self):
        MY_ARCAM.varPosition = 'nose'

    def selMouth(self):
        MY_ARCAM.varPosition = 'mouth'
        
    def takePictures(self):
        #print(MY_ARCAM.varPicture)
        #print(MY_ARCAM.varPosition)
        '''
        myCamera = Camera(prop_set = {'width':640, 'height':480})
        myDisplay = Display(resolution = (640, 480))
        if(MY_ARCAM.varPicture == 'star'):
            pic = Image("star.png")
        else:
            pic = Image("leaf.png")
        mask2 = pic.createBinaryMask(color1 = (0,0,0), color2 = (254,254,254))

        i = 0
        while not myDisplay.isDone():
            frame = myCamera.getImage()
            faces = frame.findHaarFeatures('face.xml')
            if faces:
                for face in faces:
                    print "Face at:" + str(face.coordinates())
                    facelayer = DrawingLayer((frame.width, frame.height))
                    w = face.width()
                    h = face.height()
                    print "X:" + str(w) + "Y:" + str(h)
                    facebox_dim = (w, h)
                    facebox = facelayer.centeredRectangle(face.coordinates(), facebox_dim)
                    frame.addDrawingLayer(facelayer)
                    frame.applyLayers()

                    myFace = face.crop()
                    if(MY_ARCAM.varPosition == 'eye'):
                        position = myFace.findHaarFeatures('eye.xml')
                    elif(MY_ARCAM.varPosition == 'nose'):
                        position = myFace.findHaarFeatures('nose.xml')
                    else:
                        position = myFace.findHaarFeatures('mouth.xml')
                    if position:
                        for p in position:
                            xf = face.x - (face.width() / 2)
                            yf = face.y - (face.height() / 2)
                            xm = p.x - (p.width() / 2)
                            ym = p.y - (p.height() / 2)
                            x1 = pic.width
                            x1 = x1 / 2
                            x2 = p.width()
                            x2 = x2 / 2
                            xmust = xf + xm - x1 + x2
                            ymust = yf + ym
                            frame = frame.blit(pic, pos = (xmust, ymust), alpha = None,  mask = mask2, alphaMask = None)
                            i = i+1
                            if(i % 20 == 0):
                                s = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
                                frame.save(s+'.jpg')
                            
            else:
                print "No faces detected."
            frame.save(myDisplay)
            sleep(.1)
        '''
    def viewPictures(self):
        #path = self.pathEntry.get()
        path = tkFileDialog.askopenfilename() 
        try:
            image = img.open(path)
            global photo
            photo = ImageTk.PhotoImage(image)
            self.imageLabel = Label(self.initWinName, image=photo)
            self.imageLabel.place(x=400, y=100)
        except IOError:
            tk.messagebox.showerror('Error','The picture path is wrong or there is no such picture!')

def guiStart():
    initWindow = Tk()
    ar = MY_ARCAM(initWindow)
    ar.createForm()
    initWindow.mainloop()

guiStart()
