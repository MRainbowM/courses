from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Регистрация')

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)
