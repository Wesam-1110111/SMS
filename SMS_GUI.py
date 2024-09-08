import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



class App(tk.Tk):
	def __init__(self, title, size=[400, 300]):
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}+350+180')
		self.minsize(size[0], size[1])

		main = Body(self)
		main.pack(expand=True, fill='both')



		self.mainloop()




class Body(ttk.Frame):
	def __init__(self, master):
		super().__init__(master)
		
		self.USER = ''
		self.PASSWORD = ''

		

		self.frame = self.login_frame()

		self.user = self.user_passwd_frame('User name: ')
		self.passwd = self.user_passwd_frame('Password: ', True)

		self.frame.pack(pady=50)


	def login_frame(self):

		frame = ttk.Frame(self, borderwidth=2, relief=tk.GROOVE, width=400, height=250)
		frame.pack_propagate(False)
		

		ttk.Label(frame, text='Log in', font='40px').pack(pady=25)

		login_btn = ttk.Button(frame, text='Submit', command=self.check)
		login_btn.pack(side='bottom', pady=20)

		return frame

	def user_passwd_frame(self, label_text, display_text=False):

		up = tk.StringVar()

		frame = ttk.Frame(self.frame)
		frame.pack(pady=10)

		label = ttk.Label(frame, text=label_text)
		label.pack(side='left')

		entry = ''

		if display_text:
			entry = ttk.Entry(frame, textvariable=up, show='*')
		else: 
			entry = ttk.Entry(frame, textvariable=up, show='')

		entry.pack()

		return up


	def check(self):
		if self.user.get() == self.USER and self.passwd.get() == self.PASSWORD:
			print('cool')
			self.frame.forget()
			self.menu_frame('Home Menu').pack(pady=30, expand=True, fill='both')
		else:
			# print('user name or password is wrong')
			messagebox.showerror(title='error',message='User name or Password is wrong')


	def menu_frame(self, title, btns_titles=None):

		btns_titles = ['Teacher', 'Student', 'About SMS']

		frame = ttk.Frame(self,borderwidth=2, relief=tk.GROOVE)
		label = ttk.Label(frame, text=title, font=40)
		label.pack(pady=30)

		if btns_titles != None:
			for i in btns_titles:
				ttk.Button(frame, text=i).pack(pady=10, ipadx=20, ipady=10)

		exit_btn = ttk.Button(frame, text='Back', command=lambda: self.pack_forget(frame, self.frame))
		exit_btn.place(relx=1, rely=1, anchor='se')

		frame.pack(pady=30, expand=True, fill='both')
		return frame


	def pack_forget(self, frame_forget, frame_pack):

		frame_forget.forget()
		frame_pack.pack(pady=50)


if __name__ == '__main__':

	App('SMS', [600, 350])