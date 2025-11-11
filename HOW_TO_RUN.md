# =========================================================================
# Scripts Guide - كيفية تشغيل المشروع
# =========================================================================

## 🟢 للتطوير المحلي (Local Development):

### Windows:
```cmd
run_local.bat
```

### أو يدوياً:
```cmd
set DJANGO_SETTINGS_MODULE=config.settings_local
env\Scripts\python.exe manage.py runserver
```

**الإعدادات:**
- ✅ Database: SQLite (db.sqlite3)
- ✅ Static Files: مجلد محلي (staticfiles/)
- ✅ Media Files: مجلد محلي (media/)
- ✅ لا يحتاج اتصال بالإنترنت
- ✅ سريع للتجربة والتطوير

---

## 🔵 للإنتاج مع AWS (Production with AWS):

### Windows:
```cmd
run_aws.bat
```

### أو يدوياً:
```cmd
set DJANGO_SETTINGS_MODULE=config.settings
env\Scripts\python.exe manage.py runserver
```

**الإعدادات:**
- ✅ Database: PostgreSQL (AWS RDS)
- ✅ Static Files: Amazon S3
- ✅ Media Files: Amazon S3
- ✅ يحتاج اتصال بالإنترنت
- ✅ جاهز للنشر (deployment)

---

## 📋 أوامر مفيدة:

### عمل migrations للقاعدة المحلية:
```cmd
set DJANGO_SETTINGS_MODULE=config.settings_local
env\Scripts\python.exe manage.py makemigrations
env\Scripts\python.exe manage.py migrate
```

### إنشاء superuser للقاعدة المحلية:
```cmd
set DJANGO_SETTINGS_MODULE=config.settings_local
env\Scripts\python.exe manage.py createsuperuser
```

### جمع الملفات الثابتة (Static files):

**للتطوير المحلي:**
```cmd
set DJANGO_SETTINGS_MODULE=config.settings_local
env\Scripts\python.exe manage.py collectstatic
```

**لـ AWS S3:**
```cmd
set DJANGO_SETTINGS_MODULE=config.settings
env\Scripts\python.exe manage.py collectstatic
```

---

## ⚙️ الفروقات بين الإعدادات:

| **الميزة** | **settings_local.py** | **settings.py** |
|------------|----------------------|-----------------|
| Database | SQLite | PostgreSQL (AWS RDS) |
| Static Files | Local folder | Amazon S3 |
| Media Files | Local folder | Amazon S3 |
| AWS Required | ❌ لا | ✅ نعم |
| Internet | ❌ لا | ✅ نعم |
| Speed | ⚡ سريع جداً | 🌐 يعتمد على الإنترنت |
| Use Case | التطوير والتجربة | الإنتاج والنشر |

---

## 🔄 التبديل بين الإعدادات:

**ملاحظة مهمة:** لازم تعيد تشغيل السيرفر بعد تغيير الإعدادات!

1. أوقف السيرفر الحالي (Ctrl+C)
2. شغل الـ script المناسب
3. السيرفر هيشتغل بالإعدادات الجديدة

---

## 📝 ملاحظات:

- ملف `settings.py` = للإنتاج مع AWS
- ملف `settings_local.py` = للتطوير المحلي
- البيانات **لا تتشارك** بين القاعدتين (كل واحدة منفصلة)
- الصور المرفوعة محلياً **لن تظهر** على AWS والعكس صحيح
