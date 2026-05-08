"""
Problema 2: Knapsack Fraccionado
Paradigma: Greedy (Matroide ponderada + Greedy-choice property)
Ordena por densidad de valor (precio/peso) descendente y toma
tantas unidades como quepan de cada artículo.
"""

def knapsack_fraccionado(items, W):
    """
    items: lista de dicts con keys 'nombre', 'precio', 'peso', 'disponible'
           precio = valor total del artículo
           peso   = unidades disponibles (peso total del artículo)
           disponible = cuántas unidades (u's) hay
    W: capacidad máxima en u's
    Retorna (valor_total, detalle_tomado)
    """
    # Calcula densidad = precio por unidad de peso
    items_con_densidad = []
    for item in items:
        densidad = item['precio'] / item['disponible']  # precio por u
        items_con_densidad.append({**item, 'densidad': densidad})

    # Ordenar por densidad descendente (greedy choice)
    items_con_densidad.sort(key=lambda x: x['densidad'], reverse=True)

    valor_total = 0.0
    detalle = []
    capacidad_restante = W

    for item in items_con_densidad:
        if capacidad_restante <= 0:
            break
        # Tomar la menor cantidad entre lo disponible y lo que cabe
        tomar = min(item['disponible'], capacidad_restante)
        valor_ganado = tomar * item['densidad']
        valor_total += valor_ganado
        detalle.append({
            'nombre': item['nombre'],
            'unidades_tomadas': tomar,
            'valor_aportado': valor_ganado
        })
        capacidad_restante -= tomar

    return valor_total, detalle


def main():
    # Caso 1: ejemplo del enunciado
    # Item 1: 10u disponibles, $60 → densidad $6/u
    # Item 2: 20u disponibles, $100 → densidad $5/u
    # Item 3: 30u disponibles, $120 → densidad $4/u
    # Knapsack: 50u
    print("=== Caso 1 (ejemplo del enunciado, W=50) ===")
    items1 = [
        {'nombre': 'Item 1', 'precio': 60,  'disponible': 10},
        {'nombre': 'Item 2', 'precio': 100, 'disponible': 20},
        {'nombre': 'Item 3', 'precio': 120, 'disponible': 30},
    ]
    valor, detalle = knapsack_fraccionado(items1, 50)
    for d in detalle:
        print(f"  {d['nombre']}: {d['unidades_tomadas']} unidades → ${d['valor_aportado']:.2f}")
    print(f"  Valor total: ${valor:.2f}\n")

    # Caso 2: capacidad muy ajustada
    print("=== Caso 2 (W=15, 3 ítems) ===")
    items2 = [
        {'nombre': 'Oro',   'precio': 500, 'disponible': 10},
        {'nombre': 'Plata', 'precio': 200, 'disponible': 20},
        {'nombre': 'Bronce','precio': 50,  'disponible': 30},
    ]
    valor, detalle = knapsack_fraccionado(items2, 15)
    for d in detalle:
        print(f"  {d['nombre']}: {d['unidades_tomadas']} unidades → ${d['valor_aportado']:.2f}")
    print(f"  Valor total: ${valor:.2f}\n")

    # Caso 3: un solo ítem, capacidad mayor que disponible
    print("=== Caso 3 (W=100, 1 ítem con 30u) ===")
    items3 = [
        {'nombre': 'Diamante', 'precio': 900, 'disponible': 30},
    ]
    valor, detalle = knapsack_fraccionado(items3, 100)
    for d in detalle:
        print(f"  {d['nombre']}: {d['unidades_tomadas']} unidades → ${d['valor_aportado']:.2f}")
    print(f"  Valor total: ${valor:.2f}\n")

    # Caso 4: capacidad 0
    print("=== Caso 4 (W=0) ===")
    valor, detalle = knapsack_fraccionado(items1, 0)
    print(f"  Valor total: ${valor:.2f} (esperado $0.00)\n")


if __name__ == "__main__":
    main()
