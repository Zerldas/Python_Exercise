from rich.console import Console
from rich.table import Table
from employees.dev import Dev
from employees.designer import Designer
from employees.manager import Manager
from employees.marketer import Marketer
from project import Project
import datetime

class System:
    def __init__(self):
        self.employees = []
        self.projects = []
        self.assignments = {}
    
        # Khởi tạo dữ liệu
    def load_from_file(self, filename):
        print(f"\nĐang tải dữ liệu từ {filename} ...")

        section = None
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if line == "[EMPLOYEES]":
                    section = "emp"
                    continue
                elif line == "[PROJECTS]":
                    section = "proj"
                    continue
                
                parts = [p.strip() for p in line.split("|")]

                # Employee
                if section == "emp":
                    emp_id, first, last, birth, email, role, extra = parts
                    birth = datetime.datetime.strptime(birth, "%Y-%m-%d").date()
                    if role == "dev":
                        obj = Dev(emp_id, first, last, birth, email, extra)
                    elif role == "designer":
                        obj = Designer(emp_id, first, last, birth, email, extra)
                    elif role == "manager":
                        obj = Manager(emp_id, first, last, birth, email, int(extra))
                    elif role == "marketer":
                        obj = Marketer(emp_id, first, last, birth, email, extra)
                    else:
                        print(f" Role không hợp lệ: {role}")
                        continue
                    
                    self.add_employee(obj)
                
                  # Project
                elif section == "proj":
                    pid, name, desc, start, end, completed = parts

                    start = datetime.datetime.strptime(start, "%Y-%m-%d").date()
                    end = None if end == "None" else datetime.datetime.strptime(end, "%Y-%m-%d").date()
                    completed = completed.lower() == "true"

                    pr = Project(pid, name, desc, start, end, completed, [])
                    self.add_project(pr)
                
        print("Tải dữ liệu hoàn tất")        


    # Quản lý nhân viên
    def print_list_employee(self):
        if not self.employees:
            print("Không có nhân viên nào trong hệ thống.")
            return

        console = Console()
        table = Table(title="Danh sách nhân viên", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=10)
        table.add_column("Họ và tên", min_width=20)
        table.add_column("Email", min_width=20)
        table.add_column("Chức vụ/Chuyên môn", min_width=15)
        table.add_column("Lương", justify="right")

        for emp in self.employees:
            role_spec = ""
            if hasattr(emp, 'role'):
                role_spec = emp.role
            elif hasattr(emp, 'specialization'):
                role_spec = emp.specialization
            elif hasattr(emp, 'kpi'):
                role_spec = f"KPI: {emp.kpi}"
            elif hasattr(emp, 'experience'):
                role_spec = f"Manager ({emp.experience} năm KN)"
            
            table.add_row(str(emp.id), f"{emp.first_name} {emp.last_name}", emp.email, role_spec, f"{emp.calculate_salary():,.2f} VND")
        console.print(table)

    # Trả về nhân viên có id tương ứng, nếu không có thì trả về None.
    def get_employee(self, emp_id: str):
        for emp in self.employees:
            if getattr(emp, "id", None) == emp_id:
                return emp
        return None

    # Thêm một nhân viên mới vào hệ thống.
    def add_employee(self, employee):
        if not hasattr(employee, "id"):
            raise ValueError("Nhân viên cần phải có id")
        if self.get_employee(employee.id) is not None:
            raise ValueError(f"Nhân viên với id={employee.id} đã tồn tại")
        self.employees.append(employee)

    # Xóa một nhân viên ra khổi hệ thống
    def remove_employee(self, emp_id: str):
        self.employees = [emp for emp in self.employees if emp.id != emp_id]
        for project in self.projects:
            project.remove_member(emp_id)

    # Xóa nhân viên khỏi hệ thống và gỡ họ ra khỏi tất cả các dự án.
    def update_employee(self, emp_id, **kwargs):
        # tìm emp theo id
        emp = self.get_employee(emp_id)
        if emp is None:
            raise ValueError(f"Không tìm thấy nhân viên với id = {emp_id}")
        for key, value in kwargs.items():
            if hasattr(emp, key):
                setattr(emp, key, value)

    # Quản lí dự án
    # Trả về project có id tương ứng, nếu không có thì trả về None.
    def get_project(self, project_id: str):
        for pr in self.projects:
            if getattr(pr, "id", None) == project_id:
                return pr
        return None
    
    # In danh sách dự án ra bảng
    def print_list_project(self):
        if not self.projects:
            print("Không có dự án nào trong hệ thống.")
            return

        console = Console()
        table = Table(title="Danh sách dự án", show_header=True, header_style="bold cyan")
        table.add_column("ID", style="dim", width=10)
        table.add_column("Tên dự án", min_width=20)
        table.add_column("Ngày bắt đầu")
        table.add_column("Ngày kết thúc")
        table.add_column("Trạng thái")
        table.add_column("Số lượng thành viên:", justify="center")

        for proj in self.projects:
            table.add_row(str(proj.id), proj.name, str(proj.start_date), str(proj.end_date or "N/A"), proj.progress(), str(len(proj.team_members)))
        console.print(table)

    # Thêm một dự án mới vào hệ thống.
    def add_project(self, project):
        if not hasattr(project, "id"):
            raise ValueError("Project này chưa có id, không thể thêm vào hệ thống")
        if self.get_project(project.id) is not None:
            raise ValueError(f"Project với id = {project.id} đã tồn tại")
        self.projects.append(project)
        self.assignments[project.id] = []

    # Xóa một dự án mới vào hệ thống 
    def remove_project(self, project_id: str):
        project = self.get_project(project_id)
        if project is None:
            raise ValueError("Không tồn tại project mà bạn muốn xóa")
        if project_id in self.assignments:
            del self.assignments[project_id]

    # Cập nhật thông tin của một dự án theo id
    def update_project(self, project_id:str, **kwargs):
        project = self.get_project(project_id)
        if project is None:
            raise ValueError(f"Không tìm thấy project với id = {project_id}")
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)

    # Quản lý phân công công việc
    #  Gán một nhân viên vào một dự án.
    def assign_employee_to_project(self, emp_id: str, proj_id: str):
        employee = self.get_employee(emp_id)
        project = self.get_project(proj_id)

        if employee is None:
            raise ValueError(f"Không tìm thấy nhân viện phù hợp với id = {emp_id}")
        if project is None:
            raise ValueError(f"Không tìm thấy project phù hợp với id = {proj_id}")
        
        project.add_member(employee)
        if emp_id not in self.assignments[proj_id]:
            self.assignments[proj_id].append(emp_id)

    # Gỡ một nhân viên ra khỏi dự án.
    def remove_employee_from_project(self, emp_id: str, proj_id: str):
        employee = self.get_employee(emp_id)
        project = self.get_project(proj_id)
        
        if employee is None:
            raise ValueError(f"Không tìm thấy nhân viện phù hợp với id = {emp_id}")
        if project is None:
            raise ValueError(f"Không tìm thấy project phù hợp với id = {proj_id}")
        
        if employee and project:
            project.remove_member(employee)
            if emp_id in self.assignments[proj_id]:
                self.assignments[proj_id].remove(emp_id)

    # Lấy danh sách đối tượng nhân viên đang tham gia dự án cụ thể.
    def get_project_assignments(self, proj_id: str):
        if self.get_project(proj_id) is None:
            raise ValueError(f"Không tìm thấy project phù hợp với id = {proj_id}")
        return [self.get_employee(emp_id) for emp_id in self.assignments.get(proj_id, [])]
    
    # In danh sách thành viên của một dự án ra bảng.
    def print_project_assignments(self, proj_id: str):
        project = self.get_project(proj_id)
        if project is None:
            raise ValueError(f"Không tìm thấy project phù hợp với id = {proj_id}")
        
        members = self.get_project_assignments(proj_id)
        console = Console()
        table = Table(title=f"Thành viên dự án: {project.name}", show_header=True, header_style="bold green")
        table.add_column("ID", style="dim", width=10)
        table.add_column("Họ và tên")
        table.add_column("Email")

        for member in members:
            table.add_row(str(member.id), f"{member.first_name} {member.last_name}", member.email)
        console.print(table)

    #   Trả về danh sách các dự án mà một nhân viên đang tham gia.
    def get_employee_assignments(self, emp_id: str):
        if self.get_employee(emp_id) is None:
            raise ValueError(f"Không tìm thấy nhân viên phù hợp với id = {emp_id}")
        return [self.get_project(proj_id) for proj_id, members in self.assignments.items() if emp_id in members]