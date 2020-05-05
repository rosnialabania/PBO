#Fungsi str() berfungsi untuk mengubah objek menjadi string

str(object = '')
str(object = b'', encoding='utf-8', errors = 'strict')

#Fungsi str() memiliki beberapa parameter, yaitu

#encoding – encoding, defaultnya utf-8
#errors – respon error saat terjadi kesalahan decoding, defaultnya strict


#Fungsi repr() berfungsi untuk mengembalikan representasi dari suatu objek

repr(object)
#tambahan seringkali termasuk nama dan alamat objek.Kelas dapat mengontrol apa fungsi ini yang dikembalikan untuk instance-nya dengan 
#mendefinisikan metode __repr__().
