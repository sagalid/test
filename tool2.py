#!/bin/python3
import scapy.all
import sys

def write_pcap(capture, nombre):
    pcap_file = nombre+ ".pcap"
    scapy.all.wrpcap(pcap_file, capture)
    return pcap_file


def main():
    if len(sys.argv) == 3:
        nombre_captura = sys.argv[1]
        segundos = int(sys.argv[2])
    else:
        print(f"uso: {sys.argv[0]} <nombre_captura> <segundos>")
        exit()

    print("Snifeando... ", end="")
    capture = scapy.all.sniff(timeout=segundos, filter="")
    pcap_file = write_pcap(capture, nombre_captura)
    print("OK")

if __name__ == "__main__":
    main()

