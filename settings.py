import sys
import os
import time
import xncode
import subprocess as SUB

W='\033[1;37m'
X='<\033[1;31mX\033[1;37mcode>'
U='\033[1;36m'
P='\033[1;35m'
G='\033[1;32m'
ans = (lambda a: raw_input(a))
shel = (lambda b: os.system(b))
subshel = (lambda c: SUB.check_output(c, shell=True, stdin=sys.stdin).rstrip())
sts=sys.stdout
T=time.localtime()
day=['SENIN', 'SELASA', 'RABU', 'KAMIS', 'JUMAT', 'SABTU', 'MINGGU'][T.tm_wday]
tgl=T.tm_mday
bln=['', 'JANUARI', 'FEBRUARI', 'MARET', 'APRIL', 'MEI', 'JUNI', 'JULI',
    'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER', 'DESEMBER'][T.tm_mon]
thn=T.tm_year
jam=T.tm_hour
men=T.tm_min
det=T.tm_sec

def writes(i):
    for x in i+'\n':
        sts.write(x)
        sts.flush()
        time.sleep(0.09)

def asep_checker():
    me = sts.write
    ans("    %s SEBELUM MEMULAI, BAHASA DI ALIHKAN KE BAHASA DEFAULT\n    Untuk Performa Yang Lebih Baik, Gunakan Ukuran Layar (88)\n    Atau Anda Dapat Mengatur Dengan Menempatkan\n    Ukuran Layar Agar Sejajar Dengan Garis Di Bawah !\n"%(X)+'-'*88+'\nTekan [ ENTER ] Untuk Melanjutkan !'); shel('clear')
    xncode.xcode_banner()
    me('    Wellcome To Xcode...\n    ----------------------->>\n    Start Installation Time   : '); writes('%s:%s:%s  %s\n                                %s, %s-%s-%s'%(jam, men, det, time.tzname[1], day, tgl, bln, thn))
    dev=[]
    sc='getprop '
    U='\033[1;36m'

    device_information_list=['ro.build.version.release', 'ro.build.version.sdk', 'ro.build.version.security_patch', 'ro.product.locale.region', 'ro.product.manufacturer', 'ro.product.mod_device', 'ro.product.model', 'persist.sys.device_name', 'net.lte.ims.data.enabled']
    [dev.append(subshel(sc+x)) for x in device_information_list]
    me('                         ***** Trying To Configurate *****\n')
    me('    Device Product     : '); writes(dev[4])
    me('    Device Models      : '); writes(dev[6])
    me('    Device Version     : '); writes(dev[0])
    me('    Device Name        : '); writes(dev[7])
    me('    Device Mod Name    : '); writes(dev[5])
    me('    Devive Sdk Version : '); writes(dev[1])
    me('    Security Path      : '); writes(dev[2])
    me('    Region             : '); writes(dev[3])
    me('    Connection         : '); writes(dev[8])
    if dev[8] == 'false':
        me('\n    Please Turn On Your Data Connection And Install Some Modules... !'); time.sleep(1)
        ans('\n    Please [ ENTER ] to Continue Install some Modules !')
    shel('pip2 install --upgrade pip && pip2 install uncompyle6 && pip2 install pycrypto')
    me('    %s Trying To Check Path...'%(X))
    pip=subshel('pip2 list').split('\n')
    if 'uncompyle6' in pip and 'pycrypto' in pip:
        me('    %s Checking Succes, All Request Completed !\n    Please Wait to Unpack Xcode Path...'%(X)); MySite = '/data/data/com.termux/files/home/.local/lib/python2.7/site-packages'
    else:
        me('    Some Modules Cant Installed :( Please Try Again With Shell Command\n    Usage : $ pip2 install pycrypto && pip2 install uncompyle6'); MySite = '/data/data/com.termux/files/home/.local/lib/python2.7/site-packages'
    from sub import Xcode_Path as XP
    if MySite in sys.path:
        XP()
    else:
        XP(code=True)
    me('    One More Step Agains... !')
    pypath='/data/data/com.termux/files/usr/lib/python2.7'
    shel('chmod 777 sub.py')
    shel('chmod 777 main.py')
    shel('mv sub.py '+pypath)
    if os.path.exists(pypath+'/sub.py'):
        writes('    Succes...\n    Now, You Can See The Directories List !')
        delet=ans('    Path Was Installed, Do you want to get rid of useless path?\n    [Y]es | will [N]ot : ').upper()
        if delet == 'Y':
            os.remove('settings.py')
        elif delet == 'N':
            os.rename('settings.py', 'File_Udah_Gaguna.py')
        shel('rm -rf xncode.pyc')
        shel('rm -rf settings.pyc')
        shel('rm -rf main.pyc')
        shel('rm -rf sub.pyc && clear')
        print '-'*88+'\n'+' '*18+'Installation %sDone%s, Please %sRun Again%s This Scripts !\n'%(G, W, P, W)+'-'*88



if __name__ == '__main__' and sys and os and time and True: # and a gila ya ? :v
    if 1 + 7 != 9 and W and X and sts:
        basmalah = ans('    Tulis " BISMILLAHIRROHMANIRROHIM " Jangan Di Copas : ').upper()
        if basmalah == 'BISMILLAHIRROHMANIRROHIM':
            asep_checker()
