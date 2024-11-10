class Hewan {
    String nama;

    public Hewan(String nama) {
        this.nama = nama;
    }

    public void bersuara() {
        System.out.println("Hewan ini bersuara.");
    }
}

class Kucing extends Hewan {
    public Kucing(String nama) {
        super(nama);
    }

    @Override
    public void bersuara() {
        System.out.println(nama + " mengeluarkan suara: Meow!");
    }

    public void tidur() {
        System.out.println(nama + " sedang tidur.");
    }
}

public class ContohInheritance {
    public static void main(String[] args) {
        Kucing kucing = new Kucing("Kitty");
        kucing.bersuara();
        kucing.tidur();
    }
}
