from control_room import *


if __name__ == "__main__":
    # Buat partikel
    p1 = particel(2.0, 10.0)  # massa = 2 kg, v = 10 m/s
    print("Energi Kinetik:", {p1.energi_kinetik()})
    print(p1.energi_potensial_benda(5))

    # Ubah dimensi
    p1.work_particel()
    particel.ubah_dimensi(2)
    p1.work_particel()

    # Hitung energi potensial gravitasi antara Bumi dan satelit
    m_bumi = 5.97e24
    m_satelit = 1000
    r = 7000e3
    print(f"Energi Potensial Gravitasi:", {particel.energi_potensial(m_bumi, m_satelit, r)})
