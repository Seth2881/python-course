class Car:
    def __init__(self,model:str,brand:str,power:float,fuel_tank:int,doorsCount:int=5) :
        self.model = model
        self.brand = brand
        self.power = power
        self.doorsCount = doorsCount
        self.is_started = False
        self.fuel_tank_max = fuel_tank
        self.fuel_tank = 0.8*fuel_tank
        self.conso_km_100 = 12.3

    def start(self) :
        if not self.is_started :
            print(f'votre {self.brand} {self.model} est démarré')
            self.is_started = True
        else :
            self.stop()

    def stop(self) :
        if not self.is_started :
            self.start()
        else :
            print(f'votre {self.brand} {self.model} est stoppé')
            self.is_started = False

    def forward(self,km) :
        if self.fuel_tank != 0 and self.is_started: 
            essence_conso = self.conso_km_100 * km / 100
            self.fuel_tank -= essence_conso if self.fuel_tank-essence_conso >= 0 else(self.fuel_tank)
            print(f"vous avez avancé de {km}km et avez dépensé {essence_conso}Litres d'essence")
        else :
            self.alerte_plein()

    def alerte_plein(self) :
        print('votre réservoir est vide, faites le plein !')

    def fill_fuel_tank(self) :
        if self.fuel_tank != self.fuel_tank_max and self.fuel_tank+5 < self.fuel_tank_max and not self.is_started:
            self.fuel_tank += 5
            print(f'votre réservoir est de {self.fuel_tank}/{self.fuel_tank_max}')
        else :
            print('votre réservoir est trop plein !')

####################################################################

from time import sleep  # juste pour rendre le test plus lisible

def test_car():
    print("\n=== CRÉATION DE LA VOITURE ===")
    voiture1 = Car(model="308", brand="Peugeot", power=130, fuel_tank=50)

    print(f"Modèle : {voiture1.brand} {voiture1.model}")
    print(f"Puissance : {voiture1.power} ch")
    print(f"Portes : {voiture1.doorsCount}")
    print(f"Réservoir : {voiture1.fuel_tank}/{voiture1.fuel_tank_max} L")
    print(f"Démarrée : {voiture1.is_started}")

    # 1️⃣ Test démarrage
    print("\n=== TEST DÉMARRAGE / ARRÊT ===")
    voiture1.start()   # devrait démarrer
    voiture1.start()   # devrait s'arrêter (car tu appelles stop() dans start())
    voiture1.start()   # redémarre

    # 2️⃣ Test forward (moteur allumé)
    print("\n=== TEST forward ===")
    voiture1.forward(20)   # avance de 20 km
    print(f"Réservoir restant : {voiture1.fuel_tank:.2f}/{voiture1.fuel_tank_max} L")

    # 3️⃣ Test forward (moteur éteint)
    print("\n=== TEST forward MOTEUR ÉTEINT ===")
    voiture1.stop()
    voiture1.forward(10)   # ne doit pas forward, doit appeler alerte_plein()

    # 4️⃣ Test consommation jusqu’à réservoir vide
    print("\n=== TEST CONSOMMATION TOTALE ===")
    voiture1.start()
    while voiture1.fuel_tank > 0:
        voiture1.forward(50)
        sleep(0.2)
        if voiture1.fuel_tank <= 0:
            break
    print(f"Réservoir vide : {voiture1.fuel_tank:.2f} L")

    # 5️⃣ Test alerte plein (tentative de rouler sans essence)
    print("\n=== TEST ALERTE PLEIN ===")
    voiture1.forward(10)

    # 6️⃣ Test remplissage (moteur allumé puis éteint)
    print("\n=== TEST REMPLISSAGE ===")
    voiture1.fill_fuel_tank()  # moteur allumé → ne doit pas fill
    voiture1.stop()
    for _ in range(12):  # tente de fill par paliers de 5 L
        voiture1.fill_fuel_tank()

    print(f"Réservoir final : {voiture1.fuel_tank}/{voiture1.fuel_tank_max} L")

# --- Lancement du test ---
if __name__ == "__main__":
    test_car()