from fastapi import FastAPI

app = FastAPI()

# Danh sách sinh viên mẫu
students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]

# 1. Endpoint đúng: /students
# 2. Tên hàm rõ nghĩa: get_all_students (Lấy toàn bộ sinh viên)
@app.get("/students")
def get_all_students():
    # 3. Trả về TOÀN BỘ danh sách students thay vì chỉ trả về students[0]
    return students