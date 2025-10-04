#include <iostream>
using namespace std;

void non_return_func(string nama, long long nim) {
  cout << "Nama saya "<< nama << " dengan NIM " << nim <<endl;
}

int return_func(int tinggi) {
  if (tinggi <= 0) {
    return -1;
  }
  else if (tinggi <= 150) {
    return tinggi + 20;
  }
  else {
    return tinggi - 5;
  }
}

int main() {
  cout << "Halo Praktikan Pemrograman Dasar 2025\n" << endl;

  cout << "[FUNCTION NON RETURN]" << endl;
  non_return_func("Budi", 21120125120001);

  cout << "\n[RETURN FUNCTION]" << endl;
  cout << "Tinggi saya sekitar " << return_func(150);

  return 0;
}
