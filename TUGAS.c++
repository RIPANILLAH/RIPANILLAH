#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, double> ongkos = {{"jawa", 9000}, {"kalimantan", 10000}, {"sumatra", 11000}, {"sulawesi", 12000}};
    double beban;
    std::string tujuan;

    std::cout << "Masukkan beban (dalam kg): ";
    std::cin >> beban;
    std::cout << "Masukkan tujuan (jawa, kalimantan, sumatra, atau sulawesi): ";
    std::cin >> tujuan;

    double hasil = beban * ongkos[tujuan];
    if (hasil > 1000000) {
        hasil -= 10000;
    }
    double diskon;
    if (beban < 20) {
        diskon = 0;
    } else if (beban >= 20 && beban < 40) {
        diskon = 0.025;
    } else {
        diskon = 0.03;
    }
    hasil -= hasil * diskon;

    std::cout << "Ongkos kirim untuk beban " << beban << " kg ke " << tujuan << " adalah " << hasil << std::endl;

    return 0;
}
