import os

# Django specific settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


import sys
# add the project path into the sys.path
sys.path.append('/Lavori/tools/ipcnaming')
# add the virtualenv site-packages path to the sys.path
sys.path.append('/Lavori/tools/venv/Lib/site-packages')


# noinspection PyUnresolvedReferences
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import wx
from names.view import ViewChoice
from names.controller import Controller
from names.model import Model


class PcbHandlerApp(wx.App):
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def OnInit(self):
        model = Model()
        controller = Controller(model)
        view = ViewChoice(parent=None, controller=controller)
        view.Show()
        return True


if __name__ == '__main__':
    app = PcbHandlerApp(False)
    app.MainLoop()
