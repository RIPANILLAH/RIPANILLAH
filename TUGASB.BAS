CLS
PRINT "========== SELAMAT DATANG DI PROGRAM =========="
SLEEP (3)

CLS
PRINT "========== SILAHKAN PILIH MENU DI BAWAH INI =========="
PRINT "1. List Buku"
PRINT "2. Pinjam Buku"
PRINT "3. Kembalikan Buku"
PRINT "4. Keluar"
PRINT "======================================================"
INPUT "SILAHKAH PILIH MENU DIATAS: ", y
IF y = 1 THEN
        PRINT "                      Daftar Buku Yang Ada Di Sini                   "
        PRINT "====================================================================="
        PRINT " Judul                       Nama Penulis                  Keterangan"
        item$ = "\                      \                                 \         \"
        OPEN "MYBOOK.DAT" FOR INPUT AS #1
        DO UNTIL EOF(1)
                INPUT #1, J$, NP$, K$
                PRINT USING item$; J$; NP$; K$
        LOOP
END IF



