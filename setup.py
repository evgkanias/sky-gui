import setuptools
import os

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fr:
    requirements = fr.read().splitlines()

setuptools.setup(
    name="skylight-gui",
    version="v1.0b2",
    author="Evripidis Gkanias",
    maintainer="Evripidis Gkanias",
    author_email="ev.gkanias@ed.ac.uk",
    maintainer_email="ev.gkanias@ed.ac.uk",
    description="A package providing a GUI for the skylight_gui package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/skylight-gui/",
    license="GPLv3+",
    project_urls={
        "Bug Tracker": "https://github.com/evgkanias/sky-gui/issues",
        "Source": "https://github.com/evgkanias/sky-gui"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Topic :: Scientific/Engineering :: Visualization"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={'': [
        "README.md",
        os.path.join('data', 'PragueSkyModelDatasetGroundInfra.dat'),
        os.path.join('data', 'icon.png')]
    },
    install_requires=requirements,
    python_requires=">=3.9",
)
