"""
Problema 1: Hacer Sencillo (Coin Change)
Denominaciones: {1, 5, 10, 25}
Paradigma: Greedy (Matroide ponderada)
"""

def hacer_sencillo(m):
    """
    Dado un monto m (en centavos), retorna la lista de monedas usadas
    y el total de monedas para alcanzar m con la menor cantidad posible.
    Greedy: siempre toma la moneda de mayor denominación posible.
    """
    denominaciones = [25, 10, 5, 1]
    resultado = {}
    total_monedas = 0

    for d in denominaciones:
        if m >= d:
            cantidad = m // d
            resultado[d] = cantidad
            total_monedas += cantidad
            m = m % d

    return resultado, total_monedas


def main():
    casos = [
        293,   # Q2.93 → 11×25 + 1×10 + 1×5 + 3×1 = 16 monedas
        100,   # Q1.00 → 4×25
        41,    # Q0.41 → 1×25 + 1×10 + 1×5 + 1×1
        1,     # Q0.01 → 1×1
        0,     # Q0.00 → sin monedas
        999,   # Q9.99
    ]

    for monto in casos:
        monedas, total = hacer_sencillo(monto)
        print(f"Monto: Q{monto // 100}.{monto % 100:02d} ({monto} centavos)")
        for denom, cant in monedas.items():
            if cant > 0:
                print(f"  {cant} moneda(s) de Q0.{denom:02d}")
        print(f"  Total de monedas: {total}")
        print()


if __name__ == "__main__":
    main()
