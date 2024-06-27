"""Stub file for reflex/components/radix/themes/components/checkbox.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Literal
from reflex.components.component import Component, ComponentNamespace
from reflex.components.core.breakpoints import Responsive
from reflex.components.radix.themes.layout.flex import Flex
from reflex.components.radix.themes.typography.text import Text
from reflex.event import EventHandler
from reflex.vars import Var
from ..base import LiteralAccentColor, LiteralSpacing, RadixThemesComponent

LiteralCheckboxSize = Literal["1", "2", "3"]
LiteralCheckboxVariant = Literal["classic", "surface", "soft"]

class Checkbox(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        size: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["1", "2", "3"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str, Literal["1", "2", "3"]
                        ],
                    ]
                ],
                Union[
                    Literal["1", "2", "3"],
                    reflex.components.core.breakpoints.Breakpoints[
                        str, Literal["1", "2", "3"]
                    ],
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                reflex.vars.Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        default_checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        required: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        name: Optional[Union[reflex.vars.Var[str], str]] = None,
        value: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Checkbox":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: Checkbox size "1" - "3"
            variant: Variant of checkbox: "classic" | "surface" | "soft"
            color_scheme: Override theme color for checkbox
            high_contrast: Whether to render the checkbox with higher contrast color against background
            default_checked: Whether the checkbox is checked by default
            checked: Whether the checkbox is checked
            disabled: Whether the checkbox is disabled
            required: Whether the checkbox is required
            name: The name of the checkbox control when submitting the form.
            value: The value of the checkbox control when submitting the form.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class HighLevelCheckbox(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        text: Optional[Union[reflex.vars.Var[str], str]] = None,
        spacing: Optional[
            Union[
                reflex.vars.Var[
                    Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        size: Optional[
            Union[reflex.vars.Var[Literal["1", "2", "3"]], Literal["1", "2", "3"]]
        ] = None,
        as_child: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        variant: Optional[
            Union[
                reflex.vars.Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        default_checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        required: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        name: Optional[Union[reflex.vars.Var[str], str]] = None,
        value: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "HighLevelCheckbox":
        """Create a checkbox with a label.

        Args:
            text: The text of the label.
            text: The text label for the checkbox.
            spacing: The gap between the checkbox and the label.
            size: The size of the checkbox "1" - "3".
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            variant: Variant of checkbox: "classic" | "surface" | "soft"
            color_scheme: Override theme color for checkbox
            high_contrast: Whether to render the checkbox with higher contrast color against background
            default_checked: Whether the checkbox is checked by default
            checked: Whether the checkbox is checked
            disabled: Whether the checkbox is disabled
            required: Whether the checkbox is required
            name: The name of the checkbox control when submitting the form.
            value: The value of the checkbox control when submitting the form.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Additional properties to apply to the checkbox item.

        Returns:
            The checkbox component with a label.
        """
        ...

class CheckboxNamespace(ComponentNamespace):
    @staticmethod
    def __call__(
        *children,
        text: Optional[Union[reflex.vars.Var[str], str]] = None,
        spacing: Optional[
            Union[
                reflex.vars.Var[
                    Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        size: Optional[
            Union[reflex.vars.Var[Literal["1", "2", "3"]], Literal["1", "2", "3"]]
        ] = None,
        as_child: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        variant: Optional[
            Union[
                reflex.vars.Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        default_checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        required: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        name: Optional[Union[reflex.vars.Var[str], str]] = None,
        value: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "HighLevelCheckbox":
        """Create a checkbox with a label.

        Args:
            text: The text of the label.
            text: The text label for the checkbox.
            spacing: The gap between the checkbox and the label.
            size: The size of the checkbox "1" - "3".
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            variant: Variant of checkbox: "classic" | "surface" | "soft"
            color_scheme: Override theme color for checkbox
            high_contrast: Whether to render the checkbox with higher contrast color against background
            default_checked: Whether the checkbox is checked by default
            checked: Whether the checkbox is checked
            disabled: Whether the checkbox is disabled
            required: Whether the checkbox is required
            name: The name of the checkbox control when submitting the form.
            value: The value of the checkbox control when submitting the form.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Additional properties to apply to the checkbox item.

        Returns:
            The checkbox component with a label.
        """
        ...

checkbox = CheckboxNamespace()
