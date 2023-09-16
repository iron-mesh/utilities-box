print("load init")

from PyUB.utils import register_ubwidget
from .MyUBWidget import MyUBWidget

# Attribute ub_info is optional
ub_info ={"description": "Type brief description of your plugin... ",
          "author": "John Smith",
          "author_webpage": "https://ironmesh.ru",
          "author_email": "ironmesh.studio@gmail.com",
          "version":"0.1.2",
          "wiki_url": "https://...."}

register_ubwidget(MyUBWidget)



