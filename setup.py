from distutils.command.build import build

from setuptools import setup
import os

class build_grpc(build):
    sub_commands = [("build_grpc", None)] + build.sub_commands


version_file = os.path.join(os.path.dirname(__file__), "./", "version.py")
with open(version_file) as f:
    exec(f.read())

setup (
    cmdclass={
        "build": build_grpc
    },
    version = __version__
)
