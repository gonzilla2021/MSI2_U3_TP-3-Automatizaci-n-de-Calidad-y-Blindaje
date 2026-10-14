import unittest


def autorizar_venta(stock, cantidad, cliente_activo):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")

    autorizada = False

    if cliente_activo and stock >= cantidad:
        autorizada = True

    return autorizada


class TestAutorizarVenta(unittest.TestCase):
    def test_venta_autorizada(self):
        # Arrange: cliente activo y stock suficiente.
        stock, cantidad, cliente_activo = 8, 3, True

        # Act: ejecutar la función.
        resultado = autorizar_venta(stock, cantidad, cliente_activo)

        # Assert: la venta debe autorizarse.
        self.assertTrue(resultado)

    def test_cliente_inactivo(self):
        # Arrange: hay stock, pero el cliente está inactivo.
        stock, cantidad, cliente_activo = 8, 3, False

        # Act
        resultado = autorizar_venta(stock, cantidad, cliente_activo)

        # Assert
        self.assertFalse(resultado)

    def test_stock_insuficiente(self):
        # Arrange: el cliente está activo, pero faltan unidades.
        stock, cantidad, cliente_activo = 2, 3, True

        # Act
        resultado = autorizar_venta(stock, cantidad, cliente_activo)

        # Assert
        self.assertFalse(resultado)

    def test_cantidad_invalida(self):
        # Arrange: una venta de cero unidades es inválida.
        stock, cantidad, cliente_activo = 8, 0, True

        # Act: ejecutar y guardar la excepción producida.
        try:
            autorizar_venta(stock, cantidad, cliente_activo)
            error = None
        except ValueError as exc:
            error = exc

        # Assert: debe producirse una excepción controlada.
        self.assertIsInstance(error, ValueError)
        self.assertEqual(str(error), "La cantidad debe ser positiva")


if __name__ == "__main__":
    unittest.main()
