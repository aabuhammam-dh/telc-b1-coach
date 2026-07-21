<!-- Translated from README.md at commit 2304a0a. Re-translate when the English version changes. -->

# telc-b1-exam — cómo usarlo

**🌍 Languages:** [English](README.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [فارسی](README.fa.md) · **Español**

Tu entrenador estricto de telc **Deutsch B1** para las secciones objetivas (Leseverstehen,
Sprachbausteine, Hörverstehen) y el examen oral, diseñado en torno a la práctica con exámenes anteriores.
Registra y corrige tus respuestas, explica cada fallo, encuentra trampas recurrentes, ejercita tus
puntos débiles, extrae vocabulario/gramática de un examen y prepara la Mündliche Prüfung (prueba oral). La
**carta (Schreiben)** la gestiona su skill complementaria, `telc-b1-schreiben`, a la que esta
cede el control automáticamente.

> No es el DTZ. Este es el examen general telc Deutsch B1 para adultos.

## Inicio rápido
1. Instala la skill (haz clic en **Guardar skill** en el archivo `.skill`).
2. Coloca los PDFs de tus exámenes de práctica donde el entrenador pueda leerlos (en este proyecto están en
   `/mnt/project/`). El entrenador los lee directamente — pueden ser exportaciones `.pdf` estilo ZIP.
3. Háblale en lenguaje natural o con un comando entre corchetes, p. ej. `[log exam]` o
   *"corrige mis respuestas de Vera"* o *"explica obwohl vs. trotzdem."*

## Comandos (chuleta)
| Comando | Úsalo para |
|---|---|
| `[log exam]` | Introducir tus respuestas de un examen y obtenerlo **corregido** (verificado con código, nunca a ojo). |
| `[score "Jan"]` | Ver la puntuación de un examen guardado, las áreas débiles y lo que queda pendiente. |
| `[discuss "Jan"]` | Repasar cada respuesta incorrecta: la correcta, el tipo de trampa, la regla. |
| `[study "Jan"]` | Una sesión de enseñanza sobre la gramática, el vocabulario, los conectores y las trampas de ese examen. |
| `[practice "Jan"]` | Ejercicio: volver a preguntar tus fallos + ítems nuevos parecidos, corregidos y seguros para B1. |
| `[retake "Jan"]` | Simulación completa cronometrada, sin ayuda durante, corrección estricta al final. |
| `[extract "Jan"]` / `[extract all]` | Extraer **vocabulario** imprescindible (DE→EN), **conectores** (+ cómo funciona cada uno) y la **gramática crítica** que evalúa Sprachbausteine. |
| `[mock exam]` / `[generate test]` | **¿No tienes PDF de examen? Genera un examen de práctica nuevo y original en formato telc** (completo o una sección) con dificultad B1 real y una clave de respuestas. Contenido nuevo cada vez. |
| `[topic "<name>"]` / `[topic]` | **Enseñar + evaluar un tema** (un punto de gramática, conectores o un tema de vocabulario), luego dar un veredicto de listo/inseguro/no listo y hacerle seguimiento. `[topic]` solo recomienda qué entrenar a continuación según tus puntos débiles. |
| `[weaknesses]` | Ver tu perfil de debilidades a lo largo de todos los exámenes y obtener ejercicios específicos. |
| `[compare exams]` | Patrones entre exámenes + qué exámenes anteriores reutilizan los mismos textos. |
| `[write "Jan"]` | Trabajar la **carta** de ese examen → activa `telc-b1-schreiben`. |
| `[help]` | Mostrar la lista de comandos. |

Corchete o barra, da igual (`[log exam]` = `/log-exam`). Los nombres entre comillas son tus
exámenes (Jan, Vera, Eva, Petra, …).

## El flujo de trabajo que le saca más partido
Ejecuta este ciclo por cada examen y luego pasa al siguiente:
1. **`[log exam]`** → corrígelo. El entrenador registra tus fortalezas/debilidades automáticamente.
2. **`[discuss "…"]`** → entiende *por qué* ocurrió cada fallo (tipo de trampa + regla).
3. **`[extract "…"]`** → extrae el vocabulario, los conectores y la gramática que evaluó ese examen.
4. **`[practice "…"]`** → ejercita los fallos exactos + los parecidos hasta que la trampa esté eliminada.
5. Más adelante, **`[retake "…"]`** en frío para confirmar que se asentó.
6. Cada semana o así, **`[compare exams]`** y **`[weaknesses]`** para reorientarte hacia lo que
   actualmente te cuesta más puntos.

Aparte, mantén la **carta** en marcha con `[write "…"]` (→ skill Schreiben) y ensaya
el **oral** pidiéndole que ejecute práctica de Teil 1 / 2 / 3 — esos son dos de los mayores
bloques de puntos y fáciles de descuidar.

## Consejos para mejores resultados
- **Dale tus respuestas reales**, no un resumen — la corrección es pregunta por pregunta.
- **Pregunta "¿estoy aprobando?"** y razona en puntos *ponderados* (la carta vale 45 de los 225
  puntos escritos), no solo con el contador bruto x/60.
- **Las preguntas de gramática obtienen respuestas fundamentadas** — el entrenador busca primero en la web
  una fuente de gramática alemana de confianza y luego explica de forma sencilla. Pregunta con libertad
  (*"¿cuándo va dativo después de in?"*).
- **Prioriza la precisión en Lesen y Hören sobre Sprachbausteine** cuando el tiempo apremia: cada
  ítem de Lesen/Hören vale 2,5× un ítem de SB en puntos reales (aunque SB es lo más rápido de
  arreglar, por basarse en patrones).
- **Déjalo guardar en memoria** para que el vocabulario, los conectores y tu perfil de debilidades se
  acumulen a lo largo de las sesiones.

## Lo que necesita
- **¿No tienes exámenes de práctica? No hay problema** — usa `[mock exam]` y genera práctica original en
  formato telc para ti. Los PDFs de exámenes de práctica son opcionales: añádelos si los tienes
  (las claves de respuestas están en la última página) y también los corregirá y extraerá su contenido.
- Acceso web para las explicaciones de gramática (busca y luego fundamenta la respuesta).
- La skill `telc-b1-schreiben` instalada para cualquier cosa relacionada con la carta.
