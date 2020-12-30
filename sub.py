
import re
import xncode as x
import os
import sys
ans = (lambda a : raw_input(a))
shell = (lambda x : os.system(x))
X='<\033[1;31mX\033[1;37mcode>'

case    = x.mycase
encoder = x.encoders
decoder = x.decoders
encod   = x.encode
decod   = x.decode
exn     = x.ex_encode
exd     = x.ex_decode
myen    = x.myencoders
hese    = x.hexec
xbanner = x.xcode_banner

enc_inf="    encoders(str, format, password)"
Str='    string   : '
enc='    format   : [A]lphabet, [N]umber, [P]unctuation | [D]efault >> '
pwd='    password : '

ohellno="""
Wellcome To Xncoders...

This Are All Function From sub.py

__all__ = ['decode', 'decoders', 'encode', 'encoders', 'ex_decode', 'ex_encode',
           'help', 'hexec', 'info', 'main', 'myencoders', 'update', 'write',
           'xcode_banner', 'xnxx']

__dict__ = 'maaf Modul Ini Dilarang Ada Scammer Directori !, Ntar Ketauan Dong :('

function:

    decode(s)
    # Hanya Uncompile Function decode saja !

    decoders(s, password={}None{})
    # Multi Fungsi Uncompile encoders. Dimana Setiap Format Yang Berbeda
    # Akan Mengotomatisasi Fungsi ini Untuk Membaca Dan Memecahkan Compile Nya
    # Untuk Password, Diharapkan Bertanya Dulu Kepada Pembuat script :)

    encode(s)
    # Mungkin Tidak Spesial Sama Sekali, Namun encode Memiliki 3hex Digit Yang
    # Berbeda, Masukan encode('sss') sebagai Contoh, Dan Outputnya Akan Menjadi
    # Berbeda Dengan Ketiganya

    encoders(s, format=None, password={}None{})
    # Gunakan Encoders sebagai Alat Enkripsi Masakini :) Yang Dapat Bekerja
    # Layak nya marshal, Ya Kalo Di Bilang Sih Bukan Marshal, Karena
    # Ga bisa menCompile Sebuah atau Beberapa Fungsi
    # Format = ['alphabet', 'punct', 'number'] default nya 'PUNCTUATION'
    # password. Dilindungi Dalam Enkripsi. Jadi Aman Recoders Bos Que..

    ex_encode(s)
    # sama kaya encode, Gak Ada Spesial Nya Buat Yang Ini :(

    ex_decode(s)
    # cuman balikin string asli yang udah di compile ama ex_encode doang

    help()
    # Tampilkan Bantuan Ini Dan Keluar Jauh Jauh :(

    hexec()
    # Inilah Yang Membuat Tools Ini Seperti Marshal, decoders nya pun Bekerja dengan
    # semestinya, Gunakan hexec() apabila script Telah Di Compile dengan myencoders
    # Contoh :
    #    from sub import hexec
    #    dec='Ini String Yang Udah Di Compile'
    #    hexec(dex)
    #    Output Nya Pasti Kaya Script Biasanya, Ya Bisa Di Bilang Adik Nya Marshal
    #    Tadinya Nama Fungsi nya Mau Marshel, Tapi Gapapa Lah :)

    info()
    # Tampilkan animasi dari Developer :)

    menu()
    # Fungsi __main__ Utama Jika Sub Dipanggil Dengan Perintah python2 Tanpa
    # panggilan Import :)

    myencoders(filepath, outpath, format, password)
    # Gunakan myencoders untuk mengenkripsi File Fungsi nya Samalah Kaya Encoders
    # emang dalem nya encoders sih :)
    # Cuman Nambah with open(file, READ) Aja

    update()
    # Untuk Update Tools Ini Apabila Ada Versi Baru
    # Lebih baik Update Tools Dengan Manual, Karena Mungkin saja Terjadi Error

    write(s)
    # Ini Buat Yang Baru Belajar, Pahami Aja, Ntar Juga Suka :)

    xcode_banner()
    # Nah Kalo Yang Ini Jangan Di recode Ya BossQue, Ni Buat Segini Juga UYUHAN
    # AING MIKIRAN NA LIEUR, kalo mau pake Join Member Xcode Dlu Yah
    # Walaupun Tidak Ada Lisensinya, Tapi apasalahnya Izin Dulu :)

    xnxx()
    # ini buat Buka File Yang Mau Di hexec, Jadi Fungsinya Mencari String Dalam
    # File Yang memerintahkan hexec,
    # Ngerti lah pasti :( Cape Ni Gwe Nulis Basa Basi Njig_-
    # Di bayar Nggak Cape Iya


Udah Segitu Pasti Faham Lah, Kalo Masih Ga Faham Contact Aja W, Tuh Ada Di Info
    Sekiaan Da HaturNuhun Buat Baraya Yang Parantos Maca Dugi Dieu
    SAMPURASUN URANG SUNDA !!!

"""



