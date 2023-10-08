from PySide6.QtWidgets import QWidget, QFormLayout, QLabel, QScrollArea, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from .Properties import AbstractProperty
from typing import Any
import pickle


class PropertyContainer:

    def __getattr__(self, item):
        if item in self.__annotations__:
            return self.get_property_value(item)
        else:
            raise AttributeError(f"<{item}> doesn't exist")

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
            cls._lable_list[key].setWordWrap(True)
            layout.setWidget(row, QFormLayout.LabelRole, cls._lable_list[key])
            layout.setWidget(row, QFormLayout.FieldRole, prop.get_input_widget())
            row += 1
        scroll_area.setWidget(widget_content)
        return scroll_area

    @classmethod
    def get_property(cls, name: str) -> AbstractProperty:
        """ Return property instance with <name>"""
        return cls.__annotations__[name]

    @classmethod
    def get_property_value(cls, name: str) -> Any:
        """ Return the value of a property with <name> """
        return cls.__annotations__[name].value()

    @classmethod
    def update_data(cls) -> bool:
        """ Extract data from gui widgets
        Return True if any value has been changed, False - otherwise"""
        is_updated = False

        for key, prop in cls.__annotations__.items():
            update_status = prop.extract_widget_data()
            if not is_updated and update_status:
                is_updated = True
        return is_updated


    @classmethod
    def propvalues_to_dict(cls) -> dict[str, (AbstractProperty, Any)]:
        """ Return dictionary of properties values"""
        prop_values_dict = {}
        for key, prop in cls.__annotations__.items():
            prop_values_dict[key] = (type(prop), prop.value())
        return prop_values_dict

    @classmethod
    def set_propvalues_from_dict(cls, prop_dict: dict[str, (AbstractProperty, Any)]) -> None:
        """ Recieve dictionary of properties values and rewrite properties values"""
        for key, prop in cls.__annotations__.items():
            if (key in prop_dict) \
                    and (isinstance(prop, prop_dict[key][0]))\
                    and (isinstance(prop_dict[key][1], type(prop.value()))):
                prop.set_value(prop_dict[key][1])

    @classmethod
    def prop_params_to_dict(cls) -> dict[str, (AbstractProperty, dict)]:
        """ Return dictionary of properties parameters"""
        prop_params_dict = {}
        for name, prop in cls.__annotations__.items():
            prop_params_dict[name] = (type(prop), prop.get_parameters_dict())
        return prop_params_dict

    @classmethod
    def set_prop_params_from_dict(cls, params_dict: dict[str, (AbstractProperty, dict)]) -> None:
        """ Recieve dictionary of properties parameters and rewrite properties parameters"""
        for name, prop in cls.__annotations__.items():
            if (name in params_dict) \
                    and (isinstance(prop, params_dict[name][0])):
                prop.set_parameters_from_dict(params_dict[name][1])

    @classmethod
    def retranslate(cls) -> None:
        for key, label in cls._lable_list.items():
            label.setText(cls.get_property(key).get_name())

        for key, prop in cls.__annotations__.items():
            prop.retranslate()

