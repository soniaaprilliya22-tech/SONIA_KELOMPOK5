<?php
    declare(strict_types=1);


//class MyClass sebagai pendefinisi method
    class MyClass {


        public function akar(float $nilai) : float {
            return sqrt($nilai);
        }


        public function printNama(string $nama): string {
            return "Nama saya $nama";
        }


        public function printUmur(int $umur){
            echo "Umur saya $umur <br>";
        }


        public function printPekerjaan() {
            echo "Saya adalah seorang mahasiswa";
        }
    }


    $angka = 121;
    //$objek adalah instance dari MyClass
    $objek = new MyClass();


    //pemanggilan method pada PHP menggunakan ->
    echo "Akar kuadrat dari $angka adalah: ".$objek->akar($angka);
    echo "<hr>";
    echo $objek->printNama("Sonia")."<br>";
    $objek->printUmur(18);
    $objek->printPekerjaan();
?>