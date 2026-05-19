# TuringLab Simulator — Proje Raporu

## Öğrenci Bilgileri

- Ders: Otomata Teorisi ve Biçimsel Diller
- Proje: Turing Machine Simulator
- Öğrenci: Fatma Betül Pehlivan
- Numara: 233311036

---

# 1. Proje Hakkında Genel Bilgi

Bu projedeki amacım YAML dosyalarından Turing Machine tanımlarını okuyabilen ve makineleri adım adım çalıştırabilen bir simülatör geliştirmekti.

Projeye ilk başladığımda Turing makineleri teorik olarak çok daha basit görünüyordu. Ancak iş uygulama kısmına gelince özellikle kafa hareketlerini yönetmek, transition mantığını kurmak ve sonsuz döngüleri engellemek düşündüğümden daha zor oldu.

Projede zamanla sadece temel bir simulator yapmak yerine sistemi geliştirmeye başladım. İlk başta yalnızca Single Tape Turing Machine yapısı vardı. Daha sonra görselleştirme sistemi, GIF üretimi, test sistemi ve MultiTapeTM desteği ekledim.

Şu anda sistem şunları destekliyor:

- YAML tabanlı sistem tanımları
- Single Tape Turing Machine
- Multi Tape Turing Machine
- Step-by-step execution history
- GIF görselleştirme sistemi
- Pytest ile otomatik testler
- Timeout kontrolü
- Input validation
- Accept / Reject durumları

Projeyi geliştirirken en çok hoşuma giden şey sistemin zamanla gerçek bir simülatöre benzemeye başlaması oldu.

---

# 2. Proje Yapısı

Projeyi daha düzenli tutabilmek için sistemi farklı dosyalara ayırdım.

## tm_engine.py

Bu dosya projenin ana motor kısmını içeriyor.

Burada:

- Tape class
- TMResult
- TMConfiguration
- SingleTapeTM
- MultiTapeTM

gibi yapıları oluşturdum.

Bu kısım:

- YAML dosyalarını okuyor
- transition’ları parse ediyor
- kafa hareketlerini yönetiyor
- şeride yazma işlemlerini yapıyor
- execution history tutuyor
- accept/reject sonucu döndürüyor

En çok zorlandığım kısım transition mantığını doğru kurmaktı. Çok küçük bir transition hatası bile makinenin tamamen bozulmasına neden oluyordu.

---

## visualizer.py

Bu kısım projenin en eğlenceli bölümlerinden biri oldu.

Başta sadece terminal çıktısı vardı fakat daha sonra Turing Machine’in çalışmasını görsel hale getirmek istedim.

Bu sistem:

- PNG frame oluşturuyor
- state bilgisini gösteriyor
- kafa konumunu işaretliyor
- GIF oluşturuyor

Özellikle debugging sırasında çok faydalı oldu çünkü bazı hataları görsel olarak fark etmek terminal çıktısından daha kolaydı.

GIF sistemi eklendikten sonra projenin gerçekten çalışan bir simülatör gibi görünmesi hoşuma gitti.

---

## main.py

Bu dosya kullanıcı arayüzü gibi çalışıyor.

Kullanıcı:

- sistem seçebiliyor
- input verebiliyor
- simülasyonu çalıştırabiliyor
- geçmiş adımları görebiliyor
- GIF oluşturabiliyor

İlk başta çok basit bir terminal çıktısı vardı ama sonradan daha okunabilir hale getirmeye çalıştım.

Ayrıca test süreçlerinde simülasyon sonuçlarını daha okunabilir hale getirmek için terminal çıktılarında küçük iyileştirmeler yaptım.

---

## tests/

Başta test yazmayı çok düşünmüyordum ama proje büyüdükçe testlerin ne kadar önemli olduğunu fark ettim.

Çünkü bazı makineler:

- sonsuz döngüye giriyordu
- yanlış accept veriyordu
- reject olması gereken inputları kabul ediyordu

Bu yüzden pytest kullanarak test sistemi oluşturdum.

Şu anda:

- engine testleri
- machine testleri
- visualizer testleri
- invalid yaml testleri
- timeout testleri
- MultiTapeTM testleri

bulunuyor.

Test sistemi hata ayıklamayı ciddi şekilde kolaylaştırdı.

