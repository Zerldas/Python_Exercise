from .person import Person

class Designer(Person):
    def __init__(self, id_person, first_name, last_name, birth, email, kpi):
        super().__init__(id_person, first_name, last_name, birth, email)
        self.kpi = kpi

    @property
    def kpi(self) -> str:
        return self.__kpi
    
    @kpi.setter
    def kpi(self, kpi_value: str):
        if not isinstance(kpi_value, str) or not kpi_value.strip():
            raise ValueError("Chuyên môn/KPI không được để trống")
        self.__kpi = kpi_value

    # --- Salary Calculation ---
    def calculate_salary(self):
        # Lương của Designer = Lương cơ bản + Thưởng theo KPI.
        kpi_bonus = {
            "Not Enough": 1.05 * self.base_salary,
            "Enough": 1.25 * self.base_salary,
            "Good": 1.5 * self.base_salary,
            "Excellent": 1.65 * self.base_salary
        }
        # Lấy tiền thưởng dựa trên kpi, nếu kpi không hợp lệ thì thưởng là 0.
        bonus = kpi_bonus.get(self.kpi, 0.0)
        return self.base_salary + bonus
    
    def __str__(self) -> str:
        return (f"""Designer: ID: {self.id},\n                           
        Name: {self.first_name} {self.last_name}\n                            
        Date Of Birth: {self.birth} (Age: {self.age})\n                            Email Address: {self.email}\n                            
        KPI: {self.kpi}\n                            
        Salary: {self.calculate_salary:.2f}""")