from decimal import Decimal, ROUND_HALF_UP


VAT_RATE = Decimal("0.24")


def hind_ilma_kaibemaksuta(hind_koos_kaibemaksuga: Decimal) -> Decimal:
	"""Tagasta 24% kaibemaksuga hinna netohind sentide tapsusega."""
	if hind_koos_kaibemaksuga < 0:
		raise ValueError("Hind ei saa olla negatiivne.")

	netohind = hind_koos_kaibemaksuga / (Decimal("1") + VAT_RATE)
	return netohind.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def main() -> None:
	sisend = input("Sisesta toote hind koos kaibemaksuga eurodes: ").strip()
	hind = Decimal(sisend.replace(",", "."))
	print(f"Hind ilma kaibemaksuta: {hind_ilma_kaibemaksuta(hind):.2f} EUR")


if __name__ == "__main__":
	main()
