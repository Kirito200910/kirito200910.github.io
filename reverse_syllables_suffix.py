"""
reverse_syllables_suffix.py
---------------------------
Pequeña utilidad CLI en Python que toma una palabra (o una frase) por
entrada, invierte el orden de las sílabas de cada palabra y añade el
sufijo "pa" al final de cada palabra resultante.

Ejemplo:
    Entrada:  "palabra bonita"
    Salida :  "bralapa nitabona pa"

Sustituyendo las sílabas:
  - palabra -> pa | la | bra  => bra la pa  -> bralapa
  - bonita  -> bo | ni | ta   => ta ni bo   -> tanibo + pa -> tanibopa

Uso:
    python reverse_syllables_suffix.py

Se puede importar la función `transform` desde otros scripts.
"""

import re
import sys
from typing import List

# Conjunto de vocales (incluye vocales acentuadas y diéresis)
VOWELS = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"

# Expresión regular muy simplificada para separar sílabas en castellano.
#   1) Onset (consonantes antes del núcleo)   -> [^vowel]*
#   2) Núcleo (grupo de vocales contiguas)     -> [vowel]+
#   3) Coda especial con 'y' + vocal opcional  -> (?:y[vowel]+)?
_SYLLABLE_RE = re.compile(
    rf"[^{VOWELS}]*[{VOWELS}]+(?:y[{VOWELS}]+)?",
    re.IGNORECASE,
)

def syllabify(word: str) -> List[str]:
    """Divide *word* en sílabas (algoritmo muy simple)."""
    if not word:
        return []

    syllables = _SYLLABLE_RE.findall(word)

    # Si sobran consonantes al final (por la simplicidad de la regex),
    # se añaden a la última sílaba.
    consumed = "".join(syllables)
    leftover = word[len(consumed):]
    if leftover and syllables:
        syllables[-1] += leftover
    elif leftover:
        syllables.append(leftover)

    return syllables

def transform_word(word: str, suffix: str = "pa") -> str:
    """Invierte las sílabas de *word* y añade *suffix*."""
    sylls = syllabify(word)
    reversed_word = "".join(reversed(sylls))
    return reversed_word + suffix

def transform_sentence(sentence: str, suffix: str = "pa") -> str:
    """Procesa cada palabra de la sentencia."""
    return " ".join(transform_word(w, suffix) for w in sentence.split())


def main(argv=None):
    argv = argv or sys.argv[1:]
    if argv:
        # Si se pasan argumentos, se tratan como una frase completa.
        input_text = " ".join(argv)
        print(transform_sentence(input_text))
        return

    print("Escribe una palabra o frase (CTRL+D para salir):")
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(transform_sentence(line))
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
