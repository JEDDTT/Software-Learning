// book class

class Book {
  constructor(title, author, publisher, year, genre) {
    this.title = title;
    this.author = author;
    this.publisher = publisher;
    this.year = year;
    this.genre = genre;
  }
  changeTitle(newTitle) {
    this.title = newTitle;
  }
  changeAuthor(newAuthor) {
    this.author = newAuthor;
  }
}

export default Book;
