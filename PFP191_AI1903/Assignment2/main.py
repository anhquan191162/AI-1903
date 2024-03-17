import os

__location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

class Sach():
    def __init__(self, Ten_sach, Ten_tac_gia, Nha_xuat_ban, Nam_XB, Gia_ban):
        self.Ten_sach = Ten_sach
        self.Ten_tac_gia = Ten_tac_gia
        self.Nha_xuat_ban = Nha_xuat_ban
        self.Nam_XB = Nam_XB
        self.Gia_ban = Gia_ban
    
class Quan_ly():
    def __init__(self):
        self.list = []
    def add(self):
        n = int(input("Nhap so sach muon nhap: "))
        for i in range(1,n+1):
            print(f"Nhap cuon sach so {i}")
            Ten_sach = str(input("Nhap ten sach: ")).replace(' ','_')
            Ten_tac_gia = str(input("Nhap ten tac gia: ")).replace(' ','_')
            Nha_xuat_ban = str(input("Nhap ten nha xuat ban: ")).replace(' ','_')
            Nam_XB = int(input("Nhap nam xuat ban: "))
            Gia_ban = float(input("Nhap gia ban: "))
            self.list.append(Sach(Ten_sach, Ten_tac_gia, Nha_xuat_ban, Nam_XB, Gia_ban)) 
        with open(os.path.join(__location__,'FU.txt'),'w+') as file:
            file.write("======================\n")
            file.write(str(len(self.list)))
            
            for sach in self.list:
                file.write(f"\nTen sach: {sach.Ten_sach}\nTen tac gia: {sach.Ten_tac_gia}\nNha xuat ban: {sach.Nha_xuat_ban}\nNam xuat ban: {sach.Nam_XB}\nGia ban: {sach.Gia_ban}\n\n")
            file.write("======================")

                
            

    def hien_thi(self):
        with open(os.path.join(__location__, 'FU.txt'), 'r') as file:
            file.readline() 
            print(f"{'TEN SACH'.ljust(30)} {'TEN TAC GIA'.center(30)} {'NAM XB'.rjust(10)} {'GIA BAN'.rjust(10)}")
            for sach in self.list:
                print(f"{str(sach.Ten_sach).ljust(30)} {str(sach.Ten_tac_gia).center(30)} {str(sach.Nam_XB).rjust(10)} {str(sach.Gia_ban).rjust(10)}")
    
    
            
    def sap_xep_2(self):
        with open(os.path.join(__location__, 'FU.txt'), 'r') as file:
            file.readline() 
            with open(os.path.join(__location__,'FU2024.txt'),'w') as file:

                file.write(f"{'TEN SACH'.ljust(30)} {'TEN TAC GIA'.center(30)} {'NAM XB'.rjust(10)} {'GIA BAN'.rjust(10)}")
                for sach in self.list.sort(key= lambda x : x.Nam_XB ,reverse=True):
                    file.write(f"\n({str(sach.Ten_sach).ljust(30)} {str(sach.Ten_tac_gia).center(30)} {str(sach.Nam_XB).rjust(10)} {str(sach.Gia_ban).rjust(10)})\n")
    def tim_kiem(self):
        name = input('NHAP TEN CUON SACH MUON TIM')
        for sach in self.list:
            if sach.Ten_sach == name:
                print(f"{sach.Ten_Tac_gia}\n{sach.Nha_xuat_ban}")
            else:
                print("Khong tim thay ten cuon sach tren!")
    def tim_kiem_2(self):
        tg = input('NHAP TEN TAC GIA MUON TIM: ')
        for sach in self.list:
            if sach.Ten_tac_gia == tg:
                print(f"{sach.Ten_sach}\n{sach.Nha_xuat_ban}")
            else:
                print('Khong tim thay tac gia tren!')
def main():
    print("============================")
    print("1.NHAP THONG TIN CUA N CUON SACH CUA FU")
    print("2.IN RA MAN HINH THONG TIN VUA NHAP")
    print("3.SAP XEP THONG TIN GIAM DAN THEO NAM XUAT BAN VA HIEN THI")
    print("4.TIM KIEM THEO TEN SACH")
    print("5.TIM KIEM THEO TAC GIA")
    print("6.KET THUC")
    print("============================")

main()
key = Quan_ly()
opt = int(input("LUA CHON YEU CAU: "))
while opt != 6:
    if opt == 1:
        key.add()
    elif opt == 2:
        key.hien_thi()
    elif opt == 3:
        key.sap_xep_2()
    elif opt == 4:
        key.tim_kiem()
    elif opt == 5:
        key.tim_kiem_2()
    else:
        print("VUI LONG LUA CHON LAI.")
    print()
    main()
    opt = int(input("LUA CHON YEU CAU: "))
print("DA THOAT.")
    
