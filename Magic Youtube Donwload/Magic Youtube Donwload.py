from pytube import  YouTube , Playlist 
from pytube.cli import on_progress 
from tkinter import * 
from tkinter.ttk import Combobox, Progressbar
from tkinter import filedialog
from pytube.query import StreamQuery


def finish():
    print('Download Done.')

def Top():
    top = Toplevel()
    top.title('Youtube Donwloader')
    Label(text='Download Successfully',fg='green').pack()
    top.mainloop()

def downloadVideo(): 
    print('in fun download video')
    try:
        RES = qtychoise.get()
        url = urlEntry.get()

        if(len(url) > 1):
            resaultLabel.config(text='Downloading...',fg='black')
            videos = YouTube(url,on_progress_callback=on_progress)
            
            if(RES == str(choise[0])):
                stream = videos.streams.filter(progressive=True,res=RES)
                if(stream == True):
                    resaultLabel.config(on_progress)
                    stream.first().download(output_path=OUTPUT_PATH)
                    
                    
                else:
                    resaultLabel.config(text='Selected resolution Not Available')

                for i in stream:
                    print(i, "\n")
                
            elif(RES == choise[1]):
                stream = videos.streams.filter(progressive=True, res=RES)
                if(stream == True):
                    stream.first().download(output_path=OUTPUT_PATH)
                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in stream:
                    print(i, "\n")
            elif(RES == choise[2]):
                stream = videos.streams.filter(progressive=True, res=RES)
                if(stream == True):
                    stream.first().download(output_path=OUTPUT_PATH)
                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in stream:
                    print(i, "\n")
            elif(RES == choise[3]):
                stream = videos.streams.filter(progressive=True,res=RES)
                if(stream == True):
                    stream.first().download(output_path=OUTPUT_PATH)
                else:
                    resaultLabel.config(text='Selected resolution Not Available')

                for i in stream:
                    print(i, "\n")
            elif(RES == choise[3]):
                videos.streams.get_lowest_resolution().download(FolderName)
            elif(RES == choise[4]):
                videos.streams.get_highest_resolution().download(FolderName)
            elif(RES == choise[5]):
                videos.streams.get_audio_only().download(FolderName)
            
            Top()
        else:
            btnDonwload.config(background='red')
            resaultLabel.config(text='Download Failed',fg='red')

    except Exception as err:
        print(err)
        resaultLabel.config(text=f'Download Failed..{err}', fg='red')


def downloadPlaylist():   

        RES = qtychoise.get()
        url = urlEntry.get()
        playlist = Playlist(url)
        global nb_videos_in_Playlist 
        nb_videos_in_Playlist = len(playlist.video_urls)
        resaultLabel.config(text=f'0 / {nb_videos_in_Playlist}' )
        
        for pl in playlist.videos:
            filter_PlayList = pl.streams.filter(progressive="True", res=RES)
            if(RES == str(choise[0])):
                if(filter_PlayList == True):
                    for video in filter_PlayList:
                        video.download(output_path=OUTPUT_PATH)
                        finish()

                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in filter_PlayList:
                    print(i, "\n")

            if(RES == str(choise[1])):
                if(filter_PlayList == True):
                    for video in filter_PlayList:
                        video.download(output_path=OUTPUT_PATH)
                        finish()

                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in filter_PlayList:
                    print(i, "\n")
            if(RES == str(choise[2])):
                
                if(filter_PlayList == True):
                    for video in filter_PlayList:
                        video.download(output_path=OUTPUT_PATH)
                        finish()

                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in filter_PlayList:
                    print(i, "\n")
            if(RES == str(choise[3])):
                if(filter_PlayList == True):
                    for video in filter_PlayList:
                        video.download(output_path=OUTPUT_PATH)
                        finish()

                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in filter_PlayList:
                    print(i, "\n")
            if(RES == str(choise[4])):
                if(filter_PlayList == True):
                    for video in filter_PlayList:
                        video.download(output_path=OUTPUT_PATH)
                        finish()

                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in filter_PlayList:
                    print(i, "\n")
            if(RES == str(choise[5])):
                filter_PlayList = pl.streams.filter(
                    progressive="True", res=RES)
                if(filter_PlayList == True):
                    for video in filter_PlayList:
                        video.download(output_path=OUTPUT_PATH)
                        finish()

                else:
                    resaultLabel.config(
                        text='Selected resolution Not Available')

                for i in filter_PlayList:
                    print(i, "\n")


def openLocation():
    global FolderName
    FolderName = filedialog.askdirectory()
    showDirectoryLabel.config(text=FolderName)


def Download():
    print('in fun Download ')

    btnDonwload.config(background='green')
    print('in if fun radioButtonValue ')

    
    if(radioButtonValue.get() == 1):

        print('in if fun radioButtonValue 1')
        downloadVideo()
    elif(radioButtonValue.get() == 2):

        print('in if fun radioButtonValue 2')
        downloadPlaylist()
    else:
        print('Error,Try Again!')

FolderName = ''
OUTPUT_PATH = FolderName
nb_videos_in_Playlist = 0


win = Tk()
win.columnconfigure(0,weight=1)
win.title('Magic Youtube Donwload')
# win.iconbitmap('youtube.ico')
win.resizable(False,False)

f = 'Helvitica 20 bold'
fd = 'Helvitica 7 bold'
fnt = ('jost', 15)


label_title = Label(win, text='Magic Youtube Donwload',foreground='red',font=fnt)
label_title.grid(row=0, padx=100,pady = 20)


urlLabel = Label(win, text='- Paste Url -', foreground='black', font=fnt)
urlLabel.grid(row=1)

r=StringVar()
# r.set('https://www.youtube.com/watch?v=tPEE9ZwTmy0&ab_channel=hiddentracktv2')
urlEntry = Entry(win,width=60,textvariable=r)
urlEntry.grid(row=2,pady=10)    



radioButtonValue = IntVar()
radioButtonValue.set(1)
rad0 = Radiobutton(win, text='Video', variable=radioButtonValue, value=1).grid(row=3)
rad1= Radiobutton(win, text='Playlist', variable=radioButtonValue,value=2).grid(row=4)


qualityLabel = Label(win, text='- Choose Quality - ', foreground='black', font=fnt)
qualityLabel.grid(row=5)

choise = ['360p','480p' ,'720p' , '1080p', 'Low Quality Video', 'High Quality Video' , 'Audio file']
qty= StringVar()
qty.set(choise[5])
qtychoise =Combobox(win,textvariable=qty, values=choise)
qtychoise.grid(row=6, pady=10)

locationLabel = Label(win,text='- Location - ', foreground='black', font=fnt,pady=10)
locationLabel.grid(row=7)

photo = PhotoImage(file="photos\photoDirectory.png")
photoimage = photo.subsample(20, 20)
directoryLabel = Button(win, image=photoimage,pady=10,command=openLocation)
directoryLabel.grid(row=8)

showDirectoryLabel = Label(win, pady=10)
showDirectoryLabel.grid(row=9)


resaultLabel = Label(win,pady=10,foreground='green')
resaultLabel.grid(row=10)

Label(win, text='Developed by Amr Nasser', foreground='black', font=fd).grid(row=11,  pady=10)

btnDonwload = Button(win, text='Download',command=Download, width=40,font=fnt, background='#A6A6A6')
btnDonwload.grid(row=12)
bFrame = Frame(win,width=450,height=2,bg="black").grid(row=13)
win.mainloop()
