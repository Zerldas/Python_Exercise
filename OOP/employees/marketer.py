from .person import Person

class Marketer(Person):

    def __init__(self, id_person, first_name, last_name, birth, email, specialization):
        super().__init__(id_person, first_name, last_name, birth, email)

        self.specialization = specialization

    @property
    def specialization(self) -> str:
        return self.__specialization
    
    @specialization.setter
    def specialization(self, spec_value: str):
        if not isinstance(spec_value, str) or not spec_value.strip():
            raise ValueError("Chuyên môn không được để trống")
        self.__specialization = spec_value

    # --- Salary Calculation ---
    def calculate_salary(self):
        # Lương của Marketer = Lương cơ bản + Thưởng theo hệ số chuyên môn.
        specialization_bonus = {
            "SEO": 1.1 * self.base_salary, # Sử dụng self.base_salary từ lớp cha
            "Content": 1.3 * self.base_salary,
            "Social Media": 1.5 * self.base_salary,
            "Email Marketing": 1.7 * self.base_salary
        }
        # Lấy tiền thưởng dựa trên chuyên môn, nếu không có thì thưởng là 0.
        bonus = specialization_bonus.get(self.specialization, 0.0)
        return self.base_salary + bonus
    
    def __str__(self) -> str:
        return (f"""Marketer: ID: {self.id},\n                            
        Name: {self.first_name} {self.last_name}\n                            
        Date Of Birth: {self.birth} (Age: {self.age})\n                            Email Address: {self.email}\n                            
        Specialization: {self.specialization}\n                            
        Salary: {self.calculate_salary:.2f}""")