oauth="""\n\n\n...Xncoders...\nAn Multi Decoders++\nTuntunan Untuk Recoders Pemula :)\n...\nIlmu Itu Gratis, Cuman Cara Nyari Nya Aja Yang Bayar Yekan?\nUntuk Itu Buat Yang Suka Recode.. Saya Tidak Mencaci Anda\nJustru Saya Mendukung Anda.. Cuman Kalo Mau Cari Ilmu Dan Recode Itu\nBilang Dulu "Saya Mau Recode", W Juga Pasti Ngizinin\nDan Pasti We Buka Tuh Compile main.py Cman People Cari Gampang aja\nSukanya Recode, Ganti Nama Author Tros Posting Lagi Ke Github\nTross Share Di Facebook/WhatsApp/Yotob dll.\nTross Ganti PP facebook Pake Gambar Anonimus\nTross Nongol Di Komentar Orang Awam, Tross Bilang\nWe Bantu Hack Facebook.. Halaaah :v\nAnda Sehat? Gapapa Lah Masih W Maapin...\n\n\n__Auth__\n_Audy and zollam_\nXCODE SCHIZOPHRENICS4\n\n__Team__\nXcode\n\n__ver__\n1.0\n\n__Repr__\nGaada Referensinya asw :(\n\n__License__\nGaada, Tapi Insyaallah Halal soalnya W Gak Recode Sc Orang :v\nCuman Test Unmarshal Aja Jadi Gak Sengaja Recode Sc Spam Orang :)\n\n__thanks To__\n\nAllah.SWT\n\n..:: People ::..\n\nNuubie from nuubi.herokuapp.com\nDebby Anggraeni from CIKU370\nRiana Sri Rahayu from Ciwidey City*\nWawan Wandi From Boling City\nAnton . Maap Ni orang Gatau Dari mana Tapi Makasih dah :)\nKira Llawlet\n\n..:: Team ::..\n\nSGB TEAM\nCIKU370\nNETSECs\n\n..:: Links ::..\n\nstackoverflow.com\npythonindo.com\ndan XNXX yang udah memotifikasi kita semua :)\n__Gak Lupa Juga__\nAll Family Linux User +62\nDan Yang Clone Script Ini :)\n\n\nWHAT NEXT ??\nOke Tunggu Beberapa Minggu Lagi.. W luncurin Script Bobol Nasa :v\nWkwwk Becanda.. Liat Aja Nanti, Udah Taun Baru Pokonya :)\nShare Ya, Kalo Udah Ada Yang Mecahin Compile main.py Punya Saya\nNtar Di Update Lagi. Nambahin Enkripsi Sama Dekripsi nya :)\nMakasih Buat Kalian Yang Udah Clone Script Ini :)\n\nBuat Yang Bingung Atau Kedapatan Bug ( except Tidak Tertanggapi ) Atau\nYang Udah Bisa Mecahin Encode Main.py, Hubungi Develop Ya :)\n+-------------------+----------+----------------+\n| +62 858-5986-0998 |   audy   |     Rahayu     |\n| +62 882-2341-5503 |  zollam  |   Den Hamdan   |\n|-------------------+----------+----------------|\n|      WhatsApp     |    Me    |        FB      |\n+-------------------+----------+----------------+\n"""

def mycase(s):
    return case(s)

def encoders(s, format=None, password=None):
    return encoder(s, format=format, password=password)

def decoders(s, password=None):
    return decoder(s, password=password)

def encode(s):
    return encod(s)

def decode(s):
    return decod(s)

def ex_encode(s):
    return exn(s)

def ex_decode(s):
    return exd(s)

def myencoders(inpath, outpath, format=None, password=None):
    return myen(inpath, outpath, format, password=password)

def hexec(s):
    hese(s)

def Xcode_Path(code=False):
    result=x.MPTH(x=True)
    if result is None:
        print '    %s Something Went Wrong !'%(X); exit()
    print '    %s Trying To building encryption...'%(X); time.sleep(1)
    if os.path.exists(result+'/xncode.pyc'):
        print '    %s Installation Done !'%(X); time.sleep(1)
    else:
        for x in sys.path:
            try:
                if os.path.exists(x+'/xncode.pyc'):
                     print '    %s Installation Done !'%(X); time.sleep(1)
            except:
                pass
        if os.path.exists(result+'/xncode.pyc') is False:
            print '    %s Installation Fail !\n    Please Tell Xcode Team Or Try All Step in First Step\n    ( $ git clone https://github.com/schizophrenics4/Xncoders.git )\n    If Installation Is Failed Again Please Tell This Bugs To Audy !\n    Thank You For Your Attentions ...'%(X); exit()


