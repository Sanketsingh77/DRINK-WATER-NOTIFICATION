import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="PLEASE DRINK WATER NOW!!",
            message=r"The National Academies of Sciences determined that an adequate daily fluid intake is about 15.5 cups 3.7 liters of fluids a day for men and about 11.5 cups 2.7 liters of fluids a day for women",
            # app_icon=r"C:\Users\SANKET\OneDrive\Desktop\jhjgjh\icon.ico",
            timeout=10
        )
        time.sleep(60*1)
