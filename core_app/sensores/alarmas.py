from core_app.models import HistoryAlarmas, Inmueble, Elemento, Evento
import getpass
import datetime
from MySmartHome.settings import NAME_DB, USER_DB, HOST_DB, PWD_DB
import psycopg2

class Alarma:        
    
    def reg_act_alarmas(self, id_estado, fech, id_inmb, id_elemen):
        
        ha = HistoryAlarmas(estado = id_estado, fecha = fech, user = self.request.user, inmueble  = id_inmb, 
                            elemento = id_elemen)
        ha.save()
        
    def consul_events(self, user_id, fech_1, fech_2):
        result = []

        inmbs = Inmueble.objects.all().filter(user = user_id)
        
        for im in inmbs:
            result.extend(list(self.consul_events_inmb(inmueb_id = im.id, fecha1 = fech_1, fecha2 = fech_2, sw = '0')))
        
        return result 
    
    def consul_events_inmb(self, inmueb_id, fecha1, fecha2, sw): 
        result = []

        elems = Elemento.objects.all().filter(inmueble = inmueb_id)
        if (elems.__len__() > 0):           

            for e in elems:
                result.extend(list(self.consul_events_elem(elem_id = e.id , fech_1 = fecha1, fech_2 = fecha2)))
                        
        else:
            if (sw == '1'):
                eventos = "Inmueble sin elementos"
                result.append(eventos) 
                 
        return result
    
    def consul_events_elem(self, elem_id, fech_1, fech_2):
        result  = []
        
        if (fech_1 != None and fech_2 == None):            
            for x in list(Evento.objects.all().filter(activo = elem_id, fecha_hora_evento__gte = fech_1
                        ).select_related(' evento__sensor__elemento__inmueble', 'evento__sensor__tiposensor'
                        ).values('nombre', 'fecha_hora_evento', 'codigo', 'sensor__tiposensor__nombre', 
                        'sensor__elemento__inmueble__nombre', 'sensor__elemento__nombre', 'sensor__nombre'
                        ).order_by('-fecha_hora_evento')[:20]):
                        #'prioridad', 
                result.append(x)
                                                         
        else:
            if (fech_2 != None and fech_1 != None):
                for x in list(Evento.objects.all().filter(elemento = elem_id, fecha__range = [fech_1, fech_2]
                            ).select_related('evento__elemento__inmueble', 'evento__sensor').values(
                            'nombre', 'fecha', 'codigo', 'prioridad', 'tipoEven', 'elemento__inmueble__nombre', 
                            'elemento__nombre', 'sensor__nombre').order_by('-fecha')[:20]):
                
                    result.append(x)
            
            else:
                if (fech_1 == None and fech_2 != None):
                    for x in list(Evento.objects.all().filter(elemento = elem_id, fecha__lte = fech_2
                                ).select_related('evento__elemento__inmueble', 'evento__sensor').values(
                                'nombre', 'fecha', 'codigo', 'prioridad', 'tipoEven', 'elemento__inmueble__nombre', 
                                'elemento__nombre', 'sensor__nombre').order_by('-fecha')[:20]):
                    #Evento.objects.get(Q(question__startswith='Who'), Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))
                        result.append(x)
                
                else:
                                      
                    for x in list(Evento.objects.all().filter(elemento = elem_id).select_related(
                                'evento__elemento__inmueble', 'evento__sensor').values('nombre', 'fecha', 
                                'codigo', 'prioridad', 'tipoEven', 'elemento__inmueble__nombre', 
                                'elemento__nombre', 'sensor__nombre').order_by('-fecha')[:20]):
                        result.append(x)

        return result
               
#    def consul_hist(self, fech_even1, fech_even2, fech_alr1, fech_alr2):