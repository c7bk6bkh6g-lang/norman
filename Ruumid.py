tyyp = input(
	"Mis tüüpi ruumiga on tegemist (toitlustus, kaubandus, teenindus, sport, üritus)? "
).strip().lower()
pindala = int(input("Kui suur ruum on (m2)? "))
teenindajad = int(input("Mitu teenindajat ruumis on? "))

if tyyp == "sport":
	kokku_lubatud = pindala // 30
elif tyyp == "toitlustus":
	kokku_lubatud = pindala // 10
elif tyyp == "kaubandus":
	kokku_lubatud = pindala // 15
elif tyyp == "teenindus":
	kokku_lubatud = pindala // 10
elif tyyp == "üritus" or tyyp == "uritus":
	kokku_lubatud = pindala // 20
else:
	print("Tundmatu ruumitüüp!")
	raise SystemExit

kliente_lubatud = max(0, kokku_lubatud - teenindajad)

print()
print("Väljund:")
print(
	f"{pindala} m2 ruumi on lubatud maksimaalselt {kliente_lubatud} inimest"
	f" juhul kui ruumis on {teenindajad} teenindajat."
)