---

# 3. Geliştirilen Turing Makineleri

## TM-1 · Unary to Binary

Bu makinede unary sayıyı binary sayıya dönüştürmeye çalıştım.

İlk başta direkt dönüşüm yapmaya çalıştım ama transition’lar çok karıştı. Daha sonra işaretleme mantığı kullanarak çözmeye karar verdim.

Makine unary kısmını sürekli tarıyor ve binary çıktıyı oluşturmaya çalışıyor.

En zor kısım kafa hareketlerini doğru ayarlamaktı çünkü bazı durumlarda makine sonsuz döngüye giriyordu.

---

## TM-2 · Binary Compare

Bu makinede `#` sembolüyle ayrılmış iki binary sayıyı karşılaştırdım.

Başta mantık kolay görünüyordu fakat tek şeritli yapıda sürekli iki taraf arasında gidip gelmek oldukça karıştırıcı oldu.

En büyük problem reject durumlarını doğru tasarlamaktı. Bunun nedeninin bazı reject transition’larının eksik olması olduğunu sonradan fark ettim. Test yazarak bu problemi fark ettim.

---

## TM-3 · String Copy

Bu makinenin amacı girdiyi kopyalamaktı.

Örneğin:

```text
abba
```

girdisini:

```text
abba#abba
```

haline getiriyor.

Bu kısımda işaretleme mantığı kullandım. Çünkü hangi karakterin kopyalandığını takip etmek gerekiyordu.

En zorlandığım şey bazı karakterlerin üstüne yanlışlıkla tekrar yazılmasıydı.

---

## TM-4 · Student Choice

Bu kısımda kendi seçtiğim problemi çözmeye çalıştım.

Önce problemi küçük adımlara ayırdım sonra her adım için transition’lar oluşturdum.

Özellikle edge-case inputlarda hata almamak için ekstra testler yazdım.

---

# 4. MultiTapeTM (Bonus)

Projeyi geliştirirken MultiTapeTM kısmını da eklemek istedim çünkü teorik olarak nasıl çalıştığını merak ediyordum.

Başta kolay görünüyordu ama multiple tape yönetmek düşündüğümden daha zor oldu.

Bu yapıda:

- birden fazla tape
- birden fazla head
- multi-read
- multi-write
- multi-move
- transition execution
- transition lookup
- gerçek run loop

sistemi oluşturdum.

Bu kısmı geliştirirken Turing makinelerinin teorik tarafını daha iyi anlamaya başladım.

---

# 5. Visualizer Sistemi (Bonus)

Visualizer sistemi projeye eklediğim en keyifli özelliklerden biri oldu.

Çünkü sadece terminal çıktısı görmek yerine makinenin gerçekten çalışmasını izlemek daha motive ediciydi.

Bu sistem:

- frame oluşturuyor
- tape hücrelerini çiziyor
- kafa konumunu gösteriyor
- state bilgisini yazıyor
- GIF üretiyor

Ayrıca debugging sırasında da çok yardımcı oldu.

Bazı transition hatalarını GIF üzerinden fark etmek daha kolaydı.

---

# 6. Test ve Debug Süreci

Projede en çok zaman alan şey debugging kısmıydı.

Özellikle:

- infinite loop
- yanlış reject
- yanlış accept
- blank symbol problemleri
- kafa hareket hataları

çok sık yaşandı.

Bazı durumlarda tek bir transition yüzünden bütün sistem bozuluyordu.

Bu yüzden pytest kullanarak sürekli test etmeye başladım.

Zamanla test sistemi sayesinde hangi inputlarda hata olduğunu daha hızlı bulabildim.

Şu anda tüm testler başarılı şekilde çalışıyor.

Ayrıca debugging sırasında istenmeyen sonsuz çalışmaları azaltmak için step-limit koruma mekanizmaları ekledim.

Bir diğer geliştirme ise transition davranışlarını analiz ederken execution history yapısını daha okunabilir hale getirmek oldu.

---

# 7. Karmaşıklık Analizi

Çoğu Single Tape TM sürekli şerit üzerinde ileri geri hareket ettiği için yaklaşık olarak:

```text
O(n²)
```

karmaşıklığında çalışıyor.

