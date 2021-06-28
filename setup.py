from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='roolang',
    author="Cryptex",
    url='https://github.com/rooLang/rooLang',
    project_urls={
        "Issue tracker": "https://github.com/rooLang/rooLang/issues",
        "Discord": "https://discord.gg/n625ahZAtZ",
    },
    version="0.0.1a",
    packages=find_packages(),
    license="AGPLv3",
    description='A language for roo',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
)
