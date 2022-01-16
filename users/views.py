from django.views.generic import TemplateView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
