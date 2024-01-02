#include <iostream>
#include <map>
#include <string>
#include <iomanip>

using namespace std;

void hitung_ongkos_kirim() {
    map<string, int> ongkos = {{"jawa", 9000}, {"kalimantan", 10000}, {"sumatra", 11000}, {"sulawesi", 12000}};
    double beban;
    string tujuan;
    double hasil, potongan, diskon, jumlah_diskon;

    while (true) {
        cout << "Masukkan beban (dalam kg): ";
        cin >> beban;
        cout << "Masukkan tujuan (jawa, kalimantan, sumatra, atau sulawesi): ";
        cin >> tujuan;

        hasil = beban * ongkos[tujuan];
        potongan = (hasil > 1000000) ? 10000 : 0;
        hasil -= potongan;

        if (beban < 20) {
            diskon = 0;
        } else if (beban >= 20 && beban < 40) {
            diskon = 0.025;
        } else {
            diskon = 0.03;
        }

        jumlah_diskon = hasil * diskon;
        hasil -= jumlah_diskon;

        cout << "Tujuan: " << tujuan << endl;
        cout << "Beban: " << beban << endl;
        cout << "Jumlah Diskon: " << jumlah_diskon << endl;
        cout << "Potongan: " << potongan << endl;
        cout << "Hasil: " << hasil << endl;

        cout << "Apakah anda ingin melakukan perhitungan lagi? (ya/tidak): ";
        string lanjut;
        cin >> lanjut;
        if (lanjut != "ya") {
            break;
        }
    }
}

int main() {
    hitung_ongkos_kirim();
    return 0;
}
