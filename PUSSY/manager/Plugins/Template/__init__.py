
from PyUB.utils import register_ubwidget
from .MyUBWidget import MyUBWidget

# Attribute ub_info is optional
ub_info ={"description": "Type brief description of your plugin... ",
          "author": "Iron Mesh",
          "author_webpage": "https://ironmesh.ru",
          "author_email": "products@ironmesh.ru",
          "version": "0.1.2",
          "wiki_url": "https://...."}

register_ubwidget(MyUBWidget)



