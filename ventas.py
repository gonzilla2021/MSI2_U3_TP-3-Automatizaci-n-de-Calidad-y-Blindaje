def autorizar_venta(stock, cantidad, cliente_activo):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")

    autorizada = False

    if cliente_activo and stock >= cantidad:
        autorizada = True

    return autorizada
