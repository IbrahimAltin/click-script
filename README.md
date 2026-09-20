# click-script

Windows üzerinde çalışan, klavye kısayollarıyla kontrol edilen basit bir otomatik tıklama scripti. Google Colab gibi uzun süren oturumlarda, sekmeden uzun süre uzak kalındığında bağlantının kopmasını önlemek amacıyla belirli aralıklarla fare tıklaması yapmak için hazırlanmıştır.

## Özellikler

Script çalıştırıldığında aşağıdaki tuşlarla kontrol edilir:

| Tuş | İşlev |
|-----|-------|
| `w` | Tek seferlik manuel tıklama yapar |
| `x` | Sürekli (yüksek hızlı) otomatik tıklamayı başlatır/durdurur |
| `f` | Her 10 saniyede bir tıklama yapan gecikmeli modu başlatır/durdurur (Colab bağlantısını açık tutmak için önerilen mod) |
| `esc` | Programdan çıkar |

Hem `x` hem `f` modu durdurulduğunda toplam tıklama sayısı, toplam çalışma süresi ve saniye başına tıklama (CPS) bilgisini konsola yazdırır.

## Gereksinimler

- Python 3.x
- Windows işletim sistemi (script `win32api` / `win32con` kullanır)
- Aşağıdaki kütüphaneler:
  - `pywin32`
  - `keyboard`

## Kurulum

```bash
pip install pywin32 keyboard
```

## Kullanım

```bash
python click_script.py
```

Script başladığında konsolda tuş kısayolları listelenir. Colab oturumunu açık tutmak için genellikle `f` tuşuna basarak gecikmeli modu başlatmak yeterlidir; script her 10 saniyede bir otomatik tıklama yapar. İşiniz bittiğinde `f` tuşuna tekrar basarak durdurabilir veya `esc` ile programdan çıkabilirsiniz.

## Not

- `keyboard` kütüphanesi Windows'ta klavye olaylarını genel sistem düzeyinde dinlediği için bazı durumlarda scriptin yönetici (admin) yetkisiyle çalıştırılması gerekebilir.
- Script yalnızca Windows için tasarlanmıştır.
