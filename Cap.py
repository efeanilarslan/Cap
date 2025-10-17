import numpy as np
import matplotlib.pyplot as plt
#pip install numpy matplotlib

f = float(input("Sinyalin Frekansi ne olmali (Hz) "))
Genlik_max = float(input("Max genlik ne olmali "))
Faz = float(input("Faz açisi ne olmali (radyan)"))
k = float(input("Kaç periyot görüntü çikarilsin"))
T = 1/f
t = np.linspace(0, k*T, 1000)

v_anlk = Genlik_max * np.sin(2 * np.pi * f * t + Faz)

r=float(input("Direnc değeri(Ohm)"))
c=float(input("Kapasitor değeri(Farat)"))

Xc=1 / (2 * np.pi * f * c)
Z = np.sqrt(r**2 + Xc**2)

Genlik_max_cikis_yüksekgeç = Genlik_max * (r / Z)
Cfaz_yüksekgeç = np.arctan(Xc / r)
Genlik_max_cikis_alçakgeç = Genlik_max * (Xc / Z)
Cfaz_alçakgeç = -np.arctan(r / Xc)

v_cikis_yüksekgeç = Genlik_max_cikis_yüksekgeç * np.sin(2 * np.pi * f * t + Faz + Cfaz_yüksekgeç)
v_cikis_alçakgeç = Genlik_max_cikis_alçakgeç * np.sin(2 * np.pi * f * t + Faz + Cfaz_alçakgeç)

layout ="""
cc
ab
de
"""

fig, axs = plt.subplot_mosaic(layout, figsize=(12, 8))

axs["a"].plot()
axs["a"].set_xticks([])
axs["a"].set_yticks([])
axs["a"].plot()
axs["a"].set_xlim(0,8)
axs["a"].set_ylim(0,8)
axs["a"].plot([3,4],[6,6])
axs["a"].plot([4,4],[5.6,6.4])
axs["a"].plot([4.05,4.05],[5.6,6.4])
axs["a"].plot([4.05,5.5],[6,6])
axs["a"].plot([4.5,4.5],[6,4.5])
axs["a"].plot([4.5,4.6,4.4,4.6,4.4,4.6,4.4,4.5],[4.5,4.4,4.3,4.2,4.1,4,3.9,3.8])
axs["a"].plot([4.5,4.5],[3.8,2.3])
axs["a"].plot([3,5.5],[2.3,2.3])
axs["a"].set_title("Yüksek Geçiren Filitre")
axs["a"].text(3,3.5, "Vin\n" + str(f)+"Hz\n" + "Vmax:" + str(Genlik_max))
axs["a"].text(5.4,5, "Vout")
axs["a"].text(3.8,6.8, str(c)+"Farat")
axs["a"].text(4.65,4, str(r)+"Ohm")

axs["b"].plot()
axs["b"].set_xticks([])
axs["b"].set_yticks([])
axs["b"].set_xlim(0,8)
axs["b"].set_ylim(0,8)
axs["b"].plot([3,4],[6,6])
axs["b"].plot([4,4.03,4.06,4.09,4.12,4.15,4.18,4.21],[6,6.3,5.7,6.3,5.7,6.3,5.7,6])
axs["b"].plot([4.21,5.5],[6,6])
axs["b"].plot([4.5,4.5],[6,4.5])
axs["b"].plot([4.4,4.6],[4.5,4.5])
axs["b"].plot([4.4,4.6],[4.3,4.3])
axs["b"].plot([4.5,4.5],[4.3,2.3])
axs["b"].plot([3,5.5],[2.3,2.3])
axs["b"].set_title("Alçak Geçiren Filitre")
axs["b"].text(3,3.5, "Vin\n" + str(f)+"Hz\n" + "Vmax:" + str(Genlik_max) )
axs["b"].text(5.4,5, "Vout")
axs["b"].text(4.65,4, str(c)+" Farat")
axs["b"].text(3.8,6.8, str(r)+" Ohm")

axs["c"].plot(t, v_anlk)
axs["c"].set_title("Sinüs dalgasi "+ str(f) +"Hz")
axs["c"].set_xlabel("Zaman (saniye)")
axs["c"].set_ylabel("Genlik")
axs["c"].grid(True)

axs["d"].plot(t, v_cikis_yüksekgeç)
axs["d"].set_title("Yüksek Geçiren Çikis")
axs["d"].set_xlabel("Zaman (saniye)")
axs["d"].set_ylabel("Genlik")
axs["d"].plot([0,k*1/f],[Genlik_max_cikis_yüksekgeç,Genlik_max_cikis_yüksekgeç])
axs["d"].grid(True)

axs["e"].plot(t, v_cikis_alçakgeç)
axs["e"].set_title("Alçak Geçiren Çikis")
axs["e"].set_xlabel("Zaman (saniye)")
axs["e"].set_ylabel("Genlik")
axs["e"].plot([0,k*1/f],[Genlik_max_cikis_alçakgeç,Genlik_max_cikis_alçakgeç])
axs["e"].grid(True)

plt.tight_layout()
plt.show()
