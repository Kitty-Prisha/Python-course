class breeds:
    species="dog"
    def __init__(self,color,behaviour):
        self.color=color
        self.behaviour=behaviour
Golden_retriever=breeds("Golden yellow","Intelligent")
German_Shephard=breeds("Brown orange","watchful") 
print(Golden_retriever.species)
print(German_Shephard.species) 
print("Golden retrievers are ",Golden_retriever.color,"And they are ",Golden_retriever.behaviour) 
print("German Shephards are ",German_Shephard.color,"And they are ",German_Shephard.behaviour)         