import logging
from modules import Graph

logging.basicConfig(level=logging.INFO)

if __name__ != '__main__':
    raise RuntimeError('Run this with python3 main.py')

krl_graph = Graph()

# Bekasi Line
krl_graph.add_edge('cikarang', 'telaga_murni', 9)
krl_graph.add_edge('telaga_murni', 'cibitung', 9)
krl_graph.add_edge('cibitung', 'tambun', 9)
krl_graph.add_edge('tambun', 'bekasi_timur', 9)
krl_graph.add_edge('bekasi_timur', 'bekasi', 9)
krl_graph.add_edge('bekasi', 'kranji', 9)
krl_graph.add_edge('kranji', 'cakung', 9)
krl_graph.add_edge('cakung', 'klender_baru', 9)
krl_graph.add_edge('klender_baru', 'buaran', 9)
krl_graph.add_edge('buaran', 'klender', 9)
krl_graph.add_edge('klender', 'jatinegara', 9)

# via Pasar Senen
krl_graph.add_edge('jatinegara', 'pondok_jati', 1)
krl_graph.add_edge('pondok_jati', 'kramat', 1)
krl_graph.add_edge('kramat', 'gang_sentiong', 1)
krl_graph.add_edge('gang_sentiong', 'pasar_senen', 1)
krl_graph.add_edge('pasar_senen', 'kemayoran', 1)
krl_graph.add_edge('kemayoran', 'rajawali', 1)
krl_graph.add_edge('rajawali', 'kampung_bandan', 1)

# via Manggarai
krl_graph.add_edge('jatinegara', 'matraman', 2)
krl_graph.add_edge('matraman', 'manggarai', 2)
krl_graph.add_edge('manggarai', 'sudirman', 2)
krl_graph.add_edge('sudirman', 'sudirman_baru', 2)
krl_graph.add_edge('sudirman_baru', 'karet', 2)
krl_graph.add_edge('karet', 'tanah_abang', 2)
krl_graph.add_edge('tanah_abang', 'duri', 2)
krl_graph.add_edge('duri', 'angke', 2)
krl_graph.add_edge('angke', 'kampung_bandan', 2)

# Tangerang Line
krl_graph.add_edge('tangerang', 'tanah_tinggi', 8)
krl_graph.add_edge('tanah_tinggi', 'batu_ceper', 8)
krl_graph.add_edge('batu_ceper', 'poris', 8)
krl_graph.add_edge('poris', 'kalideres', 8)
krl_graph.add_edge('kalideres', 'rawa_buaya', 8)
krl_graph.add_edge('rawa_buaya', 'bojong_indah', 8)
krl_graph.add_edge('bojong_indah', 'taman_kota', 8)
krl_graph.add_edge('taman_kota', 'pesing', 8)
krl_graph.add_edge('pesing', 'grogol', 8)
krl_graph.add_edge('grogol', 'duri', 8)

# Rangkasbitung Line
krl_graph.add_edge('tanah_abang', 'palmerah', 7)
krl_graph.add_edge('palmerah', 'kebayoran', 7)
krl_graph.add_edge('kebayoran', 'pondok_ranji', 7)
krl_graph.add_edge('pondok_ranji', 'jurang_mangu', 7)
krl_graph.add_edge('jurang_mangu', 'sudimara', 7)
krl_graph.add_edge('sudimara', 'rawa_buntu', 7)
krl_graph.add_edge('rawa_buntu', 'serpong', 7)
krl_graph.add_edge('serpong', 'cisauk', 7)
krl_graph.add_edge('cisauk', 'cicayur', 7)
krl_graph.add_edge('cicayur', 'parung_panjang', 7)
krl_graph.add_edge('parung_panjang', 'cilejit', 7)
krl_graph.add_edge('cilejit', 'daru', 7)
krl_graph.add_edge('daru', 'tenjo', 7)
krl_graph.add_edge('tenjo', 'tigaraksa', 7)
krl_graph.add_edge('tigaraksa', 'cikoya', 7)
krl_graph.add_edge('cikoya', 'maja', 7)
krl_graph.add_edge('maja', 'citeras', 7)
krl_graph.add_edge('citeras', 'rangkas_bitung', 7)

# Bogor Line
krl_graph.add_edge('jakarta_kota', 'jayakarta', 10)
krl_graph.add_edge('jayakarta', 'mangga_besar', 10)
krl_graph.add_edge('mangga_besar', 'sawah_besar', 10)
krl_graph.add_edge('sawah_besar', 'juanda', 10)
krl_graph.add_edge('juanda', 'gondangdia', 10)
krl_graph.add_edge('gondangdia', 'cikini', 10)
krl_graph.add_edge('cikini', 'manggarai', 10)
krl_graph.add_edge('manggarai', 'tebet', 10)
krl_graph.add_edge('tebet', 'cawang', 10)
krl_graph.add_edge('cawang', 'duren_kalibata', 10)
krl_graph.add_edge('duren_kalibata', 'pasar_minggu_baru', 10)
krl_graph.add_edge('pasar_minggu_baru', 'pasar_minggu', 10)
krl_graph.add_edge('pasar_minggu', 'tanjung_barat', 10)
krl_graph.add_edge('tanjung_barat', 'lenteng_agung', 10)
krl_graph.add_edge('lenteng_agung', 'univ_pancasila', 10)
krl_graph.add_edge('univ_pancasila', 'univ_indonesia', 10)
krl_graph.add_edge('univ_indonesia', 'pondok_cina', 10)
krl_graph.add_edge('pondok_cina', 'depok_baru', 10)
krl_graph.add_edge('depok_baru', 'depok', 10)
krl_graph.add_edge('depok', 'citayam', 10)

# Nambo
krl_graph.add_edge('citayam', 'pondok_rajeg', 6)
krl_graph.add_edge('pondok_rajeg', 'cibinong', 6)
krl_graph.add_edge('cibinong', 'nambo', 6)

# Bogor
krl_graph.add_edge('citayam', 'bojong_gede', 5)
krl_graph.add_edge('bojong_gede', 'cilebut', 5)
krl_graph.add_edge('cilebut', 'bogor', 5)

# Priok
krl_graph.add_edge('jakarta_kota', 'kampung_bandan', 10)
krl_graph.add_edge('kampung_bandan', 'ancol', 10)
krl_graph.add_edge('ancol', 'tanjung_priok', 10)

# route search
# krl_graph.bfs('cikarang', 'bekasi')
# krl_graph.bfs('bekasi', 'cikarang')
# krl_graph.bfs('jatinegara', 'bogor')
# krl_graph.bfs('bogor', 'rangkas_bitung')
krl_graph.bfs('rangkas_bitung', 'tanjung_priok')
