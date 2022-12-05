# Graphical User Interface (GUI) for models of skylight ![GitHub top language](https://img.shields.io/github/languages/top/evgkanias/sky-gui) [![GitHub license](https://img.shields.io/github/license/evgkanias/sky-gui)](https://github.com/evgkanias/sky-gui/blob/main/LICENSE) ![GitHub last-commit](https://img.shields.io/github/last-commit/evgkanias/sky-gui) ![Build Status](https://app.travis-ci.com/evgkanias/sky-gui.svg?branch=main)

![Rendered GUI](https://raw.githubusercontent.com/evgkanias/sky-gui/ed281c98525acefabd0f06bc28c4552ec7f07220/docs/gui-1.png)

This (Python-based) GUI allows for interactive exploration of the skylight information provided by the different models.
The GUI is based on the one implemented by
[Vévoda et al. (2022)](https://cgg.mff.cuni.cz/publications/infrared-skymodel-2022/) for their Prague Sky Model
(original C++ code
[here](https://cgg.mff.cuni.cz/wp-content/uploads/2022/09/vevoda_2022_infrared_sky_implementation.zip)).
There are three available datasets that work with this model, which can be downloaded form here:
* [Google Drive with the near-infrared (SWIR) dataset](https://drive.google.com/file/d/1ZOizQCN6tH39JEwyX8KvAj7WEdX-EqJl/view?usp=sharing)
  (omits data in different altitudes)
* [Google Drive with the full model](https://drive.google.com/drive/folders/19Iw0mB_UFTtbrFcojHmHc7mjc3PYe_AC?usp=sharing)
  (omits near infrared data)
* [Google Drive with the hemispherical model](https://drive.google.com/drive/folders/1R9dTbOhBXthY3y9BTI4H28acl9dJLIaV?usp=sharing)
  (omits polarisation data and different altitudes)

## Installation

You can easily install the package by using pip as:
```commandline
pip install git+https://github.com/evgkanias/sky-gui.git
```

Alternatively you need to clone the GitHub repository, navigate to the main directory of the project, install the dependencies and finally
the package itself. Here is an example code that installs the package:

1. Install the [skylight](https://pypi.org/project/skylight/) package by using the instructions from
[here](https://github.com/evgkanias/sky/#readme), or run:
```commandline
pip install skylight
```

2. Clone this repo.
```commandline
mkdir ~/src
cd ~/src
git clone https://github.com/evgkanias/sky-gui.git
cd sky-gui
```
3. Install the required libraries. 
   1. using pip :
      ```commandline
      pip install -r requirements.txt
      ```

   2. using conda :
      ```commandline
      conda env create -f environment.yml
      ```
4. Install the package.
   1. using pip :
      ```commandline
      pip install .
      ```
   2. using conda :
      ```commandline
      conda install .
      ```
   
Note that the [pip](https://pypi.org/project/pip/) project might be needed for the above installation.

## Run the graphical user interface (GUI)

To run the GUI, open a Python terminal and run the below.

```python
from skylight_gui import SkyModelGUI

gui = SkyModelGUI()
gui()
```

Alternatively, go to the examples directory and run the script that opens the graphical environment.

```commandline
cd examples
python run_gui.pyw
```

This will open the GUI which should look like this:

![Initial GUI](https://raw.githubusercontent.com/evgkanias/sky-gui/ed281c98525acefabd0f06bc28c4552ec7f07220/docs/gui-0.png)

By clicking the file-name filed, you can choose the dataset file, which will load automatically.
Once loaded, you can click "Render" (or choose the auto-update option) and this will print an image
of the sky radiance, sun radiance, degree of polarisation, transmittance, or angle of polarisation (depending on the
rendering mode), as shown below:

![Rendered GUI](https://raw.githubusercontent.com/evgkanias/sky-gui/ed281c98525acefabd0f06bc28c4552ec7f07220/docs/gui-1.png)

By clicking the saving file-name, you can define the file-name and type of data you want to save. Theses
are:
* Image file (PNG or JPEG)
* Raw data (CSV or EXCEL)

The raw data option will save the data of the chosen mode but for all the available wavelengths and the
extracted visible light (RGB).

## Report an issue

If you have any issues installing or using the package, you can report it
[here](https://github.com/evgkanias/sky-gui/issues).

## Author

The code is written by [Evripidis Gkanias](https://evgkanias.github.io/).

## Credits

The original (C++) code for this model was written by [Petr Vévoda](https://cgg.mff.cuni.cz/members/vevoda/) et al. from [Alexander Wilkie's](https://cgg.mff.cuni.cz/members/wilkie/) group in Charles University, which was part of their  [wide spectral range sky radiance model](https://cgg.mff.cuni.cz/publications/infrared-skymodel-2022/).

## Copyright

Copyright &copy; 2022, Evripidis Gkanias; Institute of Perception,
Action and Behaviour; School of Informatics; the University of Edinburgh.
