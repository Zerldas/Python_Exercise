from abc import ABC, abstractmethod
import datetime as date

# Lớp Person là một lớp cơ sở trừu tượng cho tất cả các loại nhân viên.
class Person(ABC):
    # Thuộc tính private, sử dụng __ để "name mangling", tránh bị ghi đè ở lớp con.
    _base_salary = 2000.0 # Lương cơ bản chung
    _age = 0
    # Phương thức khởi tạo (constructor) của lớp.
    def __init__(self, id_person, first_name, last_name, birth, email):
        self.id = id_person
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth 
        self.email = email

    # --- ID ---
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_person):
        self._id = id_person

    # --- First Name ---
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name.strip(): 
            raise ValueError("Tên không được để trống")
        self._first_name = first_name

    # --- Last Name ---
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if not last_name.strip(): # Kiểm tra họ không được để trống
            raise ValueError("Họ không được để trống")
        self._last_name = last_name

    # --- Birth Date ---
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        # Chuẩn hóa kiểu dữ liệu về datetime.date nếu nó là datetime.datetime
        if isinstance(birth, date.datetime):
            birth = birth.date()
        if not isinstance(birth, date.date):
            raise TypeError("Ngày sinh phải là kiểu datetime.date hoặc datetime.datetime")
        
        # Kiểm tra tính hợp lệ của ngày sinh
        today = date.date.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        if not (0 <= age <= 120):
            raise ValueError("Ngày sinh không hợp lệ, tuổi phải từ 0 đến 120")
        
        self._birth = birth
        self._age = age

    # Age (Read-Only)
    @property
    def age(self):
        return self._age

    # Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Địa chỉ email không hợp lệ")
        self._email = email

    @property
    def base_salary(self):
        return self._base_salary

    @property
    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    def __str__(self):
        return f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age}"

