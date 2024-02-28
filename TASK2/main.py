import eel

eel.init("GUI")

@eel.expose
async def add(num1, num2):
    result = num1 + num2
    return result
@eel.expose
async def sub(num1, num2):
    result = num1 - num2
    return result
@eel.expose
async def div(num1, num2):
    result = num1 / num2
    return result
@eel.expose
async def mult(num1, num2):
    result = num1 * num2
    return result
# def sin(num1, num2):
#     result = num1 + num2
#     return result
# def cos(num1, num2):
#     result = num1 + num2
#     return result
# def tan(num1, num2):
#     result = num1 + num2
#     return result
# def ln(num1, num2):
#     result = num1 + num2
#     return result
# def clear(num1, num2):
#     result = num1 + num2
#     return result
# def clear_one(num1, num2):
#     result = num1 + num2
#     return result


eel.start('index.html', size=(500, 600), chrome_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')