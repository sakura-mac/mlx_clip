from setuptools import setup, find_packages

with open('requirements.txt', encoding='utf-8') as f:
    required = f.read().splitlines()

setup(
    name='mlx_clip',
    version='0.2',
    packages=find_packages(),
    description='A simple package to use CLIP on apple silicon using the MLX libraries from Apple',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Harper Reed',
    author_email='harper@modest.com',
    url='https://github.com/yourusername/yourrepository',
    install_requires=required,
)
