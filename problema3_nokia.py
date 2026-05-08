"""
Problema 3: Combinaciones en teclado Nokia 3230
Teclado:
  1 2 3
  4 5 6
  7 8 9
  * 0 #

Movimientos válidos: arriba, abajo, izquierda, derecha
Teclas prohibidas: * y #
Paradigma: Programación Dinámica (subestructura óptima + subproblemas traslapados)

Relación de recurrencia:
  f(d, 1) = 1                          para todo d en {0..9}
  f(d, k) = Σ f(v, k-1)  para v en ADJ[d],  k > 1

Respuesta = Σ f(d, n) para d en {0..9}
"""

# Posiciones en la grilla 4×3:
# (fila, col) de cada dígito
POSICION = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
    '*': (3, 0), '0': (3, 1), '#': (3, 2),
}

GRILLA = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#'],
]

PROHIBIDAS = {'*', '#'}
DIGITOS_VALIDOS = [str(d) for d in range(10)]  # 0-9


def construir_adyacencias():
    """
    Para cada dígito válido (0-9), calcula sus vecinos válidos
    (arriba, abajo, izquierda, derecha) excluyendo * y #.
    """
    adyacencias = {}
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izq, der

    for digito in DIGITOS_VALIDOS:
        fila, col = POSICION[digito]
        vecinos = [digito]  # puede presionarse la misma tecla (quedarse)
        for df, dc in direcciones:
            nf, nc = fila + df, col + dc
            if 0 <= nf < 4 and 0 <= nc < 3:
                vecino = GRILLA[nf][nc]
                if vecino not in PROHIBIDAS:
                    vecinos.append(vecino)
        adyacencias[digito] = vecinos

    return adyacencias


ADJ = construir_adyacencias()


def nokia_dp(n):
    """
    Cuenta combinaciones de n dígitos usando DP bottom-up.
    dp[d] = número de combinaciones de longitud k que terminan en dígito d
    """
    if n == 0:
        return 0

    # Caso base: longitud 1 → una combinación por cada dígito válido
    dp = {d: 1 for d in DIGITOS_VALIDOS}

    for _ in range(2, n + 1):
        tmp = {d: 0 for d in DIGITOS_VALIDOS}
        for d in DIGITOS_VALIDOS:
            for vecino in ADJ[d]:
                tmp[d] += dp[vecino]
        dp = tmp

    return sum(dp.values())


def nokia_dp_con_detalle(n):
    """Versión que también retorna las combinaciones si n es pequeño (≤ 3)."""
    if n > 3:
        return nokia_dp(n), []

    def generar(actual, longitud_restante):
        if longitud_restante == 0:
            return [actual]
        combinaciones = []
        ultimo = actual[-1]
        for vecino in ADJ[ultimo]:
            combinaciones.extend(generar(actual + vecino, longitud_restante - 1))
        return combinaciones

    todas = []
    for d in DIGITOS_VALIDOS:
        todas.extend(generar(d, n - 1))

    return len(todas), sorted(todas)


def main():
    print("Adyacencias del teclado Nokia:")
    for d in DIGITOS_VALIDOS:
        print(f"  {d} → {ADJ[d]}")
    print()

    # Casos de prueba
    casos = [1, 2, 3, 4, 5, 10]
    for n in casos:
        if n <= 3:
            total, combis = nokia_dp_con_detalle(n)
            print(f"n={n}: {total} combinaciones")
            if n <= 2:
                print(f"  {combis}")
        else:
            total = nokia_dp(n)
            print(f"n={n}: {total} combinaciones")
    print()

    # Verificación del ejemplo del enunciado: n=2 → 36
    total_n2, _ = nokia_dp_con_detalle(2)
    print(f"Verificación n=2: {total_n2} (esperado: 36) → {'✓ CORRECTO' if total_n2 == 36 else '✗ ERROR'}")


if __name__ == "__main__":
    main()
