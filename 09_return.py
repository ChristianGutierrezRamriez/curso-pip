def find_volume(length=1, width=1, depth=1):
  return length * width * depth

print(find_volume(5,4,3))
print(find_volume(width=10))

def find_volume2(lenght=1, width=1, depth=1):
  return lenght*width*depth, width, 'hola'

result=find_volume2(5,4,3)
print(result)
print(result[0])
vol,wid,text=find_volume2(5,4,3)
print(vol, wid, text)