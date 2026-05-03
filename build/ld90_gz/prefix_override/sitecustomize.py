import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/cayo-sousa/ws_ld90_sim/install/ld90_gz'
