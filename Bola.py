class Bola:
    def __init__(self, canvas, x, y, diametro, velocidade_x, velocidade_y, cor):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diametro,diametro,fill=cor)
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
    def move(self):
        coordenadas = self.canvas.coords(self.image)
        if(coordenadas[2]>=(self.canvas.winfo_width()) or coordenadas[0]<0):
            self.velocidade_x = -self.velocidade_x
        if(coordenadas[3]>=(self.canvas.winfo_height()) or coordenadas[1]<0):
            self.velocidade_y = -self.velocidade_y
        self.canvas.move(self.image, self.velocidade_x, self.velocidade_y)
   
        