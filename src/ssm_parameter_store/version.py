from pkg_resources import get_distribution, DistributionNotFound
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("ssm-parameter-store")
except PackageNotFoundError:
    __version__ = 'unknown'  # package not installed
