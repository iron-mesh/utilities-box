import sys
import Code.PyUB.utils as utils


path = r"D:\MAIN\Программирование\Проекты\Utilities Box\Code\src\Plugins"

sys.path.append(path)

for i in sys.path:
    print (i)

module = __import__("Hello Test")
module2 = __import__("Hello Test 2")
module3 = __import__("Hello Test")
module4 = __import__("Hello Test 2")

print(utils.ubwidgets_list)