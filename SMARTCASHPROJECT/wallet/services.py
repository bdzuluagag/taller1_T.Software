from wallet import movements as mov
import os
from django.conf import settings
from django.http import HttpResponse

class MovementService:
    def __init__(self, user):
        self.user = user

    def get_user_movements(self, incomes, exits):
        return mov.read_movements(incomes, exits, self.user)

    def generate_movements_csv(self, user_movements):
        mov.generate_movements_csv(user_movements, self.user)
        file_path = os.path.join(settings.MEDIA_ROOT, f'static/user_movements/{self.user.username}_movements.csv')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/octet-stream')
        return HttpResponse('El archivo no existe.')
