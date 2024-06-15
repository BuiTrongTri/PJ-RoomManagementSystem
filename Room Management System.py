from tkinter import *
from tkinter import Tk, Label, Entry, Button, messagebox, ttk, END
import tkinter.font as tkFont

class Room:
    def __init__(self, room_number, capacity, status, price):
        self.room_number = room_number
        self.capacity = capacity
        self.status = status
        self.price = price

def RoomManagementSystem():
    # tạo ra cửa sổ ứng dụng
    window = Tk()

    # setup thông tin cho window
    window.title("Room Management System")
    window.geometry("620x610")
    window.configure(bg="#F0F0F0")  # Đặt màu nền cho cửa sổ chính

    # tạo list để lưu trữ toàn bộ các object
    list_room = []

    # cập nhật treeview
    def populate_treeview():
        for i, room in enumerate(list_room, start=1):
            tag = "odd" if i % 2 == 0 else "even"
            treeview.insert("", "end", text=str(i), values=(room.room_number, room.capacity, room.status, room.price), tags=(tag,))

    # mô tả các funtion cho ứng dụng
    ## add room
    def add_room():
        room_value = room.get()
        capacity_value = capacity.get()
        status_value = status.get()
        price_value = price.get()

        # Kiểm tra người dùng đã nhập đủ giá trị vào entry chưa (nếu để int ở trên thì khi nhập thiếu chương trình sẽ lỗi mà không in ra cảnh báo dưới được)
        if not (room_value and capacity_value and status_value and price_value):
            messagebox.showwarning("Add Room", "Please fill all fields.")
            return

        # chuyển các giá trị sang int
        room_value = int(room_value)
        capacity_value = int(capacity_value)
        price_value = int(price_value)

        # kiểm tra phòng đã tồn tại chưa
        is_exist = False
        for room_item in list_room:
            if room_item.room_number == room_value:
                is_exist = True
                messagebox.showinfo("Add Room", f"Room {room_value} already exists")
                break
            
        if not is_exist:
            new_room = Room(room_value, capacity_value, status_value, price_value)

            # thêm vào list
            list_room.append(new_room)

            # list comprehension
            print([new_room.room_number for new_room in list_room])

            # Thêm dòng mới vào treeview
            treeview.delete(*treeview.get_children())
            populate_treeview()

            # hiển thị thông báo
            messagebox.showinfo("Add Room", f"Room {room_value} is added successfully")

            # xóa giá trị ở entry
            room.delete(0, END)
            capacity.delete(0, END)
            status.delete(0, END)
            price.delete(0, END)

    ## search room
    def search_room():
        search_value = int(search.get())

        is_exist = False

        # tìm kiếm trong list list_room
        for room_item in list_room:
            # tìm kiếm theo room_number
            if room_item.room_number == search_value:
                is_exist = True
                messagebox.showinfo("Search Room", f"Room Name: {room_item.room_number}, Capacity: {room_item.capacity}, Status: {room_item.status}, Price: {room_item.price}")
                break
            
        # nếu không tìm thấy room_number
        if not is_exist:
            messagebox.showinfo("Search Room", f"Room Name: {search_value} not found")

    ## delete room
    def delete_room():
        room_value = room.get()
        selected_room = treeview.selection()

        if selected_room:
            # Lấy giá trị của cột "ID"
            item_room = treeview.item(selected_room[0])['text']  
            index = int(item_room) - 1
            del list_room[index]
            messagebox.showinfo("Delete Room", f"Room with ID {item_room} has been deleted.")
        elif room_value:
            is_exist = False
            for room_item in list_room:
                if room_item.room_number == int(room_value):
                    is_exist = True
                    list_room.remove(room_item)
                    messagebox.showinfo("Delete Room", f"Room Number {room_value} has been deleted")
                    break
                
            if not is_exist:
                messagebox.showinfo("Delete Room", f"Room Number {room_value} not found")
        else:
            messagebox.showwarning("Delete Room", "Please select a room or enter a room number to delete.")

        # Update treeview
        treeview.delete(*treeview.get_children())
        populate_treeview()

    ## update_room
    def update_room():
        room_value = room.get()
        capacity_value = capacity.get()
        status_value = status.get()
        price_value = price.get()

        # Kiểm tra người dùng đã nhập đủ giá trị vào entry chưa (nếu để int ở trên thì khi nhập thiếu chương trình sẽ lỗi mà không in ra cảnh báo dưới được)
        if not (room_value and capacity_value and status_value and price_value):
            messagebox.showwarning("Update Room", "Please fill all fields.")
            return

        # chuyển các giá trị sang int
        room_value = int(room_value)
        capacity_value = int(capacity_value)
        price_value = int(price_value)

        is_exist = False

        for room_item in list_room:
            if room_item.room_number == room_value:
                is_exist = True
                room_item.capacity = capacity_value
                room_item.status = status_value
                room_item.price = price_value
                messagebox.showinfo("Update Room", f"Room Number {room_value} is updated successfully")
                break
            
        if not is_exist:
            messagebox.showinfo("Update Room", f"Room Number {room_value} is not found")

        # Update treeview
        treeview.delete(*treeview.get_children())
        populate_treeview()

    ## reset
    def reset():
        room.delete(0, END)
        capacity.delete(0, END)
        status.delete(0, END)
        price.delete(0, END)
        search.delete(0, END)

    # Tạo font chữ tùy chỉnh
    heading_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
    title_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
    label_frame_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
    label_font = tkFont.Font(family="Helvetica", size=12)

    # Tạo tiêu đề căn giữa
    title_label = Label(window, text="Room Management System", font=title_font)
    title_label.grid(row=0, column=0, sticky="w", padx=150, pady=5)

    # Tạo LabelFrame
    label_frame = LabelFrame(window, text="Room Details", padx=10, pady=10, font=label_frame_font)
    label_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    label_frame.configure(bg="#DDEBF7")  # Đặt màu nền cho LabelFrame

    # setup các widget trong LabelFrame
    # tạo label
    room_lbl = Label(label_frame, text="Room Number:", anchor="w", font=label_font, bg="#DDEBF7")
    capacity_lbl = Label(label_frame, text="Capacity:", anchor="w", font=label_font, bg="#DDEBF7")
    status_lbl = Label(label_frame, text="Status:", anchor="w", font=label_font, bg="#DDEBF7")
    price_lbl = Label(label_frame, text="Price ($):", anchor="w", font=label_font, bg="#DDEBF7")
    search_lbl = Label(label_frame, text="Search Room:", anchor="w", font=label_font, bg="#DDEBF7")

    # tạo entry 
    room = Entry(label_frame, font=label_font)
    capacity = Entry(label_frame, font=label_font)
    status = Entry(label_frame, font=label_font)
    price = Entry(label_frame, font=label_font)
    search = Entry(label_frame, font=label_font)

    # tạo button 
    add_btn = Button(label_frame, text="Add Room", width=15, command=add_room, font=label_font, bg="#ADD8E6")
    delete_btn = Button(label_frame, text="Delete Room", width=15, command=delete_room, font=label_font, bg="#FFB6C1")
    update_btn = Button(label_frame, text="Update Room", width=15, command=update_room, font=label_font, bg="#90EE90")
    reset_btn = Button(label_frame, text="Reset", width=15, command=reset, font=label_font, bg="#F0E68C")
    search_btn = Button(label_frame, text="Search Room", width=15, command=search_room, font=label_font, bg="#FFD700")

    # dán các widget lên window
    ## dán widget lable
    room_lbl.grid(row=0, column=0, sticky="e", pady=5)
    capacity_lbl.grid(row=1, column=0, sticky="e", pady=5)
    status_lbl.grid(row=2, column=0, sticky="e", pady=5)
    price_lbl.grid(row=3, column=0, sticky="e", pady=5)
    search_lbl.grid(row=4, column=0, sticky="e", pady=25)

    ## dán widget entry
    room.grid(row=0, column=1, sticky="w", pady=5)
    capacity.grid(row=1, column=1, sticky="w", pady=5)
    status.grid(row=2, column=1, sticky="w", pady=5)
    price.grid(row=3, column=1, sticky="w", pady=5)
    search.grid(row=4, column=1, sticky="w", pady=25)

    ## dán widget button
    add_btn.grid(row=0, column=2, padx=20, pady=5)
    delete_btn.grid(row=1, column=2, padx=20, pady=5)
    update_btn.grid(row=2, column=2,  padx=20, pady=5)
    reset_btn.grid(row=3, column=2, padx=20, pady=5)
    search_btn.grid(row=4, column=2, padx=20, pady=25)

    # tạo treeview. Link tham khảo: https://pythonassets.com/posts/treeview-in-tk-tkinter/
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", font=heading_font, background="#DDEBF7", foreground="black")
    treeview = ttk.Treeview(window, columns=("Room Number", "Capacity", "Status", "Price ($)"))
    treeview.heading("#0", text="ID")
    treeview.column("#0", width=50) 
    treeview.heading("Room Number", text="Room Number")
    treeview.column("Room Number", width=120) 
    treeview.heading("Capacity", text="Capacity")
    treeview.column("Capacity", width=120) 
    treeview.heading("Status", text="Status")
    treeview.column("Status", width=120) 
    treeview.heading("Price ($)", text="Price ($)")
    treeview.column("Price ($)", width=120) 
    treeview.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # Đặt màu nền cho các hàng của Treeview
    treeview.tag_configure('odd', background='#F0F0F0')  # Màu nền cho hàng lẻ
    treeview.tag_configure('even', background='#E0E0E0')  # Màu nền cho hàng chẵn

    # chạy ứng dụng
    window.mainloop()

