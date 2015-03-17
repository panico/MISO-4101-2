from core_app.models import HistoryAlarmas, Inmueble, Elemento, Evento
import getpass
import datetime


class Alarma:        
    def reg_act_alarmas(self, id_estado, fech, id_inmb, id_elemen):
        
        ha = HistoryAlarmas(estado = id_estado, fecha = fech, user = self.request.user, inmueble  = id_inmb, 
                            elemento = id_elemen)
        ha.save()
        
    def consul_events(self, user_id, fech_1, fech_2):
        result = []
        results = {}

        inmbs = Inmueble.objects.all().filter(user = user_id)
        for im in inmbs:
            eventos = self.consul_events_inmb(inmueb_id = im.id, fecha1 = fech_1, fecha2 = fech_2)
            for x in eventos:
                result.append(x)
                
        results['eventos'] = result                    
        
        return results 
    
    def consul_events_inmb(self, inmueb_id, fecha1, fecha2): 
        result = []
        results = {}

        elems = Elemento.objects.all().filter(inmueble = inmueb_id)
        if (elems.__len__() > 0):           
            for e in elems:
                eventos = self.consul_events_elem(elem_id = e.id , fech_1 = fecha1, fech_2 = fecha2)
                for x in eventos:
                    result.append(x)
        else:
                eventos = "Inmueble sin elementos"
                result.append(eventos)
                
        results['eventos'] = result          
        return results
    
    def consul_events_elem(self, elem_id, fech_1, fech_2):
        results = {}

        if (fech_1 != None and fech_2 == None):
            eventos = Evento.objects.all().filter(elemento = elem_id, fecha = fech_1)                                                
        else:
            if (fech_2 != None):
                eventos = Evento.objects.all().filter(elemento = elem_id, fecha__range = [fech_1, fech_2])
            else:
                eventos = "Debe registrar la fecha inicial"
        
        results['eventos'] = eventos 
        return results
                                                
#    def consul_hist(self, fech_even1, fech_even2, fech_alr1, fech_alr2):