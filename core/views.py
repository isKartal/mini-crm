from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Customer, Deal, Note
from .forms import CustomerForm, DealForm, NoteForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hesap oluşturuldu: {username}. Giriş yapabilirsiniz.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def index(request):
    customers_count = Customer.objects.filter(created_by=request.user).count()
    deals_count = Deal.objects.filter(created_by=request.user).count()
    # recent_notes = Note.objects.filter(created_by=request.user).order_by('-created_at')[:5] # Optional
    
    context = {
        'customers_count': customers_count,
        'deals_count': deals_count,
    }
    return render(request, 'index.html', context)

@login_required
def customer_list(request):
    customers = Customer.objects.filter(created_by=request.user)
    return render(request, 'core/customer_list.html', {'customers': customers})

@login_required
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.save()
            messages.success(request, 'Müşteri başarıyla eklendi.')
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'core/customer_form.html', {'form': form, 'title': 'Müşteri Ekle'})

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.customer = customer
            note.created_by = request.user
            note.save()
            messages.success(request, 'Not eklendi.')
            return redirect('customer_detail', pk=pk)
    else:
        form = NoteForm()

    return render(request, 'core/customer_detail.html', {'customer': customer, 'note_form': form})

@login_required
def deal_list(request):
    deals = Deal.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'core/deal_list.html', {'deals': deals})

@login_required
def deal_add(request):
    if request.method == 'POST':
        form = DealForm(request.POST, user=request.user)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.created_by = request.user
            deal.save()
            messages.success(request, 'Satış fırsatı eklendi.')
            return redirect('deal_list')
    else:
        form = DealForm(user=request.user)
    return render(request, 'core/deal_form.html', {'form': form, 'title': 'Fırsat Ekle'})

@login_required
def deal_update(request, pk):
    deal = get_object_or_404(Deal, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Satış fırsatı güncellendi.')
            return redirect('deal_list')
    else:
        form = DealForm(instance=deal, user=request.user)
    return render(request, 'core/deal_form.html', {'form': form, 'title': 'Fırsat Düzenle'})
