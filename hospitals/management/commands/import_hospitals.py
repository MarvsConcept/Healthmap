import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point, GEOSGeometry
from hospitals.models import Hospital

class Command(BaseCommand):
    help = 'Load GeoJSON data into Hospital model'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file', type=str, help='Path to the GeoJSON file')

    def handle(self, *args, **options):
        geojson_file = options['geojson_file']
        self.stdout.write(self.style.SUCCESS(f'Loading data from {geojson_file}'))

        try:
            with open(geojson_file, 'r') as f:
                data = json.load(f)
                for feature in data.get('features', []):
                    properties = feature.get('properties', {})
                    geometry = feature.get('geometry', {})
                    geom_type = geometry.get('type', '')

                    if geom_type == 'Point':
                        lon, lat = geometry.get('coordinates', [None, None])
                        if lon is None or lat is None:
                            self.stdout.write(self.style.WARNING(f'Missing coordinates for Point feature'))
                            continue
                        location = Point(lon, lat)

                    elif geom_type == 'Polygon':
                        try:
                            polygon = GEOSGeometry(json.dumps(geometry))
                            location = polygon.centroid
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f'Error processing Polygon: {e}'))
                            continue

                    else:
                        self.stdout.write(self.style.WARNING(f'Skipping unsupported geometry type: {geom_type}'))
                        continue

                    Hospital.objects.update_or_create(
                        name=properties.get('name', 'Unknown'),
                        defaults={
                            'location': location,
                            'amenity': properties.get('amenity', ''),
                            'healthcare': properties.get('healthcare', ''),
                            'opening_hours': properties.get('opening_hours', ''),
                            'emergency': properties.get('emergency', ''),
                            'operator_type': properties.get('operator:type', '')
                        }
                    )

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {geojson_file}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON from the file'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
