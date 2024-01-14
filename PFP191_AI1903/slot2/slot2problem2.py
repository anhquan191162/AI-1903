def get_score():
    user_data =input("Nhap diem: ")
    try:
        user_num = int(user_data)
        return user_num
    except ValueError:
        print("Khong phai so nguyen.")
        return (get_score())
    
user_score = get_score()
def score_converter(user_score):
    data = user_score

    if data <= 10:
        if data >= 8.5:
            print("Diem chu : A \nDiem thang 4: 4")
        elif data <= 8.4 and data >= 7:
            print("Diem chu : B\nDiem thang 4 : 3")
        elif data <= 6.9 and data >= 5.5:
            print("Diem chu : C\n Diem thang 4 : 2")
        elif data <= 5.4 and data >= 4:
            print("Diem chu: D\n Diem thang 4: 1")
        elif data <= 3.9:
            print("Diem chu: F\n Diem thang 4: 0")
    else: 
        print("Gia tri lon hon 10")
        

score_converter(user_score)