from .person import Person

class Marketer(Person):

    def __init__(self, id_person, first_name, last_name, birth, email, specialization):
        super().__init__(id_person, first_name, last_name, birth, email)

        self.specialization = specialization

    @property
    def specialization(self) -> str:
        return self.specialization
    
    @specialization.setter
    def specialization(self, spec_value: str):
        if not isinstance(spec_value, str) or not spec_value.strip():
            raise ValueError("Chuyên môn không được để trống")
        self._specialization = spec_value

    # --- Salary Calculation ---
    @property
    def calculate_salary(self) -> float:
        # Lương của Marketer = Lương cơ bản + Thưởng theo chuyên môn.
        specialization_bonus = {
            "SEO": 0.1 * self.base_salary, # Sử dụng self.base_salary từ lớp cha
            "Content": 0.2 * self.base_salary,
            "Social Media": 0.3 * self.base_salary,
            "Email Marketing": 0.4 * self.base_salary
        }
        # Lấy tiền thưởng dựa trên chuyên môn, nếu không có thì thưởng là 0.
        bonus = specialization_bonus.get(self.specialization, 0.0)
        return self.base_salary + bonus
    
    def __str__(self) -> str:
        return (f"""Marketer: ID: {self.id},\n                            Name: {self.first_name} {self.last_name}\n                            Date Of Birth: {self.birth} (Age: {self.age})\n                            Email Address: {self.email}\n                            Specialization: {self.specialization}\n                            Salary: {self.calculate_salary:.2f}""")