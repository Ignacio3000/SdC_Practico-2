# SdC_Practico-2
Practico N°2 de la materia Sistemas de Computación.


Este repositorio contiene la segunda entrega del **Práctico N°2** de la materia *Sistemas de Computación*. 
Este trabajo práctico consiste en recuperar el índice GINI de un país (por defecto, Argentina) mediante la API REST del Banco Mundial para el período 2011–2020, convertir el valor float resultante a int, sumarle uno (+1) y presentar el resultado. Para abordar esta tarea, hemos desarrollado cuatro implementaciones distintas: 

1. **Python puro** (sin extensiones).
2. **Python + ctypes** (llamadas a una librería C compartida).
3. **Python + C** (extensión en C como módulo nativo).
4. **Python + C + ASM** (extensión mixta donde la rutina de conversión en assembler se enlaza a través de C).

---

## 📁 Estructura de carpetas (nivel 2)

```
.
├── build/                # Objetos y librerías construidos
├── dist/                 # Distribuciones generadas (wheel, sdist)
├── my_wrappers.egg-info/ # Metadata del paquete (PKG-INFO, SOURCES.txt, dependency_links.txt, top_level.txt)
├── perfomance_tests/     # Benchmarks y scripts de pyperf
├── src/                  # Código fuente y scripts Python
│   ├── c_src/            # C y ASM para wrappers
│   └── scripts/          # APIs de ejemplo (pure.py, ctypes, C, ASM)
├── out/                  # Diagramas (PUML y PNG)
├── Makefile              # Reglas de compilación e instalación
├── setup.py              # Configuración de setuptools para extensiones
└── README.md
```

---

## 🛠 Prerrequisitos

- **NASM** (ensamblador x86\_64)
- **GCC** (soporte `-fPIC` y enlazado de librerías compartidas)
- **Python 3.10+**
- **pip** (para instalación de paquetes)
- **pyperf** (para benchmarking)

Instalar en Ubuntu/Debian:

```bash
sudo apt update && sudo apt install -y nasm gcc python3-dev python3-pip python3-pyperf && pip3 install --user setuptools
```

---

## 🚧 Compilación y construcción

En la raíz del proyecto, ejecute:

```bash
make all
```

Esta regla realiza:

- Crea la carpeta `build/`.
- Ensambla `convert_to_int.asm` → `build/convert_to_int.o`.
- Compila `convertion.c` → `build/convertion_ctypes.o`.
- Genera la librería compartida `lib_convertion_ctypes.so`.
- Ejecuta `python3 setup.py sdist bdist_wheel` para generar `dist/`.

---

## 📦 Instalación


```bash
make install
```

Para instalar el paquete localmente (y registrar las extensiones C/ASM), lo que ejecuta internamente:

```bash
pip install . --upgrade
```

---

## 🐍 Uso de las APIs Python

Los scripts en `src/scripts/` siguen un flujo común:

1. Recuperan el índice GINI de la API del Banco Mundial (`requests`).
2. Convierten el valor `float` a `int` y le suman 1, ya sea en una única llamada o repetido un millón de veces.

Cada variante muestra un enfoque distinto para la conversión:

- **api_only_python.py**: 100% Python. Maneja el procesamiento y la conversión dentro de funciones nativas.
- **api_ctypes.py**: enlaza al C compartido con `ctypes`. Demuestra carga dinámica (`LD_LIBRARY_PATH`) y definición de prototipos.
- **api_c.py**: módulo nativo en C compilado vía `setuptools`. Invoca funciones C directamente para mejorar rendimiento.
- **api_c_asm.py**: combina C y ensamblador. La conversión crítica se implementa en ASM para optimización de bajo nivel.




> **Nota**: los módulos `float_to_int_c` y `float_to_int_asm` se instalan al ejecutar `pip install .`.

---

## ⚡ Benchmark y profiling

Dentro de `perfomance_tests/benchmark.py` se usa `pyperf` para medir el desempeño de cada implementación:

1. Configure qué benchs activar (variables `PY_BENCH`, `CTYPES_BENCH`, `ASM_BENCH`).
2. Ejecute:

   ```bash
   make benchmark
   ```
> **Nota**: Ejecutar tres veces, una para cada variable activa).
3. Compare resultados:

   ```bash
   make compare
   ```

Los JSON generados (`*_converter.json`) se usan para comparar y visualizar las diferencias de velocidad.

---

## 🐞 Depuración con GDB

Puede depurar la variante C/ASM con gdb:

```bash
make gdb
```

Esto lanza:

```
gdb -q --args python3-dbg src/scripts/api_c_asm.py
```

Durante la sesión, inspeccione el stack y los registros antes, durante y después de la llamada a la rutina ASM.

---

## 🧹 Limpieza del proyecto

Para eliminar artefactos de compilación y distribuciones:

```bash
make clean
```

---

## 📊 Diagramas y pruebas adicionales

- **Diagrama de secuencias**: `out/diagrama_secuencias.puml` y `out/diagrama_secuencias.png`.




