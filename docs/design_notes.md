Design Notes
TM-1 · Unary to Binary
Strateji

Bu makinede amacım unary biçimindeki sayıyı binary biçimine çevirmekti. İlk başta direkt dönüştürmeye çalıştım ama durumlar çok karıştı. Sonrasında girdideki 1 sembollerini tek tek işaretleyip binary sonucu şeridin başka kısmına yazdırma mantığı kullandım. Makine sürekli sağa gidip unary kısmını kontrol ediyor, sonra geri dönüp binary çıktıyı oluşturuyor.

Durum Sayısı

Bu makinede birkaç farklı durum kullandım çünkü hem işaretleme hem geri dönüş hem de binary yazma işlemleri gerekiyordu. Daha az durumla yapılabilir ama okunabilirlik çok düşüyordu.

Şerit Alfabesi

Ek olarak X sembolünü kullandım. Bunun nedeni işlenen hücreleri tekrar işlememekti. Başta sadece 1 ve 0 kullanmaya çalıştım ama hangi hücrenin işlendiğini takip etmek çok zor oldu.

Karmaşıklık

Makine sürekli şerit üzerinde ileri geri hareket ettiği için yaklaşık olarak O(n²) karmaşıklığında çalışıyor.

Hata Ayıklama Hikayesi

En çok zorlandığım hata blank sembolüyle ilgiliydi. Makine bazen şeridin başına dönerken sonsuz döngüye giriyordu. Sorunun kafa hareketlerinden kaynaklandığını fark edip geçişleri yeniden düzenledim.

TM-2 · Binary Compare
Strateji

Bu makinede # sembolüyle ayrılmış iki binary sayıyı karşılaştırdım. İlk sayı ikinci sayıdan büyükse kabul edecek şekilde tasarladım. Başta mantığı kurmak kolay görünüyordu ama tek şeritli yapıda sürekli ileri geri gitmek zor oldu.

Durum Sayısı

Karşılaştırma işlemi için birden fazla kontrol durumu kullandım. Özellikle iki taraf arasında gidip gelirken hangi aşamada olduğumu takip etmek için ek durumlar gerekti.

Şerit Alfabesi

# ayırıcı sembolü işlemi çok kolaylaştırdı. Ekstra işaretleme sembolleri de bazı karşılaştırma adımlarında yardımcı oldu.

Karmaşıklık

Makine birçok kez şeridi baştan sona taradığı için yaklaşık O(n²) karmaşıklığında çalışıyor.

Hata Ayıklama Hikayesi

En zor hata compare kısmındaydı. Bazı girdilerde makine her şeyi kabul ediyordu. Bunun nedeni reject path’lerinden birinin eksik olmasıydı. Test yazarak hangi girdilerde hata verdiğini buldum.

TM-3 · String Copy
Strateji

Bu makinede amaç girdiyi # sembolünden sonra tekrar oluşturmaktı. Örneğin abba girdisini abba#abba haline getiriyor. Bunun için karakterleri tek tek işaretleyip kopyalama yöntemi kullandım.

Durum Sayısı

Makinede işaretleme, kopyalama ve geri dönüş için ayrı durumlar kullandım. Çünkü tek şerit üzerinde çalışırken hangi karakterin kopyalandığını takip etmek gerekiyordu.

Şerit Alfabesi

A ve B gibi yardımcı semboller kullandım. Bunlar işlenen karakterleri belirtmek için gerekliydi.

Karmaşıklık

Makine sürekli ileri geri hareket ettiği için yaklaşık O(n²) zamanda çalışıyor.

Hata Ayıklama Hikayesi

En çok zorlandığım kısım karakterlerin üstüne yanlışlıkla tekrar yazılmasıydı. Bazı durumlarda kopyalanan veri bozuluyordu. İşaretleme mantığını düzelterek problemi çözdüm.

TM-4 · Student Choice
Strateji

Öğrenci seçimi kısmında kendi belirlediğim kontrol problemini çözmeye çalıştım. Önce problemi küçük adımlara böldüm sonra her adım için transition kuralları oluşturdum.

Durum Sayısı

