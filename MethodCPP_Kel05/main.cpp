#include <iostream>
using namespace std;

class MyClass {
  public:
    void non_return_method(string kelompok){
      cout << "Halo, kami dari kelompok " << kelompok <<endl;
    }

    int return_method(int angka){
      return angka*angka;
    }
};

int main() {

MyClass obj;

  cout << "[NON RETURN METHOD]" <<endl;

  obj.non_return_method("05");

  cout << "\n[RETURN METHOD]" <<endl;

  int angka = 13;

  cout << "Hasil kali dari " << angka << " dengan " << angka << " adalah " << obj.return_method(angka);

  return 0;
}
