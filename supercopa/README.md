Soal
    1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

        1. Membuat direktori baru sesuai nama toko saya nantinya "supercopa"
        2. Mengaktifkan virtual environment dengan python -m venv env dan env\Scripts\activate
        3. Lalu buat requirements.txt dan menginstall semua dependencies yang ada didalamnya dengan menjalankan pip install -r requirements.txt
        4. Lalu buat proyek Django baru sesuai nama toko saya tadi yaitu "supercopa"
        5. Konfigurasi environment variables dan projectnya, di .env sama .env.prod buat konfigurasi productionnya
        6. Tambahin import os dan from dotenv import load_dotenv di settings.py buat nge-load environment variables dari file .env yang tadi 
        7. Adjust allowed host di settings.py buat development 
        8. Tambahin konfigurasi PRODUCTION di file settings.py
        9. Lengkapi code DATABASES di settings.py, buat productionnya pake PostgreSQL, kalo developmentnya pake SQlite
        10. Jalanin migrasi database nya
        11. Jalanin server Django nya, teruus check di browser web udah berhasil atau belum (pake yang http://localhost:8000)
        12. Berhentiin dulu servernya, terus non-aktifin virtual environment nya
        13. Terus post ke repo yang di Github, pake git init dulu, terus tambahin file .gitiggnore nya, terus connect in si repositori lokalnya sama yang di Github, buatt branch utama (saya namain master), terus add, commit, dan terakhir push
        14. Buat new project di pws (saya namain supercopa juga), terus simpan si Project Credentials dan Project Command nya, terus dibagian environs nya didalam raw editornya paste yang ada di file .env.prod
        15. Tambahin URL Deployment PWS yang udah ada ke allowed host yang ada di settings.py tadi
        16. Isi Git credential Manager pake Project credentials yang tadi udh di dapat
        17. Hapus file sensitif dulu kayak .env, .env.prod, db.sqlite3, atau folder env/ kalo ga sengaja ke upload di git, terus kl udh push lagi ke pws sm git nya
        18. Nyalain env lagi
        19. Buat aplikasi baru yang dinamain 'main' di dalam si "supercopa" (pakai ini python manage.py startapp main)
        20. Tambahin 'main' ke settings.py yang di bagian installed apps, hal itu buat daftarin si 'main' ke proyek supercopa nya
        21. Buat file main.html di dalem folder templates, terus isi nama, npm, kelas. Kalo udah coba buka file main.html nya di browser udah muncul atau belum
        22. Di dalem file models.py buat model yang namanya Products terus tambahin atribut wajib, buat atribut tambahannya saya menambahkan jumlah stok, size, official merch, dan is signed. Sama buat property yang isi nya fungsi buat cek stok udah mau habis atau belum dan fungsi nambahin stok dan simpan perubahannya ke database
        23. Buat migrasi model dan implementasiin ke basis data lokalnya
        24. Import fungsi render nya dari modul djangonya (di views.py) dan massukin fungsi show_main nya
        25. Ubah template yang tadi di main.html
        26. Buat berkas urls.py didalam folder main, isi sama konfigurasi routing buat aplikasi main nya.
        27. Import fungsi include dari Django di urls.py yang di "supercopa" bukan yang tadi di main, tambahin path juga di urlpatterns
        28. Terakhir push ke repositori GitHub dan PWS (pake git add, commit, push origin master, sama push pws master


    2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    <img width="1682" height="1097" alt="Screenshot 2025-09-10 101411" src="https://github.com/user-attachments/assets/749358ad-33f4-40cb-98ef-27ff7f33c6db" />
    
    

    3. Jelaskan peran settings.py dalam proyek Django

        settings.py merupakan file konfigurasi utama Django yang mengatur path proyek, keamanan (seperti SECRET_KEY dan DEBUG), aplikasi 
(INSTALLED_APPS), middleware, database (SQLite untuk development, PostgreSQL untuk production), template, validasi, internasionalisasi, dan file statis (STATIC_URL).


    4. Bagaimana cara kerja migrasi database di Django?

        Kan migrasi model tujuannya buat ngelacak perubahan di model basis data kita, nah migrasi ini adalah instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefine di dalam kode terbaru kita. Caranya Django membuat file migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. Kemudian, migrate mengaplikasikan perubahan model yang udah ada di dalam berkas migrasi ke basis data dengan jalanain perintah sebelumnya.

    5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 

        Menurut saya Django cocok untuk pemula karena dia open source jadi mudah dicari dan souce code atau dokumentasinya mudah di dapat, cepat karena fiturnya efisien jadi di Django pemula langsung bisa lihat hasilnya tanpa harus banyak konfigurasi manual, lengkap yang dimana fitur" nya lengkap dan  ga bener" dari nol jadi cocok buat pemula, dan fleksibel karena di dukung MVT dan Python jadi bisa eksplore banyak jenis aplikasi dari yang sederhana sampe kompleks.

    6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

        Engga adaa, ka fahri baik banget dan helpfull sekali, rating bintang 5 
