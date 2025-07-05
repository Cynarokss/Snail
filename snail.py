#!/usr/bin/env python3
import time

print("        /^\\    /^\\")
print("       ( o )  ( o )")
print("        \\_/    \\_/")
print("        //     //     ___")
print("       //     //   ./   \\_")
print("      / ~----~/   /      \\")
print("    /         : ./   __   ~-")
print("   |  \\________):   /  \\   |")
print("   |        /   |  | o o|  |")
print("   |       |    |  \\_~_/   |")
print("   |        \\ __\\_____.   /")
print("    \\                ~--~/")
print("    .|                     ~-_")
print("   /__________________________~~_")

inicio = time.time()

try:
    while True:
        tiempo_actual = time.time()
        transcurrido = tiempo_actual - inicio
        minutos = int(transcurrido // 60)
        segundos = int(transcurrido % 60)
        print(f"\rR e l a x... S l o w  =  g o o d: {minutos:02d}:{segundos:02d}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nV e r y  s l o w... S n a i l t a s t i c.")
