# ✈️ Sistema de Reservas de Vuelos

Sistema de gestión de reservas de asientos para vuelos comerciales desarrollado en Python con interfaz gráfica usando Tkinter.

## 📋 Descripción

Aplicación de escritorio que simula un sistema de reservas de vuelos comerciales en un aeropuerto. Permite crear vuelos, asignar rutas y precios, reservar y cancelar asientos, generar reportes estadísticos y realizar simulaciones de ventas masivas.

## 🎯 Características Principales

- ✅ **Gestión de Vuelos**: Crear vuelos con matrices de asientos personalizables (hasta 50x20)
- ✅ **Asignación de Datos**: Configurar código de vuelo, origen, destino y precio
- ✅ **Visualización Gráfica**: Ver estado del avión con interfaz visual (asientos libres/ocupados)
- ✅ **Reservas**: Sistema de reserva de asientos individuales o consecutivos
- ✅ **Cancelaciones**: Liberar asientos reservados
- ✅ **Estadísticas**: Reportes de ocupación y recaudación por vuelo
- ✅ **Búsqueda**: Filtrar vuelos por destino
- ✅ **Simulación**: Venta masiva aleatoria por porcentaje
- ✅ **Reinicio**: Limpiar todos los asientos de un vuelo

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **GUI**: Tkinter (biblioteca estándar)
- **Estructuras de Datos**: Listas y matrices (sin diccionarios)
- **Módulos adicionales**: random

## 📦 Requisitos

- Python 3.6 o superior
- Tkinter (incluido por defecto en Python)

