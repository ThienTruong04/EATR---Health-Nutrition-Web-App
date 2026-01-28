# 📱 Deploy EATR to Google Play Store & Android

Hướng dẫn chi tiết để đưa ứng dụng EATR lên Android và Google Play Store.

## 🎯 Các Phương Án Deploy

### Phương Án 1: PWA (Progressive Web App) - **ĐỀ XUẤT CHO BẮT ĐẦU**

**Ưu điểm:**

- ✅ Đơn giản nhất, không cần viết lại code
- ✅ Hoạt động trên mọi platform (Android, iOS, Desktop)
- ✅ Có thể cài đặt như native app
- ✅ Offline support
- ✅ Push notifications

**Nhược điểm:**

- ⚠️ Không thể submit lên Google Play Store trực tiếp (cần wrapper)
- ⚠️ Giới hạn truy cập một số tính năng native

### Phương Án 2: Capacitor + PWA - **TỐT NHẤT**

**Ưu điểm:**

- ✅ Wrap web app thành native Android app
- ✅ Submit được lên Google Play Store
- ✅ Truy cập được native features (camera, GPS, etc.)
- ✅ Giữ nguyên code web hiện tại

**Nhược điểm:**

- ⚠️ Cần học thêm Capacitor (không nhiều)
- ⚠️ File APK lớn hơn native app

### Phương Án 3: React Native hoặc Flutter

**Ưu điểm:**

- ✅ Performance tốt nhất
- ✅ Native look & feel
- ✅ Submit lên cả Google Play & App Store

**Nhược điểm:**

- ❌ Phải viết lại toàn bộ frontend
- ❌ Học curve cao hơn

---

## 🚀 HƯỚNG DẪN: Phương Án 2 (Capacitor) - RECOMMENDED

### Bước 1: Chuẩn Bị

```bash
# Install Node.js (nếu chưa có)
# Download từ: https://nodejs.org/

# Install Capacitor CLI
npm install -g @capacitor/cli
```

### Bước 2: Thêm PWA Features vào Flask App

**Tạo file `manifest.json`:**

