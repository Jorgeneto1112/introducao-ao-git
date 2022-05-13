import math
def haversine(raio, lat1, long1, lat2, long2):
  lat1 = math.radians(lat1) 
  lat2 = math.radians(lat2) 
  long1 = math.radians(long1) 
  long2 = math.radians(long2) 

  a = math.sin((lat2-lat1)/2)**2
  b = math.cos(lat1)*math.cos(lat2)
  c = math.sin((long2-long1)/2)**2 

  raiz = math.sqrt(a + (b*c))

  d = 2*raio* math.asin(raiz)

  return d