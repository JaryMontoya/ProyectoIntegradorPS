"""Stub file for reflex/components/radix/themes/components/slider.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import List, Literal, Optional, Union
from reflex.components.component import Component
from reflex.components.core.breakpoints import Responsive
from reflex.event import EventHandler
from reflex.vars import Var
from ..base import LiteralAccentColor, RadixThemesComponent

class Slider(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        width: Optional[str] = "100%",
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
        radius: Optional[
            Union[
                reflex.vars.Var[Literal["none", "small", "full"]],
                Literal["none", "small", "full"],
            ]
        ] = None,
        default_value: Optional[
            Union[
                reflex.vars.Var[Union[List[Union[float, int]], float, int]],
                Union[List[Union[float, int]], float, int],
            ]
        ] = None,
        value: Optional[
            Union[reflex.vars.Var[List[Union[float, int]]], List[Union[float, int]]]
        ] = None,
        name: Optional[Union[reflex.vars.Var[str], str]] = None,
        min: Optional[
            Union[reflex.vars.Var[Union[float, int]], Union[float, int]]
        ] = None,
        max: Optional[
            Union[reflex.vars.Var[Union[float, int]], Union[float, int]]
        ] = None,
        step: Optional[
            Union[reflex.vars.Var[Union[float, int]], Union[float, int]]
        ] = None,
        disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        orientation: Optional[
            Union[
                reflex.vars.Var[Literal["horizontal", "vertical"]],
                Literal["horizontal", "vertical"],
            ]
        ] = None,
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
        on_value_commit: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Slider":
        """Create a Slider component.

        Args:
            *children: The children of the component.
            width: The width of the slider.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: Button size "1" - "3"
            variant: Variant of button
            color_scheme: Override theme color for button
            high_contrast: Whether to render the button with higher contrast color against background
            radius: Override theme radius for button: "none" | "small" | "full"
            default_value: The value of the slider when initially rendered. Use when you do not need to control the state of the slider.
            value: The controlled value of the slider. Must be used in conjunction with onValueChange.
            name: The name of the slider. Submitted with its owning form as part of a name/value pair.
            min: The minimum value of the slider.
            max: The maximum value of the slider.
            step: The step value of the slider.
            disabled: Whether the slider is disabled
            orientation: The orientation of the slider.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The component.
        """
        ...

slider = Slider.create
