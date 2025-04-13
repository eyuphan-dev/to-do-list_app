# To-Do List App 📝

Basit ama işlevsel bir Django tabanlı yapılacaklar listesi uygulaması.

## 🔍 Proje Hakkında

Bu proje, kullanıcıların görevlerini ekleyip, güncelleyip, silebildiği klasik bir CRUD (Create, Read, Update, Delete) yapısı üzerine kurulmuştur. Django framework’ü ile geliştirilen backend, HTML ve CSS ile desteklenen basit bir frontend arayüzü sunar.

## 🚀 Özellikler

- ✅ Görev ekleme
- ✏️ Görev güncelleme
- 🗑️ Görev silme
- 📋 Tüm görevleri listeleme

## 🛠 Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyebilirsin:

```bash
git clone https://github.com/eyuphan_dev/to-do-list_app.git
cd to-do-list_app
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
