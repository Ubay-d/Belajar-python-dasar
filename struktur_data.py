print('========= Struktur Data =========')
print()
print('# List: Dibahasa pemrograman lain mirip dengan array')
my_list = [1, 1, 50, 'Saya Imbar', 5.3, False]
print('my_list:', my_list)
print('my_list[0]:', my_list[0])
print('my_list[3]:', my_list[3])
print('my_list[-1]:', my_list[-1])
print('my_list[-3]:', my_list[-3])
print('len(my_list):', len(my_list))
my_list.append('Odoo')
print('my_list:', my_list)
pop_res = my_list.pop(1)
print('pop_res:', pop_res)
print('my_list:', my_list)
print()

print('# Tuple: Mirip dengan list tetapi bukan diperuntukan untuk banyak dimodifikasi.')
# my_tuple = 1, 50, 'Saya Imbar', 5.3, False
my_tuple = (1, 1, 50, 'Saya Imbar', 5.3, False)
print('my_tuple', my_tuple)
print('my_tuple[2]', my_tuple[2])
print('len(my_tuple):', len(my_tuple))
print('my_tuple.index(50):', my_tuple.index(50))
print()

print('# Dictionary: Mirip JSON/Objek di javascript')
my_dict = {
'nama': 'Imbar Budiman',
'berat_badan': 63,
'tinggi_badan': 171,
}
print('my_dict', my_dict)
my_dict['alamat'] = 'Cikarang, Bekasi'
my_dict.update({
'keahlian': 'Programming',
'hobi': 'Ngoding',
})
print('my_dict', my_dict)
print("my_dict['nama']", my_dict['nama'])
berat_badan = my_dict['berat_badan']
print('berat_badan', berat_badan)
alamat = my_dict.get('alamat', 'Tidak ada alamat')
print('alamat:', alamat)
print('my_dict:', my_dict)
del my_dict['alamat']
print('my_dict:', my_dict)
print()

print('# Set: Mirip seperti tuple tapi tidak bisa ada duplikasi item/value/nilai')
print('# Set biasanya dipakai untuk filter/cleansing data yang duplikat, karena Set hanya akan menampung data yang unik')
my_set = {1, 11, 11, 4, 'Imbar', 5, 'Imbar'}
print('my_set', my_set)
my_set.add('Budiman')
my_set.add(4) # Ini tidak berpengaruh apa-apa karena 4 sudah ada.
print('my_set', my_set)