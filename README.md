# 观前须知😁
- Want to see the English version for introduction of PomodoroGUI? You can check it here [GUI For English](https://github.com/WilsonHuang080705/PomodoroClock/blob/main/README_GUI_en_US.md)
- 如果想要参阅带有用户界面的番茄钟，请参阅[GUI For Chinese](https://github.com/WilsonHuang080705/PomodoroClock/blob/main/README_GUI_zh_CN.md)
# Pomodoro Clock

## 简介
Pomodoro Clock 是一个基于番茄工作法的时间管理工具，由 Matrix Huang 开发。该工具旨在帮助用户通过设定工作和休息的周期来提高工作效率和专注度。

## 运行环境
- Python 3.7.x 及以上

## 使用说明（示例）
1. 克隆或下载本仓库到本地。
```
git clone https://github.com/WilsonHuang080705/PomodoroClock.git
```
2. 安装依赖库。
```
pip install -r requirements.txt
```
3. 使用 Python 运行 `PomodoroClock.py` 文件
```
Python PomodoroClock.py
```
4. 通过命令行参数自定义工作时长、短休息时长和长休息时长。
```
Python PomodoroClock.py --w 25 --sb 5 --lb 15
```
如果没有安装Python语言，你也可以点击PomodoroClock-win-x86的文件夹，再点击PomodoroClock.exe来运行程序。但请注意，.exe程序不能自定义工作时长，短休息时长和长休息时长。

## 命令行参数

- --w, --work          设置以分钟计的工作时长 (默认: 25分钟)
- --sb, --short-break  设置以分钟计的短休息时长 (默认: 5分钟)
- --lb, --long-break   设置以分钟计的长休息时长 (默认: 15分钟)
- --help               显示帮助信息
- --version            显示版本号

## 特点
- 自定义工作和休息时长。
- 完成四个番茄钟后，随机显示一句优美的诗句。
- 支持长休息，帮助用户在长时间工作后恢复精力。
- 可以暂停番茄钟，并重新开始

## 许可证
本项目遵循 GNU General Public License v3.0 (GPLv3)。详情请查看 [LICENSE](LICENSE) 文件。

## 开发者
Matrix Huang

## 联系
如果你有任何问题或建议，欢迎通过 GitHub Issues 与我联系。
Email: <15080083554@163.com>
Telegram: <https://t.me/MatrixHuangShare>
