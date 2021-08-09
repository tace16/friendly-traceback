"""This module is intended to add help attributes to various functions."""
from typing import Any, Callable, Dict

from friendly_traceback import debug_helper
from friendly_traceback.ft_gettext import current_lang

_ = current_lang.translate

short_description = {
    "back": lambda: _("Removes the last recorded traceback item."),
    "explain": lambda: _("Shows all the information about the last traceback."),
    "history": lambda: _("Shows a list of recorded traceback messages."),
    "set_lang": lambda: _("Sets the language to be used."),
    "set_prompt": lambda: _("Sets the prompt style to be used in the console."),
    "show_paths": lambda: _("Shows the paths corresponding to synonyms used."),
    "what": lambda: _("Shows the generic meaning of a given exception"),
    "where": lambda: _("Shows where an exception was raised."),
    "why": lambda: _("Shows the likely cause of the exception."),
    "www": lambda: _("Opens a web browser at a useful location."),
    "hint": lambda: _("Suggestion sometimes added to a friendly traceback."),
    "python_tb": lambda: _("Shows a normal Python traceback."),
    "friendly_tb": lambda: _("Shows a simplified Python traceback."),
    "get_include": lambda: _(
        "Returns the current value used for items to include by default."
    ),
    "set_include": lambda: _(
        "Sets the items to show by default when an exception is raised."
    ),
    "get_lang": lambda: _("Returns the language currently used."),
    "set_formatter": lambda: _("Sets the formatter to use for display."),
    "set_debug": lambda: _("Use True (default) or False to set the debug flag."),
    # The following are not translated by choice.
    "_debug_tb": (
        lambda: "Shows the full traceback, including code from friendly_traceback."
    ),
    "_show_info": lambda: "Shows the all the items recorded in the traceback.",
    "_get_exception": lambda: "Returns the exception instance.",
    "_get_frame": lambda: "Returns the frame object where the exception occurred.",
    "_get_statement": lambda: "Returns the statement in which a SyntaxError occurred.",
    "_get_tb_data": lambda: "Return a special traceback object.",
}


def add_help_attribute(functions: Dict[str, Callable[..., Any]]) -> None:
    """Given a dict whose content is of the form
    {function_name_string: function_obj}
    it adds customs `help` and  `__rich__repr` attributes for all such
    function objects.
    """
    for name in functions:
        if name not in short_description:
            debug_helper.log(f"Missing description for {name}.")
            continue
        func = functions[name]
        setattr(func, "help", short_description[name])  # noqa
        setattr(func, "__rich_repr__", lambda func=func: (func.help(),))  # noqa