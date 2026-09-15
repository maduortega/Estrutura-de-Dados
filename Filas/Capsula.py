class Produto:
    def __init__(self, serie, volume):
        self.serie = serie
        self.volume = volume
        
    def __str__(self):
        return f'N° de série: {self.serie} | Volume de O²: {self.volume}\n'
        