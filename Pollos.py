class Pollo:
  #metodos constructores
  def __init__(self, id_pollo, dato_edad):
    #atributos de la clase (get y set)
      self.codigo_pollo = id_pollo
      self.edad_pollo = dato_edad
    #llamados de otras clases
    self.objBase_datos = base_datos() # el objeto de la clase
  
#metodos publicos de modificar atributos
def getCodigo_pollo(self):
  return self.codigo_pollo

def setCodigo_pollo(self,codigo_pollo):
  self.codigo_pollo = codigo_pollo

#Metodos para conextar base datos
def guardar_pollo(self):
  self.objBase_datos.guardar_pollo(obj_pollo)
  
