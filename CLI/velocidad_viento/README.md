# Velocidad Viento

Velocidad del viento cada 10 minutos de Datos Abiertos de Colombia (Ambiente y Desarrollo Sostenible).

Más información disponible en: https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Velocidad-Viento/sgfv-3yp8/about_data

## Columnas

| Nombre            | Descripción                                                                             | Tipo         | Nombre del campo API |
| :---------------- | :-------------------------------------------------------------------------------------- | :----------- | :------------------- |
| CodigoEstacion    | Corresponde al valor de identificación de la estación dentro del catálogo de estaciones | Texto simple | `codigoestacion`     |
| CodigoSensor      | Código de identificación asignado al senso                                              | Texto simple | `codigosensor`       |
| FechaObservacion  | Fecha en la cual se realiza la medición                                                 | Fecha y hora | `fechaobservacion`   |
| ValorObservado    | Valor medido                                                                            | Número       | `valorobservado`     |
| NombreEstacion    | Corresponde a la identificación de la estación dentro del catálogo de estaciones        | Texto simple | `nombreestacion`     |
| Departamento      | Nombre del departamento donde se ubica la estación                                      | Texto simple | `departamento`       |
| Municipio         | Valor medido                                                                            | Texto simple | `municipio`          |
| ZonaHidrografica  | Corresponde al valor de identificación de la estación dentro del catálogo de estaciones | Texto simple | `zonahidrografica`   |
| Latitud           | Corresponde a la latitud en la cual se encuentra la estación                            | Número       | `latitud`            |
| Longitud          | Corresponde a la longitud en la cual se encuentra la estación                           | Número       | `longitud`           |
| DescripcionSensor | Velocidad del viento cada 10 minutos                                                    | Texto simple | `descripcionsensor`  |
| UnidadMedida      | metros/segundo                                                                          | Texto simple | `unidadmedida`       |

## Dependencias

Python 3.7.9 y superiores (3.12)

- [Requests](https://pypi.org/project/requests/)
- [Pandas](https://pypi.org/project/pandas/)
- [ProtoTools](https://pypi.org/project/prototools/)

```sh
pip install -r requirements.txt
```

Notebook:

```
!pip install -r requirements.txt
```

o:

```sh
import sys
!{sys.executable} -m pip install -r requirements.txt
```
