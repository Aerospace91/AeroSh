import subprocess
import sys

def main():
    while True:
        command = input("AeroSh>")
        if command == 'exit':
            sys.exit(0)
        subprocess.run([command])

if __name__ == "__main__":
    main()
