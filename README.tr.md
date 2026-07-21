<!-- Translated from README.md at commit 2304a0a. Re-translate when the English version changes. -->

# telc B1 Coach 🇩🇪

**🌍 Languages:** [English](README.md) · [العربية](README.ar.md) · **Türkçe** · [Русский](README.ru.md) · [Українська](README.uk.md) · [فارسی](README.fa.md) · [Español](README.es.md)

**Claude**'u — ya da beceri (skill) destekleyen başka bir yapay zekayı — **telc Deutsch B1** sınavı için sıkı ve tavizsiz bir koça dönüştüren iki ücretsiz eklenti ("skill"). Alıştırma yanıtlarınızı puanlar, her hatayı açıklar, zayıf noktalarınızı çalıştırır, sözlü sınava hazırlar ve yazma becerinizi koçlar.

<p align="center">
  <img src="assets/demo.gif" alt="telc B1 Coach iş başında — yanıtları kaydediyor, puanlıyor ve hataları açıklıyor" width="720">
</p>

> Genel **telc Deutsch B1** sınavı (yetişkinlere yönelik *Zertifikat Deutsch*) içindir. DTZ **değildir**, Goethe B1 de değildir.

Bu kılavuz, **daha önce hiç "skill" kullanmamış olsanız bile, bu bağlantıya sahip herkesin birkaç dakika içinde çalışır hale getirebilmesi** için yazılmıştır. Sadece kullandığınız uygulamaya ait bölümü takip edin.

---

## Neler elde edersiniz

Birlikte çalışan iki skill:

- **`telc-b1-exam`** — bir alıştırma sınavına verdiğiniz yanıtları kaydeder ve puanlar, her yanıtın *neden* yanlış olduğunu (tuzak + kural) size söyler, bir testten önemli kelimeleri, bağlaçları ve dilbilgisini çıkarır, zayıf noktalarınızı çalıştırır, konuşma pratiği yaptırır ve — elinizde hiç alıştırma sınavı yoksa — **gerçek telc formatında sizin için taze, özgün sınavlar üretir**. Dilbilgisi soruları gerçek kaynaklardan yanıtlanır ve basitçe açıklanır.
- **`telc-b1-schreiben`** — **yazılı mektubu** koçlar: formatı öğretir, mektubunuzu gerçek sınav değerlendiricileri gibi puanlar ve tekrar tekrar yaptığınız hataları çalıştırır.

İstediklerinizi düz bir dille (*"yanıtlarımı puanla"*, *"weil ile denn arasındaki farkı açıkla"*, *"bu mektup geçer mi?"*) ya da `[log exam]` veya `/written-grade` gibi kısa komutlarla belirtebilirsiniz.

---

## Adım 1 — Skill'leri bu sayfadan indirin

1. Bu deponun en üstüne kaydırın.
2. Yeşil **`< > Code`** düğmesine tıklayın, ardından **Download ZIP** seçeneğine tıklayın.
3. İndirdiğiniz dosyayı açın (unzip). İçinde iki klasör bulacaksınız:
   **`telc-b1-exam`** ve **`telc-b1-schreiben`**.

Hepsi bu — bu iki klasör *zaten* skill'lerin kendisidir. Şimdi bunları aşağıdaki ilgili bölümü kullanarak yapay zekanıza kurun.

---

## Adım 2 — Kurun (uygulamanızı seçin)

### 🟣 Seçenek A — Claude web sitesi veya Claude uygulaması (çoğu kişi)

1. **Her skill klasörünü ayrı ayrı zip'leyin.** Her skill için ayrı bir `.zip` gerekir:
   - **Mac:** `telc-b1-exam` klasörüne sağ tıklayın → **Compress**. `telc-b1-schreiben` için tekrarlayın.
   - **Windows:** klasöre sağ tıklayın → **Send to → Compressed (zipped) folder**. Diğeri için tekrarlayın.
   *(Sonunda elinizde `telc-b1-exam.zip` ve `telc-b1-schreiben.zip` olmalı.)*
