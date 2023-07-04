import numpy as np
import sys
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


import numpy as np

# Ensure correct usage
#sai lenh: python rec_mang.py traffic.h5
if len(sys.argv) != 2:
    sys.exit("Usage: python rec_mang.py model.h5")
#load model
model = tf.keras.models.load_model(sys.argv[1])


    # dictionary to label all traffic signs class.
classes = { 
    0:'Speed limit (20km/h)',
    1:'Speed limit (30km/h)', 
    2:'Speed limit (50km/h)', 
    3:'Speed limit (60km/h)', 
    4:'Speed limit (70km/h)', 
    5:'Speed limit (80km/h)', 
    6:'End of speed limit (80km/h)', 
    7:'Speed limit (100km/h)', 
    8:'Speed limit (120km/h)', 
    9:'No passing', 
    10:'No passing veh over 3.5 tons', 
    11:'Right-of-way at intersection', 
    12:'Priority road', 
    13:'Yield', 
    14:'Stop', 
    15:'No vehicles', 
    16:'Veh > 3.5 tons prohibited', 
    17:'No entry', 
    18:'General caution', 
    19:'Dangerous curve left', 
    20:'Dangerous curve right', 
    21:'Double curve', 
    22:'Bumpy road', 
    23:'Slippery road', 
    24:'Road narrows on the right', 
    25:'Road work', 
    26:'Traffic signals', 
    27:'Pedestrians', 
    28:'Children crossing', 
    29:'Bicycles crossing', 
    30:'Beware of ice/snow',
    31:'Wild animals crossing', 
    32:'End speed + passing limits', 
    33:'Turn right ahead', 
    34:'Turn left ahead', 
    35:'Ahead only', 
    36:'Go straight or right', 
    37:'Go straight or left', 
    38:'Keep right', 
    39:'Keep left', 
    40:'Roundabout mandatory', 
    41:'End of no passing', 
    42:'End no passing veh > 3.5 tons'
}
    # initialise GUI
top = tk.Tk()
top.geometry('600x600')
top.title('TRAFFIC SIGN')
top.configure(background='#CDCDCD') # màu nền cho cửa sổ là màu xám

label = Label(top, background='#CDCDCD', font=('arial', 18, 'bold'))
sign_image = Label(top)


def classify(file_path):
        global label_packed
        image = Image.open(file_path).convert("RGB")
        image = image.resize((30, 30))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        #print(image.shape)
        prediction = np.argmax(model.predict([image]), axis=1) 
        '''
        dự đoán nhãn của hình ảnh bằng cách truyền mảng hình ảnh vào mô hình
        sử dụng np.argmax để lấy chỉ số của nhãn có xác suất cao nhất.
        '''
        pred = prediction[0] # giá trị nhãn được dự đoán
        print(prediction[0]) 
        sign = classes[pred] # lấy tên của nhãn dựa trên chỉ số nhãn
        print(sign)
        label.configure(foreground='#364196', text=sign)


def show_classify_button(file_path):
        classify_b = Button(top, text="Check", command=lambda: classify(file_path), padx=12, pady=6)
        classify_b.configure(background='#364196', foreground='white', font=('arial', 14, 'bold'))
        classify_b.place(relx=0.79, rely=0.46)


def upload_image():
        try:
            file_path = filedialog.askopenfilename()
            uploaded = Image.open(file_path)
            uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
            im = ImageTk.PhotoImage(uploaded)

            sign_image.configure(image=im)
            sign_image.image = im
            label.configure(text='')
            show_classify_button(file_path)
        except:
            pass


upload = Button(top, text="Upload", command=upload_image, padx=12, pady=6)
upload.configure(background='#364196', foreground='white', font=('arial', 14, 'bold'))

upload.pack(side=BOTTOM, pady=70)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="NHẬN DIỆN BIỂN BÁO", pady=40, font=('Times New Roman', 32, 'bold'))
heading.configure(background='#CDCDCD', foreground='#8B0000')
heading.pack()
top.mainloop()