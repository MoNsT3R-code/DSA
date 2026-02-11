class Person(object):

    def __init__ (self, name, id_number):

        self.name = name
        self.id_number = id_number

    def display(self):

        print(self.name, self.id_number)

    def get_profile(self):

        return f"{self.name}, {self.age}"

class Student(Person):

    def __init__ (self, name, id_number, semester):
        super().__init__(name, id_number)

        self.semester = semester
        self.borrow_book = []

    def addborrowedbook(self, Book, Borrowed_date):

            Borrowed_book = Borrowedbook(Book, Borrowed_date)
            self.Borrowed_books.append(Borrowed_book)

    def get_details(self):
        

        return f'{self.name}, {self.id_number}, {self.semester}, {self.borrow_book}'

class Librarian(Person):

    def __init__ (self, name, id_number, staff_id, shift, display_student_list
):
        super().__init__(name, id_number)

        self.staff_id = staff_id
        self.shift = shift
        self.display_student_list = display_student_list

class Book(object):

    def __init__ (self, title, author, isbn):

        self.title = title
        self.author = author
        self.isbn = isbn

class Borrowedbook(Book):

    def __init__ (self, Book, Borrow_date):
        
        self.Book = Book
        self.Borrow_date = Borrow_date


book1 = Book("Clean Code", "Robert Martin", "12345")
book2 = Book("Python 101", "Mike", "99999")
borrowed1 = BorrowedBook(book1, "2024-05-01")
borrowed2 = BorrowedBook(book2, "2024-05-05")
student = Student("Zain", 102, 5)
student.borrowed_books.extend([borrowed1, borrowed2])
librarian = Librarian("Huma", 201, "Evening")
librarian.students.append(student)
print_profiles([student, librarian])

'''

def helper(x):              #1
    count = 0               #1
    for i in range(x):      #n
        count += 1          #n
        return count        #1
def q2(n):                  #1
    total = 0               #1
    for j in range(1, n + 1): #n
        total += helper(j)    #1+2+3+...+n
        return total          #1

#it is the series of sum 1+2+3+...+n, let n = k, 1+2+3+...+k, (k(k+1))/2, (k^2+k)/2 = k^2 + k = n^2+n
#In big O we take the largest exponent digit so here the value of Big O is n^2

def q3(n):                     #1
    total = 0                  #1
    i = 1                      #log3(n)
    while i <= n:              #10log3(n)
        for j in range(10):    #10log3(n)
            total += 1         #10log3(n)
        i *= 3                 
    return total               #1

#the time complexity is log3n*10, as in while loop i<=n and i*=3 so we conclude that the value of n will be within 100
#10log3n

def q4(n):                  #1
    total = 0               #1
    for i in range(1, n + 1): #n
        for j in range(1, n + 1):  #n*n
            total += 1             #n
            if total > n:          #n
                break              #1
    return total                   #1

#n**2
'''