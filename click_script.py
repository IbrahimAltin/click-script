import win32api, win32con
import keyboard
import time
import threading

tiklama_sayac = 0
autoClickCloser = False
delayClickCloser = False
click_thread = None

def clickEvent():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    time.sleep(0.1)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    print("Click eventi çalıştı.")


def autoClicker_loop():
    global tiklama_sayac
    start_time = time.time() # zaman sayacı başlangıç

    while(autoClickCloser):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

        time.sleep(0.001)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        tiklama_sayac += 1 

    print("Otomatik Tıklama Döngüsü Durduruldu.")

    end_time = time.time() # zaman sayacı bitiş
    total_time = end_time - start_time # zaman sayacı total

    total_cps = tiklama_sayac / total_time

    print(f"[SAYI] Toplam Tıklama Sayısı: {tiklama_sayac}")

    print(f"[SÜRE] Toplam Çalışma Süresi: {total_time:.2f} saniye")

    print(f"[CPS] Toplam Tıklama / Çalışma Süre : {total_cps:.2f}")

    tiklama_sayac = 0


def delayClicker_loop():
    global tiklama_sayac
    start_time = time.time() # zaman sayacı başlangıç

    while(delayClickCloser):
        time.sleep(10)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

        time.sleep(0.0001)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        tiklama_sayac += 1 

        end_time = time.time() # zaman sayacı bitiş
        total_time = end_time - start_time # zaman sayacı total

        print(f"{tiklama_sayac}. tıklama yapıldı\t\t{total_time:.2f} saniye")

    print("Otomatik Tıklama Döngüsü Durduruldu.")

    print(f"[SÜRE] Toplam Çalışma Süresi: {total_time:.2f} saniye")

    print(f"[SAYI] Toplam Tıklama Sayısı: {tiklama_sayac}")

    tiklama_sayac = 0


def autoClickStatus():
    global autoClickCloser, click_thread

    autoClickCloser = not autoClickCloser   # autoClickCloser'ı tersine çevir

    if autoClickCloser == True:
        print("Otomatik Tıklayıcı BAŞLATILDI.")
        # Yeni bir thread oluştur ve başlat
        click_thread = threading.Thread(target=autoClicker_loop)
        click_thread.start()
    else:
        print("Otomatik Tıklayıcı DURDURULDU.")


def delayClickStatus():
    global delayClickCloser, click_thread

    delayClickCloser = not delayClickCloser   # delayClicker_loop'ı tersine çevir

    if delayClickCloser == True:
        print("Otomatik Tıklayıcı BAŞLATILDI.")
        # Yeni bir thread oluştur ve başlat
        click_thread = threading.Thread(target=delayClicker_loop)
        click_thread.start()
    else:
        print("Otomatik Tıklayıcı DURDURULDU.")
        


# --- Program Başlangıcı ---
print('█' * 60)
print('█' *20 + " PROGRAM BAŞLATILDI " + '█' *20)
print('█' * 60)
print('█' *12 + "Clicker  :        'w' tuşu ile tıkla" + '█' *12)
print('█' *8 + "autoClicker  :    'x' tuşu ile Başlat/Durdur" + '█' *8)
print('█' *8 + "delayClicker :    'f' tuşu ile Başlat/Durdur" + '█' *8)
print('█' * 60)
print('█' *12 + "Çıkış yapmak için 'esc' tuşuna basın" + '█' *12)
print('█' * 60)


keyboard.on_press_key('w', lambda e: clickEvent()) # click eventini başlatmak için 'w' tuşuna basın

keyboard.on_press_key('x', lambda e: autoClickStatus()) # autoClicker eventini başlatmak için 'x' tuşuna basın

keyboard.on_press_key('f', lambda e: delayClickStatus()) # delayClicker eventini başlatmak için 'f' tuşuna basın

keyboard.wait('esc') # Programı kapatmak için 'q' basın    
 
print("Program sonlandırıldı.")
