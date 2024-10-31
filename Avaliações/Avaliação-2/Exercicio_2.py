class Motor:
    def status(self):
        return 'Vrum Vrum'

class Pneu:
    def status(self):
        return 'Vrum!!'

class Veiculo:
    def status(self):
        motor_status= Motor.status(self)
        pneu_status= Pneu.status(self)
        return motor_status,"yes, its alive!!!!", pneu_status

v= Veiculo()
print(v.status())