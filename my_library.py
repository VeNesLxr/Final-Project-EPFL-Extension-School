import flask
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from flask import render_template

app=flask.Flask("my_library")


#function to get html page
def get_html(page_name):
    html_file = open("templates/" + page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content


#function to get the books for the search request
def get_books_search():
    booksdb = open("booksdb.txt")
    content = booksdb.read()
    booksdb.close()
    books = content.split("---")
    if books == [""]:
        books = [elem.replace("", "You didn't add any book yet!") for elem in books]
    return books


#function to get the books for the books.html
def get_books():
    booksdb = open("booksdb.txt")
    content = booksdb.read()
    booksdb.close()
    books = content.split("\n")
    if books == [""]:
        books = [elem.replace("", "You didn't add any book yet!") for elem in books]
    return books


#function to get the wish to read list
def get_wish_list():
    toreadlistdb = open("toreadlistdb.txt")
    content = toreadlistdb.read()
    toreadlistdb.close()
    wishbooks = content.split("\n")
    if wishbooks == [""]:
        wishbooks = [elem.replace("", "Your list is still empty!") for elem in wishbooks]
    return wishbooks

#function to write on the wish to read list
def write_wish(wishread, author):
    file = open("toreadlistdb.txt", "a") 
    file.write("Book to read: " + wishread + "\n")
    file.write("Author: " +author+ "\n")
    file.write("---" + "\n" )
    file.close()
    return wishread + author

#function to count the occurences of a word
def count_occurences():
    file = open("booksdb.txt")
    text = file.read()
    new_text = text.lower()
    list_mot = new_text.split()
    file.close()
    list = []

    roman = list_mot.count("roman")
    list.append(roman)
    fiction = list_mot.count("fiction")
    list.append(fiction)
    biography = list_mot.count("biography")
    list.append(biography)
    novel = list_mot.count("novel")
    list.append(novel)
    poetry = list_mot.count("poetry")
    list.append(poetry)
    history = list_mot.count("history")
    list.append(history)
    unknown = list_mot.count("unknown")
    list.append(unknown)
    polar = list_mot.count("polar")
    list.append(polar)
    
    return list


class Book:
    
    #properties
    def __init__(self, title, author, genre, comment, ):
        self.title = title
        self.author = author
        self.genre = genre
        self.comment = comment

    ##methods
    #write info book in db.txt
    def write_info_book(self, file):   
    
        file = open("booksdb.txt", "a")
        file.write("Title: " +self.title +"\n")
        file.write("\t" + "Author: " + self.author + "\n")
        file.write("\t"+ "Genre: " + self.genre + "\n")
        file.write("\t"+ "Your comment: " + self.comment + "\n")
        file.write("---" + "\n")
        file.close()
    
    #delete a book in txt file
    def delete_book_txt(self):
        booksdb = open("booksdb.txt")
        content = booksdb.read()
        booksdb.close()
        books = content.split("---")
        
        newbooks = []
        title = flask.request.args.get("b")
        for book in books:
            if title.lower() not in book.lower():
                newbooks.append(book)
        open("booksdb.txt","w").write('---'.join(newbooks))
         

#go to homepage
@app.route("/")
def homepage():
    return get_html("index")

#go to books
@app.route("/books")
def to_books():
    html_page = get_html("books")
    books = get_books()
    all_books = ""
    for book in books:
        all_books += "<p>" + book + "</p>"
    
    return html_page.replace("$$BOOKS$$", all_books)
    

#go to wish-list
@app.route("/wishlist")
def wish_read():
    html_page = get_html("wishlist")
    wishes = get_wish_list()
    all_wishes = ""
    for wish in wishes:
        all_wishes += "<p>" + wish + "</p>"
    
    return html_page.replace("$$WISHES$$", all_wishes)    

#function to save the books
@app.route("/save")
def button_save():
    title = flask.request.args.get("a")
    author= flask.request.args.get("n")
    genre = flask.request.args.get("g")
    comment = flask.request.args.get("c")
    if genre == "":
        book = Book(title = title, author = author, genre = "Unknown", comment = comment)
        book.write_info_book(file= "booksdb.txt")
    else:
        book = Book(title = title, author = author, genre = genre, comment = comment)
        book.write_info_book(file= "booksdb.txt")
    
    html_page = get_html("save")
    return html_page.replace("$$SAVE$$", title +"\t" + author +"\t" + genre +"\t"+ comment)

#function to search a book by title, author or key-word
@app.route("/search")
def search_book():
    query = flask.request.args.get("q") 
    html_page = get_html("books")
    books = get_books_search()
    result = ""
    for book in books:
        if book.lower().find(query.lower()) != -1:
            result += "<p>" + book + "</p>"  
    if result == "":
        result+= "<p>" + "No result found" + "</p"
            
    return html_page.replace("$$BOOKS$$", result)

#function to delete the book
@app.route("/delete")
def delete():
    title = flask.request.args.get("b") 
    html_page =get_html("delete")
    
    if title == None or title == "":
        return html_page.replace("$$DELETE$$", "You didn't enter any book to delete")
    else:
        Book.delete_book_txt(self= title)
        return html_page.replace("$$DELETE$$", title.upper())
    

#function to add to wish to read list
@app.route("/add_to_wishlist")
def add_wish():
    wishread = flask.request.args.get("w")
    author = flask.request.args.get("f")
    wishes = write_wish(wishread, author)
    html_page = get_html("add_to_wish")

    return html_page.replace("$$SAVEWISHES$$", wishes)    


#function to delete a book from the wishlist
@app.route("/remove_from_wishlist")
def remove_from_wishlist():
    html_page = get_html("remove_from_wishlist")
    book_to_remove = flask.request.args.get("r")
    toreadlistdb = open("toreadlistdb.txt")
    content = toreadlistdb.read()
    toreadlistdb.close()
    wishbooks = content.split("---")

    newwishes = []
    for book in wishbooks:
        if book_to_remove.lower() not in book.lower():
            newwishes.append(book)
    open("toreadlistdb.txt","w").write('---'.join(newwishes))

    return html_page.replace("$$REMOVEWISHES$$", book_to_remove)


#function to go to the pie chart
@app.route("/image")
def pie_view():
    list_genre = count_occurences()
    
    mylabels ="Roman", "Fiction", "Biography", "Novel", "Poetry", "History", "Unknown", "Polar"
    size = list_genre

    plt.figure()
    fig1, ax1 =plt.subplots()
    ax1.pie(size, labels=mylabels, startangle=90)
    ax1.axis('equal')
    
    plt.savefig('static/images/pie.png')

    return render_template("image.html")

