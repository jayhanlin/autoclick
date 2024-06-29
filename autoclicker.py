import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard

class AutoClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("自動點擊器")
        self.root.geometry("300x200")
        
        self.clicking = False
        self.click_interval = 10  # 默認間隔為10毫秒
        
        self.label = tk.Label(root, text="按F2開始，F3停止")
        self.label.pack(pady=10)
        
        self.status = tk.Label(root, text="狀態: 未啟動")
        self.status.pack(pady=5)
        
        self.speed_label = tk.Label(root, text="點擊速度:")
        self.speed_label.pack()
        
        self.speed_scale = ttk.Scale(root, from_=1, to=1000, orient='horizontal', 
                                     command=self.update_speed)
        self.speed_scale.set(self.click_interval)
        self.speed_scale.pack(pady=5)
        
        self.interval_label = tk.Label(root, text=f"間隔: {self.click_interval}毫秒")
        self.interval_label.pack()
        
        keyboard.add_hotkey('F2', self.start_clicking)
        keyboard.add_hotkey('F3', self.stop_clicking)
    
    def update_speed(self, value):
        self.click_interval = int(float(value))
        self.interval_label.config(text=f"間隔: {self.click_interval}毫秒")
    
    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.status.config(text="狀態: 正在點擊")
            self.click()
    
    def stop_clicking(self):
        self.clicking = False
        self.status.config(text="狀態: 已停止")
    
    def click(self):
        if self.clicking:
            pyautogui.click()
            self.root.after(self.click_interval, self.click)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()