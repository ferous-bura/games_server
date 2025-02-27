from django.shortcuts import HttpResponse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / 'setup-keno.zip'


def download_game(request):

    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    except Exception as e:
        print(e)

        