from datetime import date
class Project:
    
    def __init__(self, id, name, description, start_date, end_date, complete, team_members):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.complete = complete
        self.team_members = team_members # Danh sách các nhân viên trong dự án

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def start_date(self) -> date:
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def complete(self) -> bool:
        return self._complete

    @complete.setter
    def complete(self, value):
        self._complete = value

    @property
    def team_members(self) -> list:
        return self._team_members

    # CRUD 
    # Thêm một thành viên vào dự án
    
    def add_member(self, member):
        if member not in self.team_members:
            self.team_members.append(member)

    # Xóa một thành viên khỏi dự án
    def remove_member(self, member):
        if member in self.team_members:
            self.team_members.remove(member)

    # Đặt ngày bắt đầu dự án là ngày hiện tại
    def set_start_date_today(self):
        self.start_date = date.today()
    
    # Đặt ngày kết thúc
    def set_end_date_today(self):
        self.end_date = date.today()

    # Đánh dấu dự án đã hoàn thành và gán ngày kết thúc là hôm nay
    def mark_complete(self):
        self.complete = True
        self.set_end_date_today()

    # Đánh dấu dự án chưa hoàn thành và xóa ngày kết thúc
    def mark_incomplete(self):
        self.complete = False
        self.end_date = None

    # Trả về chuỗi mô tả trạng thái dự án (Hoàn thành / Chưa hoàn thành)
    def progress(self):
        return "Hoàn thành" if self.complete else "Chưa hoàn thành"

    def __str__(self):
        members = ', '.join([str(m) for m in self.team_members])
        return (
            f"Project ID: {self.id}\n"
            f"Tên dự án: {self.name}\n"
            f"Mô tả: {self.description}\n"
            f"Ngày bắt đầu: {self.start_date}\n"
            f"Ngày kết thúc: {self.end_date}\n"
            f"Trạng thái: {self.progress()}\n"
            f"Thành viên: {members}"
        )
        