# Developer: Matrix Huang
# Website: https://github.com/WilsonHuang080705/PomodoroClockc
import wx
import random
import pygame
import time

class PomodoroClock(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 300))
        
        self.work_minutes = 25
        self.short_break_minutes = 5
        self.long_break_minutes = 15
        self.pomodoros_completed = 0
        self.paused = False
        self.remaining_time = None

        # Initialize pygame mixer for sound
        pygame.mixer.init()
        self.ding_sound = pygame.mixer.Sound("ding.wav")  # Load the ding sound file

        # Create panel and sizer for layout
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(10, 10)

        # Create input fields and labels
        work_label = wx.StaticText(panel, label="工作时长(分钟):")
        self.work_text = wx.TextCtrl(panel, value=str(self.work_minutes), size=(50, -1))
        
        sb_label = wx.StaticText(panel, label="短休息时长(分钟):")
        self.sb_text = wx.TextCtrl(panel, value=str(self.short_break_minutes), size=(50, -1))
        
        lb_label = wx.StaticText(panel, label="长休息时长(分钟):")
        self.lb_text = wx.TextCtrl(panel, value=str(self.long_break_minutes), size=(50, -1))

        self.timer_label = wx.StaticText(panel, label="")

        # Buttons for start, pause/resume and help
        start_button = wx.Button(panel, label="开始")
        pause_resume_button = wx.Button(panel, label="暂停/继续")
        help_button = wx.Button(panel, label="帮助")
        
        # Set sizer
        sizer.Add(work_label, pos=(0, 0), flag=wx.LEFT, border=10)
        sizer.Add(self.work_text, pos=(0, 1), flag=wx.EXPAND)
        
        sizer.Add(sb_label, pos=(1, 0), flag=wx.LEFT, border=10)
        sizer.Add(self.sb_text, pos=(1, 1), flag=wx.EXPAND)
        
        sizer.Add(lb_label, pos=(2, 0), flag=wx.LEFT, border=10)
        sizer.Add(self.lb_text, pos=(2, 1), flag=wx.EXPAND)
        
        sizer.Add(self.timer_label, pos=(3, 0), span=(1, 2), flag=wx.EXPAND | wx.TOP, border=20)

        sizer.Add(start_button, pos=(4, 0), flag=wx.LEFT | wx.BOTTOM, border=10)
        sizer.Add(pause_resume_button, pos=(4, 1), flag=wx.BOTTOM, border=10)
        sizer.Add(help_button, pos=(5, 0), span=(1, 2), flag=wx.EXPAND | wx.TOP, border=20)
        
        panel.SetSizer(sizer)

        # Bind button events
        start_button.Bind(wx.EVT_BUTTON, self.on_start_pomodoro)
        pause_resume_button.Bind(wx.EVT_BUTTON, self.toggle_pause)
        help_button.Bind(wx.EVT_BUTTON, self.show_help)

        self.Show()

    def countdown(self, remaining_time, is_break=False, long_break=False):
        if self.paused:
            return
        
        if remaining_time <= 0:
            if long_break:
                self.pomodoros_completed += 1
                self.show_random_message()
                self.countdown(self.long_break_minutes * 60, is_break=True, long_break=True)
            else:
                if is_break:
                    self.pomodoros_completed += 1
                    if self.pomodoros_completed % 4 == 0:
                        self.countdown(self.long_break_minutes * 60, is_break=True, long_break=True)
                    else:
                        self.countdown(self.short_break_minutes * 60, is_break=True)
                else:
                    self.countdown(self.work_minutes * 60)
            return

        minutes, seconds = divmod(remaining_time, 60)
        self.timer_label.SetLabel(f"剩余时间: {minutes:02d} 分钟 {seconds:02d} 秒")
        
        # Use wx.CallLater for a non-blocking delay
        wx.CallLater(1000, self.countdown, remaining_time - 1, is_break, long_break)

    def toggle_pause(self, event):
        self.paused = not self.paused
        if self.paused:
            self.timer_label.SetLabel("已暂停")
        else:
            self.countdown(self.remaining_time)

    def show_random_message(self):
        messages = ["面朝大海，春暖花开。",
                    "想要的都拥有，得不到的都释怀。",
                    "明月松间照，清泉石上流",
                    "日出江花红胜火，春来江水绿如蓝。"]
        random_message = random.choice(messages)
        self.timer_label.SetLabel(random_message)
        
        # Play the "ding" sound when the message is shown
        self.ding_sound.play()

        # Show a dialog with completion message
        wx.MessageBox("恭喜你完成了一个番茄钟！休息一下吧。", "任务完成", wx.OK | wx.ICON_INFORMATION)

    def on_start_pomodoro(self, event):
        try:
            self.work_minutes = int(self.work_text.GetValue())
            self.short_break_minutes = int(self.sb_text.GetValue())
            self.long_break_minutes = int(self.lb_text.GetValue())
        except ValueError:
            self.show_error_message("请输入有效的数字!")
            return

        self.remaining_time = self.work_minutes * 60
        self.countdown(self.remaining_time)

    def show_error_message(self, message):
        wx.MessageBox(message, "错误", wx.OK | wx.ICON_ERROR)

    def show_help(self, event):
        help_message = (
            "番茄钟使用指南：\n\n"
            "1. 设置工作时长、短休息时长和长休息时长。\n"
            "2. 点击'开始'按钮开始计时。\n"
            "3. 当时间结束时，您将听到'叮'的提示音，并看到任务完成的消息。\n"
            "4. 点击'暂停/继续'来暂停和恢复计时。\n"
            "5. 每完成四个番茄钟，您将进入长休息时段。"
        )
        wx.MessageBox(help_message, "帮助", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = wx.App(False)
    PomodoroClock(None, title="番茄钟计时器")
    app.MainLoop()
