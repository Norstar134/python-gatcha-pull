## Rough unnormalised database - Limited Banners

| character_id (KEY)    | character_name  | character_rank    | character_path  | character_element | gatcha_banner | versions | pull amount   |
|-----------------------|-----------------|-------------------|-----------------|-------------------|---------------|----------|------|
| 1 | Seele | 5 star | The Hunt | Quantum | Butterfly on Swordtip | 1.0, 1.4 | 0
| 2 | Jing Yuan | 5 Star | Erudition | Lightning | Swirl of Heavenly Spear | 1.0, 2.0, 2.7 | 10
| 3 | Silver Wolf | 5 Star | Nihility | Quantum | Contract Zero | 1.1, 3.0 |  0
| 4 | Luocha | 5 Star | Abundance | Imaginary | Laic Pursuit | 1.1, 2.1 | 0
| 5 | Blade | 5 Star | Destruction | Wind | A Lost Soul | 1.2, 1.6 | 0
| 6 | Kafka | 5 Star | Nihility | Lightning | Indelible Coterie | 1.2, 1.6, 2.5 | 0
| 7 | Dan Heng IL | 5 Star | Destruction | Imaginary | Epochal Spectrum | 1.3, 2.0, 2.6 | 0
| 8 | Fu Xuan | 5 Star | Preservation | Quantum | Forseen, Foreknown, Foretold | 1.3, 2.2 | 0
| 9 | Jingliu | 5 Star | Destruction | Ice | Gentle Eclipse of the Moon | 1.4, 2.1 | 0
| 10 | Topaz & Numby | 5 Star | The Hunt | Fire | Sunset Clause | 1.4, 2.2  2.5 | 50
| 11 | Huohuo | 5 Star | Abundance | Wind | Bloom in Gloom | 1.5, 2.4 | 0
| 12 | Argenti | 5 Star | Erudition | Physical | Thorns of Scented Crown | 1.5, 2.3 | 0
| 13 | Ruan Mei | 5 Star | Harmony | Ice | Floral Triptych | 1.6, 2.3 | 0
| 14 | Dr. Ratio | 5 Star | The Hunt | Imaginary | Panta Rhei | 1.6 | 0
| 15 | Black Swan | 5 Star | Nihility | Wind | Indelible Coterie | 2.0, 2.5 | 0
| 16 | Sparkle | 5 Star | Harmony | Quantum | Sparkling Splendor | 2.0, 2.4 | 0
| 17 | Acheron | 5 Star | Nihility | Lightning | Words of Yore | 2.1, 2.6 | 0
| 18 | Adventurine | 5 Star | Preservation | Imaginary | Gilded Imprisonment | 2.1, 2.6 | 0
| 19 | Robin | 5 Star | Harmony | Physical | Just Intonation | 2.2, 2.5, 3.0 | 0
| 20 | Boothill | 5 Star | The Hunt | Physical | Dusty Trail's Lone Star | 2.2, 3.0 | 0
| 21 | Firefly | 5 Star | Destruction | Fire | Firefull Flyshine | 2.3, 2.7 | 0
| 22 | Jade | 5 Star | Erudition | Quantum | Lien on Life, Lease on Fate | 2.3, 3.0 | 0
| 23 | Yunli | 5 Star | Destruction | Physcial | Earth Hurled, Ether Curled | 2.4 | 0
| 24 | Jiaoqiu | 5 Star | Nihility | Fire | Cauldron Contrivance | 2.4 | 0
| 25 | Feixiao | 5 Star | The Hunt | Wind | Stormrider's Bolt | 2.5, 3.0 | 0
| 26 | Lingsha | 5 Star | Abundance | Fire | Let Scent Sink In | 2.5, 3.0 | 0
| 27 | Rappa | 5 Star | Erudition | Imaginary | Eyes of a Ninja | 2.6 | 0
| 28 | Sunday | 5 Star | Harmony | Imaginary | Eyes to the Stars | 2.7 | 0
| 29 | Fugue | 5 Star | Nihility | Fire | The Long Voyage Home | 2.7 | 0
| 30 | The Herta | 5 Star | Erudition | Ice | Message From Beyond | 3.0 | 0
| 31 | Algaea | 5 Star | Rememberance | Lightning | Time Woven Into Gold | 3.0 | 0

## 1NF

* There are only single valued attributes
* Attribute Domain does not change
* There is a unique name for every Attribute/Column
* The order in which data is stored does not matter

