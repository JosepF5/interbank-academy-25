"""
main.py

Aplicación CLI que procesa un archivo CSV de transacciones bancarias y genera:
 - Balance final (suma de créditos menos suma de débitos)
 - Transacción de mayor monto
 - Conteo de transacciones por tipo
"""

import csv
import argparse
import sys

def procesar_transacciones(ruta_csv):
    """
    Lee el CSV en ruta_csv y calcula:
      - total de créditos
      - total de débitos
      - conteo de transacciones
      - transacción de monto máximo
    Devuelve un dict con balance_final, transacción_máxima y conteos.
    """
    total_credito = 0.0
    total_debito = 0.0
    conteos = {'Crédito': 0, 'Débito': 0}
    max_tx = {'id': None, 'monto': 0.0}

    try:
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                tx_id = fila.get('id')
                tx_tipo = fila.get('tipo')
                try:
                    monto = float(fila.get('monto', '0'))
                except ValueError:
                    print(f"⚠️  Monto inválido “{fila.get('monto')}” en ID {tx_id}, se omite.", file=sys.stderr)
                    continue

                if tx_tipo == 'Crédito':
                    total_credito += monto
                    conteos['Crédito'] += 1
                elif tx_tipo == 'Débito':
                    total_debito += monto
                    conteos['Débito'] += 1
                else:
                    print(f"⚠️  Tipo desconocido “{tx_tipo}” en ID {tx_id}, se omite.", file=sys.stderr)
                    continue

                if monto > max_tx['monto']:
                    max_tx['id'] = tx_id
                    max_tx['monto'] = monto

    except FileNotFoundError:
        print(f"❌  Archivo no encontrado: {ruta_csv}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"❌  Falta la columna en el CSV: {e}", file=sys.stderr)
        sys.exit(1)

    return {
        'balance_final': total_credito - total_debito,
        'transaccion_maxima': max_tx,
        'conteos': conteos
    }

def imprimir_reporte(resultados):
    """Imprime en pantalla el reporte de transacciones."""
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {resultados['balance_final']:.2f}")
    print(f"Transacción de Mayor Monto: ID {resultados['transaccion_maxima']['id']} - {resultados['transaccion_maxima']['monto']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {resultados['conteos']['Crédito']}  Débito: {resultados['conteos']['Débito']}")

def main():
    parser = argparse.ArgumentParser(
        description='Procesa un archivo CSV de transacciones bancarias y muestra un reporte.'
    )
    parser.add_argument(
        'archivo_csv',
        help='Ruta al archivo CSV con columnas id,tipo,monto'
    )
    args = parser.parse_args()

    resultados = procesar_transacciones(args.archivo_csv)
    imprimir_reporte(resultados)

if __name__ == '__main__':
    main()
