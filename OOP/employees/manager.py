from .person import Person

class Manager(Person):
    def __init__(self, id_person, first_name, last_name, birth, email, experience):
        super().__init__(id_person, first_name, last_name, birth, email)
        self.experience = experience # [1; ...]

    @property
    def experience(self) -> int:
        return self.__experience

    @experience.setter
    def experience(self, exp_value: int):
        if not isinstance(exp_value, int) or exp_value < 0:
            raise ValueError("Số năm kinh nghiệm phải là một số nguyên không âm")
        self.__experience = exp_value

    def calculate_salary(self):
        # Lương của Manager = Lương cơ bản + Thưởng kinh nghiệm.
        # Giả sử mỗi năm kinh nghiệm được thưởng thêm 2 đơn vị tiền tệ.
        bonus = 2.0 * self.experience
        return self.base_salary + bonus
    
    def __str__(self) -> str:
        return (f"""Manager:  ID: {self.id},\n                            
        Name: {self.first_name} {self.last_name}\n                            
        Date Of Birth: {self.birth} (Age: {self.age})\n 
        Email Address: {self.email}\n                            
        Experience: {self.experience} years\n                            
        Salary: {self.calculate_salary:.2f}""")