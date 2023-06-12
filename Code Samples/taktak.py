
import Code.manager.Plugins.Downloader as dnldr
from Code.PyUB.Types import UBWidget


for i in dir(dnldr):
    print(i)

for i in dir(dnldr):
    if issubclass(i, UBWidget):
        print(i)
