#!/data/data/com.termux/files/home/Xcoders/XPATH/core.py
# -*- coding : utf-8 -*-
# CoAuth : __AudyXcode__
import sys
import os
import time
import shutil
import xncode
import subprocess as SUB

# //// SENGAJA SAYA BUAT RAPIH SEBISA SAYA, KARENA SUKA BANYAK YANG LIAT.
# //// TAKUTNYA DI BILANG PROGRAMERS KEMAREN SORE :V
W='\033[1;37m'
X='<\033[1;31mX\033[1;37mcode>'
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
P='\033[1;35m'
U='\033[1;36m'
R_='\033[41;37;1m'
G_='\033[42;37;1m'
Y_='\033[43;37;1m'
B_='\033[44;37:1m'
P_='\033[45;37:1m'
U_='\033[46;37:1m'
W_='\033[47;37:1m'
N_='\033[0;37;1m'

# ////    SILAHKAN RECODE DAN BELAJAR.. TIDAK USAH MENGGANTI CREDIT / AUTHOR NAME ////#
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

# //// ini fungsi Text Berjalan Coe
def writes(i, tm):
    for x in i+'\n':
        sts.write(x)
        sts.flush()
        time.sleep(tm)

# //// MAAF SAYA ENKRIPSI, KARENA JIKA KANG RECODE MUNCUL DAN TAU TUJUANNYA WAH BAHAYA
# //// BISA BISA BANYAK FIRUS COV-19 DI HP ANDA :(
def agus_checker():
    import zlib, marshal, base64
    exec marshal.loads(zlib.decompress(base64.b64decode('eJx1Uttu00AQnY1zby7lInhCChKV8tJYSgXtA6pAArUvlEuREuUlcrybeO34Es+6iXntB/Ch/AQzm0AlJNbas3M5M2fWtg+HVaf9jjb+IlAAoYBZBSTAzAHlgBTwfFYFVYOwDpISDtxXQBz8Ksia9cszS2lwXtb3lCaELfZV1fqyAaoN6giWFXh2dT1J3oAQ4v9VeyHZBNV5qEoETLmkC7IF94L4PZBtkEdM/vkUZn1QfQiPQXZseiK78HV6aNqzRdy0C7fDPl/6lMCVnvH24KfxyKg8LnbuUq8VugXm7lov3Kw0QZqMR+fY4wrURp1mnh95K4X4ikLBpriQwTbC1Xah1fl4hYtoo8vX44tgtQ0XqEdZiS0i7hI/lYq9F+R5C1+q5SrQYbSOkzTb5GiKu+2u/MGMBjFiTydk65ZD47L4gNYJfvh883Hw8gSx80/I1Cgw/fL++zU++mO587lOtJnPqZGpWFnD3/7GKvhpzvMMmW4cfislmiqdmWcCI5hu+C+JS762NT+Vt2xyqxRtJFeJFysr7gdxKm0Qg8Lote0Vp3fK9rqyOLH4zfLjSOrcktJMJTaR2sQ2J5EhD/oAyIm3KvEvTZMtkirW6pKLcEDQEnXRFsf0OBaf/D274jHhb6N+m/c=')))


"""
MUNGKIN BEBERAPA PROGRAMINGS JARANG MENGGUNAKAN PRINSIP END INI...
TIDAK RUMIT BAGI MEREKA NAMUN MUNGKIN MEREKA TIDAK SUKA DENGAN INI
PRINSIP TEXT DOWN TO UP, YANG KAYA END-ING DI FILM KALO UDAHAN ASW :(

JIKA BELAJAR FUNGSI INI JANGAN GUNAKAN DULU WRITES, ATAU TEXT BERGERAK
YA ITU SIH ANJURAN SAYA, SOALNYA RIBET BANGET, HARUS CUT STRING LAH
HARUS NGITUNG STRING LAH, AH CAPE BNGKE :(

KELIATAN NYA SIH SIMPLE KAYA GITU, ERROR DIKIT FATAL TU :(
"""

zollam="""\n..:: %s XCODERS %s ::..\nUnmarshal and Other Compile Tools\nSebenernya Ni Script Udah Lama Bet Di Hape Gwe, Cuman Pas Waktu Itu Gak Kepikiran\nBuat Post Ni Script,  Dan W Sibuk Cari Artikel Yang Bisa  Mastiin  Facebook Masih\nBisa  Di  Tuyul,   Eh Lama  Lama  Ganemu  Yawdah  Bikin  Ni Konten  Di Github  :v\n\nCocok Untuk Para  Recoders Yang Uncreative, Ya Seringkali Recode Nya Jarang Mikir\nNya, Kaya Anda :D :v.  Thanks Udah Clone Script Unmarshal Ini Ea :) Bismillah Dlu\nBaca Doa Dulu, Karena KebanyakanOrang YangGagal Dalam Coding Dan Recode Jadi Gila\n\n*** %sThanks For%s ***\n... Allah Subhanahu Wa Ta'ala ...\n__Auth__\n-*- Audy | Sri Rahayuu -*-\n-*- zollam | Den Hamdan -*-\n__Inspiration__\n-*- Debby Anggraeni -*-\n-*- Nuubi Heroku Apps -*-\n__Teams__\n-*- XCODE | CiKu370 | NETSc | SGBTEAM | MCPCIV | LyPathX -*-\nAnd For Any People Yang Udah Clone Sc Kami :)\n\n*** %sLicense%s ***\nGak Ada Tapi Insyaallah Halal, AMIIIN\n\n*** %sSource%s ***\n[%shttps://github.com/schizophrenics4/Xcoders%s]\n\n*** %sContact%s ***\n+----------------+------------+-----------------+-----------+\n|    WhatsApp    |  Facebook  |    InstaGram    | XcodeTeam |\n+----------------+------------+-----------------+-----------+\n| 0857-5986-0998 |   Rahayuu  |   TydackPunya   |   Audy    |\n| 0882-2341-5503 | Den Hamdan | @zollam.frontal |  zollam   |\n+----------------+------------+-----------------+-----------+\n\n~~> TAMBAHAN <~~\nJIKA MENGGUNAKAN  UNMARSHAL DAN FILE BERFORMAT  PYC GUNAKAN UNPYC TERLEBIHDAHULU\nDAN BILA  SOURCE MARSHALL BERISI  zlib.decompress(base64.b64decode LANGSUNG SAJA\nUNMARSHAL, KARENA JIKA DI COMPILE MANUAL DULU SERINGKALI TERJADI ERROR DAN TERUS\nMENERUS GAGAL, KARENA SAYA MENGGUNAKAN WHILE FUNCTION, DAN JIKA DI BIARKAN TERUS\nDENGAN PESAN  ERROR MESSAGE,  LAMA-LAMA PERANGKAT ANDA PANAS,  RUSAK,  DAN  MATI\nSEKETIKA :(  DAN COBA MENU XCODERS YANG DI PAKAI DI MAIN.PY YA, ITU COMPILE SAYA\n
"""%(R_, N_, Y, W, Y, W, Y, W, U, W, P, W)

