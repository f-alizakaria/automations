import os
import sys
import fileinput


def createHandddleDirIfNotExists():
    if not os.path.isdir('/usr/local/handddle/applications'):
        os.system('mkdir -p /usr/local/handddle/applications')

    if not os.path.isdir('/var/log/handddle_jetson_python'):
        list_dir = ['client', 'commands', 'datas', 'demo','farm_manager','gui','master','message','scanner','server','slave','tlv_message','watchdog']
        [os.system(f'mkdir -p /var/log/handddle_jetson_python/{dir}') for dir in list_dir]


def findPathFileOrDir(file, path=f"/home/{sys.argv[1]}", exclude=False):
    if not exclude:
        cmd = f"runuser -l {sys.argv[1]} -c 'find {path} -name {file}'"
    else:
        path = f"/home/{sys.argv[1]}/Documents"
        cmd = f"runuser -l {sys.argv[1]} -c 'find {path} -name {file} -not -path {path} '"
    stream = os.popen(cmd)
    output = stream.read().replace('\n', '')
    return output


def activateApp(userDirectory, appName):
    if not os.path.isfile(f"{userDirectory}/{appName}.desktop"):
        os.system(f"runuser -l {sys.argv[1]} -c 'cp {findPathFileOrDir(f'{appName}.desktop')} {userDirectory}'")
    if os.path.isfile(f"{userDirectory}/{appName}.desktop"):
        os.system(f"chmod a+x {f'{userDirectory}/{appName}.desktop'}")


def createDesktopApps(userDesktopDirectory):
    if not os.path.isdir(findPathFileOrDir('logos', '/usr/local/handddle')):
        os.system(f"cp -r {findPathFileOrDir('logos')} {findPathFileOrDir('applications', '/usr/local/handddle')}")

    activateApp(appName='handddle', userDirectory=userDesktopDirectory)
    activateApp(appName='maintenance', userDirectory=userDesktopDirectory)

    modifyDesktopFile("maintenance.desktop")
    modifyDesktopFile("handddle.desktop")
    modifyDesktopFile("handddle_app.desktop")


def userDesktopDir():
    if os.path.isdir(f'/home/{sys.argv[1]}/Desktop'):
        return f'/home/{sys.argv[1]}/Desktop'
    elif os.path.isdir(f'/home/{sys.argv[1]}/Bureau'):
        return f'/home/{sys.argv[1]}/Bureau'


def createAppAutoStart():
    if not findPathFileOrDir('autostart', f'/home/{sys.argv[1]}/.config'):
        os.system(f'mkdir -p /home/{sys.argv[1]}/.config/autostart')

    if not findPathFileOrDir('handddle_app.desktop', f'/home/{sys.argv[1]}/.config/autostart'):
        os.system(f"cp {findPathFileOrDir('handddle_app.desktop')} {findPathFileOrDir('autostart', f'/home/{sys.argv[1]}/.config')}")


def moveServiceFile():
    os.system(f"cp {findPathFileOrDir('handddle_jetson_python.service')} /etc/systemd/system")
    os.system("systemctl enable handddle_jetson_python.service")


def emptyTrash():
    os.system("rm -rf /home/ab/.local/share/Trash/*")


def modifyDesktopFile(file):
    browser = ""
    # Check which browser is available
    if os.path.isfile('/usr/bin/google-chrome'):
        browser = '/usr/bin/google-chrome'
    elif os.path.isfile('/usr/bin/chromium-browser'):
        browser = '/usr/bin/chromium-browser'

    with fileinput.FileInput(findPathFileOrDir(f'{file}', f"/home/{sys.argv[1]}", True), inplace=True) as file:
        for line in file:
            line = line.replace('<browser>', f'{browser}')
            line = line.replace('<url>', f'{sys.argv[2]}')
            print(line, end='')


def getHandddleJetsonPythonScript():
    if not os.path.isdir(findPathFileOrDir('handddle_jetson_python', '/usr/local')):
        os.system(f"git clone http://github.com/pierremrg/handddle_jetson_python {findPathFileOrDir('handddle', '/usr/local')}/handddle_jetson_python")

    # Modify and add bash script into folder
    with fileinput.FileInput(findPathFileOrDir('check_stm.sh'), inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('<user>', f'{sys.argv[1]}'), end='')

    if not os.path.isdir(findPathFileOrDir('bash_scripts', '/usr/local')):
        os.system(f"cp -r {findPathFileOrDir('bash_scripts')} {findPathFileOrDir('handddle_jetson_python', '/usr/local')}")

    if os.path.isfile(findPathFileOrDir('check_stm.sh.bak', '/usr/local')):
        os.system(f"rm {findPathFileOrDir('check_stm.sh.bak', '/usr/local')}")


if "__main__" == __name__:
    emptyTrash()
    desktopDir = userDesktopDir()

    createHandddleDirIfNotExists() # Log and Apps
    createDesktopApps(desktopDir)
    createAppAutoStart()
    moveServiceFile()

    getHandddleJetsonPythonScript()

