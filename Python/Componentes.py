from time import sleep
import psutil
import time
import os

while True: 

    os.system("cls")

    print("Suas informações estão sendo carregadas, por favor aguarde...")

    sleep(5)

    os.system("cls")

    print("-" * 43)
    print("-" * 20 + "CPU" + "-" * 20)
    print("-" * 43)

    cpu =  psutil.cpu_times(percpu = False)

    user_cpu = round(cpu.user, 2)
    system_cpu = round(cpu.system, 2)
    idle_cpu = round(cpu.idle, 2)
    interrupt_cpu = round(cpu.interrupt, 2)
    dpc_cpu = round(cpu.dpc, 2)

    print("Usuário da CPU: {}".format(user_cpu))
    print("Sistema da CPU: {}".format(system_cpu))
    print("Parada da CPU: {}".format(idle_cpu))
    print("Interrupção da CPU: {}".format(interrupt_cpu))
    print("DPC da CPU: {}".format(dpc_cpu))

    print("-" * 43)
    print("-" * 16 + "HD/HardDisk" + "-" * 16)
    print("-" * 43)

    hd = psutil.disk_usage('C:\\')

    total_hd = round(hd.total / (1024 ** 3), 2)
    used_hd = round(hd.used / (1024 ** 3), 2)
    free_hd = round(hd.free / (1024 ** 3), 2)
    percent_hd = hd.percent

    print("Total de espaço do HD: {}".format(total_hd))
    print("Total de espaço usado: {}".format(used_hd))
    print("Total de espaço livre: {}".format(free_hd))
    print("Porcentagem do HD utilizada: {}%".format(percent_hd))

    print("-" * 43)
    print("-" * 20 + "RAM" + "-" * 20)
    print("-" * 43)

    ram = psutil.virtual_memory()

    total_ram = round(ram.total / (1024 ** 3), 2)
    available_ram = round(ram.available / (1024 ** 3), 2)
    percent_ram = ram.percent
    used_ram = round(ram.used/ (1024 ** 3), 2)
    free_ram = round(ram.free/ (1024 ** 3), 2)

    print("total de espaço livre na RAM: {}".format(total_ram))
    print("Total acessível da RAM: {}".format(available_ram))
    print("Percentual utilizado da RAM: {}%".format(percent_ram))
    print("Espaço usado da RAM: {}".format(used_ram))
    print("Espaço livre da RAM: {}".format(free_ram))

    sleep(10)

