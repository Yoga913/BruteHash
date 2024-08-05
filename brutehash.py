from banner.banner import *
import argparse
import hashlib
from beautifultable import BeautifulTable
import time

parse = argparse.ArgumentParser()
########## Daftar hash yang didukung
parse.add_argument("--hashes",help="Daftar hash yang didukung",action='store_true')
########## hash --> MD5
parse.add_argument("--md5",help="Hash MD5")
########## hash --> SHA-1
parse.add_argument("--sha1",help="Hash SHA-1")
########## hash --> SHA-224
parse.add_argument("--sha224",help="Hash SHA-224")
########## hash --> SHA-256
parse.add_argument("--sha256",help="Hash SHA-256")
########## hash --> SHA-384
parse.add_argument("--sha384",help="Hash SHA-384")
########## hash --> SHA-512
parse.add_argument("--sha512",help="Hash SHA-512")
########## hash --> SHA3-224
parse.add_argument("--sha3_224","--sha3-224",help="Hash SHA3-224")
########## hash --> SHA3-256
parse.add_argument("--sha3_256","--sha3-256",help="Hash SHA3-256")
########## hash --> SHA3-384
parse.add_argument("--sha3_384","--sha3-384",help="Hash SHA3-384")
########## hash --> SHA3-512
parse.add_argument("--sha3_512","--sha3-512",help="Hash SHA3-512")
########## Wordlist
parse.add_argument("-w","--wordlist",help="Wordlist")
########## Output
parse.add_argument("-o", "--output",default="stdout",required=False, dest='output', help="Mengarahkan output ke nama pilihan Anda")
parse = parse.parse_args()

def hashesSupported():
	"""Fungsi untuk menampilkan daftar hash yang didukung."""
	table = BeautifulTable()
	table.columns.header = [f"{RED_NORMAL}HASH{END}", f"{GREEN_NORMAL}COMMAND{END}"]
	table.rows.append(["MD5", "--md5"])
	table.rows.append(["SHA-1", "--sha1"])
	table.rows.append(["SHA-224", "--sha224"])
	table.rows.append(["SHA-256", "--sha256"])
	table.rows.append(["SHA-384", "--sha384"])
	table.rows.append(["SHA-512", "--sha512"])
	table.rows.append(["SHA3-224", "--sha3-224"])
	table.rows.append(["SHA3-256", "--sha3-256"])
	table.rows.append(["SHA3-384", "--sha3-384"])
	table.rows.append(["SHA3-512", "--sha3-512"])
	print(table) # Cetak tabel Ynag di dukung

try:
	pass_file = open(parse.wordlist,"r") # BUka World list yang Diberikan

except:
	pass # Tangkap exception jika file wordlist tidak dapat dibuka

f = open(parse.output, "a", encoding='utf-8') # # Buka file output untuk menulis

def crackMD5():
	"""Fungsi untuk meng-crack hash MD5."""
	for password in pass_file:
		password = password.replace("\n","") # menghapus Newline karakter
		enc = password.encode('utf-8') # encode Pasword Ke utf-8
		hashe = hashlib.md5(enc.strip()).hexdigest() # Hitung hash MD5

		if parse.md5 == hashe: # Jika hash cocok dengan yang di berikan
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["MD5", hashe, password])
			print(table) # Cetak Hasil dalam tebel
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close() #tutup file output
			break # Keluar dari loop

def crackSHA1():
	"""Fungsi untuk meng-crack hash SHA-1."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha1(enc.strip()).hexdigest()

		if parse.sha1 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA-1", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break

# Fungsi-fungsi crackSHA224(), crackSHA256(), crackSHA384(), crackSHA512(), crackSHA3_224(), crackSHA3_256(),
# crackSHA3_384(), dan crackSHA3_512() memiliki struktur dan alur yang sama seperti crackMD5() dan crackSHA1(),
# hanya berbeda pada algoritma hash yang digunakan.

def crackSHA224():
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha224(enc.strip()).hexdigest()

		if parse.sha224 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA-224", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break

def crackSHA256():
	"""Fungsi untuk meng-crack hash SHA256."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha256(enc.strip()).hexdigest()

		if parse.sha256 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA-256", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break

def crackSHA384():
	"""Fungsi untuk meng-crack hash SHA384."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha384(enc.strip()).hexdigest()

		if parse.sha384 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA-384", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break


def crackSHA512():
	"""Fungsi untuk meng-crack hash SHA512."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha512(enc.strip()).hexdigest()

		if parse.sha512 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA-512", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break

def crackSHA3_224():
	"""Fungsi untuk meng-crack hash SHA3_224."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha3_224(enc.strip()).hexdigest()

		if parse.sha3_224 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA3-224", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break

def crackSHA3_256():
	"""Fungsi untuk meng-crack hash SHA3_256."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha3_256(enc.strip()).hexdigest()

		if parse.sha3_256 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA3-256", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break

def crackSHA3_384():
	"""Fungsi untuk meng-crack hash SHA3_384."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha3_384(enc.strip()).hexdigest()

		if parse.sha3_384 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA3-384", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break

def crackSHA3_512():
	"""Fungsi untuk meng-crack hash SHA3_512."""
	for password in pass_file:
		password = password.replace("\n","")
		enc = password.encode('utf-8')
		hashe = hashlib.sha3_512(enc.strip()).hexdigest()

		if parse.sha3_512 == hashe:
			table = BeautifulTable()
			table.columns.header = [f"{WHITE}HASH{END}", f"{RED_NORMAL}TERENSKRIPSI{END}", f"{GREEN_NORMAL}DIDEKRIPSI{END}"]
			table.rows.append(["SHA3-384", hashe, password])
			print(table)
			f.write("HASH: MD5\nTERENSKRIPSI: {}\nDIDEKRIPSI: {}".format(hashe,password)+'\n'+'\n')
			f.close()
			break


def main():
	"""Fungsi utama untuk mengarahkan eksekusi berdasarkan argumen yang diberikan."""
	if parse.hashes:
		hashesSupported() # Jika --hashes ditentukan, tampilkan daftar hash yang didukung

	elif parse.md5:
		crackMD5() # Jika --md5 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha1:
		crackSHA1()  # Jika --SHA1 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha224:
		crackSHA224()  # Jika --SHA224 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha256:
		crackSHA256()  # Jika --SHA256 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha384:
		crackSHA384()  # Jika --sha384 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha512:
		crackSHA512()  # Jika --SHA512 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha3_224:
		crackSHA3_224()  # Jika --SHA3_224 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha3_256:
		crackSHA3_256()  # Jika --SHA3_256 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha3_384:
		crackSHA3_384()  # Jika --SHA3_384 ditentukan, tampilkan daftar hash yang didukung

	elif parse.sha3_512:
		crackSHA3_512()  # Jika --SHA3_512 ditentukan, tampilkan daftar hash yang didukung

	else:
		print(f"{RED_NORMAL}[ERR0R]{END} Argumen Tidak valid\nMeminta help : python3 hashcrack.py --help\nkeluar dari script...")
		time.sleep(2)
		exit(0) # Jika argumen tidak valid, cetak pesan kesalahan dan keluar dari skrip




if __name__ == '__main__':
	try:
		main() # Eksekusi fungsi main() jika skrip dijalankan secara langsung
	except KeyboardInterrupt:
		exit()	# Tangkap KeyboardInterrupt (CTRL+C) untuk keluar dari skrip dengan aman

