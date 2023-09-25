import platform

if platform.system() == "Windows": 
    from .windows.windows_terminal_controller import *
else:
    from menu_terminal.linux.linux_terminal_controller import Linux_TerminalController


class Os_Terminal_Controller:
        
    def __init__(self):
        self.sysOp = self.Get_os()
        self.terminal = None
        self.Set_terminal()
    
    def Get_os(self):
        return platform.system()
    
    def Set_terminal(self):
        if self.sysOp == "Windows":
            self.terminal =  Windows_TerminalController()
            
        elif self.sysOp == "Linux":
            self.terminal = Linux_TerminalController()
            
    def ReadKey(self):
        return self.terminal.key()
    
    def clear(self):
        self.terminal.clear()
    
    def hide_cursor(self):
        self.terminal.hide_cursor()
    
    def show_cursor(self):
        self.terminal.show_cursor()