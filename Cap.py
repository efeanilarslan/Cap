import numpy as np
import matplotlib.pyplot as plt

f = float(input("Sinyalin Frekansi ne olmali (Hz) "))
Genlik_max = float(input("Max genlik ne olmali "))
Faz = float(input("Faz açisi ne olmali (radyan)"))
k = float(input("Kaç periyot görüntü çikarilsin"))
T = 1/f
t = np.linspace(0, k*T, 1000)

v_anlk = Genlik_max * np.sin(2 * np.pi * f * t + Faz)

# │ ┤ ╢ ║ ┐ └ ┴ ├ ─ ┼ ╞ ═ ╬ ╧ ╤ ╨ ┘ ┌ █ 

print("Devre1 Yüksek Geçiren Filtre")
print(" (+) ————C——┐——— (+)  ")
print("            │         ")
print("   Vin      R    Vout ")
print("            │         ")
print("     ———————└——— (-)  ")
print(" ")
print("Devre2 Alçak Geçiren Filtre")
print(" (+) ————R——┐——— (+)  ")
print("            │         ")
print("   Vin      C    Vout ")
print("            │         ")
print("     ———————└——— (-)  ")
x = int(input("Hangi devre kullanilacak?(1,2)"))
r=float(input("Direnc değeri(Ohm)"))
c=float(input("Kapasitor değeri(Farat)"))
Xc=1 / (2 * np.pi * f * c)
Z = np.sqrt(r**2 + Xc**2)

if x == 1:
    Genlik_max_cikis = Genlik_max * (r / Z)
    Cfaz = np.arctan(Xc / r)
elif x == 2:
    Genlik_max_cikis = Genlik_max * (Xc / Z)
    Cfaz = -np.arctan(r / Xc)
else:
    print("Geçersiz seçim!")
    Genlik_max_cikis = 0
    Cfaz = 0

v_cikis = Genlik_max_cikis * np.sin(2 * np.pi * f * t + Faz + Cfaz)

fig, axs = plt.subplots(2, 1, figsize=(15,10))

axs[0].plot(t, v_anlk)
axs[0].set_title("Sinüs dalgasi "+ str(f) +"Hz")
axs[0].set_xlabel("Zaman (saniye)")
axs[0].set_ylabel("Genlik")
axs[0].grid(True)

axs[1].plot(t, v_cikis)
axs[1].set_title("V çikis")
axs[1].set_xlabel("Zaman (saniye)")
axs[1].set_ylabel("Genlik")
axs[1].grid(True)

plt.tight_layout()
plt.show()