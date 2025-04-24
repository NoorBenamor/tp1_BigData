# TP1 - Big Data: PubMed Scraping 

مشروع يتمثل في **جمع وتحليل بيانات من موقع PubMed** باستخدام تقنيات Web Scraping.  
يهدف المشروع إلى استخراج معلومات من المقالات الطبية والعلمية (مثل العنوان، المؤلفين، المجلة، السنة...) وتحليلها .

---

##  فكرة المشروع

يقوم السكريبت بجمع بيانات من موقع [PubMed](https://pubmed.ncbi.nlm.nih.gov/) ثم يحفظ النتائج بصيغة CSV لتحليلها لاحقًا.

---

## المكتبات المستخدمة

- مكتبة `requests` لجلب الصفحات
- مكتبة `BeautifulSoup` لتحليل محتوى HTML
- مكتبة `pandas` لمعالجة البيانات وتخزينها
- مكتبة `time` و `random` للتحكم والتنسيق

---

## هيكل المشروع
tp1_BigData/ ├── big_data.py # السكريبت الرئيسي لحساب Word Count └── pubmed_articles.csv 

## نتائج
يحتوي على اكثر من 20 الف سطر
![scraping](https://github.com/user-attachments/assets/309da9ce-6951-41b9-ad95-3d968e6490e0)

![scraping](https://github.com/user-attachments/assets/a39718b0-bbf7-4f1e-85da-71814c136022)