## 🚀 Instalación y Ejecución

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/reservas-vuelos.git
cd reservas-vuelos
```

2. Ejecuta el programa:
```bash
python ReservaDeVuelos.py
```

## 📖 Manual de Uso

### 1️⃣ Crear Nuevo Vuelo
- Ingresa el número de filas (1-50) y columnas (1-20)
- El sistema crea una matriz de asientos vacía
- Se asigna automáticamente un número interno de vuelo

### 2️⃣ Asignar Origen/Destino y Precio
- Selecciona el número de vuelo
- Ingresa código (formato: 3 letras + 3 números, ej: CM123)
- Define origen, destino y precio del boleto
- Solo se puede asignar una vez por vuelo

### 3️⃣ Ver Estado de un Vuelo
- Visualización gráfica del avión con todos los asientos
- 🟢 Verde = Asiento libre
- 🔴 Rojo = Asiento ocupado
- Muestra estadísticas: totales, ocupados, libres y porcentaje

### 4️⃣ Reservar Asiento
- Selecciona vuelo, fila (letra) y columna (número)
- Sistema valida disponibilidad
- Ejemplo: Fila A, Columna 5 = Asiento A5

### 5️⃣ Cancelar Reserva
- Selecciona el asiento a liberar
- El asiento vuelve a estar disponible
- Se actualiza el contador de ventas

### 6️⃣ Ver Estadísticas de Ocupación
- Asientos totales del vuelo
- Cantidad de asientos reservados
- Porcentaje de ocupación

### 7️⃣ Ver Estadísticas de Recaudación
- Boletos vendidos
- Precio por boleto
- Total recaudado (ventas × precio)

### 8️⃣ Buscar Vuelos por Destino
- Ingresa el destino deseado
- Muestra todos los vuelos que van a ese destino
- Indica asientos disponibles en cada uno

### 9️⃣ Ver Vuelos Disponibles
- Lista completa de todos los vuelos
- Información: código, ruta, precio y disponibilidad

### 🔟 Reservar Asientos Consecutivos
- Selecciona fila inicial y cantidad de asientos
- Reserva múltiples asientos seguidos en la misma fila
- Valida que todos estén libres antes de confirmar

### 1️⃣1️⃣ Simular Venta Masiva
- Ingresa porcentaje de ocupación deseado (1-100%)
- Reserva aleatoriamente asientos en todos los vuelos
- Si un vuelo ya supera el porcentaje, no se modifica

### 1️⃣2️⃣ Reiniciar Vuelo
- Libera todos los asientos del vuelo seleccionado
- Reinicia el contador de ventas a cero

### 1️⃣3️⃣ Salir
- Cierra la aplicación

## 🎨 Estructura de Datos

### Vuelo
Cada vuelo se representa como una lista con 6 elementos:
```python
[codigo, origen, destino, precio, matriz_asientos, cantidad_vendidos]
```

**Ejemplo:**
```python
["CM123", "San José", "México", 350.0, matriz_5x6, 15]
```

### Matriz de Asientos
- `0` = Asiento libre
- `1` = Asiento ocupado

### Numeración de Asientos
- **Filas**: Letras (A, B, C, D...)
- **Columnas**: Números (1, 2, 3, 4...)
- **Ejemplo**: Fila 0, Columna 0 = **A1**

## 🎨 Interfaz Gráfica

- **Colores**: Paleta rosa/lavanda para mejor experiencia visual
- **Ventanas emergentes**: Cada función abre su propia ventana
- **Validaciones**: Mensajes de error claros y específicos
- **Canvas**: Visualización gráfica del estado del avión

## 📁 Estructura del Proyecto
```
reservas-vuelos/
│
├── ReservaDeVuelos.py    # Archivo principal del programa
└── README.md             # Este archivo
```

## 🧪 Ejemplos de Uso

### Ejemplo 1: Crear y configurar un vuelo
```
1. Crear vuelo → 10 filas × 12 columnas
2. Asignar datos → CM123, San José → México, $350
3. Reservar asientos → A1, A2, B3, B4
4. Ver estado → Visualizar ocupación gráfica
```

### Ejemplo 2: Simular ocupación
```
1. Crear 3 vuelos diferentes
2. Asignar datos a cada uno
3. Simular venta masiva → 75%
4. Verificar estadísticas de cada vuelo
```

## ⚠️ Validaciones Implementadas

- Campos vacíos
- Tipos de datos correctos (enteros, flotantes, strings)
- Rangos válidos (filas 1-50, columnas 1-20, porcentaje 1-100)
- Formato de código de vuelo (3 letras + 3 números)
- Existencia de vuelos, filas y columnas
- Disponibilidad de asientos
- Vuelos con datos asignados

## 🐛 Manejo de Errores

- Mensajes descriptivos para cada tipo de error
- Validación de entradas antes de procesar
- Prevención de operaciones inválidas
- No permite datos duplicados o inconsistentes

## 👨‍💻 Autor

**Tu Nombre**
- Angie Mariela Alpizar Porrar
- Carne: 2025079783

## 📅 Fecha de Entrega

13 de noviembre de 2025

## 🎓 Contexto Académico

Proyecto desarrollado para el curso de **Introducción a la Programación**.

### Requisitos del Proyecto:
- ✅ Uso exclusivo de listas y matrices
- ✅ No uso de diccionarios
- ✅ Interfaz gráfica obligatoria
- ✅ 13 funcionalidades implementadas

## 📊 Distribución de Puntaje

| Funcionalidad | Puntaje | Dificultad |
|--------------|---------|------------|
| 1. Crear vuelo | 3% | Fácil |
| 2. Asignar datos | 3% | Fácil |
| 3. Ver estado | 15% | Media |
| 4. Reservar asiento | 8% | Media |
| 5. Cancelar reserva | 6% | Media |
| 6. Estadísticas ocupación | 5% | Media |
| 7. Estadísticas recaudación | 5% | Media |
| 8. Buscar por destino | 5% | Media |
| 9. Ver vuelos disponibles | 5% | Media |
| 10. Reservar consecutivos | 10% | Difícil |
| 11. Simular venta masiva | 10% | Difícil |
| 12. Reiniciar vuelo | 3% | Fácil |
| 13. Salir | 2% | Fácil |
| 14. GUI | 20% | Fácil |
| **TOTAL** | **100%** | |

## 📝 Notas Técnicas

### Conversión de Letras a Índices
```python
# A = 65 en ASCII
indice = ord('B') - ord('A')  # B = 1
letra = chr(indice + ord('A'))  # 1 = B
```

### Cálculo de Porcentaje
```python
porcentaje = (ocupados / totales) * 100
```

### Generación Aleatoria
```python
import random
random.shuffle(lista_asientos)  # Mezcla aleatoriamente
```

## 🔮 Posibles Mejoras Futuras

- [ ] Persistencia de datos (guardar en archivo)
- [ ] Sistema de login y usuarios
- [ ] Histórico de reservas
- [ ] Exportar reportes a PDF
- [ ] Múltiples clases de asientos (económica, ejecutiva)
- [ ] Sistema de precios dinámicos
- [ ] Integración con base de datos

## 📄 Licencia

Este proyecto es de uso académico y educativo.

## 🙏 Agradecimientos

Agradecimientos especiales al profesor y compañeros del curso por el apoyo durante el desarrollo del proyecto.

---


**Desarrollado con ❤️ usando Python y Tkinter**
