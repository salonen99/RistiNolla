import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'RistiNolla.xaml')
        
    def RadioButton_Checked(self, sender, e):
        pass


if __name__ == '__main__':
    Application().Run(MyWindow())
