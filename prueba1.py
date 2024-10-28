import os
from tkinter import *
import tkinter as Tk
import imutils
from PIL import Image, ImageTk
import cv2

from process.gui.image_paths import ImagePaths
from process.database.config import DataBasePaths
from process.face_processing.face_signup import FaceSignUp
from process.face_processing.face_login import FaceLogIn
from process.com_interface.serial_com import SerialCommunication

class CustomFrame(Tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=Tk.BOTH, expand=True)


class GraphicalUserInterface:
    def __init__(self, root):
        self.main_window = root
        self.main_window.title('faces access control')
        self.main_window.geometry('1280x720')
        self.frame = CustomFrame(self.main_window)

        # config stream
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

        # signup window
        self.signup_window = None
        self.input_name = None
        self.input_user_code = None
        self.name = None
        self.user_code = None
        self.user_list = None
        # face capture
        self.face_signup_window = None
        self.signup_video = None
        self.user_codes = []
        self.data = []

        # login window
        self.face_login_window = None
        self.login_video = None

        print("pase")
