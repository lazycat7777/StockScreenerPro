# from django.shortcuts import redirect
# from django.urls import reverse
# from .service import is_ip_authorized

# # Middleware для проверки доступа к сайту
# class AccessControlMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Проверяем, не находимся ли мы на странице авторизации (например, '/telegram_login')
#         if not request.path.startswith(reverse('telegram_login')) and not is_ip_authorized(request):
#             return redirect('telegram_login')  # Перенаправляем на страницу авторизации
#         return self.get_response(request)
