#!/usr/bin/env python3

from HCS import HCS

def interpret_loop():
    hcs = HCS()
    while True:
        print(">> ", end="")
        try:
            command = input()
        except EOFError as e:
            print()
            return            
        if command in ['quit', 'exit']:
            return
        try:
            print(hcs.eval(command))
        except Exception as e:
            print("Error: \n" + repr(e))        

if __name__ == '__main__':
    interpret_loop()