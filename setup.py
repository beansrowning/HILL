from setuptools import setup, find_packages

try:
    import pip_system_certs.wrapt_requests
except:
    pass

# BUG: torch-sparse is super hacky and needs a set install order.
# see: https://github.com/rusty1s/pytorch_sparse/issues/156
try:
    import torch
except ImportError as e:
    raise ImportError("torch-sparse requires pytorch to be installed first. Install with `pip install torch`", str(e))
    
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='HILL',
    version='0.1',
    description='A packaged version of the HILL model implemented by Zhu et al.',
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    url='https://github.com/beansrowning/HILL',
    author='Sean Browning',
    author_email='sbrowning@cdc.gov',
    license='MIT',
    packages=find_packages(include=["hill", "hill.*"]),
    install_requires=requirements,
    zip_safe=False
)