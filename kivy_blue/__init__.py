from kivy.utils import platform

from .providers import BluepyProvider

PROVIDERS = {}


def get_provider():
    return PROVIDERS.get(platform, BluepyProvider)()
