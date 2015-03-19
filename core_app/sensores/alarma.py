from core_app.models import HistoryAlarmas
# Inmueble, Elemento, AlarmaParametro, Alarma, 
import getpass


class Alarma:        
    def reg_act_alarmas(self, id_param_alarma, id_inmb, id_estado, fech):
        
        ha = HistoryAlarmas(user = self.request.user, inmueble  = id_inmb, 
                            parametro = id_param_alarma, estado = id_estado, fecha = fech)
        ha.save()
        
    def consul_hist(self, fech_even1, fech_even2, fech_alr1, fech_alr2):