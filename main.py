"""

    calculator program

"""

# import tkinter
import tkinter as tk
import tkinter.font as font

# import math
import math


# Text box input restrictions
def test_char(string: any) -> bool:
    if len(string) == 0:
        return True

    types: tuple[any, any] = (int, float)
    for type_ in types:
        try:
            type_(string[-1])
            return True
        except ValueError:
            continue

    for c in [
        "+", "-", "×", "÷", "=",
        ".", "%", "(", ")", "^",
        "/", "√", "!", "π", "e"
    ]:
        if string[-1] == c:
            return True
    return False


# calculator class
class Calc(tk.Frame):
    def __init__(self, master: any) -> None:
        super().__init__(master)
        self.master = master

        # Window generation
        self.master.title("calculator")

        txt_font = tk.font.Font(
            family="Modem", underline=False, size=22
        )

        vc = self.master.register(test_char)
        self.txt = tk.Entry(
            self.master, background="black", foreground="lime",
            insertbackground="lime", font=txt_font,
            validate="key", validatecommand=(vc, "%P")
        )
        self.txt.grid(row=0, column=0, columnspan=5, sticky="ew")

        self.make_Widgets()
        return

    # Numerical input
    def input(self, num: any) -> any:
        self.txt.insert(tk.END, num)
        return

    # Delete all
    def all_clear(self) -> None:
        self.txt.delete(0, tk.END)
        return

    # Delete one line
    def one_clear(self) -> None:
        text = self.txt.get()
        self.txt.delete(0, tk.END)
        self.txt.insert(0, text[:-1])
        return

    # factorial calculation
    def factorial(self) -> None:
        try:
            num = int(self.txt.get())
            result = math.factorial(num)
            self.txt.delete(0, tk.END)
            self.txt.insert(0, result)
            return

        except ValueError:
            pass

    # pi calculation
    def pi(self) -> None:
        try:
            num = int(self.txt.get())
            result = math.pi * num
            self.txt.delete(0, tk.END)
            self.txt.insert(0, result)
            return

        except ValueError:
            pass

    # exp calculation
    def exp(self) -> None:
        try:
            num = int(self.txt.get())
            result = math.exp(num)
            self.txt.delete(0, tk.END)
            self.txt.insert(0, result)
            return

        except ValueError:
            pass

    # Displaying calculation results
    def equals(self) -> None:
        value = eval(
            self.txt.get()
            .replace('÷', '/').replace('×', '*')
            .replace('＋', '+').replace('－', '-')
            .replace('%', '%').replace('^', '**')
            .replace('√', "**(1/2)").replace("e", "2.71")
            .replace("π", "3.14")
        )
        self.txt.delete(0, tk.END)
        self.txt.insert(0, value)
        print(f"Answer : {value}")
        return

    # Button press determination
    def callback(self, event: any) -> None:
        event.widget.config()
        print(
            "button pressed : "
            + str(event.widget["text"])
        )
        input_txt = event.widget["text"]

        _ = [
            self.all_clear() if str(input_txt) in "AC" else
            self.equals() if str(input_txt) in "=" else
            self.factorial() if str(input_txt) in "!" else
            self.input(input_txt)
        ]
        return

    # Button generation
    def make_Widgets(self) -> None:
        btn_lst1 = ["+", "-", "×", "÷"]
        btn_lst2 = ["00", "0", "="]
        btn_lst3 = ["√", "!", ".", "^"]
        btn_lst4 = ["π", "e", "//", "%", "AC"]

        for i in range(1, 10):
            num_btn = tk.Button(self.master, text=i, width=10, height=5)
            num_btn.grid(row=3-(i-1)//3, column=(i-1)%3)
            num_btn.bind("<Button-1>", self.callback)
            continue

        for i, j in enumerate(btn_lst1):
            str_btn = tk.Button(self.master, text=j, width=10, height=5)
            str_btn.grid(row=i+1, column=3)
            str_btn.bind("<Button-1>", self.callback)
            continue

        for i, k in enumerate(btn_lst2):
            str_btn2 = tk.Button(self.master, text=k, width=10, height=5)
            str_btn2.grid(row=4, column=i)
            str_btn2.bind("<Button-1>", self.callback)
            continue

        for i, l in enumerate(btn_lst3):
            str_btn3 = tk.Button(self.master, text=l, width=10, height=5)
            str_btn3.grid(row=5, column=i)
            str_btn3.bind("<Button-1>", self.callback)
            continue

        for i, m in enumerate(btn_lst4):
            str_btn4 = tk.Button(self.master, text=m, width=10, height=5)
            str_btn4.grid(row=i+1, column=4)
            str_btn4.bind("<Button-1>", self.callback)
            continue


def main() -> None:
    root = tk.Tk()
    app = Calc(master=root)
    app.mainloop()
    return


if __name__ == "__main__":
    main()