Student-choice sistem ise daha az tarama yaptığı için yaklaşık:

```text
O(n)
```

davranış gösteriyor.

---

# 8. Bu Projede Öğrendiklerim

Bu projede en çok öğrendiğim şey Turing Machine mantığının teoride göründüğünden çok daha zor uygulanması oldu.

Özellikle:

- transition tasarlama
- kafa hareketlerini yönetme
- debugging
- pytest ile test yazma
- büyük Python projesi düzenleme

konularında ciddi pratik kazandım.

Ayrıca küçük bir transition hatasının bile tüm sistemi bozabileceğini görmek benim için önemli bir deneyimdi.

---

# 9. Sonuç

Bu proje sayesinde Turing makinelerini sadece teorik olarak değil pratik olarak da daha iyi anlamaya başladım.

En tatmin edici kısım GIF sistemiyle makinelerin çalışmasını izlemek oldu.

Başta sadece basit bir simulator düşünüyordum fakat zamanla:

- MultiTapeTM
- visualizer
- test sistemi
- GIF generation

gibi ek özellikler eklenince proje daha gerçek bir simülatöre dönüşmeye başladı.

Her ne kadar debugging kısmı bazen zorlayıcı olsa da proje benim için oldukça öğretici oldu.

***********************************************************

# TuringLab Simulator — Project Report

## Student Information

- Course: Automata Theory and Formal Languages
- Project: Turing Machine Simulator
- Student: Fatma Betül Pehlivan
- Student ID: 233311036

---

# 1. General Overview of the Project

The main goal of this project was developing a simulator that can read Turing Machine definitions from YAML files and execute them step by step.

At the beginning, Turing Machines looked much simpler in theory. However, during the implementation process I realized that managing head movements, building transition logic and preventing infinite loops were much harder than I expected.

As the project progressed, I decided to improve the system instead of keeping it as a very basic simulator. Initially, the project only included a Single Tape Turing Machine structure. Later, I added visualization support, GIF generation, automated testing and MultiTapeTM support.

Currently, the system supports:

- YAML-based system definitions
- Single Tape Turing Machine
- Multi Tape Turing Machine
- Step-by-step execution history
- GIF visualization system
- Automated testing with pytest
- Timeout control
- Input validation
- Accept / Reject states

One of the things I enjoyed most while developing the project was seeing the simulator gradually start to feel like a real working system.

---

# 2. Project Structure

To keep the project more organized, I separated the system into different files.

## tm_engine.py

This file contains the main engine of the project.

Inside this file, I implemented:

- Tape class
- TMResult
- TMConfiguration
- SingleTapeTM
- MultiTapeTM

This part of the system:

- Reads YAML files
- Parses transitions
- Manages head movements
- Handles tape writing operations
- Stores execution history
- Returns accept/reject results

The part I struggled with the most was designing transitions correctly. Even a very small transition mistake could completely break the entire machine.

---

## visualizer.py

This became one of the most enjoyable parts of the project.

At first, the simulator only displayed terminal outputs. Later, I wanted to visualize how the Turing Machine was working.

This system:

- Creates PNG frames
- Displays state information
- Highlights head positions
- Generates GIF animations

It became especially useful during debugging because some errors were easier to notice visually than through terminal outputs.

After adding the GIF system, I liked how the project started to look like a real simulator.

---

## main.py

This file works like the user interface of the project.

The user can:

- Select a system
- Enter input
- Run simulations
- View execution history
- Generate GIF animations

Initially, the terminal output was very simple, but later I tried to make it more readable and user-friendly.

I also improved some terminal outputs to make simulation results easier to read during testing.

---

## tests/

At first, I did not think much about writing tests. However, as the project became larger, I realized how important testing actually is.

Some machines were:

- Entering infinite loops
- Producing incorrect accepts
- Accepting inputs that should be rejected

Because of this, I created a testing system using pytest.

Currently, the project contains:

- Engine tests
- Machine tests
- Visualizer tests
- Invalid YAML tests
- Timeout tests
- MultiTapeTM tests

The testing system made debugging significantly easier.

---

# 3. Implemented Turing Machines

## TM-1 · Unary to Binary

In this machine, I tried to convert unary numbers into binary numbers.

At first, I attempted to directly transform the symbols, but the transitions became too complicated. Later, I decided to use a marking-based strategy.

