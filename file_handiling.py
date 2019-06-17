import os
import time
import sys
import shutil


source_path = ('D:\EMTEL\sample_files')
onlyfiles_in_source = next ( os.walk ( source_path ) ) [ 2 ]
file_count_insource = len ( onlyfiles_in_source )

#print ( 'Files in source', file_count_insource )

dst_path = ('D:\EMTEL\Logs_Out')
if not os.path.exists (dst_path):
    os.makedirs(dst_path)
onlyfiles_in_dst = next ( os.walk ( dst_path ) ) [ 2 ]
file_count_indst = len ( onlyfiles_in_dst )
print ('Files in destination', file_count_indst)

if file_count_insource < 500 :
    now = time.time()
    old = now - 10*60
    paths = [ os.path.join ( source_path, fname ) for fname in os.listdir ( source_path ) ]
    files = sorted ( paths, key=os.path.getmtime )
    if files < old:
        print ( "Movinng", files )

    oldest = files [ 0 ]
    newest = files [ -1 ]
    print ('Oldest file is ' + oldest)
    print ('Newest filr is ' + newest)




