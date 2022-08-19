import time
import subprocess
import sys
import typer
import os

class birthday():
    def __init__(self):
        super().__init__()
    usr_home_dir=os.environ.get('HOME')
    dir_path=f"{usr_home_dir}/.config/bday-tracker"
    conf_path=f"{usr_home_dir}/.config/bday-tracker/bday-list"
    cmd = typer.Typer()

    @cmd.command()
    def bdayListAppend(name: str, surname: str, date: float, month: float, year_born: float):
        global dir_path
        global conf_path
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            with open(conf_path, "w") as f:
                f.close()

        if not os.path.exists(conf_path):
            open(conf_path, 'w').close()

        with open(conf_path, 'a') as f:
            # f.write(f"{self.args.date[0]}-{self.args.month[0]} {self.args.name[0]} {self.args.surname[0]}--{self.args.year_born[0]}\n")
            f.write(f"{date}-{month} {name} {surname}--{year_born}")

    @cmd.command()
    def CheckIsTodayBday(self):
        with open(self.conf_path) as f:
            today = time.strftime('%d-%m')
            flag = 0
            for line in f:
                line = line.split(' ')
                if today in line[0]:
                    flag = 1
                    surname = line[2].split('--')[0]
                    # line[1] is name line[2] is surname line[3] is year_born
                    subprocess.call(f'notify-send "Birthdays Today: {line[1]} {surname} "', shell=True)

            if flag == 0:
                subprocess.call('notify-send "No Birthdays today"', shell=True)


if __name__ == '__main__':
    start = birthday()
    start.cmd()
    # start.CheckIsTodayBday()
