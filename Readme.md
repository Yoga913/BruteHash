# Hash Brute
BruteHash adalah sebuah alat yang digunakan untuk mencoba memecahkan berbagai jenis hash menggunakan teknik brute force dari wordlist. Alat ini mendukung berbagai algoritma hash seperti MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3-224, SHA3-256, SHA3-384, dan SHA3-512.


## Fitur

- Mendukung berbagai algoritma hash.
- Menampilkan daftar hash yang didukung.
- Menggunakan wordlist untuk mencoba memecahkan hash.
- Menyimpan hasil ke file output atau mencetak ke standar output.
- Menangani kesalahan dalam membuka file dan interupsi keyboard (CTRL+C).


## Cara Menggunakan

1. **Clone repo ini**:

```bash
    git clone https://github.com/Yoga913/BruteHash.git
    cd BruteHash
```

2. **Menampilkan daftar hash yang didukung**:

    ```bash
    python brutehash.py --hashes
    ```

3. **Menggunakan wordlist untuk mencoba memecahkan hash**:

### Lainnya:
 ______________________________________________________
| PERINTAH      | DESKRIPSI                            |
| ------------- | -------------------------------------|
|-w / --wordlist| Worldlist untuk serangan brute force |
| -o / --output | Berkas keluaran (opsional)           |
| --hashes      | Daftar hash yang didukung            |
| -h / --help   | Minta bantuan                        |
--------------------------------------------------------
## Penggunaan Mengarah hasil ke file output:

**Hash Md5:**
```bash
    python hashcrack.py --md5 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```
**Hash SHA-1:**
```bash
    python hashcrack.py --sha1 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```

**Hash SHA224:**

```bash
    python hashcrack.py --sha224 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```

**Hash SHA256:**
```bash
    python hashcrack.py --sha256 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```
**Hash SHA384:**
```bash
    python hashcrack.py --sha384 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```
**Hash SHA512:**
```bash
    python hashcrack.py --sha512 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```

**Hash SHA3-224:**
```bash
    python hashcrack.py --sha3_224 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```
**Hash SHA3-256:**
```bash
    python hashcrack.py --sha3_256 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```
**Hash SHA-384:**
```Bash
    python hashcrack.py --sha3_384 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```
**Hash SHA-512:**
```Bash
    python hashcrack.py --sha3_512 <hash> --wordlist <path_to_wordlist> --output <path_to_output_file>
```

## Contoh Penggunaan

```bash
python hashcrack.py --md5 d41d8cd98f00b204e9800998ecf8427e --wordlist wordlist.txt

python hashcrack.py --sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 --wordlist wordlist.txt --output result.txt
```

## Saran

**Beberapa sumber wordlist yang bisa Anda pertimbangkan:**

1. **SecLists**: Ini adalah koleksi wordlist yang sangat besar dan beragam untuk berbagai keperluan. Anda bisa menemukannya di [GitHub SecLists](https://github.com/danielmiessler/SecLists). Cari folder "Passwords" untuk wordlist yang khusus untuk brute force.

2. **RockYou**: Ini adalah salah satu wordlist paling terkenal dan sering digunakan dalam pemecahan hash. Wordlist ini bisa ditemukan di berbagai tempat, termasuk [RockYou Wordlist](https://github.com/praetorian-inc/Hob0Rules/blob/master/rockyou.txt).

3. **Crunch**: Jika Anda ingin membuat wordlist sendiri, Crunch adalah alat yang memungkinkan Anda untuk menghasilkan wordlist berdasarkan pola tertentu. Anda bisa mengunduhnya di [Crunch GitHub](https://github.com/crunch-sec/crunch).

4. **Weakpass**: Situs ini menyediakan berbagai wordlist yang bisa diunduh untuk berbagai kebutuhan. Anda bisa mengunjungi [Weakpass](https://weakpass.com/).

5. **GitHub - Password Lists**: Ada banyak repositori di GitHub yang menawarkan wordlist untuk keperluan cracking hash. Misalnya, [Password Lists](https://github.com/berzerk0/Probable-Wordlists) adalah repositori yang sangat besar dengan berbagai wordlist.

Anda bisa memilih wordlist yang sesuai dengan kebutuhan Anda, atau menggunakan beberapa wordlist untuk meningkatkan peluang dalam pemecahan hash.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.

## Kontribusi

Kontribusi sangat diharapkan! Jika kamu memiliki ide atau menemukan bug, jangan ragu untuk membuka isu atau mengirimkan pull request.
---
