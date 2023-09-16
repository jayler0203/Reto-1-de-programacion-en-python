print("Bienvenido a 'La Mansión de las Almas Perdidas', una misteriosa casa embrujada")
print("abandonada en lo profundo del bosque. Corren leyendas sobre su pasado oscuro y")
print("sucesos aterradores que tu valentía deberá enfrentar. ¿Estás listo para explorarla?")
    
decision1 = input("¿Te atreves a adentrarte en la casa? (si/no): ").lower()

while decision1 != "si" and decision1 != "no":
    print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
    decision1 = input("¿Te atreves a adentrarte en la casa? (si/no): ").lower()

if decision1 == "si":
    print("\nCon paso firme, cruzas el umbral de la casa. Un escalofrío recorre tu espalda mientras")
    print("la puerta se cierra detrás de ti. Te encuentras en una penumbra inquietante, con apenas")
    print("suficiente luz para distinguir las sombras que danzan en las paredes.")
    print("Escuchas susurros y crujidos, y sientes que no estás solo aquí.")
    
    print("\nDe repente, se abren dos puertas frente a ti. Una a la izquierda y otra a la derecha.")
    decision2 = input("¿Por cuál decides entrar? (izquierda/derecha): ").lower()
    
    while decision2 != "izquierda" and decision2 != "derecha":
        print("Respuesta inválida. Por favor, responde 'izquierda' o 'derecha'.")
        decision2 = input("¿Por cuál decides entrar? (izquierda/derecha): ").lower()
    
    if decision2 == "izquierda":
        print("Has elegido la puerta izquierda. Avanzas por un estrecho pasillo y encuentras una habitación oscura.")
        print("En el centro de la habitación hay un cofre. ¿Deseas abrirlo? (si/no): ")
        
        decision3 = input().lower()
        
        while decision3 != "si" and decision3 != "no":
            print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
            decision3 = input("¿Deseas abrir el cofre? (si/no): ").lower()
        
        if decision3 == "si":
            print("Al abrir el cofre, ¡un mímico salta y te ataca! Lamentablemente, has perdido. Fin del juego.")
        else:
            print("Decides no abrir el cofre. Retrocedes por el pasillo y encuentras una puerta que te lleva al jardín trasero.")
            print("Sales corriendo y te das cuenta de que has escapado con vida. ¡Felicidades!")
            
    elif decision2 == "derecha":
        print("Has elegido la puerta derecha. Avanzas por un pasillo lleno de cuadros oscuros y siniestros.")
        print("Uno de los cuadros parece moverse. ¿Lo examinas más de cerca? (si/no): ")
        
        decision4 = input().lower()
        
        while decision4 != "si" and decision4 != "no":
            print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
            decision4 = input("¿Lo examinas más de cerca? (si/no): ").lower()
        
        if decision4 == "si":
            print("Al examinar el cuadro, el suelo cede y caes en una trampa. Has perdido. Fin del juego.")
        else:
            print("Decides no examinar el cuadro. Retrocedes por el pasillo y encuentras una puerta que te lleva al jardín trasero.")
            print("Sales corriendo y te das cuenta de que has escapado con vida. ¡Felicidades!")
            
else:
    print("Decides no entrar y abandonar la casa. ¡Has escapado!")

