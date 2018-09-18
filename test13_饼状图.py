import Analytics as Analytics
from PyQt5 import QtGui
from matplotlib import pylab
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
        QtGui.QSizePolicy.Expanding,
        QtGui.QSizePolicy.Expanding)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.updateGeometry(self)

class UsersPlatformPie(MyMplCanvas):
    def compute_initial_figure(self):
        UsersPerCountry, UsersPerPlatform = Analytics.UsersPerCountryOrPlatform()
        labels = []
        sizes = []
        print(UsersPerPlatform)
        for p, c in sorted(UsersPerPlatform.iteritems()):
            labels.append(p)
            sizes.append(c)
            colors = ['turquoise', 'yellowgreen', 'firebrick', 'lightsteelblue', 'royalblue']
        pylab.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True)
        pylab.title('Users Per Platform')
        pylab.gca().set_aspect('1')
        pylab.show()