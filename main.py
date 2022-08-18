import time
import subprocess
import sys
import argparse
import os

class birthday():
    def __init__(self):
        super().__init__()
        self.usr_home_dir=os.environ.get('HOME')
        self.dir_path=f"{self.usr_home_dir}/.config/bday-tracker"
        self.conf_path=f"{self.usr_home_dir}/.config/bday-tracker/bday-list"
        self.parser = argparse.ArgumentParser(description='Reminder for whose birthday it is')

    def bdayListAppend(self): #, name, surname, date, month, year_born):
        self.parser.add_argument("name", nargs=1, metavar='<name-of-birthday-person>', type=str, help='name of the person whose birthday it is')
        self.parser.add_argument("surname", nargs=1, metavar='<surname-of-birthday-person>', type=str, help='surname of the person whose birthday it is')
        self.parser.add_argument("date", nargs=1, metavar='<date-of-birthday>', type=int, help='date of birthday')
        self.parser.add_argument("month", nargs=1, metavar='<month-of-birthday>', type=int, help='month of birthday')
        self.parser.add_argument("year_born", nargs=1, metavar='<year-of-birthday>', type=int, help='year of birthday')
        self.args = self.parser.parse_args()
        print(self.args)
        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)
            with open(self.conf_path, "w") as f:
                f.close()

        if not os.path.exists(self.conf_path):
            open(self.conf_path, 'w').close()

        with open(self.conf_path, 'a') as f:
            f.write(f"{self.args.date[0]}-{self.args.month[0]} {self.args.name[0]} {self.args.surname[0]}--{self.args.year_born[0]}\n")


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
    # start.bdayListAppend()
    start.CheckIsTodayBday()
