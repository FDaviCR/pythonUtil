seconds = 34.00373729999998
minutes = seconds // 60
hours = minutes // 60

print ("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))
print ("%02d:%02d" % (minutes, seconds % 60))
