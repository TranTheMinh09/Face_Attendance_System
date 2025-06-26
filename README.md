# 📸 Face Attendance System

Hệ thống chấm công bằng nhận diện khuôn mặt, sử dụng Python, OpenCV và thư viện `face_recognition`.

---

## 📂 Cấu trúc thư mục

```
FACE_ATTENDANCE/
├── dataset/               # Lưu ảnh khuôn mặt đã thu thập
├── encodings/             # Lưu các mã hóa khuôn mặt (.pkl)
├── logs/                  # Lưu file log chấm công (ngày, giờ)
├── capture_faces.py       # Thu thập khuôn mặt từ webcam
├── encode_faces.py        # Mã hóa khuôn mặt thành vectors
├── recognize_and_log.py   # Nhận diện và ghi log chấm công
├── requirements.txt       # Danh sách thư viện cần cài đặt
├── .gitignore             # Bỏ qua file không cần theo dõi
└── README.md              # File mô tả dự án
```

---

## ⚙️ Cài đặt

```bash
git clone https://github.com/TranTheMinh09/Face_Attendance_System.git
cd face_attendance
pip install -r requirements.txt
```

💡 **Khuyến khích sử dụng virtualenv:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🚀 Hướng dẫn sử dụng

### 1. Thu thập khuôn mặt

```bash
python capture_faces.py
```

- Hệ thống sẽ chụp nhiều ảnh từ webcam và lưu vào `dataset/`.

---

### 2. Mã hóa khuôn mặt

```bash
python encode_faces.py
```

- Mã hóa ảnh thành vectors và lưu vào `encodings/`.

---

### 3. Nhận diện và ghi log chấm công

```bash
python recognize_and_log.py
```

- Hệ thống nhận diện khuôn mặt và ghi log vào `logs/`.

---

## 📦 Thư viện sử dụng

- `opencv-python`
- `face_recognition`
- `numpy`
- `pickle`
- `datetime`

> Tất cả thư viện cần thiết đã được liệt kê trong `requirements.txt`.

---

## 🧠 Mục tiêu dự án

- Ứng dụng kiến thức AI + Computer Vision vào thực tế
- Xây dựng hệ thống chấm công tự động đơn giản
- Củng cố kỹ năng Python, xử lý ảnh và làm việc với Git

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