| character_id (KEY)    | character_name  | character_rank    | character_path  | character_element | gatcha_banner | versions | pull amount   |
|-----------------------|-----------------|-------------------|-----------------|-------------------|---------------|----------|------|
| 1 | Seele | 5 star | The Hunt | Quantum | Butterfly on Swordtip | 1.0 | 0
| 1 | Seele | 5 star | The Hunt | Quantum | Butterfly on Swordtip | 1.4 | 0
| 2 | Jing Yuan | 5 Star | Erudition | Lightning | Swirl of Heavenly Spear | 1.0 | 10
| 2 | Jing Yuan | 5 Star | Erudition | Lightning | Swirl of Heavenly Spear | 2.0 | 10
| 2 | Jing Yuan | 5 Star | Erudition | Lightning | Swirl of Heavenly Spear | 2.7 | 10
| 3 | Silver Wolf | 5 Star | Nihility | Quantum | Contract Zero | 1.1 |  0
| 3 | Silver Wolf | 5 Star | Nihility | Quantum | Contract Zero | 3.0 |  0
| 4 | Luocha | 5 Star | Abundance | Imaginary | Laic Pursuit | 1.1 | 0
| 4 | Luocha | 5 Star | Abundance | Imaginary | Laic Pursuit | 2.1 | 0
| 5 | Blade | 5 Star | Destruction | Wind | A Lost Soul | 1.2 | 0
| 5 | Blade | 5 Star | Destruction | Wind | A Lost Soul | 1.6 | 0
...

## 2NF

* Tables must be in 1NF
* Table must not have partial dependencies

### Character Table

| character_id (KEY) | character_name | character_rank | character_path | character_element |
|--------------|----------------|----------------|----------------|-------------------|
| 1 | Seele | 5 star | The Hunt | Quantum |
| 2 | Jing Yuan | 5 Star | Erudition | Lightning |
| 3 | Silver Wolf | 5 Star | Nihility | Quantum |
| 4 | Luocha | 5 Star | Abundance | Imaginary |
| 5 | Blade | 5 Star | Destruction | Wind  |
...

### Banner Table

| banner_id (KEY) | character_id (FOREIGN KEY) | banner_name | versions | pull_amount |
|-----------|-------------|-------------|----------|-------------|
| 1 | 1 | Butterfly on Swordtip | 1.0 | 0
| 1 | 1 | Butterfly on Swordtip | 1.4 | 0
| 2 | 2 | Swirl of Heavenly Spear | 1.0 | 10
| 2 | 2 | Swirl of Heavenly Spear | 2.0 | 10
| 2 | 2 | Swirl of Heavenly Spear | 2.7 | 10
| 3 | 3 | Contract Zero | 1.1 | 0
| 3 | 3 | Contract Zero | 3.0 | 0
| 4 | 4 | Laic Pursuit | 1.1 | 0
| 4 | 4 | Laic Pursuit | 2.1 | 0
| 5 | 5 | A Lost Soul | 1.2 | 0
| 5 | 5 | A Lost Soul | 1.6 | 0
...

## 3NF

* Must be in 1st and 2nd NF
* No non-primary-key attribute is transitively dependent on the primary key

| character_name (KEY) | character_rank | character_path | character_element |
|----------------------|----------------|----------------|-------------------|
| Seele | 5 star | The Hunt | Quantum |
| Jing Yuan | 5 Star | Erudition | Lightning |
| Silver Wolf | 5 Star | Nihility | Quantum |
| Luocha | 5 Star | Abundance | Imaginary |
| Blade | 5 Star | Destruction | Wind  |
...

| banner_id (KEY) | character_name (FOREIGN KEY) | banner_name | versions | pull_amount |
|-----------|-------------|-------------|----------|-------------|
| 1 | Seele | Butterfly on Swordtip | 1.0 | 0
| 1 | Seele | Butterfly on Swordtip | 1.4 | 0
| 2 | Jing Yuan | Swirl of Heavenly Spear | 1.0 | 10
| 2 | Jing Yuan | Swirl of Heavenly Spear | 2.0 | 10
| 2 | Jing Yuan | Swirl of Heavenly Spear | 2.7 | 10
| 3 | Silver Wolf | Contract Zero | 1.1 | 0
| 3 | Silver Wolf | Contract Zero | 3.0 | 0
| 4 | Luocha | Laic Pursuit | 1.1 | 0
| 4 | Luocha | Laic Pursuit | 2.1 | 0
| 5 | Blade | A Lost Soul | 1.2 | 0
| 5 | Blade | A Lost Soul | 1.6 | 0
...