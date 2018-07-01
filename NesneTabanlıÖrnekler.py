class arabalar():
    def __init__(self,üretici,model,beğeni):
        self.üretici=üretici
        self.model=model
        self.beğeni=beğeni
    def özellikgöster(self):
        print(""" Araç Detayları : 
        üretici: {}
        model: {}
        beğeni: {}
        """.format(self.üretici,self.model,self.beğeni))
golf=arabalar("vw","golf","10 üzerinden 8")
c180=arabalar("mercedes","c180","10 üzerinden 7")
fabia=arabalar("skoda","fabia","10 üzerinden 6.7")

arabalar.özellikgöster(golf)
arabalar.özellikgöster(c180)
arabalar.özellikgöster(fabia)

