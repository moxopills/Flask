from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

blp = Blueprint('books', 'books', description='Operations on books')

books = []
next_id = 1

@blp.route('/books')
class BooksResource(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_book):
        global next_id
        book = {
            "id": next_id,
            "title": new_book['title'],
            "author": new_book['author']
        }
        next_id += 1
        books.append(book)
        return book

@blp.route('/books/<int:book_id>')
class BookResource(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((b for b in books if b['id'] == book_id), None)
        if book is None:
            abort(404, message="No Book LOL")
        return book

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, updated_data, book_id):
        book = next((b for b in books if b['id'] == book_id), None)
        if book is None:
            abort(404, message="No Book LOL")
        book['title'] = updated_data['title']
        book['author'] = updated_data['author']
        return book

    @blp.response(200, description="Book deleted successfully")
    def delete(self, book_id):
        global books
        book = next((b for b in books if b['id'] == book_id), None)
        if book is None:
            abort(404, message="No Book LOL")
        books = [b for b in books if b['id'] != book_id]
        return {"message": "Deleted Book"}