def xnxx(path):
    with open(path, 'rb') as o:
        dat=o.read()
        key=re.compile(r"`.*`.*`")
        res=key.findall(dat)
        if res is None:
            print '''    Duh Maaf File Tidak Valid, Pastikan Ia Punya String "dex='blablabla'"'''
            exit()
        else:
            #print [x for x in res]
            #data=str(res.group())[5:-1]
            data = res[0]
            axz=x.decoders(data, pw=x.decoders("""`:*-!;=?-+/:':??-?-?':!;!?-?!`:;:=!:!!;=:!*!==+*'''!:*/'--`""", password=x.execept.LovePassword))
            abs = compile(axz, 'asep', 'exec')
            exec abs ; exit()

def update():
    xz=ans('    Anda Yakin?\n    Mungkin Tools Akan Di install Ulang Apabila Tools Memiliki Pembaruan Atau Tidak\n    [ ENTER ] untuk Melanjutkan, Atau [ CTRL ] + Z untuk Keluar\n    ')
    PathName=os.path.dirname(os.abspath(__file__))
    PathToNew=os.path.dirname(PathName)
    system('git clone https://github.com/schizophrenics4/Xncoders.git')
    os.rename(PathName, 'IniBuangAja')
    system('mv Xncoders ~ && rm -rf '+PathToNew+'/IniBuangAja')
    if os.path.exists(PathToNew+'/Xncoders'):
        print '    Done !\n\n    *** Silahkan Restart Kembali Script ***'

from time import sleep as sl
def write(s):
    for c in s+'\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sl(0.06)


def info():
    pack=oauth.split('\n')
    for x in pack:
        a_name=len(x)/2
        b_name=44-a_name
        write(' '*b_name+x)
        sl(0.09)
    if __file__ == 'sub.py':
        sAnS=ans('    [ ENTER ] menu | [E] exit\n    >>> ').upper()
        if sAnS in ['', ' ']:
            main()


def main():
    shell('clear')
    xbanner()
    print """
        [1] encoders             [5] ex_encode              [U] Update
        [2] decoders             [6] ex_decode              [I] Info
        [3] encode               [7] myencoders             [H] Help
        [4] decode               [8] hexec                  [B] Back
        >>>--------------------------------------------->>> [E] Exit

    """
    tanya=(lambda x : raw_input(x))
    while 1:
        Ans=tanya(' '*4+X+' ').upper()
        try:
            ANS=int(Ans)
            if ANS == 1:
                STR = ans(Str)
                FOR = ans(enc)
                PAS = ans(pwd)
                print encoder(STR, FOR, password=PAS)
            elif ANS == 2:
                STR = ans(Str)
                PAS = ans(pwd)
                print decoder(STR, password=PAS)
            elif ANS == 3:
                STR = ans(Str)
                print encod(STR)
            elif ANS == 4:
                STR = ans(Str)
                print decod(STR)
            elif ANS == 5:
                STR = ans(Str)
                print exn(STR)
            elif ANS == 6:
                STR = ans(Str)
                print exd(STR)
            elif ANS == 7:
                print '    Ini Adalah Enkripsi File, Jika Password Kosong, Maka Akan Di isi dengan Default'
                while 1:
                    STR = ans('    inPath : ')
                    if os.path.exists(STR):
                        break
                    print '    Tidak Ada File Bernama : \033[1;31m%s\033[1;37m'%(STR)
                while 1:
                    FOR = ans('    outPath : ')
                    if os.path.exists(FOR):
                        print '    %s Sudah Ada, Bisa Ganti Ke File Lain?'
                    else:
                        break
                PAS = ans('    Password : ')
                print ' '*3, myen(STR, FOR, password=PAS)
            elif ANS == 8:
                while 1:
                    PATH = ans('    Path : ')
                    if os.path.exists(PATH):
                        xnxx(PATH)
                        exit()
        except ValueError:
            if Ans == 'U':
                update() ; break
            elif Ans == 'I':
                info() ; break
            elif Ans == 'B':
                print '\n    Makasih... :*'; break
            elif Ans == 'E':
                print '\n    Makasiiih... :*'; exit()


if __name__ == '__main__':
    main()

