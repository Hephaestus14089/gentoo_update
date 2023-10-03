"""Provides functionality for updating a Gentoo Linux system."""

from ._version import __version__
from .gentoo_update import add_prefixes, create_cli, main
from .notifier import Notifier
from .parser import Parser
from .reporter import Reporter
from .shell_runner import ShellRunner
