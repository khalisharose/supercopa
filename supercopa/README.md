Soal Tugas 2
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
    28. Terakhir push ke repositori GitHub dan PWS (pake git add, commit, push origin master, sama push pws master)


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
     <img width="1682" height="1097" alt="Screenshot 2025-09-10 101411" src="https://github.com/user-attachments/assets/749358ad-33f4-40cb-98ef-27ff7f33c6db" />

3. Jelaskan peran settings.py dalam proyek Django
    settings.py merupakan file konfigurasi utama Django yang mengatur path proyek, keamanan (seperti SECRET_KEY dan DEBUG), aplikasi (INSTALLED_APPS), middleware, database (SQLite untuk development, PostgreSQL untuk production), template, validasi, internasionalisasi, dan file statis (STATIC_URL).

4. Bagaimana cara kerja migrasi database di Django?
    Kan migrasi model tujuannya buat ngelacak perubahan di model basis data kita, nah migrasi ini adalah instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefine di dalam kode terbaru kita. Caranya Django membuat file migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. Kemudian, migrate mengaplikasikan perubahan model yang udah ada di dalam berkas migrasi ke basis data dengan jalanain perintah sebelumnya.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 
     Menurut saya Django cocok untuk pemula karena dia open source jadi mudah dicari dan souce code atau dokumentasinya mudah di dapat, cepat karena fiturnya efisien jadi di Django pemula langsung bisa lihat hasilnya tanpa harus banyak konfigurasi manual, lengkap yang dimana fitur" nya lengkap dan  ga bener" dari nol jadi cocok buat pemula, dan fleksibel karena di dukung MVT dan Python jadi bisa eksplore banyak jenis aplikasi dari yang sederhana sampe kompleks.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Engga adaa, ka fahri baik banget dan helpfull sekali, rating bintang 5 


Soal Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery sendiri kan pada dasarnya adalah proses pertukaran data dan pengiriman informasi antar komponen di dalam platform, jadi kenapa data delivery diperlukan dalam pengimplementasian sebuah platform adalah karena;
    1. Menjadi jembatan komunikasi antar sistem
        Platform di zaman sekarang kan semuanya udah modern, nah platform ini biasanya terdiri dari berbagai komponen contohnya ada frontend, backend, database, dan API. Komponen-komponen tersebut perlu bertukar data supaya bisa berfungsi dengan baik. Data juga perlu dikiriim bolak-balik dari client dan server sehingga data delivery memiliki peran yang penting.
    2. Skalabilitas dan efisiensi
        Karena menggunakan mekanisme seperti API atau HTTP, data delivery bantu mastiin supaya datanya dikirim dengan cepat, jadi bisa mendukung performa dari platform tsb.
    3. Memudahkan dalam berintegrasi dengan sistem eksternal 
        Sering kita temuin kalo platform terhubung sama layanan pihak ketiga, nah tanpa data delivery platform gabisa berfungsi secara aktif dan memberikan pengalaman kepada pengguna secara optimal.
    4. Fungsionalitas aplikasi
        Data delivery itu membuat aplikasi bisa mengambil, memproses, dan juga menampilkan informasi kepada penggunanya

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut aku JSON lebih baik. Dilihat dari segi sintaks nya yang lebih ringkas dan mudah dibaca, ukuran data nya juga lebih kecil, dan juga udah support Native JavaScript jadi bisa di parse tanpa library tambahan. Kalo kenapa JSON lebih populer dari XML salah satunya karena lebih cepat dan juga efisien daripada XML.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid di form Django dipakai untuk memvalidasi data yang dikirimin sama form dan mastiin kalau data itu udah sesuai aturan validasi yang udh di define di kelas form nya, intinya buat masttin akklau data yang masuk itu sesuai format. method ini juga bisa mencegah pemrosesan data yang berbahaya kalo inputnya bahaya, bisa juga buat ngasih kita error massage yang jelas jadi lebih mudah tau salah nya kita dimana.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Kita butuh csrf_token saat membuat form di Django supaya terhindar dari serangan CSRF. Jadi token ini bakal berbentuk string unik yang dihasilin sama si server terus di letakkan di dalam form HTMLnya jadi pas formnya dikirim servernya bakal memverifikasi tokennya, sama atau engga sama yang udh di hasilin tadi, intinya mastiin kalau requestnya dari sumber yang benar.

    Kalau kita tidak menambahkan csrf_token si Django nya bakal nolak request POST dari form tsb. Dia bakal ngembaliin error 403 atau Forbidden, karena udah defaultnya kalo si Django butuh CSSRF ttoken buat semua request (POST, PUT, maupun DELETE). Terus kalo gapake si csrf token aplikasinya jadi rentan terkena serangan csrf. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Pertama aku buat folder baru yang namanya template di root folder aku yang supercopa, terus buat file baru namanya base.html yang berisi code yang nantinya buat jadi template dasar atau skeleton buat halaman web lainnya. 
    2. Tambahin [BASE_DIR / 'template'] di settings.py bagian Templates, ini supaya si base.html tadi ter-detect sebagai file template
    3. Ubah isi main.html yang udah ada di tutoriala sebelumnya dengan code yang baru. Di code baru ini kita gunain si base.html sebagai template utama
    4. Buat formm input data yang dinamain forms.py di dalam folder main, forms.py ini yang nantinya bakal nerima data product baru
    5. Memperbaharui views.py. Disini aku ada nambahin dan ngerubah fungsi yang ada. Contohnya aku nambahin create_product buat nambahin data product otomatis kalau datanya udh di dubmit di form
    6. Terus aku import fungsi" yang udh aku buat tadi ke urls.py dan nambahin pathnya ke urlpatterns nya.
    7. Lalu balik ke main.html lagi buat nge-update code yang ada di blok content buat nampilin data product sama tombol Add product 
    8. Lalu buat file baru yang namanya create_product.html sama product_detail.html.  Isi create_product tadi itu buat ngebuat csrf token yang berfusngsi sebagai pelindung dari serangan yang berbahaya. Di dalem create_product juga ada template tag.
    9. Aku nambahin entri url aku di CSRF_TRUSTED_ORIGINS di settings.py, kalo udah aku coba runserver dan buka localhost udah muncul atau belum, mastiin aja
    10. import HttpResponse dan Serializer di views.py
    11. Buat fungsi show_xml di views.py, terus import fungsi itu ke urls.py dan tambahin path url nya di urlpatterns. kalo udah cek lagi dengan jalanin runserver lagi terus buka localhost yg xml
    12. Buat fungsi juga buat yang json terus aku ngelakuin hal yang sama kayak yang di no.11
    13. Buat fungsi show xml dan show json versi yang by id, tambahin try except juga, import fungsi nya di urls.py, terus tambahin path nya juga di urlpatterns, kalo udah run server lg buat cek dan buka localhost nya, yang kali ini masukin si product id nya
    14. Lalu buat request baru di postman pake GET terus masukin semua link localhost yang udh dibuka tadi, terus ss
    15.  Terakhir push ke repositori GitHub dan PWS (pake git add, commit, push origin master, sama push pws master)
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Tidak ada, asdos saya baik dan informatif sekali
<<<<<<< HEAD
   <img width="2508" height="1591" alt="Screenshot 2025-09-13 232410" src="https://github.com/user-attachments/assets/a68c3463-cca6-4e58-94b1-bb1ca5f019d7" />
   <img width="2562" height="1599" alt="Screenshot 2025-09-13 232432" src="https://github.com/user-attachments/assets/348c8f3d-fd5b-4348-b75e-d954de4b7c82" />
