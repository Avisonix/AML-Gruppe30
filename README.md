Herunder er der ved 1 en beskrivelse af hvordan du henter alt det nødvendige for at begynde at kode videre på hvad der tidligere er lavet, og 2 en hurtigt rundown af hvad hver fil og mappe bruges til, der er uddybende beskrivelser under hver fil/mappe, hvis du gerne vil have yderlig forklaring. 

1
Er på vej skal lige laves




2
src/aml/
  __init__.py     → gør mappen til et Python-modul (kan være tom)
  cli.py          → 'startpunkt' (samler hele pipelinen)
  data.py         → indlæs rå data (CSV/Excel/API) → DataFrame
  preprocess.py   → rens data (NA, typer, duplikater, scaling)
  features.py     → lav/udvælg features, split i X (input) og y (target)
  train.py        → træn model (Kan fx starte med LinearRegression)
  evaluate.py     → mål hvor god modellen er (fx  R^2)

data/
  raw/            → rå data (originale filer, rør dem ikke direkte, men import dem til hvor du skal bruge dem)
  processed/      → rensede/færdigbearbejdede data

models/           → trænede modeller (.pkl), vil muligvis blive gitignore senere
reports/          → figurer/rapporter (plots, metrics), vil muligvis blive gitignore senere

tests/
  test_smoke.py   → meget simpel test, men mappen kan bruges til alle mulige test

.github/workflows/
  ci.yml          → Bliver ikke brugt til noget endnu

.gitignore        → sikrer vi ikke uforvarende pusher store/hemmelige filer
requirements.txt  → Python-pakker vi bruger
pyproject.toml    → Den indeholder ikke kode, kun indstillinger.
README.md         → denne fil
