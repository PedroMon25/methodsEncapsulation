from classWindow import Window

ventana = Window ()
ventana.setDimensions(500, 500)
ventana.setTitle("Mi primera App")
ventana.setResize(True)

print (ventana.getDimensions())
print (ventana.getResize())
print (ventana.getTitle())

ventana.crear_ventana()