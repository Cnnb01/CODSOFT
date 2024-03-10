from tkinter import Tk, Text, Button, Label
import random
# creating a window
window = Tk()
# window title
window.title("Charity's random password generator")
# window size
window.geometry("600x400")

def generatePswd(n):
    charss = "~`!1@2#3$4%5^6&7*8(90)-_=+qwertyuiopasdfhjklzxcvbnm{[]}\|;:,.<>/?"
    ourPswd = "".join(random.choice(charss) for _ in range(n))
    
    return ourPswd

# inputing a value
def inputVal():
    try:
        length = int(T.get("1.0", "end-1c"))
        if length < 12:
            result_label.config(text="Password should be 12 or above characters for higher security")
        else:
            ourPswd = generatePswd(length)
            result_label.config(text=f"Your new generated password is: {ourPswd}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# inputing textbox
T = Text(window, height=1, width=10, bg='pink')
T.pack(pady=10)

#button
Button(window, text='Click to generate', font=('normal', 10), bg='hot pink', command=inputVal).pack()

# Label to display the result
result_label = Label(window, text="", font=('normal', 10))
result_label.pack(pady=10)

window.mainloop()
# if __name__ == "__main__":
#     n = int(input("Enter the password length you'd prefer(recommended 12 characters or above): "))
#     if n < 12:
#         print("Should be 12 or above characters for higher security")
#     else:
#         ourPswd = generatePswd(n)
#         print("Your new generated password is: ", ourPswd)
        