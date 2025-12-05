from abc import ABC, abstractmethod
import datetime as date

# Lớp Person là một lớp cơ sở trừu tượng cho tất cả các loại nhân viên.
class Person(ABC):
    # Thuộc tính private, sử dụng __ để "name mangling", tránh bị ghi đè ở lớp con.
    __base_salary = 2000.0 # Lương cơ bản chung
    __age = 0
    # Phương thức khởi tạo (constructor) của lớp.
    def __init__(self, id_person, first_name, last_name, birth, email):
        self.id = id_person
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth 
        self.email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_person):
        self.__id = id_person

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name.strip(): 
            raise ValueError("Tên không được để trống")
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if not last_name.strip(): # Kiểm tra họ không được để trống
            raise ValueError("Họ không được để trống")
        self.__last_name = last_name

    @property
    def birth(self):
        return self.__birth

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
        
        self.__birth = birth
        self.__age = age

    # (Read-Only)
    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Địa chỉ email không hợp lệ")
        self.__email = email

    @property
    def base_salary(self):
        return self.__base_salary

    @property
    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    def __str__(self):
        return f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age}"

