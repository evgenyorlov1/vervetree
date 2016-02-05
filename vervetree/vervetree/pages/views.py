from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class Index(View):
	
	def get(self, request):
		return render(request, 'index.html')

	def post(self, request):
		pass


class Join(View):

	def get(self, request):
		return render(request, 'Join.html')

	def post(self, request):
		pass


class Scholarship(View):

	def get(self, request):
		return render(request, 'Scholarship.html')

	def post(self, request):
		pass
	

class PasswordResset(View):
	
	def get(self, request):
		return render(request, 'PasswordResset.html')

	def post(self, request):
		pass


class ContactForm(View):
	
	def get(self, request):
		return render(request, 'ContactForm.html')

	def post(self, request):
		pass


class Prospectus(View):
	
	def get(self, request):
		return render(request, 'Prospectus.html')

	def post(self, request):
		pass


class Uni(View):
	
	def get(self, request):
		return render(request, 'Uni.html')

	def post(self, request):
		pass


class PrivacyPolicy(View):
	
	def get(self, request):
		return render(request, 'PrivacyPolicy.html')

	def post(self, request):
		pass


class CookiePolicy(View):
	
	def get(self, request):
		return render(request, 'CookiePolicy.html')

	def post(self, request):
		pass


class TermsOfService(View):
	
	def get(self, request):
		return render(request, 'TermsOfService.html')

	def post(self, request):
		pass


class UniConnect(View):
	
	def get(self, request):
		return render(request, 'UniConnect.html')

	def post(self, request):
		pass