# Hàm để kiểm tra đăng nhập. Link tham khảo: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-16.php
def login(event=None):
    username = username_entry.get()
    password = password_entry.get()

    # Kiểm tra username và password
    if username == "admin" and password == "admin":
        login_window.destroy()  # Đóng cửa sổ đăng nhập
        RoomManagementSystem()
    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showerror("Login Failed", "Invalid username or password")

# Hàm xử lý sự kiện khi đóng cửa sổ đăng nhập
def on_closing():
    login_window.destroy()
    exit()

# Tạo cửa sổ đăng nhập
login_window = Tk()
login_window.title("Login")
login_window.geometry("300x180")
login_window.configure(bg="#ECE9D8")
login_window.protocol("WM_DELETE_WINDOW", on_closing)

# Tạo font chữ tùy chỉnh cho cửa sổ đăng nhập
login_title_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
login_label_font = tkFont.Font(family="Helvetica", size=12)

# Tạo label và entry cho username
username_label = Label(login_window, text="Username", bg="#ECE9D8", fg="black", font=login_label_font)
username_label.pack(pady=5)
username_entry = Entry(login_window, font=login_label_font)
username_entry.pack(pady=5)

# Tạo label và entry cho password
password_label = Label(login_window, text="Password", bg="#ECE9D8", fg="black", font=login_label_font)
password_label.pack(pady=5)
password_entry = Entry(login_window, show="*", font=login_label_font)  # show="*" để ẩn mật khẩu
password_entry.pack(pady=5)

# Tạo nút Login
login_button = Button(login_window, text="Login", width=10, command=login, bg="#D4D0C8", fg="black", relief="raised", font=login_label_font)
login_button.pack(pady=10)

# Gắn sự kiện nhấn phím Enter vào Entry password_entry. Link tham khảo: https://python-forum.io/thread-25596.html
password_entry.bind('<Return>', login)

# Chạy cửa sổ đăng nhập
login_window.mainloop()