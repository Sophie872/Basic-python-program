def convert(seconds):
   seconds = seconds % (24 * 3600)
   hour = seconds // 3600
   seconds %= 3600
   minutes = seconds // 60
   seconds %= 60
   return "%02d:%02d:%02d" % (hour, minutes, seconds) 
n = 23451
print(convert(n))



 #Lisbeth Mujica
