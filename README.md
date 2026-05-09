# TuringLab Simulator

Otomata Teorisi ve Biçimsel Diller dersi kapsamında geliştirdiğim bir Turing Machine simulator projesi.

Bu projeyi geliştirirken amacım Turing makinelerini sadece teorik olarak değil, pratik olarak da daha iyi anlamaktı. Başta Turing makineleri kağıt üzerinde oldukça basit görünüyordu fakat transition mantığını kurmak, kafa hareketlerini yönetmek ve sonsuz döngüleri çözmek düşündüğümden daha zor oldu.

Projeyi geliştirirken sistemi adım adım büyüttüm. İlk başta yalnızca basit bir Single Tape simulator vardı. Daha sonra görselleştirme sistemi, GIF üretimi, test sistemi ve MultiTapeTM desteği ekledim. Zamanla proje küçük bir terminal uygulamasından daha gerçek bir simülatöre dönüşmeye başladı.

---

# Özellikler

Şu anda proje şunları destekliyor:

- YAML tabanlı Turing Machine tanımları
- Single Tape Turing Machine
- Multi Tape Turing Machine (Bonus)
- Step-by-step execution history
- GIF görselleştirme sistemi (Bonus)
- PNG frame üretimi
- Pytest ile otomatik testler
- Timeout kontrolü
- Input validation
- Accept / Reject durumları
- Verbose execution modu

---

# Proje Yapısı

```text
turinglab/
│
├── README.md
├── REPORT.md
├── requirements.txt
│
├── tm_engine.py
├── visualizer.py
├── main.py
│
├── machines/
│   ├── binary_compare.yaml
│   ├── binary_increment.yaml
│   ├── string_copy.yaml
│   ├── student_choice.yaml
│   ├── unary_to_binary.yaml
│   └── unary_zero_checker.yaml
│
├── tests/
│   ├── test_tm_engine.py
│   ├── test_machines.py
│   └── test_visualizer.py
│
└── docs/
    └── images/
        ├── frame_1.png
        ├── frame_2.png
        ├── frame_3.png
        ├── frame_4.png
        └── tm.gif
```

---

# Geliştirilen Turing Makineleri

## TM-1 · Unary to Binary

Unary sayıları binary biçime dönüştürür.

### Örnek

```text
111 → 11
```

---

## TM-2 · Binary Compare

`#` sembolüyle ayrılmış iki binary sayıyı karşılaştırır.

### Örnek

```text
1011#1100
```

Makine ilk binary sayının ikinci sayıdan büyük olup olmadığını kontrol eder.

---

## TM-3 · String Copy

Girdiyi ayırıcı sembolden sonra tekrar kopyalar.

### Örnek

```text
abba → abba#abba
```

---

## TM-4 · Student Choice

Proje gereksinimlerine uygun şekilde geliştirdiğim özel Turing Machine.

---

# MultiTapeTM (Bonus)

Projede geliştirdiğim bonus özelliklerden biri MultiTape Turing Machine yapısı oldu.

Başta oldukça kolay görünüyordu fakat birden fazla tape ve birden fazla head yönetmek düşündüğümden daha karmaşık hale geldi.

Bu yapı içinde:

- Multiple tape desteği
- Multiple head movement
- Multi-read işlemleri
- Multi-write işlemleri
- Transition execution
- Transition lookup
- Gerçek execution loop

sistemlerini geliştirdim.

Bu kısmı geliştirirken multi-tape makinelerin teorik olarak neden daha güçlü olduğunu daha iyi anlamaya başladım.

---

# Visualizer Sistemi (Bonus)

Projeye eklediğim en keyifli özelliklerden biri visualizer sistemi oldu.

Visualizer sistemi:

- PNG frame oluşturuyor
- Tape hücrelerini gösteriyor
- Head konumunu işaretliyor
- Current state bilgisini gösteriyor
- GIF animasyonları oluşturuyor

Bu özellik debugging sırasında da oldukça faydalı oldu çünkü kafa hareketlerini görsel olarak incelemek transition hatalarını fark etmeyi kolaylaştırdı.

Üretilen çıktılar:

```text
docs/images/
```

klasörüne kaydediliyor.

Örnek GIF çıktısı:

```text
docs/images/tm.gif
```

---

# Kurulum

Repository klonlama:

```bash
git clone <repository-url>
```

Gerekli paketleri yükleme:

```bash
pip install -r requirements.txt
```

---

# Simülatörü Çalıştırma

Ana programı çalıştırma:

```bash
python main.py
```

Program şunları yapabiliyor:

- Machine seçimi
- Input girişi
- Simülasyon çalıştırma
- Execution history görüntüleme
- GIF oluşturma

---

# Testleri Çalıştırma

Tüm testleri çalıştırma:

```bash
pytest
```

Projede şu testler bulunuyor:

- TM engine testleri
- Machine davranış testleri
- Visualizer testleri
- Edge-case testleri
- Invalid input testleri
- Timeout testleri
- MultiTapeTM testleri

---

# Örnek Çıktı

Örnek verbose execution çıktısı:

```text
Step 0 | State: q0 | Tape: [1]011B
Step 1 | State: q0 | Tape: 1[0]11B
Step 2 | State: q0 | Tape: 10[1]1B
```

---

# Geliştirme Süreci

Projede en çok zorlandığım kısım transition ve kafa hareketlerini debug etmek oldu.

Geliştirme sırasında sık yaşanan problemler:

- Infinite loop
- Yanlış accept
- Yanlış reject
- Eksik transition
- Blank symbol problemleri
- Tape üstüne yanlış yazma problemleri

Bazı durumlarda tek bir transition hatası bütün sistemin bozulmasına neden oluyordu.

Bu yüzden pytest ile test yazmak proje ilerledikçe çok önemli hale geldi.

Projede fark ettiğim şeylerden biri de Turing makinelerinin teoride göründüğünden çok daha zor uygulanması oldu.

---

# Projede Bulunan Dosyalar

Projede bulunan ana dosyalar:

- `tm_engine.py`
- `visualizer.py`
- `main.py`
- `machines/*.yaml`
- `tests/*.py`
- `REPORT.md`
- `docs/design_notes.md`

---

# Kullanılan Teknolojiler

- Python
- PyYAML
- pytest
- Pillow
- imageio
- colorama

---

# Sonuç

Bu proje sayesinde computation modellerini, automata sistemlerini ve simulator tasarımını pratik açıdan daha iyi anlamaya başladım.

Başta yalnızca küçük bir simulator geliştirmeyi planlıyordum fakat zamanla sistem:

- test desteği
- görselleştirme
- GIF üretimi
- MultiTapeTM desteği

gibi özelliklerle daha kapsamlı bir projeye dönüştü.

Her ne kadar debugging süreci bazen yorucu olsa da proje benim için oldukça öğretici ve faydalı bir deneyim oldu.

*****************************************************************

# TuringLab Simulator

This project is a Turing Machine simulator developed for the Theory of Computation and Formal Languages course.

While developing this project, my main goal was to understand Turing Machines not only theoretically but also practically. At first, Turing Machines looked simple on paper, but implementing transition logic, handling head movements, and debugging infinite loops became much harder than I expected.

I improved the project step by step during development. Initially, there was only a basic Single Tape simulator. Later, I added visualization support, GIF generation, automated tests, and MultiTapeTM support. Over time, the project evolved from a small terminal application into a more complete simulator system.

---

# Features

Currently, the project supports:

- YAML-based Turing Machine definitions
- Single Tape Turing Machine
- Multi Tape Turing Machine (Bonus)
- Step-by-step execution history
- GIF visualization system (Bonus)
- PNG frame generation
- Automated testing with pytest
- Timeout control
- Input validation
- Accept / Reject states
- Verbose execution mode

---

# Project Structure