2. Claude'da **profil simgeniz → Settings → Capabilities** yolunu izleyin ve **Code execution and file creation** özelliğinin **açık** olduğundan emin olun. *(Skill'lerin gerçekten ihtiyaç duyduğu tek şey budur.)*
3. **Customize → Skills** bölümüne gidin, **Upload skill** düğmesine tıklayın ve `telc-b1-exam.zip` dosyasını seçin. Aynısını `telc-b1-schreiben.zip` için de yapın.
4. Bitti. telc B1 sınavından bahsettiğinizde Claude bunları otomatik olarak kullanır. Buraya yüklediğiniz skill'ler hem **Claude Chat** hem de **Cowork** içinde çalışır.

> **Free planında da çalışır** — skill'ler **Free, Pro, Max, Team ve Enterprise** planlarında mevcuttur; tek gereksinim **Code execution and file creation** özelliğinin etkin olmasıdır (adım 2). Free planında yalnızca normal günlük mesaj sınırınız olur. **Team/Enterprise** için, bir yöneticinin önce Skills özelliğini kuruluş genelinde açması gerekebilir (Team'de varsayılan olarak açıktır). Buraya yükleme yapmak skill'leri Claude Code'a veya API'ye **kopyalamaz** — bunlar ayrıdır (aşağıya bakın). Menü adları sürüme göre biraz değişebilir.

### 🟢 Seçenek B — Claude Code (terminal / VS Code / JetBrains)

Zip'leme yok, yükleme yok — skill'ler bilgisayarınızdaki klasörlerden ibarettir.

1. Yoksa skills klasörünü oluşturun: `~/.claude/skills/`
   *(bu, ev dizininizdeki gizli bir `.claude` klasörünün içinde `skills` adında bir klasördür).*
2. **Hem** `telc-b1-exam` **hem de** `telc-b1-schreiben` klasörlerini içine kopyalayın.
3. Claude Code oturumunuzu yeniden başlatın. Onları otomatik olarak keşfeder ve kullanır.

*(Bunları her yerde değil de yalnızca tek bir projenin içinde mi istiyorsunuz? Klasörleri o projenin `.claude/skills/` klasörüne koyun.)*

### 🔵 Seçenek C — Skill destekleyen başka bir yapay zeka (Gemini, Codex, Cursor, Copilot…)

Agent Skills bir **açık standarttır**, bu yüzden *aynı klasörler* birçok başka yapay zeka aracında çalışır. İki durum vardır:

**C1 — `SKILL.md` dosyalarını okuyan kodlama araçları** (Gemini CLI, OpenAI Codex CLI, Cursor, GitHub Copilot ve 25+ diğerleri): skill klasörlerini o aracın skills dizinine kopyalayın — örneğin Gemini CLI için **`.gemini/skills/`** — ve yeniden başlatın. Skill hiç değiştirilmeden çalışır; yeniden yazmaya gerek yok.

- Kısayol: bunların çoğu, dosyaları otomatik olarak doğru yere koyan tek satırlık bir yükleyiciyi destekler — `npx skills add <this-repo>` — ayrıntılar için **skills.sh** adresine bakın.

