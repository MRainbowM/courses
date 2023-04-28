from django.urls import reverse_lazy
from django.views.generic import CreateView

from clients.models import Client
from users.forms import UserRegisterForm


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    # success_url = reverse_lazy('login')
    success_url = '/'

    def post(self, request, *args, **kwargs):
        answer = super().post(request, *args, **kwargs)

        if self.object is not None:
            # Пользователь успешно создан
            # -> создание клиента
            Client.objects.create(user=self.object, active=True)

        return answer
