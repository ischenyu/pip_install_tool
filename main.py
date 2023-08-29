import os,getpass,sys
from time import sleep

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def ubuntu(user_input):
    zhixing = user_input
    print(zhixing)
    if zhixing == '1':
        print(Colors.YELLOW + "准备安装，等待5秒，按Ctrl+C退出" + Colors.ENDC)
        sleep('5')
        os.system('curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh')
    elif zhixing == '2':
        print(Colors.YELLOW + "准备安装，等待5秒，按Ctrl+C退出" + Colors.ENDC)
        sleep('5')
        os.system('wget -O install.sh http://download.bt.cn/install/install-ubuntu.sh && sudo bash install.sh')
    elif zhixing == '3':
        led = input('请选择要控制的灯   1.红灯 2.绿灯 3.蓝灯')
        if led == '1':
            kg = input('1.开 2.关')
            if kg == '1':
                os.system('chmod 777 led & ./led red 1')
                print(Colors.GREEN + "完成" + Colors.ENDC)
            elif kg == '2':
                os.system('chmod 777 led & ./led red 0')
                print(Colors.GREEN + "完成" + Colors.ENDC)
            else:
                print(Colors.RED + "输入有误！" + Colors.ENDC)
        elif led == '2':
            kg = input('1.开 2.关')
            if kg == '1':
                os.system('chmod 777 led & ./led green 1')
                print(Colors.GREEN + "完成" + Colors.ENDC)
            elif kg == '2':
                os.system('chmod 777 led & ./led green 0')
                print(Colors.GREEN + "完成" + Colors.ENDC)
            else:
                print(Colors.RED + "输入有误！" + Colors.ENDC)
        elif led == '3':
            kg = input('1.开 2.关')
            if kg == '1':
                os.system('chmod 777 led & ./led blue 1')
                print(Colors.GREEN + "完成" + Colors.ENDC)
            elif kg == '2':
                os.system('chmod 777 led & ./led blue 0')
                print(Colors.GREEN + "完成" + Colors.ENDC)
            else:
                print(Colors.RED + "输入有误！" + Colors.ENDC)
    if ubuntu == '4':
        os.system('fdisk -l && df -h')
                
            

def main():
    # 使用getpass模块获取有效用户名，即实际运行脚本的用户
    if getpass.getuser() == 'root':
        pass
    else:
        print('请使用root权限运行！')
        sys.exit()
    menu = '''
 __          __             _______             _      
 \ \        / /            |__   __|           | |     
  \ \  /\  / /__ _  _ __      | |  ___    ___  | | ___ 
   \ \/  \/ // _` || '_ \     | | / _ \  / _ \ | |/ __|
    \  /\  /| (_| || | | |    | || (_) || (_) || |\__ \
     \/  \/  \__,_||_| |_|    |_| \___/  \___/ |_||___/
                                                       
                                    
                                    仅适用于玩客云                 
    请选择你现在使用的系统
    1.海纳思系统Ubuntu
    2.Armbian\n'''
    
    info_ubuntu = '''
    1.安装1panel
    2.安装宝塔面板5.9
    3.LED灯控制
    4.外部存储管理'''
    
    info_armbian = '''
    1.安装1panel
    2.安装宝塔面板5.9
    3.LED灯控制
    4.外部存储管理'''
    
    user_input = input(menu)
    
    if user_input == '1':
        os.system('clear')
        ubuntu_input = input(info_ubuntu)
        ubuntu(user_input)
        # 处理 Ubuntu 相关逻辑
        # ...
    elif user_input == '2':
        os.system('clear')
        armbian_input = input(info_armbian)
        # 处理 Armbian 相关逻辑
        # ...
    else:
        print('请输入正确的选项！')
        os.system('clear')
        main()  # 递归调用主函数，返回到菜单重新执行
    

if __name__ == '__main__':
    if getpass.getuser() == 'root':
        main()
    else:
        print('请使用root权限运行！')
        sys.exit()