The machine continuously scans the unary section and gradually generates the binary output.

The most difficult part was managing head movements correctly because the machine sometimes entered infinite loops.

---

## TM-2 · Binary Compare

In this machine, I compared two binary numbers separated by the `#` symbol.

At first, the logic seemed simple, but moving back and forth between both sides on a single tape became confusing.

The biggest issue was designing reject states correctly. Later, I realized that some reject transitions were missing, which caused the machine to incorrectly accept certain inputs. Writing tests helped me detect this issue.

---

## TM-3 · String Copy

The goal of this machine was copying the input string.

For example:

```text
abba
```

becomes:

```text
abba#abba
```

I used a marking strategy because it was necessary to track which characters had already been copied.

The most difficult issue was accidentally overwriting symbols during copying.

---

## TM-4 · Student Choice

In this section, I tried solving a custom problem of my own choice.

First, I divided the problem into smaller steps and then designed transitions for each step.

I also added extra tests to handle edge-case inputs correctly.

---

# 4. MultiTapeTM (Bonus)

While improving the project, I wanted to implement the MultiTapeTM structure because I was curious about how multi-tape systems work theoretically.

At first it looked easy, but managing multiple tapes became harder than I expected.

This structure includes:

- Multiple tapes
- Multiple heads
- Multi-read
- Multi-write
- Multi-move
- Transition execution
- Transition lookup
- Real execution loop

Working on this part helped me better understand the theoretical side of Turing Machines.

---

# 5. Visualizer System (Bonus)

The visualizer system became one of the most enjoyable features I added to the project.

Instead of only seeing terminal outputs, it was much more motivating to watch the machine actually work visually.

This system:

- Creates frames
- Draws tape cells
- Shows head positions
- Displays state information
- Generates GIF outputs

It also became very helpful during debugging.

Some transition problems were easier to notice through GIF animations.

---

# 6. Testing and Debugging Process

The debugging process was the most time-consuming part of the project.

Especially:

- Infinite loops
- Incorrect rejects
- Incorrect accepts
- Blank symbol problems
- Head movement errors

appeared frequently.

Sometimes a single incorrect transition could completely break the entire system.

Because of this, I continuously tested the machines using pytest.

Over time, the testing system helped me identify problematic inputs much faster.

Currently, all tests pass successfully.

I also added step-limit protection mechanisms to reduce the risk of unintended infinite execution during debugging.

Another improvement was making execution history easier to inspect while analyzing transition behavior.

---

# 7. Complexity Analysis

Most Single Tape Turing Machines repeatedly move back and forth on the tape, so their complexity is approximately:

```text
O(n²)
```

The student-choice system behaves closer to:

```text
O(n)
```

because it performs fewer repeated scans.

---

# 8. What I Learned From This Project

The most important thing I learned from this project is that Turing Machine logic is much harder to implement in practice than it initially appears in theory.

I gained significant experience in:

- Designing transitions
- Managing head movements
- Debugging
- Writing tests with pytest
- Organizing larger Python projects

I also realized how a very small transition mistake can completely break the entire system.

---

# 9. Conclusion

This project helped me understand Turing Machines not only theoretically but also practically.

The most satisfying part was watching the machines execute through the GIF visualization system.

Initially, I only planned to create a simple simulator, but over time I added:

- MultiTapeTM
- Visualizer
- Testing system
- GIF generation

which made the project feel more like a real simulator.

Even though the debugging process was sometimes difficult, the project became a very valuable learning experience for me.

---

## Personal Reflection / Kişisel Değerlendirme

This project significantly improved my understanding of automata theory, state transitions, and computational simulation systems.

Working on visualization, debugging, and MultiTapeTM support helped me better understand how theoretical computer science concepts can be transformed into real software applications.

Bu proje otomata teorisi, state transition yapıları ve hesaplama simülasyon sistemleri hakkındaki anlayışımı önemli ölçüde geliştirdi.

Özellikle görselleştirme sistemi, debugging süreçleri ve MultiTapeTM desteği üzerinde çalışmak; teorik bilgisayar bilimi kavramlarının gerçek yazılım sistemlerine nasıl dönüştürülebileceğini daha iyi anlamamı sağladı.


