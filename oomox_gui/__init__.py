"""Themix GUI"""
import sys

import gi

MIN_PYTHON_VERSION = (3, 10)
if (version := sys.version_info) < MIN_PYTHON_VERSION:
    OLD_PYTHON_ERROR = (
        "\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        f"You're running too old Python version: {version}.\n"
        f"Either upgrade Python to {MIN_PYTHON_VERSION} or downgrade Themix-GUI.\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )
    raise RuntimeError(OLD_PYTHON_ERROR)

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
