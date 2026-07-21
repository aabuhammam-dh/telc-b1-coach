<!-- Translated from README.md at commit 2304a0a. Re-translate when the English version changes. -->

# telc-b1-exam — nasıl kullanılır

**🌍 Languages:** [English](README.md) · [العربية](README.ar.md) · **Türkçe** · [Русский](README.ru.md) · [Українська](README.uk.md) · [فارسی](README.fa.md) · [Español](README.es.md)

Nesnel bölümler (Leseverstehen, Sprachbausteine, Hörverstehen) ve sözlü sınav için, geçmiş sınav kağıtları üzerinde alıştırma yapmayı temel alan, sıkı telc **Deutsch B1** koçunuz. Yanıtlarınızı kaydeder ve puanlar, her kaçırdığınızı açıklar, tekrarlayan tuzakları bulur, zayıf noktalarınızı çalıştırır, bir testten kelime/dilbilgisi çıkarır ve Mündliche Prüfung'a (sözlü sınav) hazırlar. **Mektup (Schreiben)**, bu skill'in işi otomatik olarak devrettiği eşlik eden skill `telc-b1-schreiben` tarafından ele alınır.

> DTZ değil. Bu, genel yetişkin telc Deutsch B1 sınavıdır.

## Hızlı başlangıç
1. Skill'i kurun (`.skill` dosyasında **Save skill** düğmesine tıklayın).
2. Alıştırma sınavı PDF'lerinizi koçun okuyabileceği bir yere koyun (bu projede `/mnt/project/` içinde bulunurlar). Koç bunları doğrudan okur — ZIP tarzı `.pdf` dışa aktarımları olabilirler.
3. Ona düz bir dille ya da köşeli parantez içinde bir komutla konuşun, örneğin `[log exam]` ya da *"Vera yanıtlarımı puanla"* ya da *"obwohl ile trotzdem arasındaki farkı açıkla."*

## Komutlar (bilgi kartı)
| Komut | Ne için kullanılır |
|---|---|
| `[log exam]` | Bir sınava verdiğiniz yanıtları girin ve **puanlanmasını** sağlayın (kodla kontrol edilir, asla göz kararı değil). |
| `[score "Jan"]` | Kaydedilmiş bir sınavın puanını, zayıf alanlarını ve hâlâ bekleyenleri görün. |
| `[discuss "Jan"]` | Her yanlış yanıtı gözden geçirin: doğrusu, tuzak tipi, kural. |
| `[study "Jan"]` | O sınavın dilbilgisi, kelime, bağlaçları ve tuzakları üzerine bir öğretim oturumu. |
| `[practice "Jan"]` | Alıştırma: kaçırdıklarınızı yeniden sorar + benzer taze maddeler, B1'e uygun şekilde düzeltilmiş. |
| `[retake "Jan"]` | Süreli tam simülasyon, sırasında yardım yok, sonrasında sıkı puanlama. |
| `[extract "Jan"]` / `[extract all]` | Bilinmesi zorunlu **kelime (DE→EN)**, **bağlaçlar** (+ her birinin nasıl çalıştığı) ve Sprachbausteine'nin test ettiği **kritik dilbilgisini** çıkarın. |
| `[mock exam]` / `[generate test]` | **Sınav PDF'i yok mu? Taze, özgün, telc formatında bir alıştırma testi üretin** (tam veya tek bölüm); gerçek B1 zorluğunda, cevap anahtarıyla. Her seferinde yeni içerik. |
| `[topic "<name>"]` / `[topic]` | **Tek bir konuyu öğret + test et** (bir dilbilgisi noktası, bağlaçlar veya bir kelime teması), ardından hazır/kararsız/hazır değil şeklinde bir karar verir ve bunu takip eder. Tek başına `[topic]` zayıf noktalarınızdan sırada ne çalışacağınızı önerir. |
| `[weaknesses]` | Tüm sınavlar genelinde zayıflık profilinizi görün ve hedefli alıştırmalar alın. |
| `[compare exams]` | Sınavlar arası kalıplar + hangi geçmiş kağıtların aynı metinleri yeniden kullandığı. |
| `[write "Jan"]` | O sınavın **mektup** görevi üzerinde çalışın → `telc-b1-schreiben`'i etkinleştirir. |
| `[help]` | Komut listesini yazdırın. |

Köşeli parantez veya slash, fark etmez (`[log exam]` = `/log-exam`). Tırnak içindeki adlar sizin sınavlarınızdır (Jan, Vera, Eva, Petra, …).

## En çok verimi aldıran iş akışı
Her sınav için bu döngüyü çalıştırın, sonra bir sonrakine geçin:
1. **`[log exam]`** → puanlayın. Koç güçlü/zayıf yönlerinizi otomatik olarak kaydeder.
2. **`[discuss "…"]`** → her kaçırmanın *neden* olduğunu anlayın (tuzak tipi + kural).
3. **`[extract "…"]`** → o sınavın test ettiği kelimeleri, bağlaçları ve dilbilgisini çıkarın.
4. **`[practice "…"]`** → tuzak yok olana kadar tam olarak kaçırdıklarınızı + benzerlerini çalıştırın.
5. Daha sonra, tekrar oturduğunu doğrulamak için soğuk soğuk **`[retake "…"]`** yapın.
6. Her hafta ya da öyle bir aralıkla, şu anda size en çok puan kaybettiren şeye yeniden nişan almak için **`[compare exams]`** ve **`[weaknesses]`** yapın.

Ayrıca, **mektubu** `[write "…"]` (→ Schreiben skill'i) ile ilerletmeye devam edin ve Teil 1 / 2 / 3 alıştırması yaptırmasını isteyerek **sözlüyü** prova edin — bunlar en büyük puan bloklarından ikisidir ve ihmal edilmesi kolaydır.

## En iyi sonuçlar için ipuçları
- **Ona gerçek yanıtlarınızı verin**, özet değil — puanlama soru soru yapılır.
- **"Geçiyor muyum?" diye sorun** — o zaman *ağırlıklı* puanlar üzerinden akıl yürütür (mektup, yazılı 225 puanın 45'idir), yalnızca ham x/60 sayacı üzerinden değil.
- **Dilbilgisi soruları temellendirilmiş yanıtlar alır** — koç önce saygın bir Almanca dilbilgisi kaynağında web araması yapar, sonra basitçe açıklar. Rahatça sorun (*"in edatından sonra ne zaman dativ olur?"*).
- **Zaman kısıtlıysa Lesen & Hören doğruluğunu Sprachbausteine'ye göre önceliklendirin**: gerçek puanlarda her Lesen/Hören maddesi bir SB maddesinin 2,5 katı değerindedir (ancak SB, kalıp tabanlı olduğu için düzeltmesi en hızlı olandır).
- **Belleğe kaydetmesine izin verin** ki kelimeler, bağlaçlar ve zayıflık profiliniz oturumlar boyunca birikip katlansın.

## Neye ihtiyacı var
- **Alıştırma sınavı yok mu? Sorun değil** — `[mock exam]` kullanın, sizin için özgün, telc formatında alıştırma üretir. Alıştırma sınavı PDF'leri isteğe bağlıdır: varsa ekleyin (cevap anahtarları son sayfadadır), onları da puanlar ve içlerinden malzeme çıkarır.
- Dilbilgisi açıklamaları için web erişimi (arar, sonra yanıtı temellendirir).
- Mektupla ilgili herhangi bir şey için `telc-b1-schreiben` skill'inin kurulu olması.