**C2 — Bunun yerine "özel botlar" kullanan sohbet asistanları** (Gemini uygulamasının **Gems** özelliği veya ChatGPT'nin **GPTs** özelliği): bunlar skill dosyalarını doğrudan okumaz, ancak bir skill sadece düz metin talimatlardan ibarettir, dolayısıyla:

1. Bir skill'in **`SKILL.md`** dosyasını açın (her klasörün içindedir) ve içindeki her şeyi kopyalayın.
2. Yeni bir **Gem** (Gemini) veya **GPT** (ChatGPT) oluşturun ve o metni talimatları olarak yapıştırın.
3. Skill kendi `references/` klasöründeki dosyalardan bahsediyorsa, bunları botun bilgi/dosyaları olarak ekleyin veya koç istediğinde ilgili olanı yapıştırın.

Bu, evrensel yedek çözümdür — esasen herhangi bir asistanda çalışır, ancak derinlemesine referans materyali Claude'daki kadar otomatik yüklenmez.

---

## Adım 3 — Çalıştığını kontrol edin

Yeni bir sohbet başlatın ve şunu yazın:

> **`[help]`**

Sınav koçu komutlarını listelemelidir. Ya da sadece *"telc B1 sınavına hazırlanmak istiyorum"* deyin, gerisini o halleder. Yazma koçunu denemek için *"bana bir B1 yazma görevi ver"* deyin.

---

## Hangi skill ne işe yarar

| Skill | Kapsamı | Söyleyin / yazın |
|---|---|---|
| **`telc-b1-exam`** | Okuma, Sprachbausteine, Dinleme + **konuşma** sınavı, puanlama, alıştırmalar, dilbilgisi, **özgün alıştırma testleri üretme** ve hazırlık takibiyle **tek konularda öğret-ve-test** | `[mock exam]`, `[topic "connectors"]`, `[log exam]`, "obwohl ile trotzdem arasındaki farkı açıkla" |
| **`telc-b1-schreiben`** | **Yazılı mektup** — format, puanlama, hata alıştırmaları, ifadeler | `/written-grade`, "bu mektup geçer mi?" |

Otomatik olarak eşleşirler: mektup üzerinde çalıştığınızda sınav koçu işi yazma koçuna devreder, bu yüzden **ikisini de kurun**.

Her skill'in kendi kısa kılavuzu da vardır: [`telc-b1-exam/README.md`](telc-b1-exam/README.md) ve [`telc-b1-schreiben/README.md`](telc-b1-schreiben/README.md).

---

## Bilmeniz gereken birkaç şey

- **Başlamak için herhangi bir alıştırma sınavına ihtiyacınız yok.** Sadece **`[mock exam]`** deyin, koç sizin için taze, özgün, telc formatında bir alıştırma testi (tam test veya tek bölüm) üretir; gerçek B1 zorluğunda, cevap anahtarıyla — her seferinde yeni içerik.
- **Resmi materyal de mi istiyorsunuz?** telc size **ücretsiz resmi bir örnek sınav** verir — *cevap anahtarları ve dinleme sesiyle birlikte* eksiksiz bir test — B1 sayfalarında. İndirin ve koça gösterin:
  **<https://www.telc.net/sprachpruefungen/deutsch/zertifikat-deutsch-telc-deutsch-b1/>**
  (sayfanın İngilizce sürümü de var). Herhangi bir telc formatındaki alıştırma sınavı işe yarar; cevap anahtarları son sayfadadır.
- **Burada telif hakkı olan içerik yok.** Bu depo telc sınav metni **içermez** — o sınavlar telif hakkıyla korunan telc materyalidir. Skill'ler **özgün** alıştırma üretir ve yalnızca sizin kendinizin sağladığı sınav PDF'lerini *okur*; bunları asla kopyalamaz veya yeniden yayınlamaz.
- **Her uygulama ayrı kurulur.** Claude web sitesine yükleme yapmak Claude Code'a veya diğer yapay zekalara senkronize olmaz — kullanmak istediğiniz her yeri ayrı ayrı ayarlayın.
- **Kutudan çıktığı gibi kullanıma hazırdır.** Skill'ler başlangıç içeriğiyle gelir (yaygın sınav tuzakları, örnek kalıplar, bir ifade bankası), bu yüzden hemen kullanışlıdırlar; siz pratik yaptıkça Claude size göre ince ayar yapar. Hiçbir kişisel veri içermez.

## Lisans

MIT — bkz. [`LICENSE`](LICENSE). Bunu fork'ladıysanız veya yeniden yayınladıysanız, telif hakkı satırına adınızı ekleyin.