Mümkün olduğunca az durum kullanmaya çalıştım ama okunabilirliği korumak için bazı ek durumlar ekledim.

Şerit Alfabesi

Şerit alfabesini sade tutmaya çalıştım. Gereksiz semboller eklemek yerine minimum yardımcı sembol kullandım.

Karmaşıklık

Makine çoğunlukla doğrusal şekilde ilerlediği için yaklaşık O(n) karmaşıklığında çalışıyor.

Hata Ayıklama Hikayesi

Kenar durumlarda makinenin yanlış reject vermesi en büyük problemdi. Özellikle boş giriş ve kısa girdiler için ek testler yazarak düzelttim.

Genel Deneyim

Bu projede en çok öğrendiğim şey Turing makinelerinin teoride basit görünmesine rağmen pratikte tasarlamasının zor olmasıydı. Özellikle tek şeritli yapıda sürekli kafa hareketlerini düşünmek gerekti. Ayrıca pytest kullanarak test yazmanın hata ayıklamayı çok kolaylaştırdığını fark ettim. MultiTapeTM ve visualizer kısmı projeyi daha eğlenceli hale getirdi çünkü gerçek bir simülatör gibi görünmeye başladı.


**********************************************************


Design Notes
TM-1 · Unary to Binary
Strategy

In this machine, my goal was to convert a unary number into binary representation. At first I tried to directly transform the symbols, but the transitions became very complicated. Later I used a marking strategy where the machine processes unary symbols one by one and gradually writes the binary output on another part of the tape.

Number of States

I used several states because the machine needed separate phases for scanning, marking, returning and writing binary digits. Using fewer states was possible, but the logic became harder to read and debug.

Tape Alphabet

I added an extra symbol X to mark processed cells. Without helper symbols it was difficult to keep track of which parts of the tape had already been processed.

Complexity

The machine repeatedly scans the tape from left to right and back again, so the overall complexity is approximately O(n²).

Debugging Story

The most difficult bug was related to blank symbols. Sometimes the machine entered an infinite loop while returning to the start of the tape. I fixed this problem by redesigning the head movement transitions.

TM-2 · Binary Compare
Strategy

This machine compares two binary numbers separated by the # symbol. The machine was designed to check the relationship between the left and right side values. The main challenge was synchronizing the comparisons while moving on a single tape.

Number of States

I used multiple checking states because the machine had to move between the two binary numbers many times.

Tape Alphabet

The # separator made parsing much easier. I also used helper symbols during some comparison steps.

Complexity

Because the machine repeatedly traverses the tape, the complexity is roughly O(n²).

Debugging Story

The hardest issue appeared during reject scenarios. Some invalid inputs were still being accepted because one reject transition path was missing. Writing additional pytest cases helped me detect this problem.

TM-3 · String Copy
Strategy

The purpose of this machine is copying the input string after a # separator. For example, the input abba becomes abba#abba. I used a marking-based strategy where characters are processed one by one and copied to the output area.

Number of States

Separate states were required for marking characters, moving across the tape and rewriting symbols.

Tape Alphabet

I used helper symbols such as A and B to represent already processed characters.

Complexity

Since the machine constantly moves back and forth across the tape, the complexity is approximately O(n²).

Debugging Story

The biggest problem was accidentally overwriting symbols during the copying process. Some transitions caused already copied data to be corrupted, so I redesigned the marking logic.

TM-4 · Student Choice
Strategy

For the student-choice machine, I selected my own checking problem and divided it into smaller logical steps before creating the transitions.

Number of States

I tried to keep the number of states small while still preserving readability.

Tape Alphabet

I intentionally kept the tape alphabet simple and avoided unnecessary helper symbols.

Complexity

This machine mostly moves in a linear way, so the complexity is approximately O(n).

Debugging Story

The biggest issue was handling edge cases correctly. Empty inputs and very short strings sometimes produced unexpected reject results, so I added extra tests.

General Experience

The most important thing I learned from this project is that Turing Machines look simple in theory but become much more difficult in practice. Managing tape head movement on a single tape required careful thinking. I also learned that writing pytest tests makes debugging significantly easier. The MultiTapeTM and visualizer parts made the project feel like a real simulator and improved my understanding of automata systems.