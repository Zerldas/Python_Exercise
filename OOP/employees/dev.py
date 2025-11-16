from .person import Person

class Dev(Person):
    def __init__(self, id_person, first_name, last_name, birth, email, role):
        super().__init__(id_person, first_name, last_name, birth, email)
        self.role = role

    @property
    def role(self) -> str:
        return self.__role
                
    @role.setter
    def role(self, role_value: str):
        if not isinstance(role_value, str) or not role_value.strip():
            raise ValueError("Vai trò không được để trống")
        self.__role = role_value # Junior, Senior, ...

    def calculate_salary(self):
        # Lương của Dev = Lương cơ bản + Thưởng hệ số theo vai trò (Junior, Senior...).
        role_bonus = {
            "Junior": 1.15 * self.base_salary, # Sử dụng self.base_salary từ lớp cha
            "Mid": 1.3 * self.base_salary,
            "Senior": 1.5 * self.base_salary,
            "Lead": 1.8 * self.base_salary
        }
        # Lấy tiền thưởng dựa trên vai trò, nếu không có thì thưởng là 0.
        bonus = role_bonus.get(self.role, 0.0)
        return self.base_salary + bonus

    def __str__(self) -> str:
        return (f"""Dev:      
        ID: {self.id},\n                           
        Name: {self.first_name} {self.last_name}\n                        
        Date Of Birth: {self.birth} (Age: {self.age})\n                            Email Address: {self.email}\n                          
        Role: {self.role}\n                            
        Salary: {self.calculate_salary:.2f}""")