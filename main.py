import tkinter as tk

# 創建主窗口
window = tk.Tk()
window.geometry('600x600')
window.title("Master Mind")

# 設置背景顏色
window.configure(bg='#F0F0F0')

# 標題
startTitle = tk.Label(window, text="Master Mind", bg='red', fg='white', font=('Arial', 36))
startTitle.grid(row=0, column=0, columnspan=2, pady=(20, 40))

# 開始按鈕
startButton = tk.Button(window, text='START', font=('Arial', 18), bg='green', fg='white', padx=20, pady=10)
startButton.grid(row=1, column=0, columnspan=2, pady=(10, 10))

# 統計按鈕
StatisticalButton = tk.Button(window, text='Statistical', font=('Arial', 18), bg='blue', fg='white', padx=20, pady=10)
StatisticalButton.grid(row=2, column=0, columnspan=2, pady=(10, 20))

# 運行主循環
window.mainloop()
