from django.shortcuts import render
from .models import Companies
from django.shortcuts import get_object_or_404
from .forms import CompanyForm

# Create your views here.
def Placements(request):
    companies = Companies.objects.all()
    return render(request, 'placements.html',{'companies': companies}) 

def companies_detail(request, c_id):
    company = get_object_or_404(Companies, pk=c_id)
    return render(request, 'details.html', {'company': company})

# def forms(request):
#     company=None
#     if request.method == 'POST':
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             company = form.cleaned_data['company_form']
#     return render(request, 'forms.html', {'company': company})