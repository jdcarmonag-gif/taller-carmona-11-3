def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("==================================")
    print("     CONVERSOR DE TEMPERATURA     ")
    print("==================================")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    
    opcion = input("Elige una opción (1 o 2): ")
    
    if opcion == '1':
        try:
            c = float(input("Ingresa la temperatura en Celsius: "))
            f = celsius_a_fahrenheit(c)
            print(f"\nResultado: {c}°C equivalen a {f:.2f}°F")
        except ValueError:
            print("\nError: Por favor, ingresa un número válido.")
            
    elif opcion == '2':
        try:
            f = float(input("Ingresa la temperatura en Fahrenheit: "))
            c = fahrenheit_a_celsius(f)
            print(f"\nResultado: {f}°F equivalen a {c:.2f}°C")
        except ValueError:
            print("\nError: Por favor, ingresa un número válido.")
            
    else:
        print("\nOpción no válida. Por favor, ejecuta el programa nuevamente.")

if __name__ == "__main__":
    main()
