import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Интерфейс для смены MAC адреса")
    parser.add_option("-m", "--mac", dest="new_mac", help="Введите новый MAC адрес")
    (options, arguents) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Неверный интерфейс")
    elif not options.new_mac:
        parser.error("[-] Неверный MAC адрес ПРИМЕР:(00:11:22:33:44:55)")
    return  options

def change_mac(interface, new_mac):
    print("[+] Для интерфейса " + interface + " присвоен новый MAC адрес: " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)