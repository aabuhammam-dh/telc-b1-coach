<!-- Translated from README.md at commit c460afa. Re-translate when the English version changes. -->

# telc B1 Coach 🇩🇪

**🌍 Languages:** [English](../README.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [فارسی](README.fa.md) · **Español**

[![CI](https://github.com/aabuhammam-dh/telc-b1-coach/actions/workflows/ci.yml/badge.svg)](https://github.com/aabuhammam-dh/telc-b1-coach/actions/workflows/ci.yml)
![License](https://img.shields.io/github/license/aabuhammam-dh/telc-b1-coach?color=blue)
[![Stars](https://img.shields.io/github/stars/aabuhammam-dh/telc-b1-coach?style=social)](https://github.com/aabuhammam-dh/telc-b1-coach/stargazers)
![Works with](https://img.shields.io/badge/works_with-Claude·Gemini·Codex-5436DA)
![Price](https://img.shields.io/badge/price-free-brightgreen)
![Exam](https://img.shields.io/badge/exam-telc_Deutsch_B1-orange)

Dos complementos gratuitos ("skills") que convierten a **Claude** —u otra IA que admita skills— en
un entrenador estricto y sin rodeos para el examen **telc Deutsch B1**. Corrige tus respuestas
de práctica, explica cada error, ejercita tus puntos débiles, te prepara para la prueba oral
y entrena tu escritura.

> ⭐ Si esto te ayuda en tu preparación, **dale una estrella al repositorio** — ayuda a que otros estudiantes lo encuentren.

<p align="center">
  <img src="assets/demo.gif" alt="telc B1 Coach en acción — registrando respuestas, corrigiendo y explicando errores" width="720">
</p>

> Para el examen general **telc Deutsch B1** (el *Zertifikat Deutsch* para adultos). **No** es el DTZ,
> ni tampoco el Goethe B1.

Esta guía está escrita para que **cualquiera con este enlace pueda ponerlo en marcha en unos minutos**,
aunque nunca hayas usado una "skill" antes. Solo sigue la sección de la app que uses.

---

## Lo que obtienes

Dos skills que funcionan juntas:

- **`telc-b1-exam`** — registra y corrige tus respuestas a un examen de práctica, te dice *por qué*
  cada respuesta fue incorrecta (la trampa + la regla), extrae el vocabulario importante, los conectores
  y la gramática de un examen, ejercita tus puntos débiles, realiza práctica oral y —si no
  tienes exámenes de práctica— **te genera nuevos exámenes originales** en el formato real de telc.
  Las preguntas de gramática se responden con fuentes reales, explicadas de forma sencilla.
- **`telc-b1-schreiben`** — entrena la **carta escrita** (Schreiben): enseña el formato, corrige tu
  carta como lo hacen los examinadores reales y ejercita los errores que repites una y otra vez.

Pides las cosas en lenguaje natural (*"corrige mis respuestas"*, *"explica weil vs. denn"*,
*"¿aprobaría esta carta?"*) o con comandos cortos como `[log exam]` o `/written-grade`.

> [!TIP]
> ¿No tienes exámenes de práctica? Solo escribe `[mock exam]` y genera exámenes originales.

---

## Cómo funciona

```mermaid
flowchart LR
  Q{Have a practice exam?}
  Q -- No --> M["[mock exam]<br/>generate an original test"]
  Q -- Yes --> L["[log exam]<br/>grade it"]
  M --> L
  L --> W["[weaknesses]<br/>find your gaps"]
  W --> P["[practice] / [topic]<br/>drill + teach"]
  P --> L
  W --> S["[write]<br/>letter → Schreiben skill"]
```

Un solo ciclo: genera o corrige un examen, encuentra tus puntos débiles, ejercítalos, repite — y ramifícate
hacia el entrenador de escritura siempre que trabajes en la carta.

---

## Paso 1 — Descarga las skills desde esta página

1. Ve al principio de este repositorio.
2. Haz clic en el botón verde **`< > Code`** y luego en **Download ZIP**.
3. Descomprime el archivo que descargaste. Dentro, en una carpeta `skills/`, encontrarás dos carpetas:
   **`telc-b1-exam`** y **`telc-b1-schreiben`**.

Eso es todo — esas dos carpetas *son* las skills. Ahora instálalas en tu IA usando la
sección correspondiente más abajo.

---

## Paso 2 — Instálalas (elige tu app)

### ⚡ Lo más rápido — instalación de una línea para Claude Code y otras CLIs

Si tienes [Node.js](https://nodejs.org) instalado, un solo comando añade **ambas** skills a **Claude Code** (y a Gemini CLI, Cursor, Codex y otras herramientas que siguen el estándar Agent Skills):

```bash
npx skills add aabuhammam-dh/telc-b1-coach
```

Reinicia tu herramienta de IA después y las skills se cargan automáticamente. *(Esto usa el instalador de código abierto [`skills`](https://github.com/vercel-labs/skills) del ecosistema Agent Skills — mantenido por la comunidad, no es una herramienta oficial de Anthropic.)*

**¿Prefieres el marketplace de plugins integrado de Claude Code?** Añade este repositorio como un marketplace y luego instala el plugin:

```text
/plugin marketplace add aabuhammam-dh/telc-b1-coach
/plugin install telc-b1-coach@telc-b1-coach
```

¿No eres de terminal, o usas el sitio web de Claude? Elige una opción de abajo en su lugar.

### 🟣 Opción A — Sitio web de Claude o app de Claude (la mayoría de la gente)

1. **Comprime cada carpeta de skill por separado.** Necesitas un `.zip` independiente para cada skill:
   - **Mac:** haz clic derecho en la carpeta `telc-b1-exam` → **Comprimir**. Repite para
     `telc-b1-schreiben`.
   - **Windows:** haz clic derecho en la carpeta → **Enviar a → Carpeta comprimida (en zip)**. Repite
     para la otra.
   *(Deberías terminar con `telc-b1-exam.zip` y `telc-b1-schreiben.zip`.)*
2. En Claude, haz clic en tu **icono de perfil → Configuración → Capacidades**, y asegúrate de que
   **Ejecución de código y creación de archivos** esté **activado**. *(Esto es lo único que las skills
   realmente necesitan.)*
3. Ve a **Personalizar → Skills**, haz clic en **Subir skill** y elige `telc-b1-exam.zip`.
   Hazlo de nuevo para `telc-b1-schreiben.zip`.
4. Listo. Claude las usa automáticamente cuando hablas del examen telc B1. Las skills que
   subes aquí funcionan tanto en **Claude Chat** como en **Cowork**.

> **También funciona en el plan Free** — las skills están disponibles en **Free, Pro, Max, Team y
> Enterprise**; el único requisito es que **Ejecución de código y creación de archivos** esté habilitado
> (paso 2). En Free solo tienes el límite diario normal de mensajes. En **Team/Enterprise**, es posible
> que un propietario deba activar primero las Skills para la organización (está activado por defecto en
> Team). Subirlas aquí **no** copia las skills a Claude Code ni a la API — esos son
> entornos separados (ver más abajo). Los nombres de los menús pueden variar ligeramente según la versión.

<details>
<summary>🟢 Opción B — Claude Code (terminal / VS Code / JetBrains)</summary>

Sin comprimir, sin subir — las skills son simplemente carpetas en tu computadora.

1. Crea la carpeta de skills si no existe: `~/.claude/skills/`
   *(esa es una carpeta llamada `skills` dentro de una carpeta oculta `.claude` en tu directorio personal).*
2. Copia **ambas** carpetas `telc-b1-exam` y `telc-b1-schreiben` (dentro de la carpeta `skills/` de la descarga) dentro.
3. Reinicia tu sesión de Claude Code. Las descubre y las usa automáticamente.

*(¿Las quieres solo dentro de un proyecto en lugar de en todas partes? Pon las carpetas en la
carpeta `.claude/skills/` de ese proyecto en su lugar.)*

</details>

<details>
<summary>🔵 Opción C — Otra IA que admita skills (Gemini, Codex, Cursor, Copilot…)</summary>

Agent Skills es un **estándar abierto**, así que las *mismas carpetas* funcionan en muchas otras
herramientas de IA. Hay dos casos:

**C1 — Herramientas de programación que leen archivos `SKILL.md`** (Gemini CLI, OpenAI Codex CLI, Cursor,
GitHub Copilot y más de 25 otras): copia las carpetas de las skills en el directorio de skills de esa
herramienta —por ejemplo, **`.gemini/skills/`** para Gemini CLI— y reiníciala. La skill funciona
sin cambios; no hay que reescribir nada.

- Atajo: muchas de estas admiten un instalador de una línea que coloca los archivos en el lugar correcto
  automáticamente — `npx skills add <this-repo>` — consulta **skills.sh** para más detalles.

**C2 — Asistentes de chat que usan "bots personalizados" en su lugar** (los **Gems** de la app de Gemini, o
los **GPTs** de ChatGPT): estos no leen los archivos de skill directamente, pero una skill son simplemente
instrucciones en texto plano, así que:

1. Abre el archivo **`SKILL.md`** de una skill (está dentro de cada carpeta) y copia todo su contenido.
2. Crea un nuevo **Gem** (Gemini) o **GPT** (ChatGPT) y pega ese texto como sus
   instrucciones.
3. Si la skill menciona archivos en su carpeta `references/`, adjúntalos como conocimiento/archivos del
   bot, o pega el que corresponda cuando el entrenador lo pida.

Esta es la alternativa universal — funciona en esencialmente cualquier asistente, aunque el material
de referencia detallado se carga de forma menos automática que en Claude.

</details>

---

## Paso 3 — Comprueba que funciona

Inicia un nuevo chat y escribe:

> **`[help]`**

El entrenador del examen debería listar sus comandos. O simplemente di *"quiero practicar para el examen
telc B1"* y tomará el control. Para probar el entrenador de escritura, di *"dame una tarea de escritura B1"*.

---

## Qué hace cada skill

| Skill | Cubre | Prueba a decir / escribir |
|---|---|---|
| **`telc-b1-exam`** | Leseverstehen, Sprachbausteine, Hörverstehen + el examen de **expresión oral**, puntuación, ejercicios, gramática, **generación de exámenes de práctica originales** y **enseñanza-y-evaluación sobre temas concretos** con seguimiento de preparación | `[mock exam]`, `[topic "connectors"]`, `[log exam]`, "explica obwohl vs. trotzdem" |
| **`telc-b1-schreiben`** | La **carta escrita** — formato, corrección, ejercicios de errores, frases | `/written-grade`, "¿aprobaría esta carta?" |

Se emparejan automáticamente: el entrenador del examen cede el control al entrenador de escritura
cada vez que trabajas en la carta, así que **instala las dos**.

Cada skill también tiene su propia guía breve: [`skills/telc-b1-exam/README.md`](../skills/telc-b1-exam/README.md)
y [`skills/telc-b1-schreiben/README.md`](../skills/telc-b1-schreiben/README.md).

---

## ¿Por qué esto?

|                                            | Chat de IA normal | **telc B1 Coach** | Curso de preparación de pago |
|--------------------------------------------|:-------------:|:-----------------:|:----------------:|
| Precio                                     |     Gratis      |     **Gratis**      |       €€€        |
| Práctica original ilimitada en formato telc |  ⚠️ genérico   |        ✅         |   ❌ conjunto fijo   |
| Corrige tus respuestas con claves de respuestas |      ❌       |        ✅         |        ✅        |
| Sigue *tus* puntos débiles a lo largo del tiempo |      ❌       |        ✅         |   ✅ (tutor)     |
| Entrenamiento de carta escrita según la rúbrica de telc |     ⚠️        |        ✅         |        ✅        |
| Funciona en tu idioma                     |      ✅       |        ✅         |     varía       |

_Guía aproximada, no una comparación científica._

---

## Un par de cosas que debes saber

- **¿Quieres material oficial también?** telc te ofrece un **examen modelo oficial gratuito** —una prueba
  completa *con claves de respuestas y el audio de comprensión auditiva*— en su página de B1. Descárgalo y
  dirige al entrenador hacia él:
  **<https://www.telc.net/sprachpruefungen/deutsch/zertifikat-deutsch-telc-deutsch-b1/>**
  (la página también tiene versión en inglés). Cualquier examen de práctica en formato telc sirve; las
  claves de respuestas están en la última página.
- **Cada app se instala por separado.** Subirlas al sitio web de Claude no las sincroniza con Claude
  Code ni con otras IAs — configúralas en cada lugar donde quieras usarlas.
- **Viene listo para usar.** Las skills incluyen contenido inicial (trampas habituales del examen,
  patrones de ejemplo, un banco de frases) para que sean útiles de inmediato; Claude se ajusta a ti a
  medida que practicas. No se incluye ningún dato personal.

> [!NOTE]
> Esto es una ayuda de estudio con IA independiente que genera práctica **original** — **no**
> es material oficial de telc y no está afiliado a telc.

---

## Preguntas frecuentes

<details>
<summary>¿Es este material oficial de telc?</summary>

No — es una ayuda de estudio independiente que genera práctica original. No está afiliada a telc.
</details>

<details>
<summary>¿Necesito un plan de pago de Claude?</summary>

No. Funciona en el plan gratuito, siempre que la Ejecución de código y creación de archivos esté habilitada.
</details>

<details>
<summary>¿Funciona en otras IAs?</summary>

Sí — está construido sobre el estándar abierto Agent Skills, así que también funciona en Gemini CLI, OpenAI Codex CLI, Cursor y otras.
</details>

<details>
<summary>No tengo ningún examen de práctica — ¿puedo usarlo igualmente?</summary>

Sí. Escribe <code>[mock exam]</code> y genera práctica original en formato telc con una clave de respuestas.
</details>

---

## Licencia

MIT — consulta [`LICENSE`](LICENSE). Si hiciste un fork o republicaste esto, añade tu nombre a la
línea de copyright.

---

> ⭐ Si esto te ayuda en tu preparación, **dale una estrella al repositorio** — ayuda a que otros estudiantes lo encuentren.
