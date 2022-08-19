import time
import subprocess
import sys
import typer
import os

cmd = typer.Typer()

usr_home_dir=os.environ.get('HOME')
dir_path=f'{usr_home_dir}/.config/bday-tracker'
bday_list_path=f'{dir_path}/bday-list'

@cmd.command()
def bdayListAppend(name: str, surname: str, date: int, month: int, year_born: int):
    global dir_path
    global bday_list_path
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        with open(bday_list_path, 'w') as f:
            f.close()

    if not os.path.exists(bday_list_path):
        open(bday_list_path, 'w').close()

    with open(bday_list_path, 'a') as f:
        f.write(f'{date}-{month} {name} {surname}--{year_born}\n')

@cmd.command()
def CheckIsTodayBday():
    global bday_list_path
    if not os.path.exists(bday_list_path):
        sys.exit()
    else:
        with open(bday_list_path) as f:
            today = time.strftime('%d-%m')
            flag = 0
            for line in f:
                line = line.split(' ')
                if today in line[0]:
                    flag = 1
                    surname = line[2].split('--')[0]
                    # line[0] is date-month line[1] is name line[2] surname--year_born
                    subprocess.call('notify-send "Birthdays Today: {line[1]} {surname}"', shell=True)
            if flag == 0:
                subprocess.call('notify-send "No Birthdays today"', shell=True)

if __name__=='__main__':
    cmd()
