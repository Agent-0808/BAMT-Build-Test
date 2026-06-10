# __main__.py
import sys

def main():
    """统一入口点：根据参数决定启动 GUI 还是 CLI"""
    # 如果有命令行参数（除了脚本名），启动 CLI
    if len(sys.argv) > 1:
        try:
            from . import cli
            cli.main()
        except ImportError:
            import ba_modding_toolkit.cli as cli
            cli.main()
    else:
        # 无参数时启动 GUI
        try:
            from . import gui
            gui.main()
        except ImportError:
            import ba_modding_toolkit.gui as gui
            gui.main()

if __name__ == "__main__":
    main()
