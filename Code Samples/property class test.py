
import PySide6.QtWidgets, json, logging
logging.basicConfig(level=logging.DEBUG)


class Property:
    def __init__(self, value):
        self._value = value

    def value(self)->None:
        return self._value

    def set_value(self, value)->None:
        self._value = value



class PropertyContainer:
    @classmethod
    def get_item(cls, item:str):
        return cls.__annotations__[item].value()

    @classmethod
    def encode_json(cls)->str:
        encode_dict = {}
        for key in cls.__annotations__.keys():
            encode_dict[key] = cls.__annotations__[key].value()

        logging.debug(f"encode_dict: {encode_dict}")
        json_dump = json.dumps(encode_dict)
        logging.debug(f"json.encoded: {json_dump}")
        logging.debug(f"json.decoded: {json.loads(json_dump)}")





class Settings(PropertyContainer):
    a: Property("Name")
    b: Property(12)
    c:Property([12,12,100])


class Plugin:
    ub_settings = Settings

    def __init__(self):
        settings = self.ub_settings
        print("plugin init")

    def change_settings(self):
        print(self.ub_settings.get_item("a"))



p =Plugin()
p.change_settings()
Settings.__annotations__["a"].set_value("Name +")
print(Settings.get_item("a"))
Settings.encode_json()






