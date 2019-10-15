﻿# latihan
## Tutorial Cara menggunakan giter
## Instalasi Git
- pertama download terlebih dahulu git nya di (git-scm.com)
- sesuaikan komputer anda tapi saya saran kan memakai yg 64bit jika kalian bisa
- selamat kalian sudah selesai mengisntal git .

## Menambahkan Config
- pada saat pertama kali menggunakan git,perlu dilakukan konfigurasi username dan email
- konfigurasi ini bisa dilakukan untuk global repostiry atau individual repository.
- jika kalian tidak konfigurasi terlebih dahulu maka akan terjadi error saat menjalan kan perintah git init commit 
- CONFIG GLOBAL REPO
$ git config --global user.name “nama_user”
$ git config --global user.email “nama_user”

![Gitconfig](https://github.com/dimashst777/latihan1/blob/master/gambar1/Untitled%201.png)  
![repolokal](https://github.com/dimashst777/latihan1/blob/master/gambar1/2.png)

File README.md berhasil dibuat..

## Membuat Repo lokal
- Buka direktory aktif, misal: d:\labs_pemrograman1 (buka menggunakan Windows Explorer) 
- klik kanan pada direktory aktif tersebut, dan pilih menu Git Bash, sehingga muncul git bash command
- Buat direktory project praktikum pertama dengan nama latihan1
- $ mkdir latihan1 $ cd latihan1
- Sehingga terbentuk satu direktori baru dibawahnya, selanjutnya masuk kedalam direktori tersebut dengan perintah cd (change directory)
- direktory aktif menjadi: d:\labs_pemrograman1\latihan1

![mkdir](https://github.com/dimashst777/latihan1/blob/master/gambar1/3.png)

## Membuat repo lokal 1.2
- jalankan perintah git init,untuk membuat repo lokal
- $ git init
- Repository baru berhasil di inisialisasi, dengan terbentuknya satu direktori hidden dengan nama .git 
- Pada direktori tersebut, semua perubahan pada working directory akan disimpan.
![gitinit](https://github.com/dimashst777/latihan1/blob/master/gambar1/Annotation%202019-10-14%20133702.png)


## Menambahkan File baru pada repository
- Untuk membuat file dapat menggunakan text editor, lalu menyimpan filenya pada direktori aktif (repository) 
- disini kita akan coba buat satu file bernama README.md (text file)
- $ echo “#Latihan 1” >> README.md
- File README.md berhasil dibuat. 
- ![echo](https://github.com/dimashst777/latihan1/blob/master/gambar1/5.png)

## Menambahkan File baru pada repository
- Untuk menambahkan file yang baru saja dibuat tersebut gunakan perintah git add.
- File README.md berhasil ditambahkan. 
- $ git add README.md
- ![GitaddReadme](https://github.com/dimashst777/latihan1/blob/master/gambar1/Annotation%202019-10-14%20133227.png)

## Commit (Menyimpan perubahan ke database)
- Untuk menyimpan perubahan yang ada kedalam database repository local, gunakan perintah git commit -m “komentar commit”
- Perubahan berhasil disimpan.
- $ git commit -m “File pertama saya”

-![Gitcommit](https://github.com/dimashst777/latihan1/blob/master/gambar1/Annotation%202019-10-14%20133402.png)

## Membuat repository server
- Server reopsitory yang akan kita gunakan adalah http://github.com 
- Anda harus membuat akun terlebih dahulu. 
- Pada laman github, klik tombol start a project dan Dari menu (icon +) klik New Repository

![Gitmenu](https://github.com/dimashst777/latihan1/blob/master/gambar1/git%20menu.png)

## Menambahkan Remote Repository
- Remote Repository merupakan repository server yang akan digunakan untuk menyimpan setiap perubahan pada local repository, sehingga dapat diakses oleh banyak user. 
- Untuk menambahkan remote repository server, gunakan perintah git remote add origin [url]
- $ git remote add origin https://github.com/.........
-![Gitaddorigin](https://github.com/dimashst777/latihan1/blob/master/gambar1/Annotation%202019-10-15%20074703.png)

## Push (Mengirim perubahan ke server)
- Untuk mengirim perubahan pada local repository ke server gunakan perintah git push.
- Perintah ini akan meminta memasukkan username dan password pada akun github.com
- $ git push -u origin master
- ![gitpushorigin](https://github.com/dimashst777/latihan1/blob/master/gambar1/Annotation%202019-10-14%20133440.png)
## Clone Repository
- Clone repository, pada dasarnya adalah meng-copy repository server dan secara otomatis membuat satu direktory sesuai dengan nama repositorynya (working directory).
- Untuk melakukan cloning, gunakan perintah git clone [url]
- ![clone](https://github.com/dimashst777/latihan1/blob/master/gambar1/Annotation%202019-10-14%20133524.png)
