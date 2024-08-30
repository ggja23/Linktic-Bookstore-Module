from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

class TestLinkticSaleOrderReturn(TransactionCase):

    def test_process_return(self):
        # Crear un cliente
        customer = self.env['linktic.customer'].create({
            'name': 'John Garcia',
            'contact_details': 'johngg@example.com'
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
                'quantity': 3,
                'price': 25.99
            })]
        })

        # Confirmar la orden
        sale_order.confirm_order()

        # Procesar una devolución parcial
        return_lines = {sale_order.order_line_ids[0]: 2}
        sale_order.process_return(return_lines)

        # Verificar cantidades y estado
        self.assertEqual(sale_order.order_line_ids[0].returned_quantity, 2, "La cantidad devuelta no es correcta")
        self.assertEqual(book.quantity_in_stock, 9, "La cantidad en stock no se actualizó correctamente")

        # Procesar devolución completa
        sale_order.process_return({sale_order.order_line_ids[0]: 1})
        self.assertEqual(sale_order.state, 'returned', "La orden no está en estado 'returned' después de la devolución completa")
