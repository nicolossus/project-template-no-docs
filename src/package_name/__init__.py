import importlib.metadata

from .models import MLP
from .utils import dotdict

__version__ = importlib.metadata.version("package_name")
