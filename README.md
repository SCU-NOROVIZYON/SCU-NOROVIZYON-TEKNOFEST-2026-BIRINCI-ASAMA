# SCU-NOROVIZYON-TEKNOFEST-2026-BIRINCI-ASAMA
## Genetic Variant Classification System 🧬
#### TEKNOFEST 2026 – Sağlıkta Yapay Zeka Yarışması

Bu repository, genetik varyantların patogenic (zararlı) veya benign (zararsız) olarak sınıflandırılması için geliştirilmiş uçtan uca bir makine öğrenmesi sistemini içermektedir.

Proje, TEKNOFEST Sağlıkta Yapay Zeka Yarışması kapsamında geliştirilmiştir.


### 🎯 Proje Amacı

Bu çalışmanın amacı, genomik varyantların klinik etkilerini otomatik olarak tahmin edebilen, genelleme gücü yüksek ve açıklanabilir bir model geliştirmektir.

Sistem, farklı gen panelleri üzerinde çalışabilecek şekilde tasarlanmış ve hem performans hem de klinik güvenilirlik dikkate alınmıştır.


### 📊 Veri Kaynakları

Projede kullanılan temel veri kaynakları:

ClinVar
→ Varyantların klinik etiketleri (benign / pathogenic)
Landrum, M. J., et al. ClinVar: improving access to variant interpretations and supporting evidence. Nucleic Acids Research, 2018.
https://www.ncbi.nlm.nih.gov/clinvar/
dbNSFP
→ Fonksiyonel skorlar ve öznitelikler
Liu, X., et al. dbNSFP v4: a comprehensive database of functional predictions and annotations for human nonsynonymous variants. Human Mutation, 2020
https://www.dbnsfp.org/


### ⚙️ Pipeline Özeti

Proje aşağıdaki adımlardan oluşmaktadır:

#### 1. Veri Toplama
ClinVar’dan varyant ve etiketler
dbNSFP’den öznitelikler
#### 2. Feature Engineering
Skorların istatistiksel özetleri (mean, std, max vb.)
Eksik veri düzenleme
#### 3. Panel Bazlı Veri Seti Oluşturma
Gen bazlı ayrım
Farklı panel senaryoları
#### 4. Train / Test Split
Data leakage önlemek için gen bazlı ayrım
Varyant bazlı ayrım
#### 5. Threshold Optimizasyonu
F1 skorunu maksimize eden eşik belirleme
#### 6. Model Eğitimi
Farklı algoritmalar ile eğitim
#### 7. Değerlendirme ve Açıklanabilirlik
ROC-AUC, PR-AUC, F1, Balanced Accuracy
Sensitivity / Specificity
SHAP analizleri


### 📁 Klasör Yapısı

├── threshold_results/
├── source_codes/
├── experiment_results/


### 📈 Çıktılar
Model performans metrikleri
Threshold optimizasyon sonuçları
SHAP açıklanabilirlik grafikleri
Eğitilmiş model dosyaları (.pkl)


### 🧠 Kullanılan Yaklaşım
Panel bazlı öğrenme yaklaşımı
Farklı öznitelik grupları (full / meta / pure)
Threshold tuning ile klinik risk optimizasyonu
Açıklanabilir yapay zeka (XAI)


### 👥 Takım

Bu proje 3 kişilik bir ekip tarafından geliştirilmiştir:
#### Beyza Nur KARATAĞ
#### Alperen İLHAN
#### Muhammed Mustafa KİLCAROĞLU

### 📌 Notlar
Bu proje araştırma ve yarışma kapsamında geliştirilmiştir. Klinik tanı, tedavi veya hasta yönetimi süreçlerinde kullanılması kesinlikle önerilmez ve bu amaçla kullanılmamalıdır. Bu tür kullanımlardan doğabilecek sonuçlardan geliştiriciler sorumlu değildir.
Veri kaynakları ilgili platformların kullanım şartlarına tabidir.
