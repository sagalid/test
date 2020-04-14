#!/bin/python3

import sys
import subprocess

def main():
    print(f"El nombre del script que se esta ejecutando es: {sys.argv[0]}")
    if len(sys.argv) > 3 or len(sys.argv) <=2:
        print(f"""
            python3 {sys.argv[0]} 1.1.1.1 3 
        """)
    else:
        try:
            subprocess.call(['ping', sys.argv[1], "-c", sys.argv[2]])
        except KeyboardInterrupt:
            print("gracias!")
            exit()
if __name__ == "__main__":
    main()
