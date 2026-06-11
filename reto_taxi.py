import json

# ============================================================
# RETO: Motor de tarifas de taxi
# Archivo de práctica — completa la función calcular_tarifa()
# ============================================================

def calcular_tarifa(hora, dia, llueve, distancia_km, zona):
    """
    Calcula la tarifa de un viaje en taxi según las reglas de negocio.

    Parámetros:
        hora        (int)  : 0-23
        dia         (str)  : "lunes", "martes", ..., "domingo"
        llueve      (bool) : True / False
        distancia_km(float): kilómetros del viaje
        zona        (str)  : "normal", "aeropuerto", "centro"

    Retorna:
        dict con "tarifa_final" (float) y "recargos" (list of str)
    """

    # --- TU CÓDIGO AQUÍ ---
    # Regla 1: tarifa base
    tarifa_base = 15 + 2.5 * distancia_km
    recargos = []
    multiplicador = 1.0
    total = 0

    # Regla 2: hora pico (7–9 AM o 5–8 PM en día laboral) → +25%
    # Pista: días laborales = lunes, martes, miércoles, jueves, viernes
    # TU CÓDIGO:
    dias_laborales = ["lunes","martes","miercoles","jueves","viernes"]
    if dia in dias_laborales and (7<= hora <=9 or 17 <= hora <= 20):
        multiplicador += 0.25 
        recargos.append("hora pico +25%")

    # Regla 3: noche (10 PM – 5 AM) → +30%
    # TU CÓDIGO:
    if hora >=22 or hora <=5:
        multiplicador += 0.30
        recargos.append("noche +30%")

    # Regla 4: fin de semana (sábado o domingo) → +15%
    # TU CÓDIGO:
    if dia in ["sabado", "domingo"]:
        multiplicador += 0.15
        recargos.append("fin de semana +15%")
    # Regla 5: lluvia → +10%
    # TU CÓDIGO:
    if llueve:
        multiplicador += 0.10
        recargos.append("lluvia +10%")

    # Regla 6: zona aeropuerto +$50 fijo / centro -$5
    # TU CÓDIGO:
    if zona == "aeropuerto":
        total += 50
        recargos.append("aeropuerto $50")
    if zona == "centro":
        total += -5
        recargos.append("centro -$5")

    total += tarifa_base * multiplicador

    # Regla 7: si total > $200, aplica 5% de descuento al excedente
    # Pista: excedente = total - 200 → total = 200 + excedente * 0.95
    # TU CÓDIGO:
    if total >200:
        excedente = total - 200
        total = 200 + excedente * 0.95
        recargos.append("descuento excedente -5%")
    
    return {
        "tarifa_final": round(total, 2),
        "recargos": recargos
    }


# ============================================================
# VERIFICADOR AUTOMÁTICO — no modifiques esta sección
# Carga prueba1.json y compara tus resultados
# ============================================================

def verificar():
    with open("prueba1.json", "r", encoding="utf-8") as f:
        datos = json.load(f)

    casos = datos["casos_de_prueba"]
    aprobados = 0

    print("\n" + "="*55)
    print("  VERIFICADOR DE RETO — Sistema de tarifas de taxi")
    print("="*55)

    for caso in casos:
        inp = caso["input"]
        esperado = caso["resultado_esperado"]["tarifa_final"]

        resultado = calcular_tarifa(
            hora         = inp["hora"],
            dia          = inp["dia"],
            llueve       = inp["llueve"],
            distancia_km = inp["distancia_km"],
            zona         = inp["zona"]
        )

        obtenido = resultado["tarifa_final"]
        ok = abs(obtenido - esperado) < 0.10   # margen de ±$0.10

        estado = "✓ CORRECTO" if ok else "✗ ERROR"
        if ok:
            aprobados += 1

        print(f"\nCaso {caso['id']}: {caso['descripcion']}")
        print(f"  Esperado : ${esperado:.2f}")
        print(f"  Obtenido : ${obtenido:.2f}  →  {estado}")
        if not ok:
            print(f"  Recargos aplicados: {resultado['recargos']}")

    print("\n" + "="*55)
    print(f"  Resultado: {aprobados}/{len(casos)} casos correctos")
    if aprobados == len(casos):
        print("  ¡Reto completado! Pasas al siguiente módulo.")
    else:
        print("  Revisa las reglas fallidas y vuelve a correr.")
    print("="*55 + "\n")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    # Prueba rápida con un solo caso antes de verificar todos:
    resultado_prueba = calcular_tarifa(
        hora=23,
        dia="viernes",
        llueve=True,
        distancia_km=8.5,
        zona="aeropuerto"
    )
    print("Prueba rápida (caso 1):", resultado_prueba)

    # Descomenta la siguiente línea cuando quieras verificar todos los casos:
    verificar()
