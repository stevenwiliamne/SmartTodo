# SmartTodo - Program To-Do List Sederhana

tasks = []

while True:
    print("\n1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tugas = input("Masukkan tugas: ")
        tasks.append(tugas)
        print("Tugas berhasil ditambahkan!")
    elif pilihan == "2":
        print("\nDaftar Tugas:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan SmartTodo!")
        break
    else:
        print("Pilihan tidak valid.")

