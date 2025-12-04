import tkinter as tk
from tkinter import ttk, messagebox, filedialog # GUI 위젯, 메시지 박스, 파일 대화상자
import json # JSON 데이터 처리
import pandas as pd # CSV, Excel 데이터 처리

class StudentManagerApp:
    def __init__(self, root):
        self.root = root # 메인 윈도우
        self.root.title("학생 관리 시스템") # 윈도우 제목 설정
        self.root.geometry("600x420") # 윈도우 크기 설정


        self.create_widgets() # 위젯 생성 함수 호출
           
    def create_widgets(self):
        input_frame = ttk.LabelFrame(self.root, text="학생 정보 입력")
        input_frame.pack(fill="x", padx=10, pady=10)


     

    def add_student(self):
        pass

    def delete_student(self):
        pass


    