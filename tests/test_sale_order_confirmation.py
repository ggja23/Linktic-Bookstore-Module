from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

class TestLinkticSaleOrder(TransactionCase):

    def test_confirm_order(self):
        # Crear un cliente
        customer = self.env['linktic.customer'].create({
            'name': 'John Doe',
            'contact_details': 'johndoe@example.com'
        })

        # Crear un autor y un libro
        author = self.env['linktic.author'].create({'name': 'Gabriel García Márquez'})
        book = self.env['linktic.book'].create({
            'title': 'Cien Años de Soledad',
            'author_id': author.id,
            'price': 25.99,
            'quantity_in_stock': 10
        })

        # Crear una orden de venta con líneas
        sale_order = self.env['linktic.sale.order'].create({
            'customer_id': customer.id,
            'order_line_ids': [(0, 0, {
                'book_id': book.id,
                'quantity': 2,
                'price': 25.99
            })]
        })

        # Confirmar la orden
        sale_order.confirm_order()

        # Verificar el estado y la cantidad de stock
        self.assertEqual(sale_order.state, 'confirmed', "La orden no está en estado 'confirmed'")
        self.assertEqual(book.quantity_in_stock, 8, "La cantidad en stock no se actualizó correctamente")

        # Intentar confirmar nuevamente (debería fallar)
        with self.assertRaises(UserError):
            sale_order.confirm_order()
