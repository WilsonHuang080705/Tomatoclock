# Before Reading😁
- If you want to check the guide of the GUI version of PomodoroClock, please click here:[GUI For English](https://github.com/WilsonHuang080705/PomodoroClock/blob/main/README_GUI_en_US.md)
- 如果想要查阅带有用户界面的番茄钟的中文指南，请参阅[GUI For Chinese](https://github.com/WilsonHuang080705/PomodoroClock/blob/main/README_GUI_zh_CN.md)

## Pomodoro Clock

## Introduction
Pomodoro Clock is a time management tool based on the Pomodoro Technique, developed by Matrix Huang. This tool aims to help users improve work efficiency and focus by setting cycles of work and rest.

## Running Environment
- Python 3.7.x or above

## Usage
1. Clone or download this repository to your local machine.
```
git clone https://github.com/WilsonHuang080705/PomodoroClock.git
```
2. Install the required packages.
```
pip install -r requirements.txt
```
3. Run the `PomodoroClock.py` file with Python.
```
Python PomodoroClock.py
```
4. Customize the work duration, short break duration, and long break duration through command-line arguments.
```
Python PomodoroClock.py --w 25 --sb 5 --lb 15
```
If you have not installed the Python language, you can still run the program by clicking on the "PomodoroClock-win-x86" folder and then clicking on PomodoroClock.exe. However, please note that at this time, you will not be able to customize the work duration, short break duration, and long break duration.

## Command-line Arguments

- --w, --work       Set the work duration in minutes (default: 25)
- --sb, --short-break  Set the short break duration in minutes (default: 5)
- --lb, --long-break  Set the long break duration in minutes after four Pomodoros (default: 15)
- --help             Show this help message and exit.
- --version          Show program's version number and exit.


## Features
- Customize work and break durations.
- Display a random motivational message after completing four Pomodoros.
- Support for long breaks to help users recover after long periods of work.

## License
This project is licensed under the GNU General Public License v3.0 (GPLv3). For details, see the [LICENSE](LICENSE) file.

## Developer
Matrix Huang

## Contact
If you have any questions or suggestions, feel free to contact me through GitHub Issues.
Mail: <15080083554@163.com>
Telegram: <https://t.me/MatrixHuangShare>
