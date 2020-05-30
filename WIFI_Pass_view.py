import subprocess
import os
from typing import Any, Union


os.system("title WIFI Password View By weezerao")

print("""\033[5;32;40m=========================================================================================================
      _       ________________   ____                                          __   _    ___
| |     / /  _/ ____/  _/  / __ \____ ____________      ______  _________/ /  | |  / (_)__ _      __
| | /| / // // /_   / /   / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  /   | | / / / _ \ | /| / /
| |/ |/ // // __/ _/ /   / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /    | |/ / /  __/ |/ |/ /
|__/|__/___/_/   /___/  /_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/     |___/_/\___/|__/|__/  v0.1
                                                                                     by weezerao
==========================================================================================================
# An open source Python script
==========================================================================================================\033[0m\n\n""")


def menu():

    print("[+] Auto ---------------- (1)")
    print("[+] Manual  ------------- (2)")
    print("[+] Exit ---------------- (3)")

    user_in = input("\n \nWIFIPasswordView> ")
    print("\n")

    if user_in == '1':
        print(" \033[5;32;40m~~~~~~~~~~~~~~~~~~~Listing All WIFI Passwords~~~~~~~~~~~~~~~~~~ \033[0m\n")
        auto_scan()
    elif user_in == '2':
        scan_profile()
    elif user_in == '3':
        exit("Thanks For Using WIFI PassWord View")
    else:
        print('''\033[1;31;40m===========================================
Invalid option! Please try again....
===========================================\033[0m \n\n''')
        menu()


def scan_profile():
    scan_name = subprocess.check_output("netsh wlan show profiles | findstr All", shell=True).decode('utf-8')
    print("\033[5;32;40m~~~~~~~~~~~~~~~~~~Listing All Profile Name / WIFI Names~~~~~~~~~~~~~~~~~~ \033[0m\n")
    print("=======================================================\n ")
    print(scan_name)
    print("======================================================= ")
    print("\n")
    manual_output()


def manual_output():
    wifi_name = input("\033[5;32;40m Enter the SSID #  \033[0m")
    try:
        wifi_key = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key=clear']).decode('utf-8').split('\n')

        for i in wifi_key:
            if "Key Content" in i:
                pas = [i]
                print("\n\n*********************************************")
                print(wifi_name, "  :", pas[0][28:-1])
                print("*********************************************\n")
                input("\033[1;31;40mPress Any Key For Exit\033[0m")

    except subprocess.CalledProcessError:
        print('''\n\n\n\n\033[1;31;40m# !!!!!!!!!! ERROR !!!!!!!!!!
# Make sure you enter the correct SSID !
# Press any Key For Main Menu......\033[0m''')
        input()
        menu()


def auto_scan():
    profile_name = subprocess.check_output("netsh wlan show profiles | findstr All", shell=True).decode('utf-8').split(
        '\n')
    for i in profile_name:
        if "All User Profile" in i:
            profile_name = [i]
            name = profile_name[0][27:-1]

            key_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode(
                'utf-8').split('\n')

            for k in key_output:
                if "Key Content" in k:
                    print("\033[0;36;40m⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\033[0m")
                    print("    Profile Name  \t   : " + name +"\n"+ k)
                    print("\033[0;36;40m⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\033[0m\n\n")

    input('''\n\n\033[1;33;40m 
# Press Any Key For Exit\033[0m''')


menu()
