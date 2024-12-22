
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return "Название книги: {}, Автор: {}, Год издания: {}".format(self.title, self.author, self.year)

b = Book('Преступление и наказание', 'Ф.М.Достоевский', 1111)
print(b.get_info())


