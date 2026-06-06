from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
import json

from .forms import TransactionForm
from .models import Transaction


def dashboard(request):
    # Datas atuais
    today = timezone.now().date()
    month = timezone.now().month
    year = timezone.now().year

    # Todas as transações
    transactions = Transaction.objects.all()

    # Filtradas
    today_transactions = transactions.filter(date=today)
    month_transactions = transactions.filter(date__month=month)
    year_transactions = transactions.filter(date__year=year)

    # Total geral
    total = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    total_today = today_transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    total_month = month_transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    total_year = year_transactions.aggregate(Sum('amount'))['amount__sum'] or 0

    # Categorias para gráfico
    categories = transactions.values('category__name').annotate(
        total=Sum('amount')
    )
    labels = [c['category__name'] for c in categories]
    data = [float(c['total']) for c in categories]

    return render(request, "finance/dashboard.html", {
        "transactions": transactions,
        "total": total,
        "total_today": total_today,
        "total_month": total_month,
        "total_year": total_year,
        "labels": json.dumps(labels),
        "data": json.dumps(data)
    })


def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = TransactionForm()
    return render(request, "finance/add.html", {"form": form})


def delete_all_transactions(request):
    Transaction.objects.all().delete()
    return redirect("dashboard")


def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    transaction.delete()
    return redirect("dashboard")