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

        inmbs = Inmueble.objects.all().filter(user = user_id)
        for im in inmbs:
            eventos = self.consul_events_inmb(inmueb_id = im.id, fecha1 = fech_1, fecha2 = fech_2, sw = '0')
            for x in eventos:
                result.append(x)
        
        return result 
    
    def consul_events_inmb(self, inmueb_id, fecha1, fecha2, sw): 
        result = []

        elems = Elemento.objects.all().filter(inmueble = inmueb_id)
        if (elems.__len__() > 0):           
            for e in elems:
                eventos = self.consul_events_elem(elem_id = e.id , fech_1 = fecha1, fech_2 = fecha2)
                for x in eventos:
                    result.append(x)
        else:
            if (sw == '1'):
                eventos = "Inmueble sin elementos"
                result.append(eventos) 
                 
        return result
    
    def consul_events_elem(self, elem_id, fech_1, fech_2):
        result = []
        
        if (fech_1 != None and fech_2 == None):
            eventos = Evento.objects.all().filter(elemento = elem_id, fecha__gte = fech_1).order_by('-fecha')[:20]
            for x in eventos:
                    result.append(x)                                                            
        else:
            if (fech_2 != None and fech_1 != None):
                eventos = Evento.objects.all().filter(elemento = elem_id, fecha__range = [fech_1, fech_2]).order_by('-fecha')[:20]
                for x in eventos:
                    result.append(x)
            else:
                if (fech_1 == None and fech_2 != None):
                    eventos = Evento.objects.all().filter(elemento = elem_id, fecha__lte = fech_2).order_by('-fecha')[:20]
                    #Evento.objects.get(Q(question__startswith='Who'), Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))
                    for x in eventos:
                        result.append(x)
                else:
#                    eventos = reversed(Evento.objects.filter(elemento = elem_id).order_by('-fecha').reverse()[:limit])
                    eventos = Evento.objects.filter(elemento = elem_id).order_by('-fecha')[:20]
                    for x in eventos:
                        result.append(x)
        return result
                                                
#    def consul_hist(self, fech_even1, fech_even2, fech_alr1, fech_alr2):