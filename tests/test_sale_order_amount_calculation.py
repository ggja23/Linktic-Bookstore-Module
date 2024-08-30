from odoo.tests.common import TransactionCase

class TestLinkticSaleOrderAmountCalculation(TransactionCase):

    def test_total_amount_calculation(self):
        # Crear un cliente
        customer = self.env['linktic.customer'].create({
            'name': 'John Doe',
            'contact_details': 'johndoe@example.com'
        })

        # Crear un autor y un libro
        author = self.env['linktic.author'].create({'name': 'Gabriel García Márquez'})
        book1 = self.env['linktic.book'].create({'title': 'Cien Años de Soledad', 'author_id': author.id, 'price': 25.99})
        book2 = self.env['linktic.book'].create({'title': 'El Amor en los Tiempos del Cólera', 'author_id': author.id, 'price': 19.99})

        # Crear una orden de venta con varias líneas
        sale_order = self.env['linktic.sale.order'].create({
            'customer_id': customer.id,
            'order_line_ids': [
                (0, 0, {'book_id': book1.id, 'quantity': 2, 'price': 25.99}),
                (0, 0, {'book_id': book2.id, 'quantity': 1, 'price': 19.99})
            ]
        })

        # Verificar el cálculo del monto total
        self.assertEqual(sale_order.total_amount, 71.97, "El monto total calculado no es correcto")
