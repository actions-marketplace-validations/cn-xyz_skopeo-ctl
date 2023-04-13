import pbr.version


__all__ = ['__version__']


version_info = pbr.version.VersionInfo('skopeo-ctl')
# We have a circular import problem when we first run python setup.py sdist
# It's harmless, so deflect it.
try:
    __version__ = version_info.version_string()
except AttributeError:
    __version__ = None