```json
{
  "name": "EATR - Health & Nutrition",
  "short_name": "EATR",
  "description": "Your personal culinary companion",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#10b981",
  "icons": [
    {
      "src": "/static/images/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/static/images/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

**Tạo Service Worker `sw.js`:**

```javascript
const CACHE_NAME = 'eatr-v1';
const urlsToCache = [
  '/',
  '/static/css/style.css',
  '/static/css/responsive.css',
  '/static/js/app.js',
  '/static/js/charts.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});
```

### Bước 3: Initialize Capacitor Project

```bash
cd C:\Users\duc90\.gemini\antigravity\scratch\eatr-health-app

# Initialize Capacitor
npm init -y
npm install @capacitor/core @capacitor/cli
npx cap init "EATR" "com.eatr.healthapp" --web-dir="static"

# Add Android platform
npm install @capacitor/android
npx cap add android
```

### Bước 4: Configure Backend API

**Cập nhật Flask để serve API cho mobile:**

```python
# app.py - Add CORS support
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for mobile app
```

**Install Flask-CORS:**

```bash
pip install flask-cors
```

### Bước 5: Build Android App

```bash
# Sync web files to Android
npx cap sync android

# Open Android Studio
npx cap open android
```

**Trong Android Studio:**

1. Wait for Gradle build to finish
2. Click **Build > Build Bundle(s) / APK(s) > Build APK(s)**
3. APK file sẽ được tạo tại: `android/app/build/outputs/apk/debug/app-debug.apk`

### Bước 6: Test APK

```bash
# Install APK trên Android device hoặc emulator
adb install android/app/build/outputs/apk/debug/app-debug.apk
```

### Bước 7: Deploy Backend lên Cloud

**Tùy chọn hosting:**

**A. Heroku (Free tier):**

```bash
# Install Heroku CLI
# Tạo file Procfile:
web: gunicorn app:app

# Deploy:
heroku create eatr-health-app
git push heroku main
```

**B. PythonAnywhere (Free):**

- Upload code lên pythonanywhere.com
- Configure WSGI file
- Free subdomain: `yourname.pythonanywhere.com`

**C. Google Cloud Platform / AWS:**

- Professional deployment
- Auto-scaling
- Cost: ~$5-20/month

### Bước 8: Update API Endpoint trong Mobile App

```javascript
// capacitor.config.json
{
  "appId": "com.eatr.healthapp",
  "appName": "EATR",
  "server": {
    "url": "https://your-backend-url.herokuapp.com",
    "cleartext": true
  }
}
```

### Bước 9: Build Release APK cho Google Play

```bash
# Generate signing key
keytool -genkey -v -keystore eatr-release-key.keystore -alias eatr -keyalg RSA -keysize 2048 -validity 10000

# Build release APK
cd android
./gradlew assembleRelease

# APK tại: android/app/build/outputs/apk/release/app-release.apk
```

### Bước 10: Submit lên Google Play Store

1. **Tạo Google Play Developer Account**
   - Phí: $25 (1 lần, trọn đời)
   - Link: <https://play.google.com/console>

2. **Prepare Assets:**
   - Icon: 512x512px
   - Feature Graphic: 1024x500px
   - Screenshots: ít nhất 2 cái (phone + tablet)
   - Privacy Policy URL
   - App description

3. **Upload APK:**
   - Go to Google Play Console
   - Create new app
   - Upload APK/AAB
   - Fill out store listing
   - Submit for review

4. **Review Process:**
   - Thường mất 1-7 ngày
   - Google sẽ test app

---

## 📋 Checklist Trước Khi Deploy

- [ ] Backend deployed lên cloud
- [ ] Database production-ready (không dùng SQLite)
- [ ] API endpoints hoạt động
- [ ] HTTPS enabled
- [ ] Privacy Policy page
- [ ] Terms of Service (nếu cần)
- [ ] App icons (192x192, 512x512)
- [ ] Screenshots (ít nhất 2)
- [ ] Feature graphic (1024x500)
- [ ] App tested on real Android device
- [ ] Permissions declared trong AndroidManifest.xml

---

## 🔧 Troubleshooting

**Lỗi "net::ERR_CLEARTEXT_NOT_PERMITTED":**

```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<application
    android:usesCleartextTraffic="true">
```

**Backend không connect từ mobile:**

- Đảm bảo Flask chạy với `host='0.0.0.0'`
- Check firewall
- Use ngrok để test: `ngrok http 5000`

**APK quá lớn:**

```bash
# Enable ProGuard minification
# android/app/build.gradle
buildTypes {
    release {
        minifyEnabled true
        shrinkResources true
    }
}
```

---

## 💡 Lộ Trình Đề Xuất

### Phase 1: Test Local (1-2 ngày)

1. Cài Capacitor
2. Build APK debug
3. Test trên device

### Phase 2: Deploy Backend (1 ngày)

1. Deploy Flask lên Heroku/Railway
2. Migrate SQLite → PostgreSQL
3. Test API endpoints

### Phase 3: Production Build (1 ngày)

1. Create release APK
2. Generate signing key
3. Test release build

### Phase 4: Google Play (3-7 ngày)

1. Create Play Console account
2. Prepare assets
3. Submit app
4. Wait for review

**Tổng thời gian: ~1-2 tuần**

---

## 📚 Resources

- **Capacitor Docs:** <https://capacitorjs.com/docs>
- **Google Play Console:** <https://play.google.com/console>
- **Icon Generator:** <https://www.appicon.co/>
- **Heroku Deployment:** <https://www.heroku.com/>
- **Flask PWA Tutorial:** <https://blog.miguelgrinberg.com/post/building-a-pwa-with-flask>

---

## 🆘 Cần Giúp Đỡ?

Nếu bạn muốn tôi giúp implement bất kỳ bước nào, hãy cho tôi biết:

- Tạo PWA manifest & service worker
- Setup Capacitor project
- Deploy backend lên Heroku
- Tạo app icons
- Write Privacy Policy

Tôi sẵn sàng hỗ trợ! 🚀
