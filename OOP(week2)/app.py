from system import System
from dev import Dev
from designer import Designer
from manager import Manager
from marketer import Marketer
from project import Project
import datetime

class App:
    def __init__(self):
        self.system = System()
        # Tự động đếm id cho project và employee
        self.employee_counter = 1
        self.project_counter = 1
    # Gen id employee tự động
    def generate_emp_id(self):
        eid = f"E{self.employee_counter}"
        self.employee_counter += 1
        return eid

    # Gen id project tự động
    def generate_proj_id(self):
        pid = f"P{self.project_counter}"
        self.project_counter += 1
        return pid

    # Lists
    def list_employees(self):
        if not self.system.employees:
            print("Không có nhân viên nào.")
            return
        print("\n=== Danh sách nhân viên ===")
        for emp in self.system.employees:
            print(f"- {emp.id}: {emp.first_name} {emp.last_name} | Email: {emp.email}")

    def list_projects(self):
        if not self.system.projects:
            print("Không có dự án nào.")
            return
        print("\n=== Danh sách dự án ===")
        for pr in self.system.projects:
            print(f"- {pr.id}: {pr.name} | Trạng thái: {pr.progress()} | Thành viên: {len(pr.team_members)}")

    # Tạo nhân viên
    def add_employee(self):
        print("\n=== Thêm nhân viên ===")
        first = input("Họ: ").strip()
        last = input("Tên: ").strip()
        birth_str = input("Ngày sinh (YYYY-MM-DD): ").strip()
        email = input("Email: ").strip()
        role_type = input("Loại nhân viên (dev/designer/manager/marketer): ").strip().lower()
         # Chuyển đổi ngày sinh từ chuỗi sang đối tượng date
        try:
            birth = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
        except:
            print("Ngày sinh không hợp lệ.")
            return

        emp_id = self.generate_emp_id()
        if role_type == "dev":
            role = input("Vai trò (Junior/Mid/Senior/Lead): ").strip()
            emp = Dev(emp_id, first, last, birth, email, role)
        elif role_type == "designer":
            kpi = input("KPI (Not Enough/Enough/Good/Excellent): ").strip()
            emp = Designer(emp_id, first, last, birth, email, kpi)
        elif role_type == "manager":
            exp = int(input("Kinh nghiệm (số năm): "))
            emp = Manager(emp_id, first, last, birth, email, 2000.0, exp)
        elif role_type == "marketer":
            spec = input("Chuyên môn (SEO/Content/Social Media/Email Marketing): ").strip()
            emp = Marketer(emp_id, first, last, birth, email, spec)
        else:
            print("Loại nhân viên không hợp lệ.")
            return

        self.system.add_employee(emp)
        print(f" Đã thêm nhân viên {emp.first_name} {emp.last_name} (ID={emp.id})")

    # Thêm project
    def add_project(self):
        print("\n=== Thêm dự án ===")
        name = input("Tên dự án: ").strip()
        desc = input("Mô tả: ").strip()
        pid = self.generate_proj_id()
        proj = Project(pid, name, desc, datetime.date.today(), None, False, [])
        self.system.add_project(proj)
        print(f" Đã thêm dự án {name} (ID={pid})")

    # Thêm nhân viên vào dự án
    def assign_employee(self):
        emp_id = input("ID nhân viên: ").strip()
        proj_id = input("ID dự án: ").strip()
        try:
            self.system.assign_employee_to_project(emp_id, proj_id)
            print(" Đã gán nhân viên vào dự án.")
        except Exception as e:
            print("Lỗi: ", e)

    # Xóa nhân viên
    def remove_employee(self):
        emp_id = input("ID nhân viên: ").strip()
        proj_id = input("ID dự án: ").strip()
        try:
            self.system.remove_employee_from_project(emp_id, proj_id)
            print(" Đã gỡ nhân viên khỏi dự án.")
        except Exception as e:
            print("Lỗi: ", e)

    # Lists ra danh sách thành viên của project
    def show_project_members(self):
        proj_id = input("ID dự án: ").strip()
        project = self.system.get_project(proj_id)
        if not project:
            print("Không tìm thấy dự án.")
            return
        print(f"\n=== Thành viên dự án {project.name} ===")
        members = self.system.get_project_assignments(proj_id)
        if not members:
            print("Chưa có thành viên nào.")
            return
        for m in members:
            print(f"- {m.id}: {m.first_name} {m.last_name}")

    # Run app
    def run(self):
        menu = {
            "1": ("Danh sách nhân viên", self.list_employees),
            "2": ("Danh sách dự án", self.list_projects),
            "3": ("Thêm nhân viên", self.add_employee),
            "4": ("Thêm dự án", self.add_project),
            "5": ("Gán nhân viên vào dự án", self.assign_employee),
            "6": ("Gỡ nhân viên khỏi dự án", self.remove_employee),
            "7": ("Hiển thị thành viên dự án", self.show_project_members),
            "8": ("Thoát", None)
        }
        while True:
            print("\n=== MENU ===")
            for k, (desc, _) in menu.items():
                print(f"{k}. {desc}")
            choice = input("Chọn hành động (1-8): ").strip()
            if choice == "8":
                print(" Thoát chương trình.")
                break
            action = menu.get(choice)
            if not action:
                print(" Lựa chọn không hợp lệ.")
                continue
            try:
                action[1]()
            except Exception as e:
                print(" Lỗi:", e)


if __name__ == "__main__":
    App().run()