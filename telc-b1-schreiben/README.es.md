<!-- Translated from README.md at commit 2304a0a. Re-translate when the English version changes. -->

# telc-b1-schreiben — cómo usarlo

**🌍 Languages:** [English](README.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [فارسی](README.fa.md) · **Español**

Tu entrenador estricto para la **carta escrita** del examen telc **Deutsch B1** (el
*Schriftlicher Ausdruck* — la carta/correo de respuesta que se escribe a mano). Enseña el formato
y el criterio de corrección exacto de telc, te da tareas en formato de examen, corrige tus cartas como lo
hacen los correctores reales de telc, ejercita los errores concretos que sueles cometer y va
desarrollando un banco de frases fluidas de B1 con seguimiento hasta que las dominas. Objetivo: **aprobar**,
no la perfección.

> Esta es la mitad de *escritura* del entrenador. La mitad de comprensión lectora/auditiva/gramática/oral vive en
> la skill complementaria **`telc-b1-exam`**, que cede el control a esta cada vez que trabajas en
> la carta. Instala las dos.

## Inicio rápido
1. Instala la skill (consulta el README del repositorio para saber cómo, en Claude y otras IAs).
2. Pide en lenguaje natural o usa un comando — p. ej. *"dame una tarea de escritura B1"*, pega una
   carta y pregunta *"¿aprobaría?"*, o escribe `/written-grade`.

## Comandos (chuleta)
| Comando | Úsalo para |
|---|---|
| `/written-teach [focus]` | Aprender el formato, el criterio de corrección, las plantillas de carta, los Redemittel, los errores comunes, la gestión del tiempo o la lista de comprobación previa a la entrega. |
| `/written-examine` | Obtener **una** tarea en el formato exacto de telc B1 (escenario + carta recibida + 4 Leitpunkte). Sin ayuda mientras escribes. |
| `/written-grade` | Corregir una carta con el criterio real de telc: "¿aprobaría?", la puntuación /45, el desglose por criterios y los errores que cuestan puntos. |
| `/written-drill [category]` | Ejercitar los tipos de error *concretos* que repites (posición del verbo, casos, registro…), extraídos de tu historial. |
| `/written-upgrade` | Convertir una carta *correcta pero plana* en una fluida — cirugía de frases para variedad y mejor redacción. |
| `[write "Jan"]` | Hacer la tarea de la carta de un examen de práctica concreto y corregirla. (Este es el puente desde `telc-b1-exam`.) |

Corchete o barra, cualquiera vale (`/written-grade` = `[written-grade]`), y el lenguaje natural
también los activa.

## Cómo se puntúa la carta (por qué el entrenador es estricto con algunas cosas)
- **Una carta, 30 minutos, ~120–150 palabras, 4 Leitpunkte** — hay que tratar los cuatro puntos.
  Vale **45 puntos** (15% del examen).
- Se corrige según tres criterios (cada uno A/B/C/D): **I** ¿cubriste los 4 puntos? · **II**
  estructura, conexión y registro correcto (du/Sie, saludo, despedida) · **III** corrección
  gramatical.
- **La regla del cero:** si el criterio **I o III (o ambos) es una D**, toda la carta obtiene **0**.
  Así que cubrir los cuatro puntos y mantenerse comprensible importa más que el lenguaje sofisticado.
El entrenador repasa estos criterios explícitamente en cada corrección — nunca una puntuación por intuición.

## El flujo de trabajo que le saca más partido
1. **`/written-teach format & rubric`** una vez, para que sepas cuál es el objetivo.
2. **`/written-examine`** → escribe una carta con el reloj de 30 minutos, sin ayuda.
3. **`/written-grade`** → obtén la puntuación /45 y los errores que cuestan puntos.
4. **`/written-drill`** → machaca los tipos exactos de error que la corrección reveló.
5. Cuando tus cartas *aprueban* pero se leen planas, **`/written-upgrade`** para lograr fluidez.
6. Repite con un nuevo `/written-examine`, o introduce la carta de un examen real mediante `[write "…"]`.

## Consejos para mejores resultados
- **Cubre siempre los cuatro Leitpunkte**, aunque sea brevemente — dejar uno fuera es una variación de 6 puntos;
  cubrir solo uno activa la regla del cero.
- **Mantén las frases simples y correctas** — una carta B1 comprensible gana a una ambiciosa
  pero rota. Los errores de posición del verbo perjudican mucho más que una terminación de caso incorrecta.
- **Deja que haga seguimiento de tu banco de frases y de tus errores recurrentes** en memoria, para que los
  ejercicios apunten a *tus* fugas y las frases resurjan hasta que sean automáticas.
- **El registro lo fija el escenario** (empresa/autoridad → `Sie`; amigo → `du`) — acierta;
  se puntúa bajo el criterio II.

## Lo que necesita
- Nada más allá de Claude y, idealmente, la skill `telc-b1-exam` instalada para que
  el traspaso examen↔escritura funcione.
- Opcional: tus propios PDFs de exámenes de práctica, si quieres que extraiga de ellos tareas de carta reales.
