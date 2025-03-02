import webbrowser

#это декоратор
#описание работы до какой-то ф -ции и после
def validator(func):
    def wrapper(url):
       if  '.' in url:
           #это твоя ф -ция
        func(url)
       else:
        print("incorrect url")
        #просто возврат ф-ции. не выполнение ,нет
        return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

    open_url("https://google.com")