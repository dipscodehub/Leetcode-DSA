# n -> Number of Disks
# src -> Source Tower
# aux -> Auxualary Tower
# des -> Destination Tower

def towerOfHanoi(n, src, des, aux):
    if n:
        towerOfHanoi(n-1, src, aux, des)
        print(f"move disk {n} from {src} to {des}")
        towerOfHanoi(n-1, aux, des, src)


src = "Tower A"
aux = "Tower B"
des = "Tower C"
n = 2
towerOfHanoi(n, src, des, aux)