<img width="2553" height="1590" alt="Screenshot 2025-09-13 232523" src="https://github.com/user-attachments/assets/24efe8c9-2878-4cba-bba9-3053dc3a4a72" />
<img width="2544" height="1592" alt="Screenshot 2025-09-13 232543" src="https://github.com/user-attachments/assets/b274b7ea-c989-4f0a-bd69-1ed864973ccd" />

   
=======

Soal Tugas 4
 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    AuthenticationForm adalah form bawaan dari django yang dipakai untuk proses login. Dia tugasnya untuk memvalidasi username dan password terhadap sistem autentikasi django. Form ini merupakan bagian dari django.contrib.auth.forms dan dirancang khusus untuk memvalidasi kredensial pengguna (username/email dan password).

    Kelebihan : 
    1. Cepat dipakai karena udah tersedia (plug dan play)
    2. Terintegrasi langsung dengan sistem auth Django
    3. Otomatis memvalidasi kredensial dengan database
    3. Dia udah ngikutin praktik standar keamanan django (hashing, valiidasi)
    4. Bisa di perluas atau di custom sesuai kebutuhan kita

    Kekurangan :
    1. Dia terbatas pada autentikasi username/password standar
    2. Tampilan default nya sederhana jadi perlu customization tambahan untuk UI yang menarik
    3. Dia ga punya fitur seperti "remember me" atau "forgot password" secara default
    4. Dia bergantung pada model User Django

 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Autentikasi adalah proses memverifikasi identitas pengguna jadi dia pada dasarnya ngeejawab pertanyaan "Siapa kamu?". Dia ngelakuin pengecekan kredensial kayak username, password, atau token buat mastiin pengguna nya benar-benar orang yang mereka klaim. Sedangkan, otorisasi adalah proses buat nentuin apa yang boleh dilakuin oleh pengguna yang udah terautentikasi kayak buat menjawab pertanyaan "Apa yang boleh kamu lakukan?". Ini melibatkan pengecekan permission, role, atau hak akses terhadap resource tertentu.
    
    nah django mengimplementasikan autentikasi melalui sistem user model, session management, dan berbagai authentication backend. Sistem ini buat menangani login, logout, dan jadi tempat penyimpanan informasi user yang sudah login dalam session. Buat otorisasi, django memakai sistem permission dan group yang fleksibel. Setiap model secara otomatis mendapat permission add, change, delete, dan view. Django juga menyediakan decorator dan mixin untuk melindungi view berdasarkan login status atau permission tertentu.

 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Session
    Kelebihan:
    1. Data yang ada disimpannya di server jadi lebih aman dari manipulasi client
    2. Dia bisa menyimpan data dalam jumlah besar tanpa batasan seperti cookies
    3. Dia mendukung tipe data kompleks ga hanya string
    4. Dia juga otomatis dibersihkan saat expired jadi bisa mengurangi risiko keamanan

    Kekurangan:
    1. Dia pake resource server (memory/database) yang bisa jadi bottleneck
    2. Susah buat di-scale pada arsitektur multi-server tanpa shared storage
    3. masih bergantung pada cookies buat menyimpan session ID
    4. sedikit lebih lambat karena dia perlu akses ke storage backend

    Cookies
    Kelebihan:
    1. Karena di simpen di client dia jadi ga membebani server 
    2. Akses nya sangat cepat karena langsung tersedia di browser
    3. Dapat bertahan lama meski browser ditutup (persistent cookies)
    4. Cocok buat aplikasi stateless dan microservices architecture

    Kekurangan:
    1. Ukuran terbatas (4KB per cookie)
    2. Rentan terhadap manipulasi dan pencurian di client-side
    3. Menimbulkan privacy concerns karena bisa digunain buat tracking
    4. Dapat dinonaktifkan oleh pengguna jadi bisa mengganggu fungsionalitas aplikasi

 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Cookies ga aman secara default karena beberapa faktor:

    1. Cookies dikirim dalam plain text kecuali pake HTTPS
    2. Bisa dimodifikasi sama pengguna atau malware di sisi client
    3. Rentan terhadap session hijacking kalau dicuri
    4. Dapat dieksploitasi lewat Cross-Site Scripting (XSS) attacks
    5. Berisiko terhadap Cross-Site Request Forgery (CSRF) attacks

    Cara Django Menangani:
    Django nyediain berbagai konfigurasi keamanan buat cookies kayak setting SECURE flag yang mastiin cookies cuma dikirim melalui HTTPS, HTTPONLY flag yang mencegah akses melalui JavaScript, dan SAMESITE attribute buat ngelindungin diri dari CSRF attacks. Django juga mengenkripsi dan menandatangani cookies buat mencegah tampering, serta nyediain built-in CSRF protection middleware.

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Aktifin env dulu kaya biasa, tambahin import UserCreationForm dan import messages di views.py
    2. Tambahin fungsi Registrasi ke viws juga tujuannya buat ngehasilin form regisstrasi secara otomatis dan ngehasilin akun pengguna ketika datanya di submit di form
    3. Buat html baru yang namanya register.html 
    4. Import fungsi register yang tadi dan tambahin path url ke urlpattern
    5. Tambahin import" lain yang dibutuhin buat fungsi login di views kayak import authenticate, login, dan authenticatationForm, tambahin juga fungsi login user 
    6. Buat html baru yang namanya login.html 
    7. Import fungsi tsb di urls.py dan tambahin path url nya ke urlpattern
    8. Tambahin import logout di views, trs sama fungsi logout_user disitu, buat button logout juga di main.html
    9. Import logout_user yang tadi ke urls.py trs juga tambahin path url nya ke urlpattern 
    10. Tambahin import login_required di views terus tambahin potongan code @login_required buat implementasiin decorator yang baru di import
    11. Tambahin import HttpResponseRedirect, reverse, dan datetime, terus ubah code bagian login_user buat nyimpen cookie baru yang namanya last_login yang isinya timestamp terakhir kali pengguna ngelakuin login. Di show main tambahin code ke dalem variabel context, sama ubah fungsi logout-user buat ngehapus cookie last_login setelah logout
    12. Buat ngegabungin model product sama usernya pertama import user di models.py sama tambahin code user di class product nya
    13. terus di makemigration dan migrate, abis itu buah fungsi create_product dan modifikasi show main
    14. Tambahin tombol filter My dan All di main.html dan tambahin nama author di product detail
    15. di run server trs buka di local host (coba) kalau udh bisa terakhir push ke repositori GitHub dan PWS (pake git add, commit, push origin master, sama push pws master)
    
>>>>>>> 3cd3225 (Tugas 4)
