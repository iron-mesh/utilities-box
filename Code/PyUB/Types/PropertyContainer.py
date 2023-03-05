from PySide2.QtWidgets import QWidget, QFormLayout, QLabel, QScrollArea, QHBoxLayout
from PySide2.QtCore import Qt
from .Properties import AbstractProperty
from typing import Any
import pickle


class PropertyContainer:

    @classmethod
    def render_layout(cls) -> QWidget:
        """Return QWidget instance with placed widgets for values inputing"""
        scroll_area = QScrollArea()
        layout = QFormLayout(scroll_area)
        layout.setVerticalSpacing(15)
        layout.setLabelAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        row:int = 0
        cls._lable_list = {}
        for key, prop in cls.__annotations__.items():
            cls._lable_list[key] = QLabel(prop.get_name())
            layout.setWidget(row, QFormLayout.LabelRole, cls._lable_list[key])
            layout.setWidget(row, QFormLayout.FieldRole, prop.get_input_widget())
            row += 1
        return scroll_area

    #comment

    @classmethod
    def get_item(cls, name: str) -> AbstractProperty:
        """ Returns instance of AbstractProperty class child"""
        return cls.__annotations__[name]

    @classmethod
    def get_item_value(cls, name: str) -> Any:
        """ Returns the value of a property wit <name> """
        return cls.get_item(name).value()

    @classmethod
    def update_data(cls) -> bool:
        """ Extracts data from gui widgets
        Returns True if any value is updated, False - otherwise"""
        prop_update_list: list[bool] = []

        def is_prop_values_updated(bool_list: list[bool]):
            for el in bool_list:
                if el:
                    return True
            return False

        for key, prop in cls.__annotations__.items():
            prop_update_list.append(prop.extract_widget_data())

        return is_prop_values_updated(prop_update_list)


    @classmethod
    def properties_to_dict(cls) -> dict:
        """ Return dictionary of properties"""
        prop_values_dict = {}
        for key, prop in cls.__annotations__.items():
            prop_values_dict[key] = prop.value()
        return prop_values_dict

    @classmethod
    def set_properties_from_dict(cls, prop_dict: dict) -> None:
        """ Recieve dictionary of properties values and rewrite properties values"""
        for key, prop in cls.__annotations__.items():
            if (key in prop_dict) and (type(prop_dict[key]) is type(prop.value())):
                prop.set_value(prop_dict[key])

    @classmethod
    def retranslate(cls) -> None:
        for key, label in cls._lable_list.items():
            label.setText(cls.get_item(key).get_name())

        for key, prop in cls.__annotations__.items():
            prop.retranslate()

