"""General utility functions."""

from __future__ import annotations

import contextlib
import os
import shutil
import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from reflex.constants import Dirs
from reflex.utils.prerequisites import get_web_dir


class AssetFolderWatch:
    """Asset folder watch class."""

    def __init__(self, root):
        """Initialize the Watch Class.

        Args:
            root: root path of the public.
        """
        self.path = str(root / Dirs.APP_ASSETS)
        self.event_handler = AssetFolderHandler(root)

    def start(self):
        """Start watching asset folder."""
        self.observer = Observer()
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()


def _decode_path(path: str | bytes | bytearray | memoryview) -> str:
    """Decode path to string.

    Args:
        path: The path to decode.

    Returns:
        The decoded path as a str.
    """
    if isinstance(path, (bytes, bytearray)):
        return path.decode()
    elif isinstance(path, memoryview):
        return path.tobytes().decode()
    return path


class AssetFolderHandler(FileSystemEventHandler):
    """Asset folder event handler."""

    def __init__(self, root):
        """Initialize the AssetFolderHandler Class.

        Args:
            root: root path of the public.
        """
        super().__init__()
        self.root = root

    def on_modified(self, event: FileSystemEvent):
        """Event handler when a file or folder was modified.

        This is called every time after a file is created, modified and deleted.

        Args:
            event: Event information.
        """
        src_path = _decode_path(event.src_path)
        dest_path = self.get_dest_path(src_path)

        # wait 1 sec for fully saved
        time.sleep(1)

        if os.path.isfile(src_path):
            with contextlib.suppress(PermissionError):
                shutil.copyfile(src_path, dest_path)
        if os.path.isdir(src_path):
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            with contextlib.suppress(PermissionError):
                shutil.copytree(src_path, dest_path)

    def on_deleted(self, event: FileSystemEvent):
        """Event hander when a file or folder was deleted.

        Args:
            event: Event infomation.
        """
        dest_path = self.get_dest_path(_decode_path(event.src_path))

        if os.path.isfile(dest_path):
            # when event is about a file, pass
            # this will be deleted at on_modified function
            return

        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)

    def get_dest_path(self, src_path: str) -> str:
        """Get public file path.

        Args:
            src_path: The asset file path.

        Returns:
            The public file path.
        """
        return src_path.replace(
            str(self.root / Dirs.APP_ASSETS),
            str(self.root / get_web_dir() / Dirs.PUBLIC),
        )
