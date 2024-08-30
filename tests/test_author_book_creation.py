from odoo.tests.common import TransactionCase

class TestLinkticAuthorBookCreation(TransactionCase):

    def test_create_author_and_book(self):
        # Crear un autor
        author = self.env['linktic.author'].create({
            'name': 'Gabriel García Márquez',
            'biography': 'Famoso autor colombiano.'
        })
        self.assertTrue(author.id, "El autor no se ha creado correctamente")

        # Crear un libro asociado al autor
        book = self.env['linktic.book'].create({
            'title': 'Cien Años de Soledad',
            'author_id': author.id,
            'published_date': '1967-05-30',
            'isbn': '978-3-16-148410-0',
            'price': 25.99,
            'quantity_in_stock': 100
        })
        self.assertTrue(book.id, "El libro no se ha creado correctamente")
        self.assertEqual(book.author_id.id, author.id, "El libro no está asociado correctamente al autor")
