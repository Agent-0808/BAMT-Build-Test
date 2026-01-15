# main.pyw

from pathlib import Path
from tkinterdnd2 import TkinterDnD
import ttkbootstrap as tb
from ui import App

if __name__ == "__main__":

    root = TkinterDnD.Tk()
    tb.Style(theme='cosmo')
    
    # 设置窗口图标
    icon_path = Path(__file__).parent / "assets" / "BAMT_128x.ico"
    if icon_path.exists():
        root.iconbitmap(str(icon_path))

    app = App(root)
    print("BA Modding Toolkit 已启动")
    
    root.mainloop()