<!-- Translated from README.md at commit 2304a0a. Re-translate when the English version changes. -->

# telc-b1-schreiben — nasıl kullanılır

**🌍 Languages:** [English](README.md) · [العربية](README.ar.md) · **Türkçe** · [Русский](README.ru.md) · [Українська](README.uk.md) · [فارسی](README.fa.md) · [Español](README.es.md)

telc **Deutsch B1** sınavının **yazılı mektubu** (*Schriftlicher Ausdruck* — el yazısıyla yazılan yanıt-mektubu/e-postası) için sıkı koçunuz. Formatı ve tam telc puanlama kriterlerini öğretir, size sınav formatında görevler verir, mektuplarınızı gerçek telc değerlendiricilerinin yaptığı gibi puanlar, tekrar tekrar yaptığınız belirli hataları çalıştırır ve akıcı B1 ifadelerinden oluşan, takip edilen bir bankayı siz onları içselleştirene kadar büyütür. Hedef: **geçmek**, mükemmellik değil.

> Bu, koçun *yazma* yarısıdır. Okuma/dinleme/dilbilgisi/sözlü yarısı, mektup üzerinde çalıştığınızda işi bu skill'e devreden eşlik eden skill **`telc-b1-exam`** içinde bulunur. İkisini de kurun.

## Hızlı başlangıç
1. Skill'i kurun (Claude ve diğer yapay zekalarda nasıl yapılacağını depo README'sinde bulabilirsiniz).
2. Düz bir dille sorun veya bir komut kullanın — örneğin *"bana bir B1 yazma görevi ver"*, bir mektup yapıştırıp *"bu geçer mi?"* diye sorun ya da `/written-grade` yazın.

## Komutlar (bilgi kartı)
| Komut | Ne için kullanılır |
|---|---|
| `/written-teach [focus]` | Formatı, puanlama kriterlerini, mektup şablonlarını, Redemittel'i, yaygın hataları, zamanlamayı veya gönderim öncesi kontrol listesini öğrenin. |
| `/written-examine` | Tam telc B1 formatında **bir** görev alın (senaryo + gelen mektup + 4 Leitpunkte). Yazarken yardım yok. |
| `/written-grade` | Bir mektubu gerçek telc kriterleriyle puanlayın: "bu geçer mi?", /45 puanı, kriter dökümü ve puan kaybettiren hatalar. |
| `/written-drill [category]` | Geçmişinizden çekilen, tekrar tekrar yaptığınız *belirli* hata türlerini çalıştırın (fiil pozisyonu, hâller, üslup…). |
| `/written-upgrade` | *Doğru ama yavan* bir mektubu akıcı bir mektuba dönüştürün — çeşitlilik ve daha iyi ifade için cümle-cerrahisi hamleleri. |
| `[write "Jan"]` | Belirli bir alıştırma sınavının mektup görevini yapın ve puanlatın. (Bu, `telc-b1-exam`'den gelen köprüdür.) |

Köşeli parantez veya slash, her ikisi de çalışır (`/written-grade` = `[written-grade]`) ve düz dil de bunları tetikler.

## Mektup nasıl puanlanır (koç bazı konularda neden sıkı davranır)
- **Bir mektup, 30 dakika, ~120–150 kelime, 4 Leitpunkte** — dört noktanın da ele alınması gerekir. **45 puan** değerinde (sınavın %15'i).
- Üç kritere göre puanlanır (her biri A/B/C/D): **I** dört noktayı da kapsadınız mı · **II** yapı, bağlantı ve doğru üslup (du/Sie, selamlama, kapanış) · **III** dilbilgisi doğruluğu.
- **Sıfır kuralı:** eğer kriter **I ve/veya III bir D** ise, mektubun tamamı **0** alır. Yani dört noktayı da kapsamak ve anlaşılır kalmak, gösterişli dilden daha önemlidir.
Koç her puanlamada bu kriterleri açıkça gözden geçirir — asla hissiyata dayalı bir puan değil.

## En çok verimi aldıran iş akışı
1. Hedefi bilmeniz için bir kez **`/written-teach format & rubric`**.
2. **`/written-examine`** → 30 dakikalık saat altında, yardımsız bir mektup yazın.
3. **`/written-grade`** → /45 puanını ve puan kaybettiren hataları alın.
4. **`/written-drill`** → puanın ortaya çıkardığı tam hata türlerini çalışın.
5. Mektuplarınız *geçtiği* halde yavan okunuyorsa, akıcılık için **`/written-upgrade`**.
6. Taze bir `/written-examine` ile tekrarlayın ya da `[write "…"]` aracılığıyla gerçek bir sınavın mektubunu besleyin.

## En iyi sonuçlar için ipuçları
- **Her zaman dört Leitpunkte'yi de kapsayın**, kısaca bile olsa — birini atlamak 6 puanlık bir sallanmadır; yalnızca birini kapsamak sıfır kuralını tetikler.
- **Cümleleri basit ve doğru tutun** — anlaşılır bir B1 mektubu, iddialı ama bozuk bir mektubu yener. Fiil-pozisyonu hataları, yanlış bir hâl ekinden çok daha fazla zarar verir.
- **İfade bankanızı ve tekrarlayan hatalarınızı bellekte takip etmesine izin verin** ki alıştırmalar *sizin* sızıntılarınıza nişanlı kalsın ve ifadeler otomatikleşene kadar tekrar tekrar yüzeye çıksın.
- **Üslup senaryoyla sabittir** (şirket/resmi kurum → `Sie`; arkadaş → `du`) — doğru yapın; bu, kriter II altında puanlanır.

## Neye ihtiyacı var
- Claude'un ötesinde hiçbir şeye gerek yok ve ideal olarak sınav↔yazma devrinin çalışması için `telc-b1-exam` skill'inin kurulu olması.
- İsteğe bağlı: gerçek mektup görevlerini içlerinden çekmesini istiyorsanız, kendi alıştırma sınavı PDF'leriniz.
