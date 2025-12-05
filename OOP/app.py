from system import System
from employees.dev import Dev
from employees.designer import Designer
from employees.manager import Manager
from employees.marketer import Marketer
from project import Project
import datetime

class App:
    def __init__(self):
        self.system = System()
        self.system.load_from_file("data.txt")
        if not self.system.employees:
            self.employee_counter = 1
        else:
            # Tìm số lớn nhất trong ID dạng "E<number>"
            max_id = max(int(emp.id[1:]) for emp in self.system.employees)
            self.employee_counter = max_id + 1

        if not self.system.projects:
            self.project_counter = 1
        else:
            max_id = max(int(pr.id[1:]) for pr in self.system.projects)
            self.project_counter = max_id + 1
        

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
        self.system.print_list_employee()

    def list_projects(self):
        if not self.system.projects:
            print("Không có dự án nào.")
            return
        print("\n=== Danh sách dự án ===")
        self.system.print_list_project()

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

    # Tìm kiếm nhân viên theo ID
    def find_employee(self):
        emp_id = input("Nhập ID nhân viên: ").strip()
        emp = self.system.get_employee(emp_id)
        if emp:
            self.emp.__str__
        else:
            print("Không tìm thấy nhân viên với ID này.")

    # Xóa employee khỏi hệ thống
    def remove_employee(self):
        emp_id = input("Nhập ID nhân viên cần xóa: ").strip()

        try:
            self.system.remove_employee(emp_id)
            print(f" Đã xóa nhân viên {emp_id} khỏi hệ thống.")
        except Exception as e:
            print("Lỗi:", e)

    # Cập nhật thông tin nhân viên
    def update_employee(self):
        emp_id = input("Nhập ID nhân viên cần cập nhật: ").strip()
        emp = self.system.get_employee(emp_id)

        if not emp:
            print("Không tìm thấy nhân viên.")
            return

        print("\n=== Cập nhật nhân viên ===")
        print("Nhấn Enter để bỏ qua trường không muốn đổi")

        new_first = input(f"Họ mới ({emp.first_name}): ").strip()
        new_last = input(f"Tên mới ({emp.last_name}): ").strip()
        new_email = input(f"Email mới ({emp.email}): ").strip()

        update_data = {}
        if new_first: update_data["first_name"] = new_first
        if new_last: update_data["last_name"] = new_last
        if new_email: update_data["email"] = new_email

        try:
            self.system.update_employee(emp_id, **update_data)
            print("Cập nhật nhân viên thành công.")
        except Exception as e:
            print("Lỗi:", e)
        
    # Thêm project
    def add_project(self):
        print("\n=== Thêm dự án ===")
        name = input("Tên dự án: ").strip()
        desc = input("Mô tả: ").strip()
        pid = self.generate_proj_id()
        proj = Project(pid, name, desc, datetime.date.today(), None, False, [])
        self.system.add_project(proj)
        print(f"Đã thêm dự án {name} (ID={pid})")

    # Thêm nhân viên vào dự án
    def assign_employee(self):
        emp_id = input("ID nhân viên: ").strip()
        proj_id = input("ID dự án: ").strip()
        try:
            self.system.assign_employee_to_project(emp_id, proj_id)
            print(" Đã gán nhân viên vào dự án.")
        except Exception as e:
            print("Lỗi: ", e)

    # Tìm kiếm dự án theo id
    def find_project(self):
        proj_id = input("Nhập ID dự án: ").strip()
        proj = self.system.get_project(proj_id)
        if proj:
            status = "Hoàn thành" if proj.completed else "Đang thực hiện"
            print(proj.__str__)
        else:
            print("Không tìm thấy dự án với ID này.")
    
    # Xóa dự án
    def remove_project(self):
        proj_id = input("Nhập ID dự án cần xóa: ").strip()
        try:
            self.system.remove_project(proj_id)
            print(f" Dự án {proj_id} đã bị xóa khỏi hệ thống.")
        except Exception as e:
            print("Lỗi:", e)
    
    # Cập nhật thông tin dự án
    def update_project(self):
        proj_id = input("Nhập ID dự án cần cập nhật: ").strip()
        proj = self.system.get_project(proj_id)

        if not proj:
            print("Không tìm thấy dự án.")
            return

        print("\n=== Cập nhật dự án ===")
        print("Nhấn Enter để bỏ qua trường không muốn đổi")

        new_name = input(f"Tên mới ({proj.name}): ").strip()
        new_desc = input(f"Mô tả mới ({proj.description}): ").strip()

        update_data = {}
        if new_name: update_data["name"] = new_name
        if new_desc: update_data["description"] = new_desc

        try:
            self.system.update_project(proj_id, **update_data)
            print("Cập nhật dự án thành công.")
        except Exception as e:
            print("Lỗi:", e)

    # Xóa nhân viên
    def remove_employee_from_project(self):
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
    
    # List ra danh sách dự án mà nhân viên đang tham gia
    def show_employee_assignments(self):
        emp_id = input("ID Nhân viên: ").strip()
        list_assign = self.system.get_employee_assignments(emp_id)
        if list_assign:
            print("\nDanh sách các dự án của nhân viên: ")
            print(list_assign)
        else:
            print("Nhân viên đang không làm việc với dự án nào")
    # Run app
    def run(self):
        menu = {
            "1": ("Danh sách nhân viên", self.list_employees),
            "2": ("Danh sách dự án", self.list_projects),
            "3": ("Thêm nhân viên", self.add_employee),
            "4": ("Tìm kiếm nhân viên", self.find_employee),
            "5": ("Xóa nhân viên", self.remove_employee),
            "6": ("Cập nhật nhân viên", self.update_employee),
            "7": ("Thêm dự án", self.add_project),
            "8": ("Tìm kiếm dự án", self.find_project),
            "9": ("Xóa dự án", self.remove_project),
            "10": ("Cập nhật dự án", self.update_project),
            "11": ("Gán nhân viên vào dự án", self.assign_employee),
            "12": ("Gỡ nhân viên khỏi dự án", self.remove_employee),
            "13": ("Hiển thị thành viên dự án", self.show_project_members),
            "14": ("Hiển thị danh sách dự án mà một nhân viên đang tham gia", self.show_employee_assignments),
            "0": ("Thoát", None)
        }
        while True:
            print("\n=== MENU ===")
            for k, (desc, _) in menu.items():
                print(f"{k}. {desc}")
            choice = input("Chọn hành động (1-14) hoặc 0 để thoát: ").strip()
            if choice == "0":
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
    app = App()
    app.run()