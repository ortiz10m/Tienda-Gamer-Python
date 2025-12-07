# Proyecto: Caja Registradora Tienda Gamer
# Autor: DavidEngineer (Estudiante @ FET)
# Fecha: Diciembre 2025
# Descripción: Sistema de ventas con un 'Easter Egg' (truco oculto) para resetear la cuenta.

print("--- 🎮 SYSTEM ONLINE: SHOCK FRAME STORE 🎮 ---")
print("Instrucciones: Escribe el precio del juego. Usa 0 para cerrar caja.")

# Variable acumuladora: Aquí iré guardando la suma total de la compra
total_a_pagar = 0

# Inicializo el precio en -1 solo para que el bucle arranque la primera vez.
# (Si lo pongo en 0, el while ni siquiera empieza).
precio = -1 

# Bucle principal: El programa no para hasta que yo escriba "0"
while precio != 0:
    texto = input("💲 Precio del juego: ")
    
    # OJO: Uso float y no int porque los precios pueden tener centavos (ej: 19.99)
    precio = float(texto)

    # --- ZONA DE TRUCOS (BACKDOOR) ---
    # Configuré mi día de cumpleaños (-19) como código de emergencia.
    # Esto sirve para cancelar la compra si el cliente se arrepiente o me equivoco.
    if precio == -19:
        print("🕵️‍♂️ ACCESO ADMIN DETECTADO: DavidEngineer")
        print("...Borrando memoria temporal...")
        print("...Cuenta reseteada a CERO. ¡Empezamos de nuevo!")
        total_a_pagar = 0  # Aquí ocurre la magia: borro la deuda.
        
    # Si no es el truco y tampoco es salir (0), entonces sumo el producto
    elif precio != 0:
        total_a_pagar = total_a_pagar + precio
        print(f"   💾 Agregado al carrito. Subtotal: ${total_a_pagar}")

# --- FASE DE COBRO Y DESCUENTOS ---
print("\n-----------------------------------")
print("Calculando factura final...")

# Regla de Negocio: Si compra más de $100, es VIP y recibe 20% off
if total_a_pagar > 100:
    print("🌟 ¡CLIENTE VIP DETECTADO!")
    print("Aplicando 20% de descuento automático.")
    
    # Matemáticas: Sacar el 20% es multiplicar por 0.20
    ahorro = total_a_pagar * 0.20
    precio_final = total_a_pagar - ahorro
    
    print(f"   Dinero ahorrado: ${ahorro}")
    print(f"✅ TOTAL A PAGAR: ${precio_final}")
    
else:
    # Si no alcanza el monto VIP, cobramos normal
    print("No aplica descuento VIP.")
    print(f"✅ TOTAL A PAGAR: ${total_a_pagar}")

print("-----------------------------------")
print("💻 Fin del programa. Corriendo en Linux.")