```text
turinglab/
│
├── README.md
├── REPORT.md
├── requirements.txt
│
├── tm_engine.py
├── visualizer.py
├── main.py
│
├── machines/
│   ├── binary_compare.yaml
│   ├── binary_increment.yaml
│   ├── string_copy.yaml
│   ├── student_choice.yaml
│   ├── unary_to_binary.yaml
│   └── unary_zero_checker.yaml
│
├── tests/
│   ├── test_tm_engine.py
│   ├── test_machines.py
│   └── test_visualizer.py
│
└── docs/
    ├── design_notes.md
    └── images/
        ├── frame_1.png
        ├── ...
        ├── frame_12.png
        └── tm.gif
```

# Implemented Turing Machines

## TM-1 · Unary to Binary

Converts unary numbers into binary representation.

### Example

```text
111 → 11
```

---

## TM-2 · Binary Compare

Compares two binary numbers separated by the `#` symbol.

### Example

```text
1011#1100
```

The machine checks whether the first binary number is greater than the second one.

---

## TM-3 · String Copy

Copies the input string after a separator symbol.

### Example

```text
abba → abba#abba
```

---

## TM-4 · Student Choice

A custom Turing Machine developed according to the project requirements.

---

# MultiTapeTM (Bonus)

One of the bonus features I developed in this project was the MultiTape Turing Machine structure.

At first, it looked relatively simple, but managing multiple tapes and multiple heads became much more complicated than I expected.

In this structure, I implemented:

- Multiple tape support
- Multiple head movement
- Multi-read operations
- Multi-write operations
- Transition execution
- Transition lookup
- Real execution loop

While developing this part, I started understanding more clearly why multi-tape machines are theoretically more powerful.

---

# Visualizer System (Bonus)

One of the most enjoyable parts of the project was implementing the visualizer system.

The visualizer system:

- Generates PNG frames
- Displays tape cells
- Marks head positions
- Shows current state information
- Creates GIF animations

This feature also became very useful during debugging because visualizing head movements made it easier to detect transition errors.

Generated outputs are saved inside:

```text
docs/images/
```

Example GIF output:

```text
docs/images/tm.gif
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

# Running the Simulator

Run the main program:

```bash
python main.py
```

The program supports:

- Machine selection
- Input handling
- Simulation execution
- Execution history display
- GIF generation

---

# Running Tests

Run all tests:

```bash
pytest
```

The project includes:

- TM engine tests
- Machine behavior tests
- Visualizer tests
- Edge-case tests
- Invalid input tests
- Timeout tests
- MultiTapeTM tests

---

# Example Output

Example verbose execution output:

```text
Step 0 | State: q0 | Tape: [1]011B
Step 1 | State: q0 | Tape: 1[0]11B
Step 2 | State: q0 | Tape: 10[1]1B
```

---

# Development Process

The most difficult part of the project was debugging transitions and head movements.

Common problems encountered during development:

- Infinite loops
- Incorrect accept states
- Incorrect reject states
- Missing transitions
- Blank symbol issues
- Incorrect tape writing operations

In some cases, even a single transition mistake caused the entire system to fail.

Because of this, writing automated tests with pytest became increasingly important as the project grew.

One of the things I realized during development was that implementing Turing Machines in practice is much more difficult than it appears in theory.

---

# Project Files

Main project files:

- `tm_engine.py`
- `visualizer.py`
- `main.py`
- `machines/*.yaml`
- `tests/*.py`
- `REPORT.md`
- `docs/design_notes.md`

---

# Technologies Used

- Python
- PyYAML
- pytest
- Pillow
- imageio
- colorama

---

# Conclusion

This project helped me better understand computational models, automata systems, and simulator design from a practical perspective.

Initially, I only planned to develop a small simulator, but over time the system evolved into a larger project with:

- automated testing support
- visualization
- GIF generation
- MultiTapeTM support

Although debugging was sometimes challenging, the project became a very educational and valuable experience for me.


---

## Future Improvements / Gelecek Geliştirmeler

- Better GUI visualization system / Daha gelişmiş görselleştirme sistemi
- More optimized TM execution / Daha optimize TM çalıştırma sistemi
- Additional MultiTapeTM examples / Ek MultiTapeTM örnekleri
- Nondeterministic TM support / Non-deterministic TM desteği
- Interactive web interface / Etkileşimli web arayüzü


- Command line usability improvements / Komut satırı kullanım geliştirmeleri

