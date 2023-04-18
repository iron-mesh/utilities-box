from PySide2.QtWidgets import QWidget, QFormLayout, QLabel, QScrollArea, QHBoxLayout, QSizePolicy
from PySide2.QtCore import Qt
from .Properties import AbstractProperty
from typing import Any
import pickle


class PropertyContainer:

    @classmethod
    def render_layout(cls) -> QWidget:
        """Return QWidget instance with placed widgets for values input"""
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        widget_content = QWidget()
        layout = QFormLayout(widget_content)
        layout.setVerticalSpacing(15)
        layout.setLabelAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        row: int = 0
        cls._lable_list = {}
        for key, prop in cls.__annotations__.items():
            cls._lable_list[key] = QLabel(prop.get_name())
            layout.setWidget(row, QFormLayout.LabelRole, cls._lable_list[key])
            layout.setWidget(row, QFormLayout.FieldRole, prop.get_input_widget())
            row += 1
        scroll_area.setWidget(widget_content)
        return scroll_area

    @classmethod
    def get_property(cls, name: str) -> AbstractProperty:
        """ Returns instance of AbstractProperty class child"""
        return cls.__annotations__[name]

    @classmethod
    def get_property_value(cls, name: str) -> Any:
        """ Returns the value of a property wit <name> """
        return cls.get_property(name).value()

    @classmethod
    def update_data(cls) -> bool:
        """ Extracts data from gui widgets
        Returns True if any value is updated, False - otherwise"""
        is_updated:bool = False

        for key, prop in cls.__annotations__.items():
            update_status:bool = prop.extract_widget_data()
            if not is_updated and update_status:
                is_updated = True
        return is_updated


    @classmethod
    def properties_to_dict(cls) -> dict[str, (AbstractProperty, Any)]:
        """ Return dictionary of properties values"""
        prop_values_dict = {}
        for key, prop in cls.__annotations__.items():
            prop_values_dict[key] = (type(prop), prop.value())
        return prop_values_dict

    @classmethod
    def set_properties_from_dict(cls, prop_dict: dict[str, (AbstractProperty, Any)]) -> None:
        """ Recieves dictionary of properties values and rewrite properties values"""
        for key, prop in cls.__annotations__.items():
            if (key in prop_dict) \
                    and (isinstance(prop, prop_dict[key][0]))\
                    and (isinstance(prop_dict[key][1], type(prop.value()))):
                prop.set_value(prop_dict[key][1])

    @classmethod
    def retranslate(cls) -> None:
        for key, label in cls._lable_list.items():
            label.setText(cls.get_property(key).get_name())

        for key, prop in cls.__annotations__.items():
            prop.retranslate()

