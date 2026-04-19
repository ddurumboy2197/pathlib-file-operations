import pathlib

def yarat_papkani(papka_nomi):
    papka = pathlib.Path(papka_nomi)
    papka.mkdir(parents=True, exist_ok=True)

def ochir_faylni(fayl_nomi):
    fayl = pathlib.Path(fayl_nomi)
    fayl.unlink(missing_ok=True)

def rekursiv_royxatlash(papka_nomi):
    papka = pathlib.Path(papka_nomi)
    for fayl in papka.rglob("*"):
        print(fayl)

# Misol
yarat_papkani("papka")
ochir_faylni("papka/fayl.txt")
rekursiv_royxatlash("papka")
```

Kodda quyidagi funksiyalar mavjud:

- `yarat_papkani(papka_nomi)`: `papka_nomi` nomli papka yaratadi.
- `ochir_faylni(fayl_nomi)`: `fayl_nomi` nomli faylni o'chiradi.
- `rekursiv_royxatlash(papka_nomi)`: `papka_nomi` nomli papkada bo'lgan barcha fayllarni ro'yxatga olish uchun rekursiv ravishda foydalanadi.
