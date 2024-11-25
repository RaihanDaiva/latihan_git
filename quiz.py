data_limbah = {
    'lokasi1': {
        'nama_lokasi': 'Area Kota 1',
        'jumlah_limbah': {
            'plastik': 500,
            'organik': 300,
            'logam': 200
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Area Kota 2',
        'jumlah_limbah': {
            'plastik': 700,
            'organik': 400,
            'logam': 250
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Area Kota 3',
        'jumlah_limbah': {
            'plastik': 600,
            'organik': 350,
            'logam': 300
        }
    }
}
# no 1
print(data_limbah)
print()
# no 2
print(data_limbah['lokasi2']['jumlah_limbah'])
print()
# no 3
print(data_limbah['lokasi3']['nama_lokasi'])
print()
# no 4
lok1_organik = data_limbah['lokasi1']['jumlah_limbah']['organik']
lok1_logam = data_limbah['lokasi1']['jumlah_limbah']['logam']
print("lokasi 1")
print(f"organik: {lok1_organik}")
print(f"logam: {lok1_logam}")
lok2_organik = data_limbah['lokasi2']['jumlah_limbah']['organik']
lok2_logam = data_limbah['lokasi2']['jumlah_limbah']['logam']
print("lokasi 2")
print(f"organik: {lok2_organik}")
print(f"logam: {lok2_logam}")
lok3_organik = data_limbah['lokasi3']['jumlah_limbah']['organik']
lok3_logam = data_limbah['lokasi3']['jumlah_limbah']['logam']
print("lokasi 3")
print(f"organik: {lok3_organik}")
print(f"logam: {lok3_logam}")
print()
# no 5

for i in range(3):
    if data_limbah[f'lokasi{i+1}']['jumlah_limbah']['organik'] > 400 or data_limbah[f'lokasi{i+1}']['jumlah_limbah']['logam'] > 250:
        print("lokasi tersebut memerlukan penanganan khusus")
    else:
        print("Lokasi tersebut dalam kondisi aman")
        
input()