def end():
    for x in zollam.split('\n'):
        a=44-(len(x)/2)
        try:
            if x[0] == '[': a+= 8
            elif x[:3] == '..:': a+= 10
            elif x[:3] == '***': a+= 7
        except: pass
        writes(' '*a+x, 0.09)


#//// JIKA INGIN BELAJAR TAMPILAN LOADING BERJALAN, SILAHKAN PELAJARI ATAU HUB SAYA :)
def asep_checker():
    me = sts.write
    ans("    %s SEBELUM MEMULAI, BAHASA DI ALIHKAN KE BAHASA DEFAULT\n    Untuk Performa Yang Lebih Baik, Gunakan Ukuran Layar (88)\n    Atau Anda Dapat Mengatur Dengan Menempatkan\n    Ukuran Layar Agar Sejajar Dengan Garis Di Bawah !\n"%(X)+'-'*88+'\nTekan [ ENTER ] Untuk Melanjutkan !'); shel('clear')
    xncode.xcode_banner()
    me('    Wellcome To Xcode...\n    ----------------------->>\n    Start Installation Time   : '); writes('%s:%s:%s  %s\n                                %s, %s-%s-%s'%(jam, men, det, time.tzname[1], day, tgl, bln, thn), 0.09)
    dev=[]
    # ANDA TAU GETPROP?? HADUHH ITU BAWAAN TERMUX.. HECK FACEBOOK MULU SII :V
    sc='getprop '
    U='\033[1;36m'

    device_information_list=['ro.build.version.release', 'ro.build.version.sdk', 'ro.build.version.security_patch', 'ro.product.locale.region', 'ro.product.manufacturer', 'ro.product.mod_device', 'ro.product.model', 'persist.sys.device_name', 'net.lte.ims.data.enabled']
    [dev.append(subshel(sc+x)) for x in device_information_list]
    me('                         ***** Trying To Configurate *****\n')
    # Ini Kalo Di Hape Gw ( XIAOMI ) Muncul semua, Tapi We Coba di oppo cuman Beberapa
    me('    Device Product     : '); writes(dev[4], 0.09)
    me('    Device Models      : '); writes(dev[6], 0.09)
    me('    Device Version     : '); writes(dev[0], 0.09)
    me('    Device Name        : '); writes(dev[7], 0.09)
    me('    Device Mod Name    : '); writes(dev[5], 0.09)
    me('    Devive Sdk Version : '); writes(dev[1], 0.09)
    me('    Security Path      : '); writes(dev[2], 0.09)
    me('    Region             : '); writes(dev[3], 0.09)
    me('    Connection         : '); writes(dev[8], 0.09)
    print '\n'
    if dev[8] == 'false':
        print('\n    Harap Hidupkan Data Seluler Anda Untuk Menginstall Modul External'); time.sleep(1)
        ans('\n    Dan Tekan [ ENTER ] Untuk Melanjutkan')
    shel('pip2 install --upgrade pip && pip2 install uncompyle6')
    pip=subshel('pip2 list').split()
    print '    Tring To Build Database...'
    count = 1
    # Kalo Percaya Gw Koding Dari Jam 2 - 2:50 Hapir 1 jam dapet 3 script
    # Eh Gataunya Benerin Errornya 4 Hari Gblg :(
    for x in pip:
        if x in ['Version', 'Package'] or '.' in list(x) or x[:2] == '--':
            count -= 1; pass
        else:
            freak=85-(len(x)/2)
            sys.stdout.write('\r[ %sINSTALLED%s ] %s%s'%(G, W, x, ' '*freak))
            sys.stdout.write('\r%sX%sCODE Configuration.Modules : %s%s%s '%(R, W, U, x, W))
            sys.stdout.flush()
            time.sleep(0.1)





# MAAF DISINI SAYA GABUT, DAN KEHILANGAN INSPIRASI :(
if __name__ == '__main__' and sys and os and time and True: # and a gila ya ? :v
    if 1 + 7 != 9 and W and X and sts:
        basmalah = ans('    Tulis " BISMILLAHIRROHMANIRROHIM " Jangan Di Copas : ').upper()
        if basmalah == 'BISMILLAHIRROHMANIRROHIM':
            asep_checker()
            agus_checker()
            end()
