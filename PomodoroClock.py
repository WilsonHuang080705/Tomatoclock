# Developer: Matrix Huang
# Website: https://github.com/WilsonHuang080705/PomodoroClock
import time
import sys
import datetime
import argparse
import textwrap
import random
import signal
import asyncio

class Timer:
    def __init__(self, prefix, seconds):
        self.prefix = prefix
        self.seconds = seconds
        self.end_time = datetime.datetime.now() + datetime.timedelta(seconds=self.seconds)

    async def countdown(self):
        while datetime.datetime.now() < self.end_time:
            remaining_time = (self.end_time - datetime.datetime.now()).total_seconds()
            minutes, seconds = divmod(int(remaining_time), 60)
            print(f"{self.prefix} {minutes:02d} 分钟 {seconds:02d} 秒", end='\r')
            await asyncio.sleep(1)

class PomodoroClock:
    def __init__(self, work_duration=25, short_break_duration=5, long_break_duration=15):
        self.work_duration = work_duration * 60  # Convert to seconds
        self.short_break_duration = short_break_duration * 60
        self.long_break_duration = long_break_duration * 60
        self.pomodoros_completed = 0

    def signal_handler(self, signal, frame):
        print("\nINFO 收到中断信号, 程序将退出。")
        sys.exit(0)

    async def start(self):
        signal.signal(signal.SIGINT, self.signal_handler)

        while True:
            print(f"INFO 欢迎使用番茄钟! \nINFO 你可以在https://github.com/WilsonHuang080705/PomodoroClock 来查看更多.\n\nINFO 开始工作，时长 {self.work_duration // 60} 分钟。\nINFO 按下Ctrl+C(Command+C)以退出番茄钟")
            
            # 工作
            await self.work()

            # 休息
            await self.take_break()

    async def work(self):
        timer = Timer("剩余时间:", self.work_duration)
        await timer.countdown()

    async def take_break(self):
        print("\nINFO 工作完成了, 休息一下吧！\nINFO 按下Ctrl+C或Command+C以退出番茄钟")
        self.pomodoros_completed += 1
        
        if self.pomodoros_completed % 4 == 0:
            print(f"INFO 4轮番茄钟已经过去, 进行长休息吧！时长 {self.long_break_duration // 60} 分钟。\nINFO 按下Ctrl+C或Command+C以退出番茄钟")
            long_break_messages = [
                "面朝大海，春暖花开。",
                "想要的都拥有，得不到的都释怀。",
                "明月松间照，清泉石上流",
                "日出江花红胜火，春来江水绿如蓝。"
            ]
            random_message = random.choice(long_break_messages)
            print(random_message)
            timer = Timer("INFO 长休息剩余时间:", self.long_break_duration)
            await timer.countdown()
        else:
            timer = Timer("INFO 剩余时间:", self.short_break_duration)
            await timer.countdown()

def parse_arguments():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent("""\
            The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. To use the Pomodoro method, choose a task to be completed, set the Pomodoro time to 25 minutes, focus on the work, not allowed to do anything unrelated to the task until the Pomodoro clock rings, and then tick on the paper to take a short break (5 minutes will do), and every four Pomodoro are completed to take a break for a little longer.
            """),
        epilog=textwrap.dedent("""\
            CORE COMMANDS
            --w, --work          Set the work duration in minutes (default: 25)
            --sb, --short-break  Set the short break duration in minutes (default: 5)
            --lb, --long-break   Set the long break duration in minutes after four Pomodoros (default: 15)
            --help               Show this help message and exit.
            --version            Show program's version number and exit.
            """),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--w", "--work", type=int, default=25, help="工作时长(分钟, 默认25分钟)")
    parser.add_argument("--sb", "--short-break", type=int, default=5, help="短休息时长(分钟, 默认5分钟)")
    parser.add_argument("--lb", "--long-break", type=int, default=15, help="长休息时长(分钟, 默认15分钟)")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0 Beta', help='显示程序版本信息')

    return parser.parse_args()

if __name__ == "__main__":
    try:
        args = parse_arguments()
        pomodoro_clock = PomodoroClock(work_duration=args.w, short_break_duration=args.sb, long_break_duration=args.lb)
        asyncio.run(pomodoro_clock.start())
    except KeyboardInterrupt:
        print("\nINFO 收到中断信号, 程序将退出。")
        sys.exit(0)